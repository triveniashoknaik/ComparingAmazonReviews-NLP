
# coding: utf-8

# In[1]:

import nltk
from nltk.corpus import PlaintextCorpusReader


# In[2]:

corpus_root = '/Users/triveninaik/Desktop'
wordlists = PlaintextCorpusReader(corpus_root, 'musical_instruments.txt')
wordlists.fileids()


# In[3]:

from nltk import FreqDist


# In[4]:

file0 = wordlists.fileids()[0]


# In[5]:

musictext = wordlists.raw(file0)


# In[6]:

musictokens = nltk.word_tokenize(musictext)


# In[7]:

musicwords = [w.lower() for w in musictokens]


# In[8]:

print(len(musicwords))


# In[9]:

print(musicwords[:110])


# In[10]:

# Creating a frequency distribution of words
ndist = FreqDist(musicwords)
nitems = ndist.most_common(100)
for item in nitems:
    print (item[0], '\t',item[1])


# In[11]:

# Creating a frequency distribution of words
ndist = FreqDist(musicwords)
nitems = ndist.most_common(100)
for item in nitems:
    print (item[0], '\t',item[1])


# In[12]:

musicbigrams = list(nltk.bigrams(musicwords))
print(musicbigrams[:100])


# In[13]:

# Regular Expression to match non-alphabetic characters
import re
# this regular expression pattern matches any word that contains all non-alphabetical
#   lower-case characters [^a-z]+
# the beginning ^ and ending $ require the match to begin and end on a word boundary 
pattern = re.compile('^[^a-z]+$')


# In[14]:

# match the pattern on a text string with all special (non-alphabetical) characters
nonAlphaMatch = pattern.match('**')
#  if it matched, print a message
if nonAlphaMatch: print ('matched non-alphabetical')


# In[15]:

# function that takes a word and returns true if it consists only
#   of non-alphabetic characters  (assumes import re)
def alpha_filter(w):
  # pattern to match word of non-alphabetical characters
  pattern = re.compile('^[^a-z]+$')
  if (pattern.match(w)):
    return True
  else:
    return False


# In[17]:

#apply the function to remove non-alphabetical words in musicwords
musicwords = [w for w in musicwords if not alpha_filter(w)]
print(len(musicwords))
print(musicwords)


# In[18]:

# get a list of stopwords from nltk
stopwords = nltk.corpus.stopwords.words('english')
print('number stopwords:', len(stopwords))
print(stopwords)


# In[24]:

newstopwords = stopwords.append("can't,won't,n't,with")


# In[25]:

print('number stopwords:', len(stopwords))
print(stopwords)


# In[23]:

newstopwords = stopwords.append("can't,won't,n't,with") 
print('number stopwords:', len(stopwords))
print(stopwords)


# In[ ]:



