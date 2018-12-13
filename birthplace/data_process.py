# os.chdir("./data/birthplace")
import random


def data_gen(k):
    if k == 1:
        f = open('./data/birth_place_train.txt', 'r', encoding='utf-8')
        train_x = []
        train_y = []
        test_x = []
        test_y = []
        while True:
            content = f.readline()
            if content == '':
                break

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            train_y.append(relation)
            # put the same entity pair sentences into a dict
            tup = (en1, en2)
            label_tag = 0

            sentence = content[3]

            en1pos = 0
            en2pos = 0

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0

            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)

        print('reading test data ...')

        f = open('./data/birth_place_test.txt', 'r', encoding='utf-8')

        while True:
            content = f.readline()
            if content == '':
                break

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            test_y.append(relation)
            # put the same entity pair sentences into a dict
            tup = (en1, en2)
            label_tag = 0

            sentence = content[3]

            en1pos = 0
            en2pos = 0

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0

            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)
        print(len(train_x))
        # print(sep)
        print(len(test_x))

        return (train_x, test_x), (train_y, test_y)
    elif k == 2:
        dic = dict()
        import re
        pattern = re.compile("\((.*?)\)")
        # e2s = {
        #     "人名": "person",
        #     "地名": "place",
        #     "机构名": "organization",
        #     "日期": "date",
        #     "货币": "money",
        #     "百分比": "percent",
        #     "时间": "time"
        # }
        e2s = {
            "人名": "per",
            "地名": "pla",
            "机构名": "org",
            "日期": "dat",
            "货币": "mon",
            "百分比": "prt",
            "时间": "tim"
        }
        with open('./data/person_name.txt', 'r', encoding='utf-8') as fin:

            content = fin.readlines()
            for name in content:
                name = name[:-1]

                dic[name] = 1

        f = open('./data/birth_place_train.txt', 'r', encoding='utf-8')
        train_x = []
        train_y = []
        test_x = []
        test_y = []
        train_pos_x = []
        train_pos_y = []
        test_pos_x = []
        test_pos_y = []
        while True:
            content = f.readline()
            if content == '':
                break

            alle = dict()

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            train_y.append(relation)

            sentence = content[3]

            en1pos = sentence.find(en1)
            en2pos = sentence.find(en2)
            im = content[4]
            res = pattern.findall(im)
            for r in res:
                e, start, end = r.split(",")

                start = int(start)
                end = int(end)
                end = end + 1

                if start == en1pos or start == en2pos:
                    continue
                else:
                    if not alle.get(e):
                        alle[e] = []
                        alle[e].append(sentence[start:end])

                    else:
                        alle[e].append(sentence[start:end])
            for e in alle.items():
                for s in e[1]:
                    sentence = sentence.replace(s, "<" + e2s[e[0]] + str(random.randint(10, 100)) + ">")

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<e>")
            else:
                sentence = sentence.replace(en1, "<v>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<e>")
            else:
                sentence = sentence.replace(en2, "<v>")
            train_pos_x.append((en1pos, en2pos))

            output = []

            # #Embeding the position
            # for i in range(fixlen):
            #     word = word2id['BLANK']
            #     rel_e1 = pos_embed(i - en1pos)
            #     rel_e2 = pos_embed(i - en2pos)
            #     output.append([word, rel_e1, rel_e2])
            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)
            # train_x=train_x

        # train_y=train_y
        print('reading test data ...')

        f = open('./data/birth_place_test.txt', 'r', encoding='utf-8')

        while True:
            content = f.readline()
            if content == '':
                break
            alle = dict()

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            test_y.append(relation)

            sentence = content[3]

            en1pos = sentence.find(en1)
            en2pos = sentence.find(en2)
            im = content[4]
            res = pattern.findall(im)
            for r in res:
                e, start, end = r.split(",")

                start = int(start)
                end = int(end)
                end = end + 1

                if start == en1pos or start == en2pos:
                    continue
                else:
                    if not alle.get(e):
                        alle[e] = []
                        alle[e].append(sentence[start:end])

                    else:
                        alle[e].append(sentence[start:end])
            for e in alle.items():
                for s in e[1]:
                    sentence = sentence.replace(s, "<" + e2s[e[0]] + str(random.randint(10, 100)) + ">")

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<e>")
            else:
                sentence = sentence.replace(en1, "<v>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<e>")
            else:
                sentence = sentence.replace(en2, "<v>")
            test_pos_x.append((en1pos, en2pos))

            output = []

            # #Embeding the position
            # for i in range(fixlen):
            #     word = word2id['BLANK']
            #     rel_e1 = pos_embed(i - en1pos)
            #     rel_e2 = pos_embed(i - en2pos)
            #     output.append([word, rel_e1, rel_e2])
            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)

        return (train_x, test_x), (train_y, test_y)
    elif k == 3:
        dic = dict()
        with open('./data/person_name.txt', 'r', encoding='utf-8') as fin:

            content = fin.readlines()
            for name in content:
                name = name[:-1]

                dic[name] = 1

        f = open('./data/birth_place_train.txt', 'r', encoding='utf-8')
        train_x = []
        train_y = []
        test_x = []
        test_y = []
        while True:
            content = f.readline()
            if content == '':
                break

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            train_y.append(relation)
            # put the same entity pair sentences into a dict
            tup = (en1, en2)
            label_tag = 0

            sentence = content[3]

            en1pos = 0
            en2pos = 0

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<实体>")
            else:
                sentence = sentence.replace(en1, "<属性>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<实体>")
            else:
                sentence = sentence.replace(en2, "<属性>")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)

        print('reading test data ...')

        f = open('./data/birth_place_test.txt', 'r', encoding='utf-8')

        while True:
            content = f.readline()
            if content == '':
                break

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            test_y.append(relation)
            # put the same entity pair sentences into a dict
            tup = (en1, en2)
            label_tag = 0

            sentence = content[3]

            en1pos = 0
            en2pos = 0

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<实体>")
            else:
                sentence = sentence.replace(en1, "<属性>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<实体>")
            else:
                sentence = sentence.replace(en2, "<属性>")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)
        print(len(train_x))
        # print(sep)
        print(len(test_x))

        return (train_x, test_x), (train_y, test_y)
    elif k == 4:
        dic = dict()
        import re
        pattern = re.compile("\((.*?)\)")

        # e2s = {
        #     "人名": "person",
        #     "地名": "place",
        #     "机构名": "organization",
        #     "日期": "date",
        #     "货币": "money",
        #     "百分比": "percent",
        #     "时间": "time"
        # }
        e2s = {
            "人名": "per",
            "地名": "pla",
            "机构名": "org",
            "日期": "dat",
            "货币": "mon",
            "百分比": "prt",
            "时间": "tim"
        }
        with open('./data/person_name.txt', 'r', encoding='utf-8') as fin:

            content = fin.readlines()
            for name in content:
                name = name[:-1]

                dic[name] = 1

        f = open('./data/birth_place_train.txt', 'r', encoding='utf-8')
        train_x = []
        train_y = []
        test_x = []
        test_y = []
        train_pos_x = []
        train_pos_y = []
        test_pos_x = []
        test_pos_y = []
        while True:
            content = f.readline()
            if content == '':
                break
            alle = dict()

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            train_y.append(relation)
            # put the same entity pair sentences into a dict
            tup = (en1, en2)
            label_tag = 0

            sentence = content[3]

            en1pos = sentence.find(en1)
            en2pos = sentence.find(en2)
            im = content[4]
            res = pattern.findall(im)
            for r in res:
                e, start, end = r.split(",")
                if e is "人名" or e is "地名":

                    start = int(start)
                    end = int(end)
                    end = end + 1
                    if start == en1pos or start == en2pos:
                        continue
                    else:
                        if not alle.get(e):
                            alle[e] = []
                            alle[e].append(sentence[start:end])

                        else:
                            alle[e].append(sentence[start:end])
            for e in alle.items():
                for s in e[1]:
                    sentence = sentence.replace(s, "<" + e2s[e[0]] + str(random.randint(10, 100)) + ">")
                    # sentence = sentence.replace(s, e2s[e[0]])

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<e>")
            else:
                sentence = sentence.replace(en1, "<v>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<e>")
            else:
                sentence = sentence.replace(en2, "<v>")
            train_pos_x.append((en1pos, en2pos))

            output = []

            # #Embeding the position
            # for i in range(fixlen):
            #     word = word2id['BLANK']
            #     rel_e1 = pos_embed(i - en1pos)
            #     rel_e2 = pos_embed(i - en2pos)
            #     output.append([word, rel_e1, rel_e2])
            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)
            # train_x=train_x

        # train_y=train_y
        print('reading test data ...')

        f = open('./data/birth_place_test.txt', 'r', encoding='utf-8')

        while True:
            content = f.readline()
            if content == '':
                break
            alle = dict()

            content = content.strip().split('#')
            # get entity name
            en1 = content[0]
            en2 = content[1]

            relation = int(content[2])
            test_y.append(relation)

            sentence = content[3]

            en1pos = sentence.find(en1)
            en2pos = sentence.find(en2)
            im = content[4]
            res = pattern.findall(im)
            for r in res:
                e, start, end = r.split(",")

                if e is "人名" or e is "地名":

                    start = int(start)
                    end = int(end)
                    end = end + 1
                    if start == en1pos or start == en2pos:
                        continue
                    else:
                        if not alle.get(e):
                            alle[e] = []
                            alle[e].append(sentence[start:end])

                        else:
                            alle[e].append(sentence[start:end])
            for e in alle.items():
                for s in e[1]:
                    sentence = sentence.replace(s, "<" + e2s[e[0]] + str(random.randint(10, 100)) + ">")

            # For Chinese
            en1pos = sentence.find(en1)
            if en1pos == -1:
                en1pos = 0
            elif dic.get(en1) is not None:
                sentence = sentence.replace(en1, "<e>")
            else:
                sentence = sentence.replace(en1, "<v>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence = sentence.replace(en2, "<e>")
            else:
                sentence = sentence.replace(en2, "<v>")
            test_pos_x.append((en1pos, en2pos))

            output = []

            # #Embeding the position
            # for i in range(fixlen):
            #     word = word2id['BLANK']
            #     rel_e1 = pos_embed(i - en1pos)
            #     rel_e2 = pos_embed(i - en2pos)
            #     output.append([word, rel_e1, rel_e2])
            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)

        return (train_x, test_x), (train_y, test_y)


if __name__ == "__main__":
    data_gen(0)
