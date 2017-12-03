import tensorflow as tf

sess=tf.InteractiveSession()
a=tf.constant(10)
b=tf.constant(32)
print(sess.run(a+b))




