### マルコフ辞書の作成　　janomeではなくmecabで形態素解析を行っている
##jsonファイルをがディレクトリ直下に作成される
#使用するのは分かち書きされる前の整形済みのテキストファイル
import MeCab
import json, os, glob

#あとあと利用しやすいようにファイル名を入れておく
markov_file="markov.json"
textfile="q.txt"
dic = {}

##分かち書き処理  引数はtextsファイルreadline()で受け取っている
def wakati(texts):
    
    #確認用
    i=0
    #関数の返り値がリストであるため
    wordlist = []
    for text in texts:
    
        #経過時間確認用(行)
        if i%10000==0:
            print(i)
        i=i+1
        
        # 形態素解析
        tagger = MeCab.Tagger("chansen")

        for chunk in tagger.parse(text).splitlines()[:-1]:
            (surface, hinshi) = chunk.split('\t')
            if  hinshi not  in ["BOS/EOS"]:
                if hinshi.startswith('記号'):
#                   記号を辞書に登録しない
                    pass
                elif '*' in hinshi.split(",")[6]:
#                   基本形が存在しない場合、表層形を返す
                    wordlist.append([surface,hinshi])
                else :
#                   基本形を返す
                    wordlist.append([hinshi.split(",")[6],hinshi])
#   返り値はリスト型
    return wordlist

def regist_dic(wordlist):
    global dic
    w1 = ""
    w2 = ""

    # 要素が3未満の場合は、何もしない
    if len(wordlist) < 3 : return

    for w in wordlist :
        word = w[0]
        if word == "" or  word == "\r\n" or word == "\n" : continue
        # 辞書に単語を設定
        if w1 and w2 :
            set_dic(dic,w1, w2, word)
        # 文末を表す語のの場合、連鎖をクリアする
        if word == "。" or word == "?" or  word == "？" or word=="!":
            w1 = ""
            w2 = ""
            continue
        # 次の前後関係を登録するために、単語をスライド
        w1, w2 = w2, word

    # 辞書を保存
    json.dump(dic, open(markov_file,"w", encoding="utf-8"))

# 三要素のリストを辞書に単語として設定 --- (*2)
def set_dic(dic, w1, w2, w3):
    # 新しい単語の場合は、新しい辞書オブジェクトを作成
    if w1 not in dic : dic[w1] = {}
    if w2 not in dic[w1] : dic[w1][w2] = {}
    if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0
    # 単語の出現数をインクリメントする
    dic[w1][w2][w3] += 1

if __name__ == '__main__':
    if os.path.exists(markov_file):
#       すでにわかち書きが存在する場合は元のjsonファイルを削除
        os.remove(markov_file)
        print('remove -> ' + markov_file)
        
    #ファイルを読み込んで処理
    #整形はされているが分かち書きされていないファイル                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     x=input("読み込むファイル > ")
    f = open("q.txt",'r',encoding="utf-8")
    text=f.readlines()
    #確認用
    print(len(text))
    print("ファイル読み込み終了")
    #分かち書き処理   
    wordlist = wakati(text)
    
    #確認用
    print("分かち書き処理終了")
    
    #マルコフ辞書への登録
    regist_dic(wordlist)
    
    #確認用
    print("マルコフ辞書への登録終了")