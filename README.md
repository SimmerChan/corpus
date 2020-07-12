把自己找到的语料和语言资源整理一下，避免以后需要的时候又浪费时间去收集（长期坑位）。

> 1. 数据使用范围、授权请参考原始发布源（如果有的话），如有侵权，请联系我删除。
> 2. 有的数据源（网站、论文）提供了多语语料，为避免重复，只在中文或外语对应章节列出（比如翻译）。如有多语资源，会在相应章节进行说明（如需要特定任务的数据集，可以分别在中文和外语语料对应章节进行查看）。
> 3. 我这里“问答”和“阅读理解”划分的标准是：输入是一段背景信息或者加上用户query，输出是从背景信息抽取的答案（或者判定不能回复）或者填空，这样的数据集归类为“阅读理解”；“问答”可以看做是对话的另外一种形式。



关注公众号：尘世美小茶馆，获取更多丰富资源。

![](Images/wechat.jpg)


目录：

- [1. NLP中文语料](#1)
  - [1.1 生语料](#1.1)
    - [1.1.1 人民日报新闻数据](#1.1.1)
    - [1.1.2 微信公众号语料库](#1.1.1)
  - [1.2 结构化数据](#1.2)
    - [1.2.1 中国古代人物传记数据库(CBDB)](#1.2.1)
  - [1.3 文本分类数据集](#1.3)
    - [1.3.1 2018法研杯](#1.3.1)
    - [1.3.2 今日头条中文新闻（短文本）分类数据集](#1.3.2)
    - [1.3.3 清华新闻分类语料](#1.3.3)
    - [1.3.4 SMP2017中文人机对话评测数据](#1.3.4)
    - [1.3.5 中国新闻网新闻分类语料](#1.3.5)
    - [1.3.6 凤凰网新闻分类语料](#1.3.6)
  - [1.4 序列标注数据集（分词、命名实体识别、词性标注等）](#1.4)
    - [1.4.1 SiGHAN2005分词数据集](#1.4.1)
    - [1.4.2 MSRA命名实体识别数据集](#1.4.2)
    - [1.4.3 人民日报命名实体识别数据集](#1.4.3)
    - [1.4.4 微博命名实体识别数据集](#1.4.4)
    - [1.4.5 影视-音乐-书籍实体标注数据](#1.4.5)
    - [1.4.6 BosonNLP NER数据](#1.4.6)
    - [1.4.7 cluener 细粒度实体识别数据集](#1.4.7)
    - [1.4.8 人民日报2014NER标注数据](#1.4.8)
    - [1.4.9 1998年1月-6月人民日报标注语料](#1.4.9)
  - [1.5 指代消解](#1.5)
    - [1.5.1 CLUEWSC2020](#1.5.1)
  - [1.6 对话](#1.6)
    - [1.6.1 好大夫医疗对话数据集](#1.6.1)
    - [1.6.2 中文医疗对话数据集](#1.6.2)
  - [1.7 情感分析](#1.7)
    - [1.7.1 携程网酒店评论数据](#1.7.1)
    - [1.7.2 外卖评论数据](#1.7.2)
    - [1.7.3 电商商品评论数据](#1.7.3)
    - [1.7.4 微博情感数据（2类）](#1.7.4)
    - [1.7.5 微博情感数据（4类）](#1.7.5)
    - [1.7.6 电影评论评分数据](#1.7.6)
    - [1.7.7 大众点评餐馆评论数据](#1.7.7)
    - [1.7.8 Amazon商品评论数据](#1.7.8)
    - [1.7.9 豆瓣电影评论数据](#1.7.9)
    - [1.7.10 大众点评用户评论（2类）](#1.7.10)
    - [1.7.11 京东用户评论数据](#1.7.11)
  - [1.8 语义相似度（文本蕴含）](#1.8)
    - [1.8.1 LCQMC](#1.8.1) 
    - [1.8.2 ChineseSTS](#1.8.2) 
    - [1.8.3 ATEC蚂蚁金服语义相似度数据](#1.8.3) 
  - [1.9 问答](#1,9)
    - [1.9.1 580万百度知道社群问答](#1.9.1)
    - [1.9.2 DuReader](#1.9.2)
    - [1.9.3 细分领域知道问答数据集](#1.9.3)
    - [1.9.4 社区问答数据集](#1.9.4)
  - [1.10 阅读理解](#1.10)
    - [1.10.1 人民日报&童话故事](#1.10.1)
    - [1.10.2 CMRC2017](#1.10.2)
    - [1.10.3 CMRC2018](#1.10.3)
    - [1.10.4 CMRC2019](#1.10.4)
    - [1.10.5 DRCD](#1.10.5)
    - [1.10.6 C^3](#1.10.6)
    - [1.10.7 ChiD](#1.10.7)
    - [1.10.8 DuReader](#1.10.8)
- [2. NLP外文语料](#2)
  - [2.1 文本分类数据集](#2.1)
    - [2.1.1 Fake News Corpus](#2.1.1)
    - [2.1.2 AG News](#2.1.2)
    - [2.1.3 ColBERT](#2.1.3)
  - [2.2 情感分析](#2.2)
    - [2.2.1 MovieTweetings](#2.2.1)
    - [2.2.2 Amazon Fine Food Reviews](#2.2.2)
    - [2.2.3 Amazon Reviews](#2.2.3)
    - [2.2.4 Yelp Open Dataset](#2.2.4)
    - [2.2.5 MovieLens](#2.2.5)
  - [2.3 对话](#2.3)
    - [2.3.1 Twitter Chat Corpus](#2.3.1)
  - [2.4 序列标注数据集（分词、命名实体识别、词性标注等）](#2.4)
    - [2.4.1 DAWT](#2.4.1) 
  - [2.5 机器翻译](#2.5)
    - [2.5.1 Europarl](#2.5.1)
    - [2.5.2 United Nations Parallel Corpus](#2.5.2)
    - [2.5.3 News-Commentary](#2.5.3)
    - [2.5.4 wikititles](#2.5.4)
    - [2.5.5 Ted Talk](#2.5.5)
    - [2.5.6 中英翻译数据集](#2.5.6)
  - [2.6 语义相似度（文本蕴含）](#2.6)
    - [2.6.1 PAWS](#2.6.1)
    - [2.6.2 DNLI](#2.6.2)
    - [2.6.3 MultiNLI](#2.6.3)
    - [2.6.4 XNLI](#2.6.4)
    - [2.6.5 SNLI](#2.6.5)
    - [2.6.6 Quora Question Pairs](#2.6.6)
  - [2.7 问答](#2.7)
    - [2.7.1 MS MARCO](#2.7.1)
  - [2.8 阅读理解](#2.8)
    - [2.8.1 HotpotQA](#2.8.1)
    - [2.8.2 SQuAD v2.0](#2.8.2)
  - [2.9 文本摘要](#2.9)
    - [2.9.1 BigPatent](#2.9.1)
- [3. 语言资源](#3)
  - [3.1 实体类](#3.1)
    - [3.1.1 百科实体](#3.1.1)
    - [3.1.2 中国古代编年史CBDB实体](#3.1.2)
  - [3.2 词典类](#3.2)
    - [3.2.1 百科词条名](#3.2.1)
    - [3.2.2 360万中文词库（包含词性和词频）](#3.2.2)
    - [3.2.3 谷歌书籍N-gram数据](#3.2.3)
- [4. KG数据](#4)
    - [4.1 百科三元组](#4.1)
    - [4.2 Dbpedia](#4.2)
    - [4.3 OpenKG](#4.3)



<h1 id='1'>1. 中文语料</h1>

<h2 id='1.1'>1.1 生语料</h2>

<h3 id='1.1.1'>1.1.1 人民日报新闻数据</h3>

包含1946年-2003年人民日报全部数据以及文革网（2005-2008）全部图文数据库。原始发布地址不详，只找到转载的[页面](http://www.360doc.com/content/10/0415/14/257553_23177268.shtml)   ，作者邮箱应该是 bjdjssgmzsf@yahoo.com ，联系过，没收到回复。原始数据是图文数据库，我将其转存[百度网盘](https://pan.baidu.com/s/1YJ6vVfJQVVLGavs1hAdSuQ)  ，然后单独整理了一个sql文件方便使用和查询。大多数情况下，只需要考虑文本内容，我写了一个脚本[rmrb.py](./Chinese/raw_corpus/rmrb.py)  将所有新闻导出到txt文件中，方便使用。新闻一共有137万多条。

<h3 id='1.1.2'>1.1.2 微信公众号语料库</h3>

[微信公众号语料库](https://github.com/nonamestreet/weixin_public_corpus)：只包含了纯文本。每行一篇，是JSON格式，name是微信公众号名字，account是微信公众号ID，title是题目，content是正文，数据大约3G。

---

<h2 id='1.2'>1.2 结构化数据</h2>

<h3 id='1.2.1'>1.2.1 中国古代人物传记数据库（CBDB）</h3>

[中国历代人物传记数据库](https://projects.iq.harvard.edu/cbdb)（The China Biographical Database, CBDB）是一个线上关系型数据库，其远期目标在于系统性地收入中国历史上所有重要的传记资料，其内容无限制地、免费地提供学术研究。截止2018年9月为止，该数据库一共收录了422,600人的传记资料，这些人主要出自七世纪至十九世纪，该数据库目前致力于增录更多的唐代和明清的人物传记资料。

CBDB的数据是用access和sqlite两种数据库进行存储，我转了一个mysql的[版本](https://pan.baidu.com/s/1olG3Fnn6gCqyo9lgNKYhrw)，表格和字段的具体说明请参考官网。由于数据是不断更新的，需要最新数据的请到官网下载。脚本[cbdb.py](./Chinese/structural_data/cbdb.py)是将sqlite中的数据导入mysql中，如果数据库表格发生改变，可能需要更新一下脚本。

<h2 id='1.3'>1.3 文本分类数据集</h2>

<h3 id='1.3.1'>1.3.1 2018法研杯</h3>
2018中国‘法研杯’法律智能挑战赛（任务：罪名预测、法条推荐、刑期预测）的[数据](https://cail.oss-cn-qingdao.aliyuncs.com/CAIL2018_ALL_DATA.zip)，数据集共包括268万刑法法律文书，共涉及183条罪名，202条法条，刑期长短包括0-25年、无期、死刑。

---

<h3 id='1.3.2'>1.3.2 今日头条中文新闻（短文本）分类数据集</h3>

今日头条中文新闻（短文本）分类[数据集](https://github.com/fateleak/toutiao-text-classfication-dataset)：共382688条，分布于15个分类中，包含民生、文化、娱乐、体育、财经、房产、骑车、教育、科技、军事、旅游、国际、证券、农业、电竞。

---

<h3 id='1.3.3'>1.3.3 清华新闻分类语料</h3>

清华新闻分类[语料](http://thuctc.thunlp.org/)：74万篇新闻文档，划分出14个候选分类类别：财经、彩票、房产、股票、家居、教育、科技、社会、时尚、时政、体育、星座、游戏、娱乐。

---


<h3 id='1.3.4'>1.3.4 SMP2017中文人机对话评测数据</h3>

包含了两个任务的[数据集](https://github.com/HITlilingzhi/SMP2017ECDT-DATA)：用户意图领域分类，特定域任务型人机对话在线评测。第一个数据集用得比较多。用户意图领域分类包含闲聊类、任务垂直类共三十一个类别，属于短文本分类的一个范畴。

---

<h3 id='1.3.5'>1.3.5 中国新闻网新闻分类语料</h3>

中国新闻网新闻分类[语料](https://github.com/zhangxiangxiao/glyph)：从中国新闻网爬取2008-2016年七个新闻种类的新闻，包括中国大陆政治、港澳台政治、国际新闻、金融、文化、娱乐、体育（论文还提到health这个类别，数据里其实没有）。每个样本只包括新闻的第一段话。每个类别样本数相同。140万训练集，11.2万测试集。（https://pan.baidu.com/s/1G-krApbhq-Lb2mxNSQXdhg#list/path=%2F，提取码：7xh0，Chinanews子文件）

---

<h3 id='1.3.6'>1.3.6 凤凰网新闻分类语料</h3>

凤凰网新闻分类[语料](https://github.com/zhangxiangxiao/glyph)：从凤凰网爬取2006-2016年五个新闻种类的新闻，包括中国大陆政治、国际新闻、港澳台、军事和社会新闻。每个样本只包括新闻的第一段话。每个类别样本数相同。80万训练集，5万测试集。（https://pan.baidu.com/s/1G-krApbhq-Lb2mxNSQXdhg#list/path=%2F，提取码：7xh0，Ifeng子文件）


<h2 id='1.4'>1.4 序列标注数据集（分词、命名实体识别、词性标注等）</h2>

<h3 id='1.4.1'>1.4.1 SiGHAN2005分词数据集</h3>
SiGHAN2005分词[数据集](http://sighan.cs.uchicago.edu/bakeoff2005/)（或在我的repo中下载）：北大、香港城市大学、台湾“中央研究院”（繁体）、微软亚研院四个机构提供的中文分词数据集。

---

<h3 id='1.4.2'>1.4.2 MSRA命名实体识别数据集</h3>

MSRA命名实体识别[数据集](https://github.com/OYE93/Chinese-NLP-Corpus/tree/master/NER/MSRA)：包含地名、人名和机构名三类。

---

<h3 id='1.4.3'>1.4.3 人民日报命名实体识别数据集</h3>

人民日报命名实体识别[数据集](https://github.com/OYE93/Chinese-NLP-Corpus/tree/master/NER/People's%20Daily)：包含地名、人名和机构名三类。

---

<h3 id='1.4.4'>1.4.4 微博命名实体识别数据集</h3>

微博命名实体识别[数据集](https://github.com/OYE93/Chinese-NLP-Corpus/tree/master/NER/Weibo)：包含地名、人名、机构名、行政区名四类。

---

<h3 id='1.4.5'>1.4.5 影视-音乐-书籍实体标注数据</h3>

影视、音乐、书籍实体标注[数据](https://github.com/LG-1/video_music_book_datasets)：类似于人名/地名/组织机构名的命名体识别数据集，大约10000条影视/音乐/书籍数据。

---

<h3 id='1.4.6'>1.4.6 BosonNLP NER数据</h3>

BosonNLP（好像不维护了，数据可以在我的repo中找到）：2000条，包含人名、地名、时间、组织名、公司名、产品名。

---

<h3 id='1.4.7'>1.4.7 cluener 细粒度实体识别数据集</h3>

[cluener](https://github.com/CLUEbenchmark/CLUENER2020)：是在清华大学开源的文本分类数据集THUCTC基础上，选出部分数据进行细粒度命名实体标注，原数据来源于Sina News RSS。数据分为10个标签类别，分别为: 地址（address），书名（book），公司（company），游戏（game），政府（government），电影（movie），姓名（name），组织机构（organization），职位（position），景点（scene）

---

<h3 id='1.4.8'>1.4.8 人民日报2014NER标注数据</h3>

人民日报2014NER标注数据（数据可以在我的repo中找到）：包含人名、地点、组织、时间。

---

<h3 id='1.4.9'>1.4.9 1998年1月-6月人民日报标注语料</h3>

1300W字的新闻[标注语料](https://pan.baidu.com/s/17djsvYfpYUXrazL0H_mtoA)，该语料可用于分词、NER、POS等任务。标记和格式请参考此[文章](https://cloud.tencent.com/developer/article/1091906)。

---

<h2 id='1.5'>1.5 指代消解</h2>

<h3 id='1.5.1'>1.5.1 CLUEWSC2020 </h3>

[CLUEWSC2020](https://github.com/CLUEbenchmark/CLUEWSC2020): WSC Winograd模式挑战中文版，中文指代消解任务，训练集：1244，开发集：304。

---

<h2 id='1.6'>1.6 对话</h2>

<h3 id='1.6.1'>1.6.1 好大夫医疗对话数据集 </h3>

医疗领域对话[数据集](https://github.com/UCSD-AI4H/Medical-Dialogue-System)，110万轮对话，共400万句：从好大夫网上爬的。

---

<h3 id='1.6.12'>1.6.2 中文医疗对话数据集 </h3>

中文医疗对话[数据集](https://github.com/Toyhom/Chinese-medical-dialogue-data)：


| 领域   | 数据量 |
| ------ | ------ |
| 男科   | 94596  |
| 内科   | 220606 |
| 妇产科 | 183751 |
| 肿瘤科 | 75553  |
| 儿科   | 101602 |
| 外科   | 115991 |

---

<h2 id='1.7'>1.7 情感分析</h2>

<h3 id='1.7.1'>1.7.1 携程网酒店评论数据</h3>

携程网酒店评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：5000+条正向评论，2000+负向评论。

---

<h3 id='1.7.2'>1.7.2 外卖评论数据</h3>

外卖评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：4000+正向，8000+负向。

---

<h3 id='1.7.3'>1.7.3 电商商品评论数据</h3>

电商商品评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：10 个类别，共 6 万多条评论数据，正、负向评论各约 3 万条，包括书籍、平板、手机、水果、洗发水、热水器、蒙牛、衣服、计算机、酒店。

---

<h3 id='1.7.4'>1.7.4 微博情感数据（2类）</h3>

微博情感[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：10万多条，带情感标注的新浪微博，正负向评论约各 5 万条。

---

<h3 id='1.7.5'>1.7.5 微博情感数据（4类）</h3>

微博情感[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：36万多条，带情感标注的新浪微博，包含4种情感，其中喜悦约 20 万条，愤怒、厌恶、低落各约5万条。

---

<h3 id='1.7.6'>1.7.6 电影评论评分数据</h3>

电影评论评分[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：28部电影，超70万用户，超200万条评分/评论数据，包括1-5分评分，及评论的点赞数。

---

<h3 id='1.7.7'>1.7.7 大众点评餐馆评论数据</h3>

大众点评餐馆评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：24 万家餐馆，54 万用户，440 万条评论/评分数据。包括总体评分（0-5），环境评分（1-5），口味评分（1-5），服务评分（1-5）

---

<h3 id='1.7.8'>1.7.8 Amazon商品评论数据</h3>

Amazon商品评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：52 万件商品，1100 多个类目，142 万用户，720 万条评论/评分数据，评分1-5。

---

<h3 id='1.7.9'>1.7.9 豆瓣电影评论数据</h3>

豆瓣电影评论[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：5万多部电影（3万多有电影名称，2万多没有电影名称），2.8万用户，280万条评分数据，评分1-5。

---

<h3 id='1.7.10'>1.7.10 大众点评用户评论（2类）</h3>

大众点评用户[评论](https://github.com/zhangxiangxiao/glyph)：从大众点评爬取的用户评论。1-3星划分为负面评论、4-5星为正面评论。每个类别样本数相同。200万训练集，50万测试集。（https://pan.baidu.com/s/1G-krApbhq-Lb2mxNSQXdhg#list/path=%2F，提取码：7xh0，dianping子文件）

---

<h3 id='1.7.11'>1.7.11 京东用户评论数据</h3>

京东用户评论[数据](https://github.com/zhangxiangxiao/glyph)：JD full是五分类数据，1-5星每个星级为一个类别，类别的样本数相同。300万训练集，25万测试集。JD binary是二分类数据，1-2星属于负面评论，4-5星属于正面评论，忽略3星，类别的样本数相同。400万训练集，36万测试集。（https://pan.baidu.com/s/1G-krApbhq-Lb2mxNSQXdhg#list/path=%2F，提取码：7xh0，JD full和JD binary子文件）

---

<h2 id='1.8'>1.8 语义相似度（文本蕴含）</h2>

<h3 id='1.8.1'>1.8.1 LCQMC</h3>

[LCQMC](http://icrc.hitsz.edu.cn/info/1037/1146.htm)：26万对句子，判别两个问句是否表示相同的意思。（https://pan.baidu.com/s/1yerI7P6Lvm7HdgrKdRJyGQ，提取码：q8y1）

---

<h3 id='1.8.2'>1.8.2 ChineseSTS</h3>

中文文本语义相似度[语料库](https://github.com/IAdmireu/ChineseSTS)：相似度值：0-5，5表示相似度最高（意思一样），0表示相似度最低(语义相反或不相干）

---

<h3 id='1.8.3'>1.8.3 ATEC蚂蚁金服语义相似度数据</h3>

ATEC蚂蚁金服语义相似度[数据](https://dc.cloud.alipay.com/index?click_from=MAIL&_bdType=acafbbbiahdahhadhiih#/topic/intro?id=3)：给定客服里用户描述的两句话，用算法来判断是否表示了相同的语义（数据集在我repo也可以下载）。

---

<h2 id='1.9'>1.9 问答</h2>

<h3 id='1.9.1'>1.9.1 580万百度知道社群问答</h3>

580万百度知道社群[问答](https://github.com/liuhuanyong/MiningZhiDaoQACorpus)：包括超过580万的问题，每个问题带有问题标签。问答对983万个，每个问题的答案个数1.7个，问题标签个数5824个。

---

<h3 id='1.9.2'>1.9.2 DuReader</h3>

[DuReader](http://ai.baidu.com/broad/introduction?dataset=dureader)：百度开源的一个QA和MRC数据集，共140万篇文档，30万个问题，及66万个答案。

---

<h3 id='1.9.3'>1.9.3 细分领域知道问答数据集</h3>

不同领域的知道问答[数据](https://github.com/SophonPlus/ChineseNlpCorpus)：包含保险、金融、法律等领域，字段有用户query，网友回答和最佳回答。

---

<h3 id='1.9.4'>1.9.4 社区问答数据集</h3>

社区问答[数据](https://github.com/brightmart/nlp_chinese_corpus)：含有410万个预先过滤过的、高质量问题和回复。每个问题属于一个话题，总共有2.8万个各式话题，话题包罗万象。从1400万个原始问答中，筛选出至少获得3个点赞以上的的答案，代表了回复的内容比较不错或有趣，从而获得高质量的数据集。除了对每个问题对应一个话题、问题的描述、一个或多个回复外，每个回复还带有点赞数、回复ID、回复者的标签。

---

<h2 id='1.10'>1.10 阅读理解</h2>

<h3 id='1.10.1'>1.10.1 人民日报&童话故事</h3>

[人民日报&童话故事](https://github.com/ymcui/Chinese-Cloze-RC)：完形填空类型的，预测的是一个词，2.8万篇文档，10万个query。

---

<h3 id='1.10.2'>1.10.2 CMRC2017</h3>

[CMRC2017](https://github.com/ymcui/cmrc2017)：新闻领域的语料，形式为完形填空和用户提问类两种，共36万+数据。

---

<h3 id='1.10.3'>1.10.3 CMRC2018</h3>

[CMRC2018](https://github.com/ymcui/cmrc2018)：维基语料，1.8万个query，形式为给定用户query从上下文抽取span。

---

<h3 id='1.10.4'>1.10.4 CMRC2019</h3>

[CMRC2019](https://github.com/ymcui/cmrc2019)：句子级别的完形填空。1000篇文档，10万个query。根据给定的一个叙事篇章以及若干个从篇章中抽取出的句子，参赛者需要建立模型将候选句子精准的填回原篇章中，使之成为完整的一篇文章。与CMRC 2017的不同是：空缺部分不再只是一个词，而是一个句子；每个篇章不只是一个空缺，会包含多个空缺位置，机器可利用的信息大大减少；候选选项中包含假选项，即该选项不属于篇章中任何一个空缺位置，显著增加了解答难度。

---

<h3 id='1.10.5'>1.10.5 DRCD</h3>

[DRCD](https://github.com/DRCKnowledgeTeam/DRCD)：维基语料，3.4万个query，形式为给定用户query从上下文抽取span（繁体汉语）。

---

<h3 id='1.10.6'>1.10.6 C^3</h3>

[C^3](https://dataset.org/c3/)：文档是混合类型的，有对话、故事、新闻报道、广告等。形式为用户提问类，结果是根据候选答案进行选择（只有一个是正确的）。1.4万篇文档，2.4万query。

---

<h3 id='1.10.7'>1.10.7 ChiD</h3>

[ChiD](https://github.com/chujiezheng/ChID-Dataset)：成语预测类型任务（完形填空），给定上下文和每个位置候选的成语列表，预测该位置应该填什么成语。共58万篇文档，72.9万query（cloze）。

---

<h3 id='1.10.8'>1.10.8 DuReader</h3>

[DuReader](http://ai.baidu.com/broad/introduction?dataset=dureader)：百度开源的一个QA和MRC数据集，共140万篇文档，30万个问题，及66万个答案。


<h1 id='2'>2. 外语语料</h1>

<h2 id='2.1'>2.1 文本分类数据集</h2>

<h3 id='2.1.1'>2.1.1 Fake News Corpus</h3>

[Fake News Corpus](https://github.com/several27/FakeNewsCorpus)：940万篇新闻，745个类别（domain）。

---

<h3 id='2.1.2'>2.1.2 AG News</h3>

[AG News](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html)：100多万的新闻数据，分为全球新闻、运动、商业和科技四类。

---

<h3 id='2.1.3'>2.1.3 ColBERT</h3>

[ColBERT](https://www.kaggle.com/moradnejad/200k-short-texts-for-humor-detection)：20万条短文本，判断是否包含幽默元素的二分类数据集，正负各十万。

---

<h2 id='2.2'>2.2 情感分析</h2>

<h3 id='2.2.1'>2.2.1 MovieTweetings</h3>

[MovieTweetings](https://github.com/sidooms/MovieTweetings)：推特电影评分数据集，822,784条，0-10分评分。

---

<h3 id='2.2.2'>2.2.2 Amazon Fine Food Reviews</h3>

[Amazon Fine Food Reviews](https://www.kaggle.com/snap/amazon-fine-food-reviews)：亚马逊上的食品评价，包含56万条评论，涉及7.4万产品，1-5分。

---

<h3 id='2.2.3'>2.2.3 Amazon Reviews</h3>

[Amazon Reviews](https://nijianmo.github.io/amazon/index.html)：美亚上面商品的评论数据，有2.3亿条。

---

<h3 id='2.2.4'>2.2.4 Yelp Open Dataset</h3>

[Yelp Open Dataset](https://www.yelp.com/dataset)：包含800多万条评论。

---

<h3 id='2.2.5'>2.2.5 MovieLens</h3>

[MovieLens](https://grouplens.org/datasets/movielens/)：包含2500万条电影评论，涉及6万2千部电影和16万用户，100万个标签。

---


<h2 id='2.3'>2.3 对话</h2>

<h3 id='2.3.1'>2.3.1 Twitter Chat Corpus</h3>

[Twitter Chat Corpus](https://github.com/Marsan-Ma-zz/chat_corpus)：500多万推特对话数据。

---

<h2 id='2.4'>2.4 序列标注数据集（分词、命名实体识别、词性标注等）</h2>

<h3 id='2.4.1'>2.4.1 DAWT</h3>

[DAWT](https://github.com/klout/opendata/tree/master/wiki_annotation)：包含了六种语言共1300万的文章，实体提及（mention）是链接到Freebase的具体实体上的，标注信息也包括了实体类别。

<h2 id='2.5'>2.5 机器翻译</h2>

<h3 id='2.5.1'>2.5.1 Europarl</h3>

 欧盟21种语言翻译[平行语料](http://www.statmt.org/europarl/)：20种语言到英语的平行语料，包括保加利亚语、捷克语、丹麦语、德语、希腊语、西班牙语、爱沙尼亚语、芬兰语、法语、匈牙利语、意大利语、立陶宛语、拉脱维亚语、荷兰语、波兰语、葡萄牙语、罗马尼亚语、斯洛伐克语、斯洛文尼亚语、瑞典语。 [百度网盘](https://pan.baidu.com/s/1jqvm7WE-csfdjCKxjjanIA)  y7k3

---

<h3 id='2.5.2'>2.5.2 United Nations Parallel Corpus</h3>

[联合国平行语料](https://cms.unov.org/UNCorpus/)，当前版本（1.0）由联合国的官方文件和其他议会文件组成，包含了联合国的六种官方语言（英语、法语、俄语、汉语、阿拉伯语、西班牙语两两之间的平行语料对），语料的内容主要是在1990-2014年之间产生和翻译的，并在句子级别上进行了对齐。[百度网盘(目前只包含中文到除阿拉伯语的其他语言翻译对)](https://pan.baidu.com/s/1PR8zbd-tvm658vWcqmYS-w)  pnhy

---

<h3 id='2.5.3'>2.5.3 News-Commentary</h3>

WMT提供的[新闻评论语料](http://data.statmt.org/news-commentary/v14/)，共98个双语对，15种语言。[百度网盘](https://pan.baidu.com/s/1CJYaZjgOj1hYnI1qyDPtfA)  igss

---

<h3 id='2.5.4'>2.5.4 wikititles</h3>

WMT提供的[维基百科标题](http://data.statmt.org/wikititles/v1/)多语对，共11个双语对，14种语言。[百度网盘](https://pan.baidu.com/s/1igFM8Iv-hchKvGhaJQ7VHQ)  inxn

News-Commentary和wikititles的[下载脚本](./Foreign/translation/wmt_downloader.py)

---

<h3 id='2.5.5'>2.5.5 Ted Talk</h3>

Ted上面有丰富的语料资源，包含了109种语言。ajinkyakulkarni14提供了2014年获取的[平行语料](https://github.com/ajinkyakulkarni14/TED-Multilingual-Parallel-Corpus)，和获取语料的[脚本](https://github.com/ajinkyakulkarni14/How-I-Extracted-TED-talks-for-parallel-Corpus-)。

neubig也提供了他们用于论文实验的Ted[数据](https://github.com/neulab/word-embeddings-for-nmt)。

[neubig数据百度网盘](https://pan.baidu.com/s/1SYjZOuhiawlxjKbgx8ooXA)  dn6y

---

<h3 id='2.5.6'>2.5.6 中英翻译数据集</h3>

中英翻译[数据集](https://github.com/brightmart/nlp_chinese_corpus)：520万对中英文平行语料，每一个对，包含一个英文和对应的中文。中文或英文，多数情况是一句带标点符号的完整的话。对于一个平行的中英文对，中文平均有36个字，英文平均有19个单词。

---

<h2 id='2.6'>2.6 语义相似度（文本蕴含）</h2>

<h3 id='2.6.1'>2.6.1 PAWS</h3>

[PAWS and PAWS-X](https://github.com/google-research-datasets/paws)：Goggle公开的同义句识别语料。PAWS是英文语料，包含108463对英文句子对；PAWS-X包含中、法、德、日、韩、西班牙六种语言的语料，每种语言大约5.3W条。

---

<h3 id='2.6.2'>2.6.2 DNLI</h3>

[Dialogue Natural Language Inference](https://wellecks.github.io/dialogue_nli/)：用于改善对话模型的一致性，判断句子对之间的关系，是蕴含、中性还是矛盾。

---

<h3 id='2.6.3'>2.6.3 MultiNLI</h3>

[MultiNLI Matched/Mismatched](https://cims.nyu.edu/~sbowman/multinli/)：43万对句子，判断是蕴含、中性还是矛盾。包含多种类型的文本，涉及口语和书面语言。

---

<h3 id='2.6.4'>2.6.4 XNLI</h3>

[XNLI](https://cims.nyu.edu/~sbowman/xnli/)：11.2万句子对，判断是蕴含、中性还是矛盾。共有十四种语言，有中文。

---

<h3 id='2.6.5'>2.6.5 SNLI</h3>

[SNLI](https://nlp.stanford.edu/projects/snli/)：57万个句子对，判断是蕴含、中性还是矛盾。

---

<h3 id='2.6.6'>2.6.6 Quora Question Pairs</h3>

[Quora Question Pairs](https://www.quora.com/q/quoradata/First-Quora-Dataset-Release-Question-Pairs)：判断两个问句是否是语义等价的，共40万对。

---

<h2 id='2.7'>2.7 问答</h2>

<h3 id='2.7.1'>2.7.1 MS MARCO</h3>

[MS MARCO](https://microsoft.github.io/msmarco/)：100多万的问答数据，也适用于阅读理解、文章排序、关键词抽取等任务。

---

<h2 id='2.8'>2.8 阅读理解</h2>

<h3 id='2.8.1'>2.8.1 HotpotQA</h3>

[HotpotQA](https://hotpotqa.github.io/)：100多万问答对。需要多跳推理才能得到正确答案，难度更大。

---

<h3 id='2.8.2'>2.8.2 SQuAD v2.0</h3>

[SQuAD v2.0](https://rajpurkar.github.io/SQuAD-explorer/)：15万问答对，依据给出的上下文，其中10万可回答，5万不可回答。

---

<h2 id='2.9'>2.9 文本摘要</h2>

<h3 id='2.9.1'>2.9.1 BigPatent</h3>

[BigPatent](https://evasharma.github.io/bigpatent/)：包含130万的美国专利文档，和人工撰写的摘要。

---

<h1 id='3'>3. 语言资源</h1>

<h2 id='3.1'>3.1 实体类（人名、地名等）</h2>

<h3 id='3.1.1'>3.1.1 百科实体</h3>

百科实体（2010年）：根据当时百科页面的标签来筛选实体类型（人名、地名），存在一定噪音，酌情使用。95433个[地名](https://pan.baidu.com/s/1CpIr1qPAUen2pfisWXMxqQ)，278577个[人名](https://pan.baidu.com/s/1OuKC3ax9Qk5krL_vH10-kg)。

---

<h3 id='3.1.2'>3.1.2 中国古代编年史CBDB实体</h3>

中国古代编年史CBDB实体（2017年）：227266个[人名](https://pan.baidu.com/s/1YMLxdAgKNrviaYC1cqod4Q)和百科的会有重合。

---

<h2 id='3.2'>3.2 词典类</h2>

<h3 id='3.2.1'>3.2.1 百科词条名</h3>

百科词条名（2010年百度百科）：一千万[词条名](https://pan.baidu.com/s/1DkgtFmhpxxq6Qx67PgU10A)。

---

<h3 id='3.2.2'>3.2.2 360万中文词库（包含词性和词频）</h3>

该[资源](https://pan.baidu.com/s/11T4CNHAQ30EHj456-gJVwQ)作者为刘邵博，由其综合多本词典整合的一个大词典，词典共有词汇3669216个词汇。词典结构为：词语\t词性\t词频。词频是用ansj分词对270G新闻语料进行分词统计词频获得。

---

<h3 id='3.2.3'>3.2.3 谷歌书籍N-gram数据</h3>

谷歌书籍N-gram[数据](https://aws.amazon.com/cn/datasets/google-books-ngrams/)：分别整理了多种语言的n-gram词典资源，包含中文，从1到5-gram都有。

---

<h1 id='4'>4. KG数据</h1>

<h2 id='4.1'>4.1 百科三元组</h2>

1.4亿三元组中文[知识图谱](https://github.com/ownthink/KnowledgeGraphData)

---

<h2 id='4.2'>4.2 Dbpedia</h2>

[Dbpedia](https://wiki.dbpedia.org/develop/datasets/dbpedia-version-2016-10)：多语知识图谱数据，共有130亿个三元组，但大部分都是英语。有760个类，1105个关系，1622个属性。

---

<h2 id='4.3'>4.3 OpenKG</h2>

开放的中文知识图谱[社区](http://www.openkg.cn/)：这里有很多垂直领域图谱数据，我就不一一放上来了。