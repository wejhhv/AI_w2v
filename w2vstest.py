###学習したモデルデータを用いてテスト(ベクトル計算など)
from gensim.models import word2vec
import sys


#モデルファイルの読み込み
model   = word2vec.Word2Vec.load('my.model')


#入力したワードについて、類似度ランキング１０を取得

word=input("言葉を入力してください")
results = model.most_similar(positive=[word], topn=10)
for r in results:
    print(r[0], '\t', r[1])




#正規版、コマンドラインにより入力を行う
"""
results = model.most_similar(positive=sys.argv[1], topn=10)

#こういう書き方もできる　positive足す用、negative引くよう　ベクトルの演算ができる

x="イチロー"
y="野球"
z="サッカー"
result=model.most_similar(positive=([x],[y]),negative=z)

#正規版
for r in results:
    print(r[0], '\t', r[1])

"""
