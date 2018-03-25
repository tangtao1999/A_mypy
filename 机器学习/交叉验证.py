from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.cross_validation import cross_val_score

iris = load_iris()
X = iris.data
y = iris.target

# x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=4)
#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(x_train, y_train)
# print(knn.score(x_test, y_test))

# knn = KNeighborsClassifier(n_neighbors=5)
# scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')  # 平均误差
# print(scores.mean())

k_range = range(1, 31)
k_score = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')
    k_score.append(scores.mean())

plt.plot(k_range, k_score)
plt.xlabel('value of K of knn')
plt.ylabel('accuracy')
plt.show()

