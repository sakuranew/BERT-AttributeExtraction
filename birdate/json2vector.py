import numpy as np
import json

dim = 768
max_len = 128
with open("birth_date_x.jsonl", "r", encoding='utf-8') as f:
    vec = np.empty([9000, dim])

    for line_index in range(9000):
        bb = json.loads(f.readline())
        # line=bb[line_index]["features"]
        line = bb["features"]

        # tokens_vec=np.empty([max_len,dim])
        tokens_vec = [token["layers"][0]["values"] for token in line]
        tokens_vec = np.array(tokens_vec)
        sen_vec = np.sum(tokens_vec, axis=0) / tokens_vec.shape[0]
        vec[line_index] = sen_vec
    sep = 6000
    np.save('data/birth_date_trainx.npy', vec[:sep])
    np.save('data/birth_date_testx.npy', vec[sep:])
