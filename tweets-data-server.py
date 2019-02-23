import os
import pandas as pd
import glob
from geojson import Point, Feature, LineString, Polygon
from geojson_utils import draw_circle
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

# WINDOWS USERS
MAPBOX_ACCESS_KEY = 'pk.eyJ1Ijoic3RhcnNrIiwiYSI6ImNqcW1uYThkcjB5OXU0MnFuMmNsd2F6bm4ifQ.UVn8HyKNEtPabiMlYwJfPw'

# LINUX MAC USERS
# app.config.from_envvar('APP_CONFIG_FILE', silent=True)
# MAPBOX_ACCESS_KEY = app.config[MAPBOX_ACCESS_KEY]

map_center = [41.3851, 2.1734]
map_zoom = 11


def dir_os_db(os_system="WIN"):
    if os_system == "WIN":
        db_folder = "%s\\db\\" % (os.getcwd())
        db_csv = glob.glob("%s*.csv" % db_folder)
    elif os_system == "OSX":
        db_folder = "%s/db/" % (os.getcwd())
        db_csv = glob.glob("%s*.csv" % db_folder)
    else:
        db_folder = "%s/db/" % (os.getcwd())
        db_csv = glob.glob("%s*.csv" % db_folder)
    return db_csv


def add_fetched_tweets_loc():

    db_csv = dir_os_db(os_system='WIN')

    _tweets_locations = []

    for db in db_csv:
        try:
            df = pd.read_csv(db)

            for index, row in df.iterrows():
                try:
                    try:
                        coordinates_lon = float(row['coordinates_lon'])
                        coordinates_lat = float(row['coordinates_lat'])
                        loc_range = 0.05
                        opacity = 1.0

                    except Exception as e:
                        coordinates_lon = float(row['_search_loc_lon'])
                        coordinates_lat = float(row['_search_loc_lat'])
                        loc_range = float(row['_search_loc_range'])
                        opacity = 0.03

                        print(e)
                        pass

                    point = Point((coordinates_lon, coordinates_lat))
                    properties_point = {
                        'title': row['place_name'],
                        'diameter': loc_range,
                        'opacity': opacity
                    }

                    feature_point = Feature(geometry=point, properties=properties_point)

                    _tweets_locations.append(feature_point)
                except Exception as e:
                    print(e)
                    print("Sorry there was an error adding a marker!")

        except Exception as e:
            print(e)

    return _tweets_locations



@app.route('/twitter_map')
def mapbox_js():
    tweets_locations = add_fetched_tweets_loc()
    return render_template(
        'twitter_map.html',
        ACCESS_KEY=MAPBOX_ACCESS_KEY,
        center_lat=map_center[0],
        center_lon=map_center[1],
        map_zoom=map_zoom,
        tweets_locations=tweets_locations

    )


if __name__ == "__main__":
    app.run()