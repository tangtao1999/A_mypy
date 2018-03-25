from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


from first_step import *
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt


# model = LogisticRegression(C=1)
# model.fit(x_train, y_train)
# print(model.score(x_train, y_train))
# 0.804713
# x_train = x_train.drop(['Age'], axis=1)


# scores = cross_val_score(model, x_train, y_train, cv=5)
# print(scores.mean())
#  0.7912977

# 1.LogisticRegression
# c：正则化系数λ的倒数，float类型，默认为1.0。
# 必须是正浮点型数。像SVM一样，越小的数值表示越强的正则化。
# C_range = [10 ** k for k in range(-4, 4)]
# # print(C_range)
# C_scores = []
# for c in C_range:
#     model = LogisticRegression(C=c)
#     scores = cross_val_score(model, x_train, y_train, cv=10, scoring='accuracy')
#     C_scores.append(scores.mean())
# plt.plot(C_range, C_scores)
# plt.xlabel('values of C for Logistic')
# plt.ylabel('cross_validated accuracy')
# plt.show()
# 0.799

# 2.KNeighborsClassifier
# K值的选择与样本分布有关，一般选择一个较小的K值，
# 可以通过交叉验证来选择一个比较优的K值，默认值是5。
# k_range = range(1, 31)
# k_scores = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, x_train, y_train, cv=10, scoring='accuracy')
#     k_scores.append(scores.mean())
# plt.plot(k_range, k_scores)
# plt.xlabel('values of k for knn')
# plt.ylabel('cross_validated accuracy')
# plt.show()
# 0.702

# 3.SVC
#  gamma ： ‘rbf’,‘poly’ 和‘sigmoid’的核函数参数。默认是’auto’，则会选择1/n_features
#    float参数 默认为auto
#    核函数系数，只对‘rbf’,‘poly’,‘sigmod’有效。
#    如果gamma为auto，代表其值为样本特征数的倒数，即1/n_features.
# g_range = np.logspace(-6, 1, 5)
# g_scores = []
# for g in g_range:
#     svc = SVC(gamma=g)
#     scores = cross_val_score(svc, x_train, y_train, cv=10, scoring='accuracy')
#     g_scores.append(scores.mean())
# plt.plot(g_range, g_scores)
# plt.xlabel('values of g for SVC')
# plt.ylabel('cross_validated accuracy')
# plt.show()
# 0.70

# 4.random_forest
# random_forest = RandomForestClassifier(n_estimators=100)
# scores = cross_val_score(random_forest, x_train, y_train, cv=5)
# print(scores.mean())
# 0.81485

# n_estimators: 也就是弱学习器的最大迭代次数，或者说最大的弱学习器的个数。
# 一般来说n_estimators太小，容易欠拟合，n_estimators太大，又容易过拟合，默认是100。
# 主要需要关注的是 n_estimators，即RF最大的决策树个数。
# n_range = [1, 1000, 100]
# n_scores = []
# for n in n_range:
#     random_forest = RandomForestClassifier(n_estimators=n)
#     scores = cross_val_score(random_forest, x_train, y_train, cv=10, scoring='accuracy')
#     n_scores.append(scores.mean())
# plt.plot(n_range, n_scores)
# plt.xlabel('values of n for random_forest')
# plt.ylabel('cross_validated accuracy')
# plt.show()
# 0.81


