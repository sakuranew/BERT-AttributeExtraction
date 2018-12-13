import pickle


def data_gen(k):
    if k == 1:
        f = open('./data/birth_date_train.txt', 'r', encoding='utf-8')
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

        f = open('./data/birth_date_test.txt', 'r', encoding='utf-8')

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
        train_x = train_x[:6000]

        train_y = train_y[:6000]

        return (train_x, test_x), (train_y, test_y)
    elif k == 2:
        f = open('./data/birth_date_train.txt', 'r', encoding='utf-8')
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

        f = open('./data/birth_date_test.txt', 'r', encoding='utf-8')

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
        # train_x=train_x[:6000]

        # train_y=train_y[:6000]

        return (train_x, test_x), (train_y, test_y)
    elif k == 3:
        dic = dict()
        with open('./data/person_name.txt', 'r', encoding='utf-8') as fin:

            content = fin.readlines()
            for name in content:
                dic[name] = 1

        f = open('./data/birth_date_train.txt', 'r', encoding='utf-8')
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
                sentence.replace(en1, "实体")
            else:
                sentence.replace(en1, "属性")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence.replace(en2, "实体")
            else:
                sentence.replace(en2, "属性")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)

        print('reading test data ...')

        f = open('./data/birth_date_test.txt', 'r', encoding='utf-8')

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
                sentence.replace(en1, "实体")
            else:
                sentence.replace(en1, "属性")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence.replace(en2, "实体")
            else:
                sentence.replace(en2, "属性")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)
        print(len(train_x))
        # print(sep)
        print(len(test_x))
        # train_x=train_x[:6000]

        # train_y=train_y[:6000]

        return (train_x, test_x), (train_y, test_y)
    elif k == 4:
        dic = dict()
        with open('./data/person_name.txt', 'r', encoding='utf-8') as fin:

            content = fin.readlines()
            for name in content:
                dic[name] = 1

        f = open('./data/birth_date_train.txt', 'r', encoding='utf-8')
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
                sentence.replace(en1, "<e>")
            else:
                sentence.replace(en1, "<a>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence.replace(en2, "<e>")
            else:
                sentence.replace(en2, "<a>")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            train_x.append(s)

        print('reading test data ...')

        f = open('./data/birth_date_test.txt', 'r', encoding='utf-8')

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
                sentence.replace(en1, "<e>")
            else:
                sentence.replace(en1, "<a>")

            en2pos = sentence.find(en2)
            if en2pos == -1:
                en2pos = 0
            elif dic.get(en2) is not None:
                sentence.replace(en2, "<e>")
            else:
                sentence.replace(en2, "<a>")
            output = []

            s = sentence
            # s=[s[i] for i in range(len(s))]
            test_x.append(s)
        print(len(train_x))
        # print(sep)
        print(len(test_x))
        # train_x=train_x[:6000]

        # train_y=train_y[:6000]

        return (train_x, test_x), (train_y, test_y)


if __name__ == "__main__":
    data_gen(0)
