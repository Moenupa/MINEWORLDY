import pandas as pd
from sklearn.metrics import explained_variance, r2_score, matthews_corrcoef

def func_procs():
    try:
        dir = "C:\\Github\\MINEWORLDY\\titanic\\"
        X_train = pd.read_csv(open(dir + "train.csv")).loc[
                :,
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
            ]
        y_train = pd.read_csv(open(dir + "train.csv")).loc[:, "Survived"]
        X_test = pd.read_csv(open(dir+"test.csv")).loc[
                :,
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
            ]
    except ValueError:
        print("VE")
    except FileNotFoundError:
        print("FE")
def