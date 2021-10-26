!pip install pandas
!pip install pyLDAvis
!pip install konlpy
!pip install git+https://github.com/e9t/PyTagCloud.git
!pip install warnings
!pip install customized_konlpy
!pip install pygame
!pip install soynlp

import pandas as pd
import re
import nltk
import numpy as np
from collections import Counter
import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
import pyLDAvis.sklearn  # sklearn의 ldamodel에 최적화된 라이브러리
from sklearn.decomposition import PCA
import pyLDAvis.gensim_models
import gensim
from gensim import corpora
from gensim.models import LdaModel
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
from sklearn.feature_extraction.text import TfidfVectorizer
import string
from sklearn.cluster import KMeans
import warnings
from konlpy.tag import Okt
from konlpy.tag import Kkma
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
from ckonlpy.tag import *
import random
import pytagcloud
from PIL import Image
from soynlp.normalizer import *

warnings.filterwarnings(action='ignore')

# 유튜브 크롤링 파일 로드
path = '/home/lab10/final/pre/'

comment_file = 'prepro_comments_2PM.csv'    #
data = pd.read_csv(path+comment_file, encoding='utf-8', header=None)
data.columns = ['comment','like','lang']
print(len(data))
data.head()
# data.like.describe(percentiles=[0.75])
# 좋아요 갯수 일정갯수 이상 만 
# idx=data[data['like']<=323].index              #좋아요 갯수 상위 15000 정도 이상 댓글만 남김
# data.drop(idx, inplace=True)

# data_2 = data[data.like >=100]
# len(data_2)

data_ko = pd.DataFrame([kor[:1] for kor in data.values if kor[2] == '(ko)'], columns=['comment'])
data_en = pd.DataFrame([en[:1] for en in data.values if en[2] == '(en)'], columns=['comment'])
data_ko.comment.values

data.lang.value_counts()

for i in range(len(data_ko.comment)):
    data_ko.comment[i] = str(data_ko.comment[i])

    # 숫자제거 / 밑줄 제외한 특수문자 제거
p = re.compile("[0-1]+")
z = re.compile("[3-9]+")
q = re.compile("\W+")
r = re.compile('[^ ㄱ-ㅣ가-힣]+')

kr = []

for i in data_ko.comment.values:
    tokens = re.sub(p," ",i)
    tokens = re.sub(z," ",tokens)
    tokens = re.sub(q," ",tokens)
    tokens = re.sub(r," ", tokens)
    kr.append(tokens)
len(kr)

kr[:2]

okt = Okt()
kkma = Kkma()
twitter = Twitter()

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

twitter.add_dictionary('투피엠', 'Noun')


stop_words = set(stopwords.words('english'))
stop_words.update('이','내','너','까지','수','네','것','요','어요','나','만','거','더','까지','뭐')


res=[]
for i in range(len(kr)):
    word_tokens = word_tokenize(kr[i])

    result = []
    for w in word_tokens: 
        if w not in stop_words: 
            result.append(w) 
    res.append(result)


res[:2]

print(len(res))

res_less3=[]
for i in range(len(res)):
    tokens = [word for word in res[i] if len(word) >= 2]
    res_less3.extend(tokens)

res_less3[:2]



ko_pos = []
for w in res_less3:
    tokens_pos = twitter.pos(w)
    ko_pos.append(tokens_pos)

ko_pos[:2]


ko_noun = []
for i in res_less3:
    tokens_pos = twitter.nouns(i)
    ko_noun.extend(tokens_pos)

ko_noun[:2]

#9. 빈도분석

c = Counter(ko_noun) # input type should be a list of words (or tokens)
k = 20
print(c.most_common(k)) # 빈도수 기준 상위 k개 단어 출력

#wordclound
noun_text = ''
for word in ko_noun:
    noun_text = noun_text +' '+word



path2='/home/lab10/final/'
filename = comment_file

youtube=np.array(Image.open('/home/lab10/final/pngwing.com (4).png'))
wordcloud = WordCloud(font_path='font/NanumGothic.ttf', background_color='black', colormap='YlOrRd', relative_scaling=.5, mask=youtube).generate(noun_text) # generate() 는 하나의 string value를 입력 받음
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud.to_file(path2+'wordcloud'+'_ko_'+filename+'.png')



## 2단어 이하 짧은 단어 제거
 # remove words less than three letters
# print(res[1])
# for word in res[1]:
#     print(word)
ko_sent_less3=[]
for i in range(len(res)):
    tokens = [word for word in res[i] if len(word) >= 2]
    ko_sent_less3.append(tokens)
ko_sent_less3[:2]

ko_sent =[]
for i in range(len(ko_sent_less3)):
    temp=" ".join(ko_sent_less3[i])
    ko_sent.append(temp)
ko_sent[:15]


data_ko['ko_sent']=ko_sent


data_ko.tail()

# BoW 모델로 벡터화
count = CountVectorizer(ngram_range=(3,6),
                        max_df = 0.05,
                        max_features=10000, stop_words=None)
docs = ko_sent
bag = count.fit_transform(docs)


"""# 잠재 디리클레 할당을 사용한 토픽 모델링"""

# LDA 사용 (BoW 기반)

lda = LatentDirichletAllocation(n_components = 5,
                                random_state = 1,
                                learning_method = 'batch')

X_topics = lda.fit_transform(bag)

# 결과 분석을 위해 각 토픽 당 중요 단어 10개 출력 (BoW 기반)
n_top_word = 10
feature_name = count.get_feature_names()
for topic_idx, topic in enumerate(lda.components_):
  print("토픽 %d:" % (topic_idx+1))
  print([feature_name[i] for i in topic.argsort()[:-n_top_word - 1: -1]])

pyLDAvis.enable_notebook()
vis = pyLDAvis.sklearn.prepare(lda, bag, count)
pyLDAvis.display(vis)

pyLDAvis.save_html(vis, path2+comment_file+'lda_ko.html')

ko_sent[:10]

model = LatentDirichletAllocation(n_components = 5,
                                random_state = 1,
                                learning_method = 'batch')

model.fit(bag) # model.fit_transform(X) is also available

tokenized_doc = data_ko['ko_sent'].apply(lambda x: x.split()) # 토큰화
tokenized_doc

vectorizer = TfidfVectorizer(stop_words='english',
                        ngram_range=(3,6), # 유니그램 바이그램으로 사용
                        min_df = 3, # 3회 미만으로 등장하는 토큰은 무시
                        max_df =10000# 많이 등장한 단어 5%의 토큰도 무시
)

X = vectorizer.fit_transform(ko_sent)
X.shape # TF-IDF 행렬의 크기 확인


svd_model = TruncatedSVD(n_components=5, algorithm='randomized', n_iter=100, random_state=122)
svd_model.fit(X)
len(svd_model.components_)

np.shape(svd_model.components_)

# CountVectorizer객체내의 전체 word들의 명칭을 get_features_names( )를 통해 추출

terms = vectorizer.get_feature_names() # 

def get_topics(components, feature_names, n=10):
    for idx, topic in enumerate(components):
        print("Topic %d:" % (idx+1), [(feature_names[i], topic[i].round(5)) for i in topic.argsort()[:-n - 1:-1]])
get_topics(svd_model.components_,terms)

dictionary = corpora.Dictionary(tokenized_doc)
corpus = [dictionary.doc2bow(text) for text in tokenized_doc]
print(corpus[1]) # 수행된 결과에서 두번째 뉴스 출력. 첫번째 문서의 인덱스는 0

print(dictionary[12])

len(dictionary)

NUM_TOPICS = 5 #5개의 토픽, k=5
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
topics = ldamodel.print_topics(num_words=10)
for topic in topics:
    print(topic)

pyLDAvis.enable_notebook()
vis2 = pyLDAvis.gensim_models.prepare(ldamodel, corpus, dictionary)
pyLDAvis.display(vis2)

pyLDAvis.save_html(vis2, path2+comment_file+'lda_dic_ko.html')

for i, topic_list in enumerate(ldamodel[corpus]):
    if i==5:
        break
    print(i,'번째 문서의 topic 비율은',topic_list)


def make_topictable_per_doc(ldamodel, corpus):
    topic_table = pd.DataFrame()

    # 몇 번째 문서인지를 의미하는 문서 번호와 해당 문서의 토픽 비중을 한 줄씩 꺼내온다.
    for i, topic_list in enumerate(ldamodel[corpus]):
        doc = topic_list[0] if ldamodel.per_word_topics else topic_list            
        doc = sorted(doc, key=lambda x: (x[1]), reverse=True)
        # 각 문서에 대해서 비중이 높은 토픽순으로 토픽을 정렬한다.
        # EX) 정렬 전 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (10번 토픽, 5%), (12번 토픽, 21.5%), 
        # Ex) 정렬 후 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (12번 토픽, 21.5%), (10번 토픽, 5%)
        # 48 > 25 > 21 > 5 순으로 정렬이 된 것.

        # 모든 문서에 대해서 각각 아래를 수행
        for j, (topic_num, prop_topic) in enumerate(doc): #  몇 번 토픽인지와 비중을 나눠서 저장한다.
            if j == 0:  # 정렬을 한 상태이므로 가장 앞에 있는 것이 가장 비중이 높은 토픽
                topic_table = topic_table.append(pd.Series([int(topic_num), round(prop_topic,4), topic_list]), ignore_index=True)
                # 가장 비중이 높은 토픽과, 가장 비중이 높은 토픽의 비중과, 전체 토픽의 비중을 저장한다.
            else:
                break
    return(topic_table)


topictable = make_topictable_per_doc(ldamodel, corpus)
topictable = topictable.reset_index() # 문서 번호을 의미하는 열(column)로 사용하기 위해서 인덱스 열을 하나 더 만든다.
topictable.columns = ['문서 번호', '가장 비중이 높은 토픽', '가장 높은 토픽의 비중', '각 토픽의 비중']
topictable[:10]

topic_word = model.components_ # model.components_also works
n_top_words = 5   # TOPIC으로 선정될 단어의 수

def get_topic_term_prob(lda_model):
    topic_term_freqs = lda_model.state.get_lambda()
    topic_term_prob = topic_term_freqs / topic_term_freqs.sum(axis=1)[:, None]
    return topic_term_prob

print(ldamodel.alpha.shape) # (n_topics,)
print(ldamodel.alpha.sum()) # 1.0

topic_term_prob = get_topic_term_prob(ldamodel)
print(topic_term_prob.shape)     # (n_topics, n_terms)
print(topic_term_prob[0].sum())  # 1.0


