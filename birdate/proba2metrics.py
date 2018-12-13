import os
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import data_process

for k in range(1, 5):
    (_, x), (_, label) = data_process.data_gen(k)
    label = np.array(label)
    proba_filename = os.path.join('result', "test_results" + "_" + str(k) + ".tsv")
    r = np.loadtxt(proba_filename, dtype=float, delimiter="\t")
    predict = np.argmax(r, axis=1)
    with open("./result/error_sentences" + str(k) + ".txt", "w", encoding='utf-8') as f:
        fn = ""
        fp = ""
        for i in range(len(predict)):
            if label[i] != predict[i]:
                if label[i]:
                    fn += x[i]
                    fn = fn + "\n0          1\n" + "%.3f          %.3f\n" % (r[i][0], r[i][1])
                else:
                    fp += x[i]
                    fp = fp + "\n0          1\n" + "%.3f          %.3f\n" % (r[i][0], r[i][1])
        f.write("实际为1，预测为0\n")
        f.write(fn)
        f.write("实际为0，预测为1\n")
        f.write(fp)

    target_names = ['0', '1']
    print(classification_report(label, predict, target_names=target_names, digits=3))
    print(confusion_matrix(label, predict))
    with open("./result/res" + str(k) + ".txt", "w", encoding='utf-8') as f:
        f.write("task:" + str(k) + "\n")
        f.write(classification_report(label, predict, target_names=target_names, digits=3))
        f.write("\n")
        f.write(str(confusion_matrix(label, predict)))
        f.write("\n")

        f.write("-------------------------------------------------------------")
