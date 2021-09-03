import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from wordcloud import WordCloud

DATA_IN_PATH ='C:/Users/User/Desktop/workspace/vsc/CRWALING/twitter/twt_1500/'

train_data = pd.read_csv(DATA_IN_PATH + '갓세븐.csv', header=0, delimiter='\t', quoting=3)
print(train_data.head(5))

print(f'전체 학습 데이터의 개수: {len(train_data)}')

print(train_data['내용'])

# train_length = train_data['내용'].astype(str).apply(len)
# print(train_data.head(5))