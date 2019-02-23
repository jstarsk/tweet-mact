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
            array = []

            for index, row in df.iterrows():
                try:
                    score = 0.0
                    if row['lang'] == "es":
                        score = round(clf.predict(row['text']), 3)
                        array.append(score)
                        if score < 0.5:
                            row['label'] = 'NEG'
                        elif score > 0.5:
                            row['label'] = 'POS'
                        else:
                            row['label'] = 'NEU'
                    elif row['lang'] == "ca":
                        score = round(clf.predict(row['text']), 3)
                        array.append(score)
                        if score < 0.5:
                            row['label'] = 'NEG'
                        elif score > 0.5:
                            row['label'] = 'POS'
                        else:
                            row['label'] = 'NEU'
                    elif row['lang'] == "en":
                        score = round(clf.predict(row['text']), 3)
                        array.append(score)
                        if score < 0.5:
                            row['label'] = 'NEG'
                        elif score > 0.5:
                            row['label'] = 'POS'
                        else:
                            row['label'] = 'NEU'
                    print(row['text'] + ' ==> %.5f ==> %s' % (score, row['label']))

                except Exception as e:
                    pass

            se = pd.Series(array)
            df['sentiment_classifier_score'] = se.values
            df.to_csv(db, index=False)

        except Exception as e:
            print(db)
            print(e)


if __name__ == "__main__":
    sentiment_classifier_tweets()
