# -*- coding: utf-8 -*-
# @Author: Moenupa 2019/05/21

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
    global models
    X_train, y_train, X_test = func_procs()

    X_train, X_test = num_replace(X_train, X_test)
    X_train, X_test = impute(X_train, X_test)
    # saving processed X_train data
    X_train.to_csv("C:\\Github\\MINEWORLDY\\titanic\\X_train_proc.csv", index=False)
    X_test.to_csv("C:\\Github\\MINEWORLDY\\titanic\\X_test_proc.csv", index=False)
    models = ["XG","ADA","BG","ET","RF","ST","KN","DT", "SVC", "LSVC", "NSVC", "ST2", "MLP", "GB"]
    for model in models:
        classifier = train_model(model, X_train.drop(columns=['PassengerId']), y_train)
        y_pred = classifier.predict(X_test.drop(columns=['PassengerId']))
        result = pd.concat([X_test, pd.DataFrame(y_pred, columns=["Survived"])], axis=1)
        print("\t{0}\t{1}".format(model, sum(y_pred)/152-1))
        result.to_csv("C:\\Github\\MINEWORLDY\\titanic\\output\\data\\{0}_data.csv".format(model), index=False)
        result.loc[:,['PassengerId','Survived']].to_csv("C:\\Github\\MINEWORLDY\\titanic\\output\\{0}_output.csv".format(model), index=False)
def train_model(model, X_train, y_train):
    '''
    Process one model by training data
    Input: X_train,y_train
    Output: regressor by the need
    '''
    if model == 'XG':
        clsfr = XGBClassifier()
    elif model == 'ADA':
        clsfr = AdaBoostClassifier()
    elif model == 'DT':
        clsfr = DecisionTreeClassifier()
    elif model == 'SVC':
        clsfr = SVC()
    elif model == 'KN':
        clsfr = KNeighborsClassifier(n_neighbors=5, weights="uniform", algorithm="auto",
            leaf_size=30, p=2, metric="minkowski", metric_params=None)
    elif model == 'BG':
        clsfr = BaggingClassifier(base_estimator=MLPClassifier())
    elif model == 'ET':
        clsfr = ExtraTreesClassifier()
    elif model == 'RF':
        clsfr = RandomForestClassifier()
    elif model == 'ST':
        estimators = [
            ('MLP',MLPClassifier()),
            ('RF',RandomForestClassifier()),
            ('XG',XGBClassifier()),
            ('ADA',AdaBoostClassifier())
        ]
        clsfr = StackingClassifier(estimators=estimators)
    elif model == 'NSVC':
        clsfr = NuSVC()
    elif model == 'LSVC':
        clsfr = LinearSVC()
    elif model == 'ST2':
        estimators = [
            XGBClassifier(),
            AdaBoostClassifier(),
            RandomForestClassifier(),
            MLPClassifier()]
        clsfr = StackingCVClassifier(classifiers = estimators, meta_classifier = MLPClassifier())
    elif model == 'MLP':
        clsfr = MLPClassifier(learning_rate='adaptive', max_iter=1000)
    elif model == 'GB':
        clsfr = GradientBoostingClassifier()

    clsfr.fit(X_train,y_train)
    return clsfr

if __name__ == "__main__":
    main()