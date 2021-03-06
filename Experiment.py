# -------------------------------------------------------------
# regression with all the other types of regression models
# import
from sklearn import linear_model
from sklearn import svm
from sklearn.metrics import r2_score,mean_squared_error

classifiers = [
    svm.SVR(),
    linear_model.SGDRegressor(),
    linear_model.BayesianRidge(),
    linear_model.LassoLars(),
    linear_model.ARDRegression(),
    linear_model.PassiveAggressiveRegressor(),
    linear_model.TheilSenRegressor(),
    linear_model.LinearRegression()]

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import dataset
data = pd.read_csv(r"C:\Users\slaik\Documents\Sandeep\Scripts\Python\PycharmProjects\DLMLPYRTRAINING\Day3\Data\Logistic_regression1.csv")

#Example: various way of fetching data from pandas
X = data.loc[0:len(data)-2, "Height"]
print(X)
X = data["Height"][:-1]
print(X)
X = data[:-1]["Height"]
print(X)

weight_val = [np.log(i/(1-i)) for i in data["Weight"].values]

# fetch the data
Train_F = data[:-1]["Height"].values.reshape(-1, 1)
print(Train_F)
plt.plot(Train_F, "b.")
Train_T = data[:-1]["Weight"].values.reshape(-1, 1)
print(Train_T)
plt.plot(Train_T, "bo")

Test_F = data[-1:]["Height"].values.reshape(-1, 1)
print(Test_F)
plt.plot(len(Train_F), Test_F, "g.")
Test_T = data[-1:]["Weight"].values.reshape(-1, 1)
print(Test_T)
plt.plot(len(Train_T), Test_T, "go")

for item in classifiers:
    # build model
    model = item

    # train model
    try:
        model.fit(Train_F, Train_T)
    except:
        model.fit(Train_F)

    # score model
    score = model.score(Train_F, Train_T)

    # predict
    predict = model.predict(Test_F)

    #error%
    mse = mean_squared_error(Test_T,predict)
    r2 = r2_score(Test_T,predict)

    # print everything
    print(item)
    print("score\n", score)
    print("predict:\n", predict)
    print("actual:\n", Test_T)
    print("mean_squared_error:\n",mse)
    print("R2:\n",r2)

#show plot
plt.show()

# ---------------------------------------------------------------
# classification with logisticregression
# from sklearn.linear_model import LogisticRegression
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# data = pd.read_csv("Data/Logistic_classification1.csv")
#
# #first we'll have to convert the strings "No" and "Yes" to numeric values
# data.loc[data["default"] == "No", "default"] = 0
# data.loc[data["default"] == "Yes", "default"] = 1
# X = data["balance"].values.reshape(-1, 1)
# Y = data["default"].values.reshape(-1, 1)
#
# x_test = data["balance"][-1:].values.reshape(-1, 1)
# y_test = data["default"][:-1].values.reshape(-1, 1)
#
# LogR = LogisticRegression()
# LogR.fit(X, np.ravel(Y.astype(int)))
# score = LogR.score(X, np.ravel(Y.astype(int)))
# print("Score:\n", score)
#
# coeff = LogR.coef_
# intercept = LogR.intercept_
# print("Coeff\n", coeff)
# print("Intercept\n", intercept)
#
# predict = LogR.predict(x_test)
# predict_proba_class = LogR.predict_proba(x_test)
# print("Prediction Feature:\n", x_test)
# print("Prediction Value:\n", predict)
# print("Prediction Class:\n", predict_proba_class)
#
# def model_plot(x):
#     return 1/(1+np.exp(-x))
#
# points = [intercept+coeff*i for i in X.ravel()]
# points = np.ravel([model_plot(i) for i in points])
# plt.plot(points,'g')
#
# #matplotlib scatter funcion w/ logistic regression
# plt.plot(X,'rx')
# plt.plot(Y,'bo')
# plt.xlabel("Credit Balance")
# plt.ylabel("Probability of Default")
# # https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
# plt.legend(["Logistic Regression Model","X","Y"],
#            loc="lower right", fontsize='small')
# plt.show()



