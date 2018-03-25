from sklearn import svm
from sklearn import datasets
import pickle  # 1
from sklearn.externals import joblib  # 2

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X, y)

# save 1

# with open('save/clf.pickle', 'wb') as f:
#     pickle.dump(clf, f)
#
# with open('save/clf.pickle', 'rb') as f:
#     clf2 = pickle.load(f)
#     print(clf2.predict(X[0:1]))


# save 2
joblib.dump(clf, 'save/clf.pkl')
clf3 = joblib.load('save/clf.pkl')
print(clf3.predict(X[0:1]))
