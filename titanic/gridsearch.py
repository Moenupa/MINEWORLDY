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
    dir = "C:\\Github\\MINEWORLDY\\titanic\\"
    X_train = pd.read_csv(dir + "X_train_proc.csv")
    y_train = pd.read_csv(open(dir + "train.csv")).loc[:, "Survived"]
    param_dict = {
        'n_estimators':[340],
        'max_depth':[9],
        'random_state': [0],
        'min_samples_split': [2],
        'min_samples_leaf': [2],
        'min_weight_fraction_leaf': [0],
    }
    classifier = RandomForestClassifier()
    grid = GridSearchCV(classifier, param_dict, scoring = 'roc_auc', n_jobs = -1, refit=True)
    grid.fit(X_train, y_train)
    print(grid.best_score_)
    print(grid.best_params_)

if __name__ == "__main__":
    main()
