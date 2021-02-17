import nltk


def get_dict(lst):
    dct = {}
    for i in lst:
        i = "غغ " + i
        i = i + " غغغ"
        str = i.split()
        for j in str:
            if j in dct:
                dct[j] += 1
            else:
                dct[j] = 1
    # dct['ننن'] = 0
    # for i in dct.keys():
    #     if dct[i] == 1:
    #         dct['ننن'] += 1
    dct = {k: v for k, v in dct.items() if v != 1}
    return dct


def get_bigram(f, mydict):
    bigram = []
    for i in f:
        i = "غغ " + i
        i = i + " غغغ "
        # print(i)
        t = list(nltk.bigrams(i.split()))
        # print(t)
        for i in range(len(t)):
            temp = list(t[i])
            # if temp[0] not in mydict.keys():
            #     temp[0] = 'ننن'
            # if temp[1] not in mydict.keys():
            #     temp[1] = 'ننن'
            t[i] = tuple(temp)
        bigram.append(t)
    return bigram


def get_pbigram(bigram , unigram):
    bidict = {}
    for s in bigram:
        for b in s:
            if b in bidict:
                bidict[b] += 1
            else:
                bidict[b] = 1
    for key in bidict.keys():
        if key in bidict and  key[0] in unigram.keys():
            bidict[key] = bidict[key] / unigram[key[0]]
        else:
            bidict[key] = 0
    return bidict


def get_punigram(unigram):
    udict = {}
    count = 0
    for u in unigram.keys():
        count += unigram[u]
    print(count)
    for u in unigram.keys():
        udict[u] = unigram[u] / count
    return udict


def open_train_set(fname):
    f = open(fname, "r")
    l = []
    for i in f:
        l.append(i)
    return l


