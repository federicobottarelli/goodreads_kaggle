# goodreads_kaggle
My repositery for GoodReads books review Kaggle competition  
For more info: https://www.kaggle.com/competitions/goodreads-books-reviews-290312
  
  To elaborate faster the data operation with my personal computer, limitated to 16GB of RAM, I've tried to do the preprocessing part of the project with a bunch of scripts with command line arguments:
  ### File description:
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
