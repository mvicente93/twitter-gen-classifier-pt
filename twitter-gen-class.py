#!/usr/bin/python
from sklearn.externals import joblib
from src.socling_features import extract_username_socling_features, extract_description_socling_features
from src.pre_processing import normalize
from src.twitter import TwitterHandler
import numpy as np
import sys


class TwitterLearn:
    def __init__(self):
        self.name_ngrams = joblib.load('models/name_chars_counter.pkl')
        self.sc_ngrams = joblib.load('models/sc_chars_counter.pkl')
        self.clf = joblib.load('models/classifier.pkl')

    def classify(self, user):
        result_vector = []

        if 'name' in user:
            name = user['name']
            result_vector.append(extract_username_socling_features(name))
        else:
            result_vector.append(extract_username_socling_features(u''))
        if 'description' in user:
            description = user['description']
            result_vector.append(extract_description_socling_features(description))
        else:
            result_vector.append(extract_description_socling_features(u''))

        screen_name = user['screen_name']
        result_vector.append(self.name_ngrams.fit_transform([normalize(name).lower().strip()]).toarray().tolist()[0])
        result_vector.append(self.sc_ngrams.fit_transform([normalize(screen_name).lower().strip()]).toarray().tolist()[0])

        np_vector = np.array([f for vector in result_vector for f in vector]).reshape(1, -1)
        gender = self.clf.predict(np_vector)[0]

        return gender


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage python twitter-gen-class.py [twitter screen name]"

    scname = sys.argv[1]
    th = TwitterHandler()
    classifier = TwitterLearn()

    user = th.get_user(scname)

    if user != "No user":
        user = {'name': user.name, 'screen_name': user.screen_name, 'description': user.description}
        result = classifier.classify(user)
        print result
    else:
        print "Invalid screen name"


