from sklearn.metrics import precision_score
import matplotlib.pyplot as plt
import pandas as pd

dir = "C:\\Github\\MINEWORLDY\\titanic\\"
y_test = pd.read_csv(open(dir + "gender_submission.csv")).loc[:,"Survived"]
y_pred = pd.read_csv(open(dir + "output\\NB_output.csv")).loc[:,"Survived"]

print(precision_score(y_test, y_pred))