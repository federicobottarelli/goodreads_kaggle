# goodreads_kaggle
My repositery for GoodReads books review Kaggle competition  
For more info: https://www.kaggle.com/competitions/goodreads-books-reviews-290312
  
  To elaborate faster the data operation with my personal computer, limitated to 16GB of RAM, I've tried to do the preprocessing part of the project with a bunch of scripts with command line arguments with the sequent organization:
  1. [00_less_data.py](00_less_data.py)
 
  
 Things To Do:
 - [ ] to perform lemmatization implement a method to tokenize in sentences (can improve performance because is possible parallelize POS-tagging).
 - [ ] try a simple model to classify
  
 ##### Sentence pipeline
 1. Take the column with texts from the original dataframe
 2. Remove HTML tags, URL, weird character but NOT the punctuation marker (we need them for the sentence tokenization)
 3. Divide any texts in list of sentences
 4. remove punctuation
 5. tokenize the sentences in word, making a structure with a list of sentence made by list of words, with this we can apply post_tag_sent() from NLTK library.
  
  ### Detailed script's description:
  #### 00_less_data.py
  Can do two things: (work with CSV and pickle files)
    - by default return a sample of the dataset with a choosen number of rows specified with the arguments --nRows
    - with the arguments --isolateText set to True can return two dataset: one with only the Series with the string variable to be pre-processed and one with the other remain variables, is needed to specify the name of the text variable with the argument --varText
    
    
 #### 01_cleanText.py
 Is a script to pre-process string of text before the tokenization, it removes URL, HTML tag, punctuation, digits and all non-ASCII characthers.
 - accept only pickles file format and return in the same format
  


### Citation
- Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18. [bibtex]
- Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19. [bibtex]
