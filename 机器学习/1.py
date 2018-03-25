import tensorflow as tf
import numpy as np

# create data
x_data = np.random.randn(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# create structure
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

# 优化器
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)     # 激活

for step in range(25):
    sess.run(train)
    if step % 5 == 0:
        print(step, sess.run(Weights), sess.run(biases))
