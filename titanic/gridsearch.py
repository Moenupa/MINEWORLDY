# -*- coding: utf-8 -*-
# @Author: Moenupa 2019/05/21

import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.linear_model import RidgeClassifierCV
from sklearn.ensemble import AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, RandomForestClassifier, StackingClassifier, RandomForestRegressor, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC, NuSVC
from mlxtend.classifier import StackingCVClassifier
from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import auc

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

    return X_train, y_train, X_test
def num_replace(X_train, X_test):
    X_train.loc[X_train['Sex']=='male','Sex'] = 1
    X_train.loc[X_train['Sex'] == 'female', 'Sex'] = 2
    X_train.loc[X_train['Embarked'] == 'S', 'Embarked'] = 1
    X_train.loc[X_train['Embarked'] == 'C', 'Embarked'] = 2
    X_train.loc[X_train['Embarked'] == 'Q', 'Embarked'] = 3
    X_test.loc[X_test['Sex']=='male','Sex'] = 1
    X_test.loc[X_test['Sex'] == 'female', 'Sex'] = 2
    X_test.loc[X_test['Embarked'] == 'S', 'Embarked'] = 1
    X_test.loc[X_test['Embarked'] == 'C', 'Embarked'] = 2
    X_test.loc[X_test['Embarked'] == 'Q', 'Embarked'] = 3
    return X_train, X_test
def impute(X_train, X_test):
    imputer_age, imputer_emb, imputer_fare = RandomForestRegressor(), RandomForestClassifier(), RandomForestRegressor()

    dataset1 = X_train.drop(columns=['Age']).dropna().astype('float')
    imputer_emb.fit(
        dataset1.loc[:, ['Pclass','Fare']],
        dataset1.loc[:, 'Embarked']
        )
    imputer_fare.fit(
        dataset1.loc[:, ['Pclass','Embarked']],
        dataset1.loc[:, 'Fare']
        )
    nanpos = np.where(X_train.isna())
    split = [[], [], []]
    for i in range(len(nanpos[0])):
        row, col = nanpos[0][i], nanpos[1][i]
        if col == 7:
            split[0].append(row)
        elif col == 6:
            split[1].append(row)
        elif col == 3:
            split[2].append(row)
    try:
        X_train.iloc[split[0], 7] = imputer_emb.predict(X_train.iloc[split[0], [1, 6]])
        X_train.iloc[split[1], 6] = imputer_fare.predict(X_train.iloc[split[1], [1, 7]])
    except ValueError:
        X_train.fillna(0, inplace = True)
    dataset2 = X_train.dropna()
    imputer_age.fit(
        dataset2.loc[:, ['Pclass', "SibSp", "Parch", "Fare"]],
        dataset2.loc[:, 'Age']
        )
    X_train.iloc[split[2], 3] = imputer_age.predict(X_train.iloc[split[2], [1, 4, 5, 6]])

    nanpos = np.where(X_test.isna())
    split = [[], [], []]
    for i in range(len(nanpos[0])):
        row, col = nanpos[0][i], nanpos[1][i]
        if col == 7:
            split[0].append(row)
        elif col == 6:
            split[1].append(row)
        elif col == 3:
            split[2].append(row)
    try:
        X_test.iloc[split[0], 7] = imputer_emb.predict(X_test.iloc[split[0], [1, 6]])
        X_test.iloc[split[1], 6] = imputer_fare.predict(X_test.iloc[split[1], [1, 7]])
    except ValueError:
        X_test.fillna(0, inplace = True)
    X_test.iloc[split[2], 3] = imputer_age.predict(X_test.iloc[split[2], [1, 4, 5, 6]])

    X_train.loc[:,['Sex','Embarked']] = X_train.loc[:,['Sex','Embarked']].astype(int)
    X_test.loc[:,['Sex','Embarked']] = X_test.loc[:,['Sex','Embarked']].astype(int)
    return X_train, X_test

def main():
    X_train, y_train, X_test = func_procs()

    X_train, X_test = num_replace(X_train, X_test)
    X_train, X_test = impute(X_train, X_test)
    # saving processed X_train data
    X_train.to_csv("C:\\Github\\MINEWORLDY\\titanic\\X_train_proc.csv", index=False)
    X_test.to_csv("C:\\Github\\MINEWORLDY\\titanic\\X_test_proc.csv", index=False)
    param_dict = {
        'n_estimators':range(80,200,4),
        'max_depth':range(2,15,1),
        'learning_rate':np.linspace(0.01,2,20),
        'subsample':np.linspace(0.7,0.9,20),
        'colsample_bytree':np.linspace(0.5,0.98,10),
        'min_child_weight':range(1,9,1)
    }
    classifier = XGBClassifier()
    grid = GridSearchCV(classifier, param_dict, cv = 3, scoring = 'roc_auc', n_jobs = -1)
    grid.fit(X_train, y_train)
    print(grid.best_estimator)

if __name__ == "__main__":
    main()
