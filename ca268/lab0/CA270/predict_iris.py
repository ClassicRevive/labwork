
''' use classification algorithms to predict the species of
    an iris plant '''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


df = pd.read_csv('Iris.csv', index_col = 0)


# first clean up Species columm by getting rid of "Iris-"
df[['Species']] = df['Species'].str.split("-").str.get(1)
# print(df)

# split data into labels and attributes
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size = 0.2)
# X_train -> y_train, X_test -> y_test
X_train.convert_dtypes()

# normalize the values
def stochastic_scaling(df):
    df_scaled = df.copy()

    for column in df_scaled.columns:
        c = df_scaled[column]
        df_scaled[column] = (c - c.min())/c.abs().max()

    return df_scaled

X_train, X_test = stochastic_scaling(X_train), stochastic_scaling(X_test)


# implementing KNN algorithim with K = 5
classifier = KNeighborsClassifier(n_neighbors=5)

classifier.fit(X_train, y_train)

# predict
y_pred = classifier.predict(X_test)

# test accuracy of algorithm using prediction score
# score = n_correct / n_predictions

score = sum(y_pred == y_test)
print("prediction score: {} / {} ({:.4f})".format(score,
                                             len(y_pred),
                                             score/len(y_pred)))

# now using sklearn's classification_report function
print(classification_report(y_pred, y_test))

# I assumed K = 5 as this is a typical value. Now I test
# the error rate of a few K values to achieve maximum precision
error = []

# calculating %error for K values between 1 and 30
for i in range(1, 30):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))

plt.figure()
plt.plot(range(1, 30), error,
         linestyle = "dashed",
         mfc = "blue",
         ms = 10)
plt.title("error rate of kNN")
plt.xlabel("K value")
plt.ylabel("%error")
plt.show()
