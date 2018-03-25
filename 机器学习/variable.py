import tensorflow as tf
state = tf.Variable(0, name='counter')
# 常量
one = tf.constant(1)

# 定义加法步骤，但并没有直接计算
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
