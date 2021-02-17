from utils import *
import nltk
import re


hc = 0
fc = 0
mc = 0
correct = 0


def get_max(a, b, c):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return max


def get_poet(a, b, c):
    global mc, fc, hc
    m = get_max(a, b, c)
    if m == a:
        fc += 1
        return '1'
    if m == b:
        hc += 1
        return '2'
    mc += 1
    return '3'


def get_test_text(f):
    l = {}
    test_file = open(f, "r")
    for i in test_file:
        t = re.split(r'\t+', i)
        a = re.split(r'\n+', t[1])
        x = "غغ " + a[0]
        x = x + " غغغ"
        l[x] = t[0]
    return l


def func(l3, l2, l1, epsilon):
    global correct
    tst = get_test_text("test_file.txt")
    ferdowsi = open_train_set("ferdowsi_train.txt")
    hafez = open_train_set("hafez_train.txt")
    molavi = open_train_set("molavi_train.txt")

    m_count = get_dict(molavi)
    m_bigram = get_bigram(molavi, m_count)
    m_pbigram = get_pbigram(m_bigram, m_count)
    m_punigram = get_punigram(m_count)

    hf_count = get_dict(hafez)
    hf_bigram = get_bigram(hafez, hf_count)
    hf_pbigram = get_pbigram(hf_bigram, hf_count)
    hf_punigram = get_punigram(hf_count)

    f_count = get_dict(ferdowsi)
    f_bigram = get_bigram(ferdowsi, f_count)
    f_pbigram = get_pbigram(f_bigram, f_count)
    f_punigram = get_punigram(f_count)

    for key in tst.keys():
        print(key)
        y = list(key.split())
        l = []
        g = []
        h = []
        for i in y:
            # if i not in m_count.keys():
            #     h.append('ننن')
            # else:
            #     h.append(i)
            h.append(i)
        xm = list(nltk.bigrams(h))
        for i in y:
            g.append(i)
        xf = list(nltk.bigrams(g))
        for i in y:
            l.append(i)
        x = list(nltk.bigrams(l))
        pf = 1
        ph = 1
        pm = 1
        for j in xm:
            m = 0
            if j in m_pbigram.keys():
                m += l3 * m_pbigram[j]
            if j[1] in m_punigram.keys():
                m += l2 * m_punigram[j[1]]
            m += l1 * epsilon
            pm *= m
        for j in xf:
            hf = 0
            if j in hf_pbigram.keys():
                hf += l3 * hf_pbigram[j]
            if j[1] in hf_punigram.keys():
                hf += l2 * hf_punigram[j[1]]
            hf += l1 * epsilon
            ph *= hf
        for j in x:
            f = 0
            if j in f_pbigram.keys():
                f += l3 * f_pbigram[j]
            if j[1] in f_punigram.keys():
                f += l2 * f_punigram[j[1]]
            f += l1 * epsilon
            pf *= f
        print(pf, ph, pm)
        poet = get_poet(pf, ph, pm)
        if poet == tst[key]:
            correct += 1
            print("correct guess!")
        print("the poet: ", poet)
        print("the actual poet", tst[key])
    print("molavi: ", mc)
    print("hafez: ", hc)
    print("ferdowsi: ", fc)
    print("correct guesses: ", correct)


if __name__ == '__main__':
    func(0.05, 0.475, 0.475, 0.001)
