import tensorflow as tf
import numpy as np
import subprocess
import time

# result_x = []
# result_y = []
# x = []
# y = 0.0

# #Start the benchmark for the event.
# if __name__ == '__main__':
#     proc = subprocess.Popen(["sbatch", "event.mpi"],stdout=subprocess.PIPE)
#     while True:
#         line = proc.stdout.readline()
#         if not line:break
#         event_out = str(line).split()
# #Start the benchmark for the power
# if __name__ == '__main__':
#     proc = subprocess.Popen(["sbatch", "power.mpi"],stdout=subprocess.PIPE)
#     while True:
#         line = proc.stdout.readline()
#         if not line:break
#         power_out = str(line).split()
# file_num = event_out[-1][0:3]
# time.sleep(30)

# #Start indexing for events
# if __name__ == '__main__':
#     proc = subprocess.Popen(["cat", "event."+file_num+".out"],stdout=subprocess.PIPE)
#     while True:
#         line = proc.stdout.readline()
#         if not line:
#             break
#         event_out = str(line).split()
#         result_x.extend(event_out)
# print(result_x)
# event = [
#     'INST_RETIRED.ANY',
#     'CPU_CLK_UNHALTED.THREAD_ANY',
#     'UOPS_ISSUED.ANY',
#     'RESOURCE_STALLS.AN',
#     'BR_MISP_RETIRED.ALL_BRANCHES',
#     'BR_INST_RETIRED.ALL_BRANCHES',
#     'FP_ARITH_INST_RETIRED.128B_PACKED_DOUBLE',
#     'FP_ARITH_INST_RETIRED.128B_PACKED_SINGLE',
#     'FP_ARITH_INST_RETIRED.256B_PACKED_DOUBLE',
#     'FP_ARITH_INST_RETIRED.256B_PACKED_SINGLE',
#     'FP_ARITH_INST_RETIRED.SCALAR_DOUBLE',
#     'FP_ARITH_INST_RETIRED.SCALAR_SINGLE',
#     'MEM_LOAD_RETIRED.L1_HIT',
#     'L1-dcache-load-misses',
#     'LLC-loads',
#     'LLC-load-misses',
# ]
# for i in range(len(result_x)):
#     for j in range(len(event)):
#         if result_x[i] == event[j]:
#             x.append(result_x[i - 1])
# print(x)
# file_num = power_out[-1][0:3]
# time.sleep(20)

# #Start indexing for power
# if __name__ == '__main__':
#     proc = subprocess.Popen(["cat", "power."+file_num+".out"],stdout=subprocess.PIPE)
#     while True:
#         line = proc.stdout.readline()
#         if not line:
#             break
#         power_out = str(line).split()
#         result_y.extend(power_out)
# print(result_y)
# for i in range(len(result_y)):
#     if result_y[i] == 'Joules':
#         y += float(result_y[i - 1])
# print(y) [21270860401, 31304543910, 23978033126, 15130389, 2664839378, 1145, 969, 794, 711, 2689356984, 1164, 5112524040, 472483749, 28186108, 15208761],[24135155239, 44630572465, 26839082850, 23604814, 3108525614, 1025, 1274, 918, 986, 2687769161, 893, 6166127495, 476734830, 31199717, 18153762],[23951264340, 44610788181, 26667253456, 23820561, 3102241949, 1447, 1408, 863, 956, 2674795042, 917, 6150905971, 469650696, 31458782, 17938934]
#,[23995391813, 44632741074, 26846805309, 24559176, 3113719460, 1739, 1350, 1407, 1488, 2695066594, 1740, 6143002620, 476909287, 31778611, 18187921],[23854657511, 44508816569, 26634761205, 24068107, 3069889307, 369, 546, 527, 578, 2696253688, 495, 6072948201, 469001934, 31499480, 18170348]
# [23670398989,44555917060,26480458972,23488488,3070777030,710,798,895,842,2688122717,876,6028121392,470577326,31122558,18114779]
#,[50.75],[55.17],[120.46000000000001],[120.2],[431.82] [54.79]

tf.set_random_seed(777)

x_data = np.array([[21270860401/31304543910, 23978033126, 15130389, 2664839378/1145, 969, 794, 711, 2689356984, 1164, 5112524040, 472483749, 28186108, 15208761],[24135155239/44630572465, 26839082850, 23604814, 3108525614/1025, 1274, 918, 986, 2687769161, 893, 6166127495, 476734830, 31199717, 18153762],[23951264340/44610788181, 26667253456, 23820561, 3102241949/1447, 1408, 863, 956, 2674795042, 917, 6150905971, 469650696, 31458782, 17938934]
,[23995391813/44632741074, 26846805309, 24559176, 3113719460/1739, 1350, 1407, 1488, 2695066594, 1740, 6143002620, 476909287, 31778611, 18187921],[23854657511/44508816569, 26634761205, 24068107, 3069889307/369, 546, 527, 578, 2696253688, 495, 6072948201, 469001934, 31499480, 18170348],[23721312912/44508275525, 26572350949, 23443873, 3062504298/642, 588, 531, 494, 2687132631, 828, 6034708815, 472912813, 30836546, 18158306]], dtype=np.float64)
y_data = np.array([[50.75],[55.17],[120.46000000000001],[120.2],[431.82],[432.82]], dtype=np.float64)

test_x_data = np.array([[24157488648/44711151366, 26891689241, 25050019, 3110384063/1012, 1125, 1175, 1591, 2675505956, 1791, 6160913070, 476629809, 30799495, 17967602],[23995391813/44632741074, 26846805309, 24559176, 3113719460/1739, 1350, 1407, 1488, 2695066594, 1740, 6143002620, 476909287, 31778611, 18187921]], dtype=np.float64)
test_y_data = np.array([[431.6],[120.2]], dtype=np.float64)

X = tf.placeholder(tf.float64, [13])
Y = tf.placeholder(tf.float64, [1])

W1 = tf.Variable(tf.random_normal([13, 13], dtype=np.float64), name='weight1')
b1 = tf.Variable(tf.random_normal([13], dtype=np.float64), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([13, 13], dtype=np.float64), name='weight2')
b2 = tf.Variable(tf.random_normal([13], dtype=np.float64), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([13, 13], dtype=np.float64), name='weight3')
b3 = tf.Variable(tf.random_normal([13], dtype=np.float64), name='bias3')
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_normal([13, 13], dtype=np.float64), name='weight4')
b4 = tf.Variable(tf.random_normal([13], dtype=np.float64), name='bias4')
layer4 = tf.nn.relu(tf.matmul(layer3, W4) + b4)

W5 = tf.Variable(tf.random_normal([13, 1], dtype=np.float64), name='weight5')
b5 = tf.Variable(tf.random_normal([1], dtype=np.float64), name='bias5')
output = tf.nn.relu(tf.matmul(layer4, W5) + b5)

loss = tf.square(Y - output) / 2
train = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

#predicted = tf.cast(output > 0.5, dtype=tf.float64)
accuracy = Y/output*100
print(x_data[1])
#saver = tf.train.Saver({'weitght1': W1, 'bias1': b1,'weitght2': W2, 'bias2': b2,'weitght3': W3, 'bias3': b3,'weitght4': W4, 'bias4': b4,'weitght5': W5, 'bias5': b5})

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # saver.restore(sess, "test1.ckpt")
    for i in range(len(x_data)):
        for step in range(10001):
            _, cost_val = sess.run([train, loss], feed_dict={X : x_data[i], Y : y_data[i]})
            if step % 100 == 0:
                print(step, cost_val)
    #save_path = saver.save(sess, "test1.ckpt")
    out, layer, loss, a =sess.run([output, layer1, loss, accuracy], feed_dict={X : test_x_data, Y : test_y_data})
    print(f"output : {out}\n loss : {loss}\n accuracy : {a}%")