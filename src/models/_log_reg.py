import numpy as np

from sklearn.naive_bayes import GaussianNB

class NVB():
    X = None
    y = None
    clf = None

    def __init__(self, X: np.array, y: np.array):
        self.X = X
        self.y = y

    def train(self):
        self.clf = GaussianNB(random_state=0).fit(self.X, self.y)

    def predict(self, x_input : np.array):
        prediction = self.clf.predict(x_input)
        return prediction
