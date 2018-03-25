from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn.learning_curve import validation_curve  # 画图找出最好的参数
from sklearn.svm import SVC

digits = load_digits()
X = digits.data
y = digits.target

param_range = np.logspace(-6, -2.3, 5)
train_sizes, train_loss, test_loss = validation_curve(SVC(), X, y, param_name='gamma', param_range=param_range, cv=10,
                                                      scoring='neg_mean_squared_error')
train_loss_mean = -np.mean(train_loss, axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(param_range, train_loss_mean, 'o-', color='r', label='training')
plt.plot(param_range, test_loss_mean, 'o-', color='g', label='crossing-validation')
plt.xlabel("gamma")
plt.ylabel("loss")
plt.legend(loc="best")
plt.show()

# 未完成 scoring='neg_mean_squared_error')
# ValueError: not enough values to unpack (expected 3, got 2)
