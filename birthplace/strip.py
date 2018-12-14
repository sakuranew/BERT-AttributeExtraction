import re



def _split(sentence):
    return re.split(",|，|。|？|！|；", sentence)


def strip(filename):
    # filename="a"
    with open(filename, 'r', encoding='utf-8') as f:
        # new_filename=filename.split('.')
        new_filename = filename.rsplit('.', maxsplit=1)
        new_filename = new_filename[-2] + "_strip." + new_filename[-1]
        w = open(new_filename, 'w', encoding='utf-8')
        maxl = 0
        while True:
            content = f.readline()
            if content == '':
                break

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]
            sentence = content[3]
            sens = _split(sentence)
            s = e = -1
            for index, sen in enumerate(sens):
                if sen.find(en1) is not -1 or sen.find(en2) is not -1:
                    if s is -1:
                        s = index
                    e = index
            _sentence = []
            # for index,sen in enumerate(sens,start=s):
            for index, sen in enumerate(sens):
                if index < s:
                    continue
                if index is e + 1:
                    break
                _sentence.append(sen)
            _sentence = " ".join(_sentence)
            content[3] = _sentence
            new_content = "#".join(content)
            w.write(new_content)
            w.write('\n')
            if len(_sentence) > maxl:
                maxl = len(_sentence)
        print((maxl))


if __name__ == "__main__":
    file_list = ["./data/birth_place_train.txt", "./data/birth_place_test.txt"]
    for f in file_list:
        strip(f)
