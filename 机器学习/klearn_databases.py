from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

load_data = datasets.load_boston()
data_X = load_data.data
data_y = load_data.target

x_train, x_test, y_train, y_test = train_test_split(data_X, data_y, test_size=0.3)

model = LinearRegression()
model.fit(x_train, y_train)
# print(model.predict(x_test))
# print(y_test)

# X, y = datasets.make_regression(n_samples=100, n_features=1, noise=10, n_targets=1)
# plt.scatter(X, y)
# plt.show()

print(model.coef_)  # y=0.1*x + 0.3    0.1 x的参数
print(model.intercept_)  # 0.3  结尾参数
print(model.get_params())
print(model.score(x_test, y_test))  # R^2  打分  %

