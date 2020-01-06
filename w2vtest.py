###モデルファイルの読み込みのみ時間がかかる、あらかじめ読み込んでおく
###学習したモデルデータを用いてテスト(関連ワードの表示)
from gensim.models import word2vec
import sys


#モデルファイルの読み込み
model   = word2vec.Word2Vec.load('wiki.model')


#入力したワードについて、類似度ランキング１０を取得
print("学習したモデルについてキーワードより類似語を表示します")
print("終了する場合はbyeと入力してね")
word=input("言葉を入力してください>>>>")

#無条件で繰り返し
while word!="bye":
    #学習したモデルに文字が存在するとき
    if word in model.wv.vocab:
        
        results = model.most_similar(positive=[word], topn=10)
        
        for r in results:
        #ここでr[0]には言葉、r[1]には関連度（多分内積）が格納されている
            print(r[0], '\t', r[1])
    
    #この単語についてはその都度辞書にプラスするコードを書いておくべきかな
    else:
        print(word+ "は未学習の言葉です")
    
    
    #終了条件のためこの位置で
    word=input("\n言葉を入力してください>>>>")
    
"""
コマンドラインにより入力を行う場合

results = model.most_similar(positive=sys.argv[1], topn=10)

#こういう書き方もできる　positive足す用、negative引くよう　ベクトルの演算ができる

x="イチロー"
y="野球"
z="サッカー"
results=model.most_similar(positive=[x,y],negative=[z])

#正規版
for r in results:
    print(r[0], '\t', r[1])
"""