from sklearn import svm

from sklearn import neighbors,linear_model
import numpy as np
import sklearn.preprocessing as preprocessing

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import sys
print(sys.path)
# sys.path.append("g:\\NLP\\属性抽取\\elm_ml-bert")
import ensemble
"""load data and preprocess
"""
import pickle
X_train = np.load('../data/birth_place_trainx.npy')
X_test=np.load('../data/birth_place_testx.npy')
with open('../data/birth_place_trainy.pickle','rb') as f:
    y_train=pickle.load(f)
with open('../data/birth_place_testy.pickle','rb') as f:
    y_test=pickle.load(f)
y_train=np.array(y_train)
y_test=np.array(y_test)

# index=np.array(y_train,dtype='bool')
# train1=X_train[index]
# test1=y_train[index]

# t_y=np.apply_along_axis(lambda a:~a,axis=0,arr=index)
# train0=X_train[t_y]
# train0=train0[:(train1.shape[0]*2)]
# test0=y_train[t_y]
# test0=test0[:(test1.shape[0]*2)]
# X_train=np.concatenate((train0,train1),axis=0)
# y_train=np.concatenate((test0,test1),axis=0)

X_train=preprocessing.normalize(X_train, norm='l2')
X_test=preprocessing.normalize(X_test, norm='l2')

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)
print(X_train.shape)
print(y_train.shape)

"""basic ml methods
"""
# C=1.0
# svc=svm.SVC(kernel='linear', C=C)
# rbf_svc = svm.SVC(kernel='rbf', gamma=0.5, C=C)
# poly_svc = svm.SVC(kernel='poly', degree=3, C=C)
# lin_svc = svm.LinearSVC(C=C)
# knn=neighbors.KNeighborsClassifier(3)
# lr = linear_model.LogisticRegression()
# GaussianProcess=GaussianProcessClassifier(1.0 * RBF(1.0))
# DecisionTree=DecisionTreeClassifier(max_depth=5)
# RandomForest=RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)

MLP=MLPClassifier(activation="logistic",random_state=2)
MLP1=MLPClassifier(alpha=1,activation="logistic",random_state=2)
#
# AdaBoost=AdaBoostClassifier()
# Gaussian=GaussianNB()
# QuadraticDiscriminant=QuadraticDiscriminantAnalysis()
fun_list=[
    # ("svc",svc),
    # ("rbf_svc",rbf_svc),
    # ("poly_svc",poly_svc),
    # ("lin_svc",lin_svc),
    # ("knn",knn),
    # ("lr",lr),
    # ("GaussianProcess",GaussianProcess),
    # ("DecisionTree",DecisionTree),
    # ("RandomForest",RandomForest),
    ("MLP",MLP),
    ("MLP1",MLP1),

    # ("AdaBoost",AdaBoost),
    # ("Naive Bayes",Gaussian),
    # ("QDA",QuadraticDiscriminant)

]
"""ensemle methods
"""
m=ensemble.Ensemble(fun_list)
m.fit(X_train,y_train)
# m.predict_prob(X_test,y=y_test)
m.predict(X_test,y=y_test)

# m.vote(y_test)