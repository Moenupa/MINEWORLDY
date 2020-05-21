# -*- coding: utf-8 -*-
'''
@Author: Moenupa

2019/12/19 18:30
'''
#plz use the filename as your input
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, LassoLarsCV, ElasticNetCV, SGDRegressor
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor, ExtraTreesRegressor, RandomForestRegressor, StackingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR, LinearSVR, NuSVR
from sklearn.model_selection import train_test_split, GridSearchCV
from mlxtend.regressor import StackingCVRegressor
from sklearn import metrics
from sklearn.neural_network import MLPRegressor
models = {
    'ADA': 'AdaBoostRegressor',
    'BG': 'BaggingRegressor',
    'DT': 'DecisionTreeRegressor',
    'EN': 'ElasticNetCV',
    'ET': 'ExtraTreesRegressor',
    'GB': 'GradientBoostingRegressor',
    'KN': 'KNeighborsRegressor',
    'LLS': 'LassoLarsCV',
    'LR': 'LinearRegression',
    'LS': 'LassoCV',
    'NN': 'Neural Network',
    'NSVR': 'NuSupportVectorRegressor',
    'RD': 'RidgeCV',
    'RF': 'RandomForestRegressor',
    'ST': 'StackingRegressor',
    'ST2': 'StackingCVRegressor',
    'XG': 'XGBRegressor',
    'SVR':'SVR'
    }
def cpn_sep():
    print('-'*8)
def func_procs():
    global depth_whole, depth_hist, depth_valid
    #input
    while True:
        try:
            name = input('Stock Name:\t')
            #'D:\Drive_comp\Data\HK2800_O.csv'
            depth_hist = int(input('Train Size:\t'))
            cpn_sep()

        except ValueError:
            cpn_sep()

    #process data
        try:
            dataset = pd.read_csv(open('{0}.csv'.format(name.upper()))).dropna().loc[:,['Date','Close']]
            break
        except FileNotFoundError:
            continue
    data = dataset['Close'].tolist()
    depth_whole = len(data)
    depth_valid = depth_whole - depth_hist

    #real data table
    dict_df = {'y-{0}'.format(depth_hist-iter_y):data[iter_y:iter_y+depth_valid] for iter_y in range(depth_hist+1)}
    df = pd.DataFrame(dict_df)
    df.insert(0, 'Date', dataset['Date'].tolist()[depth_hist:])

    return dataset, df

def func_split(df):
    global train_s, train_e, test_s, test_e
    print('\tValid Depth:\t'+str(depth_valid))
    print('\tWhole Depth:\t'+str(depth_whole))
    while True:
        try:
            print('\tTrain Start:End, Test Start:End')
            train_s, train_e, test_s, test_e = map(int,input('Input Range:\t').split(' '))
            if 0<=train_s<=depth_valid and 0<=train_e<=depth_valid and 0<=test_s<=depth_valid and 0<=test_e<=depth_valid and train_s<train_e and test_s<test_e:
                break
            else:
                continue
        except ValueError:
            continue

    X_train, y_train, X_test, y_test = df.iloc[train_s:train_e,1:-1].values, df.iloc[train_s:train_e,-1].values, df.iloc[test_s:test_e,1:-1].values, df.iloc[test_s:test_e,-1].values

    cpn_sep()

    return X_train, y_train, X_test, y_test

def main():
    global model, models
    while True:
        dataset, df = func_procs()
        X_train, y_train, X_test, y_test = func_split(df)
        print(df)
        avg_y_test = y_test.mean()
        print('Average Test Value:\t{0}'.format(avg_y_test))
        cpn_sep()

        dict_record = {}
        report = pd.DataFrame(columns = ['EVS', 'MSE', 'RMSE','MAE', 'R2','R2-adj','MAPE','CVC'])
        for model in models.keys():
            reg = func_model(X_train,y_train)
            y_pred = reg.predict(X_test)
            dict_record[model] = y_pred
            temp_list = func_error(y_test,y_pred)
            report.loc[models[model]] = temp_list
        cpn_sep()

        print(report)
        cpn_sep()

        func_select()
        cpn_sep()
        while model != 'E':
            y_pred = dict_record[model]
            func_show(dataset,y_train,y_test,y_pred)
            func_select()

def func_select():
    global model, models
    while True:
        for key in sorted(models.keys()):
            print('\t{0}: \t{1}'.format(key,models[key]))
        model = input('Select Regressor: \t').upper()

        if model in models.keys():
            break
        elif model == 'E':
            break
        else:
            continue
def func_model(X_train,y_train):
    '''
    Process one model by training data
    Input: X_train,y_train
    Output: regressor by the need
    '''
    global model
    if model == 'XG':
        reg = XGBRegressor()
    elif model == 'RD':
        reg = RidgeCV(alphas=(0.1, 1.0, 10.0), fit_intercept=True, normalize=False,
              scoring=None, cv=5, gcv_mode=None, store_cv_values=False)
    elif model == 'LS':
        reg = LassoCV(max_iter = 10**8)
    elif model == 'LLS':
        reg = LassoLarsCV()
    elif model == 'ADA':
        reg = AdaBoostRegressor()
    elif model == 'EN':
        reg = ElasticNetCV()
    elif model == 'DT':
        reg = DecisionTreeRegressor(criterion="mse", splitter="best", max_depth=None,
            min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
            max_features=None, random_state=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None)
    elif model == 'SVR':
        reg = SVR()
    elif model == 'KN':
        reg = KNeighborsRegressor(n_neighbors=5, weights="uniform", algorithm="auto",
            leaf_size=30, p=2, metric="minkowski", metric_params=None)
    elif model == 'BG':
        reg = BaggingRegressor(base_estimator=LassoCV(max_iter = 10**8), n_estimators=10, max_samples=1.0,
            max_features=1.0, bootstrap=True, bootstrap_features=False,
            oob_score=False, warm_start=True, random_state=None, verbose=0)
    elif model == 'GB':
        reg = GradientBoostingRegressor(loss="ls", learning_rate=0.1, n_estimators=100,
            subsample=1.0, criterion="friedman_mse", min_samples_split=2,
            min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_depth=3,
            min_impurity_decrease=0.0, min_impurity_split=None, init=None,
            random_state=None, max_features=None, alpha=0.9, verbose=0,
            max_leaf_nodes=None, warm_start=False,
            validation_fraction=0.1, n_iter_no_change=None, tol=0.0001)
    elif model == 'ET':
        reg = ExtraTreesRegressor()
    elif model == 'RF':
        reg = RandomForestRegressor()
    elif model == 'ST':
        estimators = [
            ('ADA',AdaBoostRegressor()),
            ('LS',LassoCV(max_iter = 10**8)),
            ('LLS',LassoLarsCV()),
            ('RD',RidgeCV()),
            ('XG',XGBRegressor()),
            ('KN',KNeighborsRegressor())
        ]
        reg = StackingRegressor(estimators=estimators)
    elif model == 'NSVR':
        reg = NuSVR()
    elif model == 'ST2':
        estimators = [RidgeCV(), AdaBoostRegressor(), LassoCV(max_iter = 10**8), LassoLarsCV(), XGBRegressor(), KNeighborsRegressor(),ElasticNetCV()]
        reg = StackingCVRegressor(regressors = estimators, meta_regressor = LassoCV(max_iter = 10**8))
    elif model == 'LR':
        reg = LinearRegression()
    elif model == 'NN':
        reg = MLPRegressor(learning_rate = 'adaptive', max_iter = 1000)
    reg.fit(X_train,y_train)
    return reg
def func_error(y_test,y_pred):
    global depth_hist, test_e, test_s
    mae = metrics.mean_absolute_error(y_test,y_pred)
    mse = metrics.mean_squared_error(y_test,y_pred)
    r2 = metrics.r2_score(y_test,y_pred)
    evs = metrics.explained_variance_score(y_test,y_pred)
    r2_adjusted = 1-(1-r2)*(test_e-test_s-1)/(test_e-test_s-depth_hist-1)
    mape = np.mean(np.abs((y_test - y_pred)/y_test*100))
    cc = np.corrcoef(y_test,y_pred)[0][1]
    return [evs,mse,mse**0.5,mae,r2,r2_adjusted, mape,cc]
def func_show(dataset,y_train,y_test,y_pred):
    '''
    '''
    global depth_whole, train_s, train_e, test_s, test_e, depth_hist
    plt.plot(list(range(depth_whole)), dataset['Close'].tolist(), 'y:', label = 'All Historical Data')
    plt.plot(list(range(train_s+depth_hist,train_e+depth_hist)), y_train, 'g-', label = 'Training Data')
    plt.plot(list(range(test_s+depth_hist,test_e+depth_hist)), y_test, 'b-', label = 'Testing Data')
    plt.plot(list(range(test_s+depth_hist,test_e+depth_hist)), y_pred, 'r-', label = 'Predicting Data')
    plt.legend(loc = 'best')
    plt.show()
    cpn_sep()
if __name__ == "__main__":
    main()