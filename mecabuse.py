###mecabで分かち書き処理を行う場合、一定以上大きな文字列は形態素解析できない
###mecabによる分かち書き処理　　q.txt ⇒　wati1.txt
import MeCab
#ファイルオープン
f=open("q.txt","r",encoding="utf-8")
f1=open("wati1.txt","a",encoding="utf-8")

#分かち書き処理用
mecab = MeCab.Tagger("-Owakati")

#重すぎるので一行ごとに処理
#文字列として認識
datas=f.readlines()
print("ファイル読み込み終了")
print("分かち書き済みの行の数を表示します")

#ファイルクローズ処理
f.close()
i=0
print(len(datas))
#形態素解析およびファイルへの出力
for data in datas:

    text=mecab.parse(data)
    f1.write(text)

    #確認のための行数表示
    if i%10000==0:
        print(i)
    i=i+1

#ファイルクローズ処理
f1.close()

#確認用
print("終了しました")

