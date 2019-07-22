import tensorflow as tf
import numpy as np
import subprocess
import pickle
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



with open('data_x.p', 'rb') as file:
    save_x = pickle.load(file)
with open('data_y.p', 'rb') as file:
    save_y = pickle.load(file)

x_data = np.array(save_x[:(int(len(save_x)*0.7))], dtype=np.float64)
y_data = np.array(save_y[:(int(len(save_y)*0.7))], dtype=np.float64)

test_x_data = np.array(save_x[(int(len(save_x)*0.7)):], dtype=np.float64)
test_y_data = np.array(save_y[(int(len(save_y)*0.7)):], dtype=np.float64)

X = tf.placeholder(tf.float64, [None, 16])
Y = tf.placeholder(tf.float64, [None, 1])

W1 = tf.Variable(tf.random_normal([16, 50], dtype=np.float64), name='weight1')
b1 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias1')
layer1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight2')
b2 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias2')
layer2 = tf.nn.relu(tf.matmul(layer1, W2) + b2)

W3 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight3')
b3 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias3')
layer3 = tf.nn.relu(tf.matmul(layer2, W3) + b3)

W4 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight4')
b4 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias4')
layer4 = tf.nn.relu(tf.matmul(layer3, W4) + b4)

W5 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight5')
b5 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias5')
layer5 = tf.nn.relu(tf.matmul(layer4, W5) + b5)

W6 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight6')
b6 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias6')
layer6 = tf.nn.relu(tf.matmul(layer5, W6) + b6)

W7 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight7')
b7 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias7')
layer7 = tf.nn.relu(tf.matmul(layer6, W7) + b7)

W8 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight8')
b8 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias8')
layer8 = tf.nn.relu(tf.matmul(layer7, W8) + b8)

W9 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight9')
b9 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias9')
layer9 = tf.nn.relu(tf.matmul(layer8, W9) + b9)

W10 = tf.Variable(tf.random_normal([50, 50], dtype=np.float64), name='weight10')
b10 = tf.Variable(tf.random_normal([50], dtype=np.float64), name='bias10')
layer10 = tf.nn.relu(tf.matmul(layer9, W10) + b10)

W11 = tf.Variable(tf.random_normal([50, 1], dtype=np.float64), name='weight11')
b11 = tf.Variable(tf.random_normal([1], dtype=np.float64), name='bias11')
output = tf.matmul(layer10, W11) + b11

loss = tf.multiply(tf.square(Y - output),tf.constant(0.5, dtype=np.float64))
train = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

#predicted = tf.cast(output > 0.5, dtype=tf.float64)
accuracy = Y/output*100
print(W11)
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #saver.restore(sess, "new_model.ckpt")
    for a in range(1):
        for i in range(len(x_data)):
            for step in range(31):
                _, cost_val, out= sess.run([train, loss, output], feed_dict={X :[x_data[i]], Y : [y_data[i]]})
                if step % 10 == 0:
                    print(step, cost_val, out)
    save_path = saver.save(sess, "new_model.ckpt")
    for i in range(len(test_x_data)):
        out, a =sess.run([output, accuracy], feed_dict={X : [test_x_data[i]], Y : [test_y_data[i]]})
        print(f"output : {out}\naccuracy : {a}%")