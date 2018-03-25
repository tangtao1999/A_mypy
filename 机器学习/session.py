import tensorflow as tf

ma1 = tf.constant([[3, 3]])
ma2 = tf.constant([[2], [2]])
res = tf.matmul(ma1, ma2)

# 因为 product 不是直接计算的步骤,
# 所以我们会要使用 Session 来激活 product 并得到计算结果.

sess = tf.Session()
result = sess.run(res)
print(result)
sess.close()

with tf.Session() as sess:
    result2 = sess.run(res)
    print(result2)
