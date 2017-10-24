#AmazonReviews

# coding: utf-8

# In[1]:

import nltk


# In[2]:

from nltk.corpus import PlaintextCorpusReader


# In[3]:

corpus_root = '/Users/triveninaik/Desktop'
wordlists = PlaintextCorpusReader(corpus_root, 'automotive.txt')
wordlists.fileids()


# In[4]:

from nltk import FreqDist


# In[7]:

file0 = wordlists.fileids()[0]


# In[8]:

automotivetext = wordlists.raw(file0)


# In[9]:

automotivetokens = nltk.word_tokenize(automotivetext)


# In[10]:

automotivewords = [w.lower() for w in automotivetokens]


# In[11]:

print(len(automotivewords))


# In[12]:

print(automotivewords[:110])


# In[13]:

# Creating a frequency distribution of words
ndist = FreqDist(automotivewords)
nitems = ndist.most_common(50)
for item in nitems:
    print (item[0], '\t',item[1])


# In[14]:

automotivebigrams = list(nltk.bigrams(automotivewords))
print(automotivebigrams[:50])


# In[15]:

# Regular Expression to match non-alphabetic characters
import re
# this regular expression pattern matches any word that contains all non-alphabetical
#   lower-case characters [^a-z]+
# the beginning ^ and ending $ require the match to begin and end on a word boundary 
pattern = re.compile('^[^a-z]+$')


# In[16]:

# match the pattern on a text string with all special (non-alphabetical) characters
nonAlphaMatch = pattern.match('**')
#  if it matched, print a message
if nonAlphaMatch: print ('matched non-alphabetical')


# In[17]:

# function that takes a word and returns true if it consists only
#   of non-alphabetic characters  (assumes import re)
def alpha_filter(w):
  # pattern to match word of non-alphabetical characters
  pattern = re.compile('^[^a-z]+$')
  if (pattern.match(w)):
    return True
  else:
    return False


# In[18]:

# apply the function to remove non-alphabetical words in emmawords
alphaautomotivewords = [w for w in automotivewords if not alpha_filter(w)]
print(len(alphaautomotivewords))
print(alphaautomotivewords[:100])


# In[19]:

# get a list of stopwords from nltk
stopwords = nltk.corpus.stopwords.words('english')
print('number stopwords:', len(stopwords))
print(stopwords)


# In[25]:

newstopwords = stopwords.append("can't,won't,n't,with")


# In[24]:

# look at some bigrams using the nltk.bigrams function
automotivetrigrams = list(nltk.trigrams(automotivewords))
print(automotivetrigrams[:50])


# In[26]:

# get a list of stopwords from nltk
stopwords = nltk.corpus.stopwords.words('english')
print('number stopwords:', len(stopwords))
print(stopwords)


# In[27]:

newstopwords = stopwords.append("can't,won't,n't,with")


# In[31]:

print('number stopwords:', len(newstopwords))
print(newstopwords)


# In[ ]:



