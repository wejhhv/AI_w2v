

#必要なライブラリはインストール(多分ほとんどいらん)
from requests_oauthlib import OAuth1Session,OAuth1
import json
import requests
import urllib
import MeCab
import sys
import time
import pandas
import numpy as np
import re

#抜くべき対象の文字列（正規表現）
replaceList = [
        (",","\n"),
        ("(・|�|●|〇|○|▽|▼|▲|△|✨|☺|♬)+",""),
        ("@[a-zA-Z0-9_]{1,15}", ""),
        ('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', ''),
        ('[#＃][Ａ-Ｚａ-ｚA-Za-z一-鿆0-9０-９ぁ-ヶｦ-ﾟー]+', ''),
        (" +",""),
        ('&lt;', '<'),
        ('&gt;', '>'),
        ('&amp;', '&'),
        ("\n{2,10}",""),
        (";",""),
        (":","")
      
        ]


#ファイル読み込み、文字コードはUNICODE
filep=open("today.txt","r",encoding="UTF-8")
data=filep.read()
filep.close()

#すべての文字列について確認
for t in replaceList:
    #re.sub(A,B,C)　　文字列C中にAがあればBで置換する
    data=re.sub(t[0],t[1],data)

#ファイル書き込み
fileq=open("qqq.txt","w",encoding="UTF-8")
fileq.write(data)
fileq.close