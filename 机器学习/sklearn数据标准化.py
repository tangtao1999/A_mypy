from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
# print(preprocessing.scale(a))

X, y = make_classification(n_samples=300, n_features=2, n_redundant=0, n_informative=2,
                           random_state=22, n_clusters_per_class=1, scale=100)
# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.show()


X = preprocessing.minmax_scale(X, feature_range=(0, 1))  # 预测准确度大大提高
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
