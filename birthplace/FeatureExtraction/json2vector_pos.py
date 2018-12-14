import numpy as np
import json
import pickle

from sklearn.preprocessing import StandardScaler

p = 16
dim = 768
max_len = 100
sep = 8727
test = 962
with open('./data/pos_trainx.pickle', 'rb') as f:
    train_pos_x = pickle.load(f)
with open('./data/pos_testx.pickle', 'rb') as f:
    test_pos_x = pickle.load(f)
pos_embedding = np.random.rand(max_len, p)
train_pos_x.extend(test_pos_x)
# with open("./data/birth_place_x.jsonl", "r", encoding='utf-8') as f:
with open("../output.jsonl", "r", encoding='utf-8') as f:
    vec = np.empty([sep + test, dim])

    for line_index in range(sep + test):
        bb = json.loads(f.readline())
        # line=bb[line_index]["features"]
        line = bb["features"]

        # tokens_vec=np.empty([max_len,dim])
        tokens_vec = [token["layers"][0]["values"] for token in line]
        tokens_vec = np.array(tokens_vec)

        sen_vec = np.sum(tokens_vec, axis=0) / tokens_vec.shape[0]

        vec[line_index] = sen_vec

    v_min, v_max = vec.min(), vec.max()
    vec = (vec - v_min) / (v_max - v_min)
    pos_e = np.empty([sep + test, 32])

    for line_index in range(sep + test):
        pos1, pos2 = train_pos_x[line_index]
        pos_e[line_index] = np.hstack((pos_embedding[pos1, :], pos_embedding[pos2, :]))

    vec = np.hstack((vec, pos_e))

    np.save('./data/birth_place_trainx.npy', vec[:sep])
    np.save('./data/birth_place_testx.npy', vec[sep:])
