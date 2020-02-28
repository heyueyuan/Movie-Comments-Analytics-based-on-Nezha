# encoding : utf-8

from snownlp import SnowNLP 
import pandas as pd 

data = pd.read_csv("all_comments.csv")

score = 0
for d in data['comments']:
    
    s = SnowNLP(d)
    score += s.sentiments

score = score / len(data['comments']) * 100

if score > 80:
    print("电影评论情感分析为：%d , 非常建议观看" % score)
else:
    print("电影评论情感分析为：%d, 不建议观看" % score )




