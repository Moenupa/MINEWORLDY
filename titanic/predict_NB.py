from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    dir = "C:\\Github\\MINEWORLDY\\titanic\\"
    X_train = pd.read_csv(open(dir + "X_train_median_proc.csv"))
    y_train = pd.read_csv(open(dir + "train.csv")).loc[:, "Survived"]
    X_test = pd.read_csv(open(dir + "X_test_median_proc.csv"))
    y_test = pd.read_csv(open(dir + "gender_submission.csv")).loc[:,"Survived"]

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(precision_score(y_test, y_pred))
    pd.DataFrame(y_pred).to_csv(dir + "\\output\\NB_output.csv")

if __name__ == "__main__":
    main()