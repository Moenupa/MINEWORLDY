import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=340, max_depth=9, random_state=0, min_samples_split=2, min_samples_leaf=2, min_weight_fraction_leaf=0)

X_train = pd.read_csv(open("dataset_processed.csv")).loc[
    :890,
    ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    ]
y_train = pd.read_csv(open("dataset_processed_csv")).loc[:890, "Survived"]

X_test = pd.read_csv(open("dataset_processed_csv")).loc[
    890:,
    ["PassengerId", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
    ]

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

result = pd.concat([X_test.loc[:, "PassengerId"], pd.DataFrame(y_pred)], ignore_index=True)
#result.tocsv("RF_output.csv")