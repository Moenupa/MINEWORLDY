# -*- coding: utf-8 -*-
# @Author: Moenupa 2019/05/21
import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.impute import KNNImputer

def func_procs():
    try:
        dir = "C:\\Github\\MINEWORLDY\\titanic\\"


        X_train = pd.read_csv(open(dir + "train.csv")).loc[
                :,
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
            ]
        y_train = pd.read_csv(open(dir + "train.csv")).loc[
                :,
                "Survived"
            ]
        X_test = pd.read_csv(open(dir + "test.csv")).loc[
                :,
                ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
            ]
    except ValueError:
        print("VE")
    except FileNotFoundError:
        print("FE")

    X_train.loc[X_train['Sex']=='male','Sex'] = 1
    X_train.loc[X_train['Sex'] == 'female', 'Sex'] = 2
    X_train.loc[X_train['Embarked'] == 'S', 'Embarked'] = 1
    X_train.loc[X_train['Embarked'] == 'C', 'Embarked'] = 2
    X_train.loc[X_train['Embarked'] == 'Q', 'Embarked'] = 3
    X_test.loc[X_test['Sex'] == 'male','Sex'] = 1
    X_test.loc[X_test['Sex'] == 'female', 'Sex'] = 2
    X_test.loc[X_test['Embarked'] == 'S', 'Embarked'] = 1
    X_test.loc[X_test['Embarked'] == 'C', 'Embarked'] = 2
    X_test.loc[X_test['Embarked'] == 'Q', 'Embarked'] = 3
    # 数据映射

    #imp_mean = IterativeImputer(random_state=0)
    #imp_mean.fit(X_train)
    #imp_mean.transform(X_train)
    #imp_mean.transform(X_test)
    median = pd.concat([X_train.loc[:, "Age"], X_test.loc[:, "Age"]], axis = 1).median
    X_train.loc[:, "Age"].fillna(median)
    X_test.loc[:, "Age"].fillna(median)
    median = X_train.loc[:, "Fare"].median
    X_train.loc[:, "Fare"].fillna(median)
    X_test.loc[:, "Fare"].fillna(median)
    median = X_train.loc[:, "Embarked"].median
    X_train.loc[:, "Embarked"].fillna(median)
    X_test.loc[:, "Embarked"].fillna(median)
    X_train = X_train.to_csv(dir + "X_train_median_proc.csv")
    X_test = X_test.to_csv(dir + "X_test_median_proc.csv")
    print("Output Complete.")

    #X_train_child = X_train.loc[X_test['Age'] <= 18, 'Age']

if __name__ == "__main__":
    func_procs()