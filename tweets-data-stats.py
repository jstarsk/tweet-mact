import os
import numpy as np
import pandas as pd
import glob
from classifier import *

clf = SentimentClassifier()


def dir_os_db(wdir="db", os_system="WIN"):
    if os_system == "WIN":
        db_folder = "%s\\%s\\" % (os.getcwd(), wdir)
        db_csv = glob.glob("%s*.csv" % db_folder)
    elif os_system == "OSX":
        db_folder = "%s/%s/" % (os.getcwd(), wdir)
        db_csv = glob.glob("%s*.csv" % db_folder)
    else:
        db_folder = "%s/%s/" % (os.getcwd(), wdir)
        db_csv = glob.glob("%s*.csv" % db_folder)
    return db_csv


def sentiment_classifier_tweets():
    db_csv = dir_os_db(wdir="db", os_system='OSX')

    for db in db_csv:
        try:
            df = pd.read_csv(db)

            for index, row in df.iterrows():
                try:
                    if row['lang'] == "es":
                        print(row['text'] + ' ==> %.5f' % clf.predict(row['text']))
                    elif row['lang'] == "ca":
                        print(row['text'] + ' ==> %.5f' % clf.predict(row['text']))
                    elif row['lang'] == "en":
                        print(row['text'] + ' ==> %.5f' % clf.predict(row['text']))

                except Exception as e:
                    pass

        except Exception as e:
            print(e)


if __name__ == "__main__":
    sentiment_classifier_tweets()
