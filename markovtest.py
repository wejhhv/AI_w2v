##マルコフ辞書のテスト用
##辞書より、ランダムなワードを作成する
import json
import random
markov_dic = json.load(open("Skokoro.json", 'r'))


def test(markov_dic):
    ret = []
    if not '@' in markov_dic:
        return 'no dict'

    top = markov_dic['@']
    word1 = word_choice(top)
    word2 = word_choice(top[word1])
    ret.append(word1)
    ret.append(word2)
    while True:
        word3 = word_choice(markov_dic[word1][word2])
        ret.append(word3)
        if word3 == '。':
            break
        if len(ret) >= 10:
            ret.append('。')
            break

        word1, word2 = word2, word3

    return ''.join(ret)


def word_choice(sel):
    keys = sel.keys()
    ran = random.choice(list(keys))
    return ran


for i in range(0,20):
    print(test(markov_dic))    




