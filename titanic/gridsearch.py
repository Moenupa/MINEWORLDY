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

def main():

    X_train = pd.read_csv("C:\\Github\\MINEWORLDY\\titanic\\X_train_proc.csv")
    y_train = pd.read_csv(open("C:\\Github\\MINEWORLDY\\titanic\\train.csv")).loc[:, "Survived"]
    param_dict = {
        'n_estimators':[400],
        'max_depth':[6],
        'learning_rate':[0.05],
        'subsample':[0.9],
        'colsample_bytree':[0.65],
        'min_child_weight':[11]
    }
    classifier = XGBClassifier()
    grid = GridSearchCV(classifier, param_dict, scoring = 'roc_auc', n_jobs = -1, refit=True)
    grid.fit(X_train, y_train)
    print(grid.best_score_)
    print(grid.best_params_)

if __name__ == "__main__":
    main()
