import tensorflow as tf
import numpy as np
import subprocess

save_file = './test.ckpt'

if __name__ == '__main__':
    proc = subprocess.Popen(["sbatch", "job.mpi"],stderr=subprocess.PIPE)
    while True:
        line = proc.stderr.readline()
        line1 = str(line).split()
        if not line:
            break 
file_num = line1[-1]
if __name__ == '__main__':
    proc = subprocess.Popen(["cat", "job."+file_num+".out"],stderr=subprocess.PIPE)
    while True:
        line = proc.stderr.readline()
        line1 = str(line).split()
        if not line:
            break
        print(line1)


x_data = np.array([[]], dtype=np.float32)
y_data = np.array([[]], dtype=np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([12, 12]), name='weight1')
b1 = tf.Variable(tf.random_normal([12]), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([12, 12]), name='weight2')
b2 = tf.Variable(tf.random_normal([12]), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([12, 12]), name='weight3')
b3 = tf.Variable(tf.random_normal([12]), name='bias3')
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_normal([12, 12]), name='weight4')
b4 = tf.Variable(tf.random_normal([12]), name='bias4')
layer4 = tf.nn.relu(tf.matmul(layer3, W4) + b4)

W5 = tf.Variable(tf.random_normal([12, 1]), name='weight5')
b5 = tf.Variable(tf.random_normal([1]), name='bias5')
output = tf.nn.relu(tf.matmul(layer4, W5) + b5)

loss = tf.square(Y - output)
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

saver =tf.train.Saver()
 
with tf.Session() as sess:
    # saver.restore(sess, save_file)
    sess.run(tf.global_variables_initializer())
    print(sess.run(W1))
    for step in range(1001):
        _, cost_val = sess.run([train, loss], feed_dict={X: x_data, Y: y_data})
        if step % 100 == 0:
            print(step, cost_val)

    # Accuracy report
    h, p, a, w1, w2 = sess.run(
        [output, predicted, accuracy, W1, W2], feed_dict={X: x_data, Y: y_data}
    )

    saver.save(sess,save_file)