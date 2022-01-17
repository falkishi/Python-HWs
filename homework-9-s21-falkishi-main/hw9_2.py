from helper import remove_punc
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import string
import numpy as np

#Clean and lemmatize the contents of a document
#Takes in a file name to read in and clean
#Return a list of words, without stopwords and punctuation, and with all words stemmed
# NOTE: Do not append any directory names to doc -- assume we will give you
# a string representing a file name that will open correctly
def readAndCleanDoc(doc) :
    #1. Open document, read text into *single* string
        with open(doc) as file:
            
            file_r = file.read();
            
            info = file_r.splitlines();
    #2. Tokenize string using nltk.tokenize.word_tokenize
        document_tok = [nltk.tokenize.word_tokenize(i) for i in info];


    #3. Filter out punctuation from list of words (use remove_punc)
        pun_document = [remove_punc(d1) for d1 in document_tok];


    #4. Make the words lower case
        small_document = [[i.lower() for i in d1] for d1 in pun_document];



    #5. Filter out stopwords
        pause = stopwords.words('english');
        clear_tok_d = [[i.lower() for i in words if i.lower() not in pause] for words in small_document];
        fil_document= [i for i in clear_tok_d if i];

    #6. Stem words
        lemm = WordNetLemmatizer();
        st = PorterStemmer();
        clear_document_tok_l = [[st.stem(i) for i in words] for words in fil_document];

        Arr_word = [];
        for k in clear_document_tok_l:
            for i in k:
                Arr_word.append(i);

        Arr_word = [m for m in Arr_word];

        file.close();
    
        return (Arr_word);
    
#Builds a doc-word matrix for a set of documents
#Takes in a *list of filenames*
#
#Returns 1) a doc-word matrix for the cleaned documents
#This should be a 2-dimensional numpy array, with one row per document and one 
#column per word (there should be as many columns as unique words that appear
#across *all* documents. Also, Before constructing the doc-word matrix, 
#you should sort the wordlist output and construct the doc-word matrix based on the sorted list
#
#Also returns 2) a list of words that should correspond to the columns in
#docword
def buildDocWordMatrix(doclist) :
    #1. Create word lists for each cleaned doc (use readAndCleanDoc)
    w_doc = [readAndCleanDoc(k) for k in doclist];

    w_pl = set();

    for w in w_doc:
        w_pl.update(w);

    Arr_w = list(w_pl);

    Arr_w = sorted(Arr_w);

    #2. Use these word lists to build the doc word matrix
    docword = np.zeros((len(doclist),len(Arr_w)));

    for s,w in enumerate(w_doc):
        for c in w:

            docword[s,Arr_w.index(c)] = docword[s,Arr_w.index(c)] + 1;
            
    return (docword, Arr_w);
    
#Builds a term-frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns a term-frequency matrix, which should be a 2-dimensional numpy array
#with the same shape as docword
def buildTFMatrix(docword) :
    #fill in
    tf = [k / np.sum(k) for k in docword];
    
    tf = np.array(tf);
    

    return (tf);
    
#Builds an inverse document frequency matrix
#Takes in a doc word matrix (as built in buildDocWordMatrix)
#Returns an inverse document frequency matrix (should be a 1xW numpy array where
#W is the number of words in the doc word matrix)
#Don't forget the log factor!
def buildIDFMatrix(docword) :
    #fill in
    column_s = np.sum(docword , axis = 0);
    
    num_A = [0] * column_s.size;
    
    if len(docword) > 1:
        for m in docword:
            index = 0;
            
            for n in m:
                if n != 0:
                    num_A[index] = num_A[index] + 1;
                    
                index = index + 1;

    else:
         num_A = [1] * column_s.size;

    idf = np.array([]);
    
    known = np.ones((1,len(column_s)));
    
    column_s1 = column_s * known
    
    idf = np.log10(len(docword) / np.array(num_A))
    
    idf = idf * known
    


    return (idf);
    
#Builds a tf-idf matrix given a doc word matrix
def buildTFIDFMatrix(docword) :
    #fill in
    
    idf = buildIDFMatrix(docword);

    tf = [k / np.sum(k) for k in docword];
    
    tf = np.array(tf);

    tfidf = tf * idf;


    return (tfidf);
    
#Find the three most distinctive words, according to TFIDF, in each document
#Input: a docword matrix, a wordlist (corresponding to columns) and a doclist 
# (corresponding to rows)
#Output: a dictionary, mapping each document name from doclist to an (ordered
# list of the three most common words in each document
def findDistinctiveWords(docword, wordlist, doclist) :
    distinctiveWords = {};
    #fill in
    #you might find numpy.argsort helpful for solving this problem:
    #https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html
    distance = len(doclist);
    
    for k in range(distance):

        tfidf = buildTFIDFMatrix(docword);

        w_d = np.argsort(-tfidf[k,:])[:3];

        distinctiveWords[doclist[k]] = list(np.array(wordlist)[w_d]);
    
    
    return (distinctiveWords);


if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    ### Test Cases ###
    directory='lecs'
    path1 = join(directory, '1_vidText.txt')
    path2 = join(directory, '2_vidText.txt')
    
    # Uncomment and recomment ths part where you see fit for testing purposes
    
   # print("*** Testing readAndCleanDoc ***")
   # print(readAndCleanDoc(path1)[0:5])
   # print("*** Testing buildDocWordMatrix ***") 
   # doclist =[path1, path2]
   # docword, wordlist = buildDocWordMatrix(doclist)
   # print(docword.shape)
   # print(len(wordlist))
   # print(docword[0][0:10])
   # print(wordlist[0:10])
   # print(docword[1][0:10])
   # print("*** Testing buildTFMatrix ***") 
   # tf = buildTFMatrix(docword)
   # print(tf[0][0:10])
   # print(tf[1][0:10])
   # print(tf.sum(axis =1))
   # print("*** Testing buildIDFMatrix ***") 
   # idf = buildIDFMatrix(docword)
   # print(idf[0][0:10])
   # print("*** Testing buildTFIDFMatrix ***") 
   # tfidf = buildTFIDFMatrix(docword)
   # print(tfidf.shape)
   # print(tfidf[0][0:10])
   # print(tfidf[1][0:10])
   # print("*** Testing findDistinctiveWords ***")
   # print(findDistinctiveWords(docword, wordlist, doclist))
    
