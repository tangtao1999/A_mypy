import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2


# plt.figure()
# plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2, linewidth=2.0)
plt.plot(x, y1, color='red', linestyle='--')
plt.xlim(-1, 2)
plt.ylim(-2, 3)
plt.xlabel('i ma x')
plt.ylabel('i am y')
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1, 1.22, 3], ['really good', r'$good$', 'bad', 'normal'])

plt.show()
