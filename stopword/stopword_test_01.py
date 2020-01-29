import nltk
import pandas as pd

# Import stopwords with scikit-learn
from sklearn.feature_extraction import text
#Create a stopword dictionary scikit-learn
# stop = text.ENGLISH_STOP_WORDS


from nltk.corpus import stopwords
#Download nltk stopwords
#nltk.download('stopwords')
#Create a stopword dictionary
stop = stopwords.words('english')

#-----------------------------------------------------------------------------------------------
#Rate paper stopwords
#-----------------------------------------------------------------------------------------------
CUSTOM_STOPWORDS = ['i', 'me','up','my', 'myself', 'we', 'our', 'ours',
                    'ourselves', 'you', 'your', 'yours','yourself', 'yourselves',
                    'he', 'him', 'his', 'himself', 'she', 'her', 'hers' ,'herself',
                    'it', 'its', 'itself', 'they', 'them', 'their', 'theirs',
                    'themselves' ,'am', 'is', 'are','a', 'an', 'the', 'and','in',
                    'out', 'on','up','down', 's', 't']


df = pd.read_json("./dataset_json/Bug_tt.json")

df1 = pd.DataFrame()
df1["comment"] = df["comment"]
df1["stopwords_removal1"] = df["stopwords_removal"]
df1["stopwords_removal2"] = df['comment'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
df1["stopwords_removal_nltk1"] = df["stopwords_removal_nltk"]
df1["stopwords_removal_nltk2"] = df['stopwords_removal'].apply(lambda x: ' '.join([word for word in x.split() if word not in (CUSTOM_STOPWORDS)]))
#df1["stopwords_removal"] = df['stopwords_removal'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

comment_vect = []
sw_nltk_vect1 = []
sw_nltk_vect2 = []
sw_vect1 = []
sw_vect2 = []
for index, row in df1.iterrows():
    comment_str = row["comment"]
    comment_vect.append(len(comment_str.split()) )

    sr_nltk_str1 = row["stopwords_removal_nltk1"]
    sw_nltk_vect1.append(len(sr_nltk_str1.split()) )

    sr_nltk_str2 = row["stopwords_removal_nltk2"]
    sw_nltk_vect2.append(len(sr_nltk_str2.split()) )

    sw_str1 = row["stopwords_removal1"]
    sw_vect1.append(len(sw_str1.split()) )

    sw_str2 = row["stopwords_removal2"]
    sw_vect2.append(len(sw_str2.split()) )

df1["comment_cnt"] = comment_vect
df1["stopwords_removal_nltk1_cnt"] = sw_nltk_vect1
df1["stopwords_removal_nltk2_cnt"] = sw_nltk_vect2
df1["stopwords_removal1_cnt"] = sw_vect1
df1["stopwords_removal2_cnt"] = sw_vect2

# df1.to_csv("dataset_stopwords_removal_check.csv")

df2 = pd.DataFrame()
df2["comment_cnt"] = df1["comment_cnt"] 
df2["stopwords_removal_nltk1_cnt"] = df1["stopwords_removal_nltk1_cnt"]
df2["stopwords_removal_nltk2_cnt"] = df1["stopwords_removal_nltk2_cnt"]
df2["stopwords_removal1_cnt"] = df1["stopwords_removal1_cnt"]
df2["stopwords_removal2_cnt"] = df1["stopwords_removal2_cnt"]

totRows = float(df["id"].count())
# totSW1 = sum(df2["stopwords_removal1_cnt"])
# totSW2 = sum(df2["stopwords_removal2_cnt"])
# totSW_nltk1 = sum(df2["stopwords_removal_nltk1_cnt"])
# totSW_nltk2 = sum(df2["stopwords_removal_nltk2_cnt"])

totSW1 = sum(df2["stopwords_removal2_cnt"] == df2["stopwords_removal1_cnt"])
totSW_nltk1 = sum(df2["stopwords_removal_nltk2_cnt"] == df2["stopwords_removal_nltk1_cnt"])

totSW2 = sum(df2["stopwords_removal2_cnt"] < df2["stopwords_removal1_cnt"])
totSW_nltk2 = sum(df2["stopwords_removal_nltk2_cnt"] < df2["stopwords_removal_nltk1_cnt"])

totSW = float(totSW1+totSW2)
totSW_nltk = float(totSW_nltk1+totSW_nltk2)


delimiter = "\t".encode('utf-8')
df2.to_csv("dataset_stopwords_removal_check.csv", header=True, index=False, sep=delimiter, encoding = "utf-8")

#print(df1.head(10))

print "---------------------------------------------------"
print "Total Stop Words:",totSW,"/",totRows," = ", str(totSW/totRows)
print "Stop words with equal value:", totSW1
print "Stop words with less than value:", totSW2
print "---------------------------------------------------"

print "Total Stop Words NLTK:",totSW_nltk,"/",totRows," = ", totSW_nltk/totRows 
print "Stop words nltk with equal value:", totSW_nltk1
print "Stop words nltk with less than value:", totSW_nltk2

