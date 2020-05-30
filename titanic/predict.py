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

def main():
    # saving processed X_train data
    X_train = pd.read_csv("C:\\Github\\MINEWORLDY\\titanic\\X_train_proc.csv")
    X_test = pd.read_csv("C:\\Github\\MINEWORLDY\\titanic\\X_test_proc.csv")
    models = ["XG"]
    # models = ["XG","ADA","BG","ET","RF","ST","KN","DT", "SVC", "LSVC", "NSVC", "ST2", "MLP", "GB"]
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
        clsfr = XGBClassifier(n_estimators=400,max_depth=6, learning_rate=0.05, subsample=0.9, colsample_bytree=0.65, min_child_weight=11)
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
        clsfr = BaggingClassifier(base_estimator=RandomForestClassifier())
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