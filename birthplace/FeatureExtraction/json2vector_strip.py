import numpy as np
import json
def json2vector(filename):
    dim = 768

    max_len = 8727 if filename.find("train") is not -1 else 962


    with open(filename, "r", encoding='utf-8') as f:
        vec = np.empty([max_len, dim])
        # vec2 = np.empty([sep + test, dim])

        for line_index in range(max_len):
            bb = json.loads(f.readline())
            # line=bb[line_index]["features"]
            line = bb["features"]

            # tokens_vec=np.empty([max_len,dim])
            tokens_vec = [token["layers"][0]["values"] for token in line]
            tokens_vec = np.array(tokens_vec)
            sen_vec = np.sum(tokens_vec, axis=0) / tokens_vec.shape[0]
            vec[line_index] = sen_vec

            # tokens_vec2 = [token["layers"][1]["values"] for token in line]
            # tokens_vec2 = np.array(tokens_vec2)
            # sen_vec2 = np.sum(tokens_vec2, axis=0) / tokens_vec2.shape[0]
            # vec2[line_index] = sen_vec2
        if filename.find("train") is not -1:
            np.save('../data/birth_place_trainx_strip.npy', vec)
        else:
            np.save('../data/birth_place_testx_strip.npy', vec)

        # np.save('../data/birth_place_trainx2.npy', vec2[:sep])
        # np.save('../data/birth_place_testx2.npy', vec2[sep:])

if __name__ == "__main__":
    # file_list=["../data/birth_place_test_strip.jsonl"]
    file_list=["../data/birth_place_train_strip.jsonl"]

    for f in file_list:
        json2vector(f)
