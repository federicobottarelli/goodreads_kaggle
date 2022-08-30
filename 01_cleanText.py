from curses.ascii import controlnames
import pandas as pd
from nltk.corpus import stopwords 
import string
import argparse
import re
import gc
import contractions
import os
import time
## thanks to https://www.kaggle.com/code/mayerantoine/eda-nlp-goodreads-books-reviews
def cleanText(text):
    # aggiungere contractions.fix(text) 
    text = contractions.fix(text)

    # aggiungere text.lower()
    text = text.lower()

    # remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # remove the characters [\], ['] and ["]
    text = re.sub(r"\\", "", text)
    #text = re.sub(r"\'", "", text)
    text = re.sub(r"\"", "", text)
    
    # remove all non-ASCII characters:
    text = re.sub(r'[^\x00-\x7f]', r'', text)
    
    # remove URL
    text = re.sub(r"http\S+", "", text)
    
    # remove digits
    text = re.sub(r'\d+', '',text)
    
    ## DA CAPIRE MEGLIO COME FUNZIONA 
    # replace punctuation characters with spaces
    filters = '!"\'#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
    translate_dict = dict((c, " ") for c in filters)
    translate_map = str.maketrans(translate_dict)
    text = text.translate(translate_map)
    text = " ".join(text.split())

    # remove saxon adjective
    # text = re.sub(r"\bs",'',text)
    text = text.replace(" s "," ")

    return text

# parse command line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("filename", type=str)
argparser.add_argument("--folderLoc", type=str, 
                        default="/home/fede/Dataset/goodreads/")
args = argparser.parse_args()

## split the filename
file_base, file_ext = os.path.splitext(args.filename)
#### Dataset import 
df_location = f'{args.folderLoc}{args.filename}'
if file_ext == ".csv":
    df = pd.read_csv(df_location)
elif (file_ext == ".pkl") or (file_ext == ".pickle"):
    df = pd.read_pickle(df_location) 

# apply remove digit function to all the review
start = time.time()
df["review_text"] = df['review_text'].apply(cleanText)
end = time.time()
print(f"Cleaning time: {end-start}") # print exec. time
# save dataset to pickle
df.to_pickle(f'{args.folderLoc}cleaned_{args.filename[:-4]}.pkl')
print("pickle saved")
del df
gc.collect()



# punc = set(string.punctuation)
# print("starting")
# X_test['review_text'] = X_test['review_text'].apply(lambda x: [word for word in x if word not in punc])
# print("test_punct finished")
# X_train['review_text'] = X_train['review_text'].apply(lambda x: [word for word in x if word not in punc])
# print("Puncts removed")
