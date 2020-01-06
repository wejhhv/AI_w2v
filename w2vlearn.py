###分かち書きされたtxtファイルから学習したモデルを作成
##60MBのtxtで5分弱
import time
from gensim.models import word2vec

a=time.time()
sentences=word2vec.Text8Corpus("wakati2.txt")


print("ファイル読み込み完了")
model = word2vec.Word2Vec(sentences,
                          sg=1,         # 訓練アルゴリズム; 0: CBOW, 1: skip-gram
                          size=200,     # ベクトルの次元数
                          window=10,    # 同じ文章内の単語どうしの最大距離
                          min_count=2,  # これより出現回数の少ない単語は含まない
                          hs=1,         # 1: 階層的ソフトマックス, hs==0 && negative!=0: ネガティブサンプリングを使う
                          negative=0    # ネガティブサンプリング（ノイズワード）の数
                          )
model.save('wiki.model')

print("モデル作成完了")
b=time.time()

print("経過時間")
c=(b-a)/3600

print(b)

print("時間")
