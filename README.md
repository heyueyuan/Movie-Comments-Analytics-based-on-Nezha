# Movie-Comments-Analytics-based-on-Nezha
# 中文
通过爬取关于哪吒的豆瓣影评，获取数据后，利用jieba分词和wordcloud，产生云图，得到本电影影评的最直观关键词。
![image](/images/pic.png)
借助SnowNLP情感分析得出电影评论情感分析为：85 , 非常建议观看.

# English
Utilized Web crawl to acquire movie comments from a Chinese Movie Comments Website, and exported them to csv format for analysis later. By using a package called [jieba](https://github.com/fxsjy/jieba), a NLP(natural language processing) tool, to cut sentences to words and delete non-sense words, exported a wordcloud picture by using a package called wordcloud.
![image](/images/pic.png)<br>
Utilized another NLP tool, called [SnowNLP](https://github.com/isnowfy/snownlp), to make sentiment analytics. Get 85 scores by analyzing movie comments.
