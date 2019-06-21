import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b

node3 = tf.add(node1, node2)

sess = tf.Session()

print("sess.run(node1, node2) : ", sess.run([node1, node2]))
print("sess.run(node3) : ", sess.run(node3))
print("\n\n")
print(sess.run(adder_node))
print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))