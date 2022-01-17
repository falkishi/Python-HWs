#Arguments:
#  filename: name of file to read in
#Returns: a list of strings
# each string is one line in the file, 
# and all of the characters should be lowercase, have no newlines, and have both a prefix and suffix of '__' (2 underscores)
#Notes: make sure to pad the beginning and end of the string with '_'
#       make sure the string does not contain newlines
#       make sure to convert the string to lower-case
#       so "Hello World" should be turned into "__hello world__"
#hints: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
#       https://docs.python.org/3/library/stdtypes.html#str.splitlines
def getFormattedText(filename) :
    #fill in
    lines = []
    
    #Opening filename
    with open(filename,"r") as Function:
        Files = Function.read().splitlines();
        
    
    #for loop
    for Row in Files:
        down = Row.lower();
        g_string = "__" + down + "__" ;
        lines.append(g_string);

    #Closes the open file    
    Function.close();


            
    return (lines);
        
        

#Arguments:
#  line: a string of text
#Returns: a list of 3-character n-grams
def getNgrams(line) :
    #fill in
    nGrams = [];
    
    #The extension of line
    distance = len(line);
    
    G = [line[i : i + 3] for i in range(distance - 2)];
    
    nGrams = [g for g in G];

    return (nGrams);

#Arguments:
#  filename: the filename to create an n-gram dictionary for
#Returns: a dictionary
#  where ngrams are the keys and the count of that ngram is the value.
#Notes: Remember that getFormattedText gives you a list of lines, and you want the ngrams from
#       all the lines put together.
#       You should use getFormattedText() and getNgrams() in this function.
#Hint: dict.fromkeys(l, 0) will initialize a dictionary with the keys in list l and an
#      initial value of 0
def getDict(filename):
    #fill in
    nGramDict = {};
    
    Array1 = [];

    for i in getFormattedText(filename):
        
        Array2 = getNgrams(i);

        for j in Array2:
            
            if not Array1.__contains__(j):
                
                Array1.append(j);

    nGramDict = dict.fromkeys(Array1,0);

    for k in getFormattedText(filename):
        for j in getNgrams(k):
            
            nGramDict[j] = nGramDict[j] + 1;

    
    return (nGramDict);

#Arguments:
#   filename: the filename to generate a list of top N (most frequent n-gram, count) tuples for
#   N: the number of most frequent n-gram tuples to have in the output list.
#Returns: a list of N tuples 
#   which represent the (n-gram, count) pairs that are most common in the file.
#   To clarify, the first tuple in the list represents the most common n-gram, the second tuple the second most common, etc...
#You may find the following StackOverflow post helpful for sorting a dictionary by its values: 
#Also consider the dict method popitem()
#https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def topNCommon(filename,N):
    commonN = [];
    
    d_ng = getDict(filename);

    sor_d = {a : b for a,b in sorted(d_ng.items(), key = lambda obj : obj[1])} ;

    objs = [];
    
    objs = [o for o in sor_d.keys()];
    i_d = dict()
    
    for o in reversed(objs):
        
        i_d[o] = sor_d[o];

    for o in list(i_d)[0:N]:
        
        commonN.append((o, i_d[o]));
    
    
    return (commonN);

########################################## Checkpoint, can test code above before proceeding #############################################

#Arguments:
#   fileNamesList: a list of filepath strings for the different language text files to process
#Returns: a list of dictionaries 
#   where each dictionary corresponds to one of the filepath strings.
#   Each dictionary in the list
#   should have keys corresponding to the n-grams, and values corresponding to the count of the n-gram
#Hint: Use functions defined in previous step.
def getAllDicts(fileNamesList):
    langDicts = []
    
    langDicts = [getDict(filename) for filename in fileNamesList]; 
    
    return (langDicts);

#Arguments:
#   listOfDicts: A list of dictionaries where the keys are n-grams and the values are the count of the n-gram
#Returns: an alphabetically sorted list containing all of the n-grams across all of the dictionaries in listOfDicts (note, do not have duplicates n-grams)
#Notes: It is recommended to use the "set" data type when doing this (look up "set union", or "set update" for python)
#   Also, for alphabetically sorted, we mean that if you have a list of the n-grams altogether across all the languages, and you call sorted() on it, that is the output we want
def dictUnion(listOfDicts):
    unionNGrams = [];
    
    pl1 = set();
    objs = [];
    cer = 0;

    for i_d in listOfDicts:
        objs.extend(i_d.keys());

    objs_s = set(objs);
    
    pl2 = pl1.union(objs_s);
    
    ng = list(pl2);

    unionNGrams = sorted(ng);

    
    
    return (unionNGrams);


#Arguments:
#   langFiles: list of filepaths of the languages to compare testFile to.
#Returns a sorted list of all the n-grams across the languages
# Note: Use previous two functions.
def getAllNGrams(langFiles):
    allNGrams = [];
    
    g_d = getAllDicts(langFiles);

    ng = dictUnion(g_d);

    allNGrams = [g for g in ng];

    return (allNGrams);

########################################## Checkpoint, can test code above before proceeding #############################################

#Arguments:
#   testFile: mystery file's filepath to determine language of
#   langFiles: list of filepaths of the languages to compare testFile to.
#   N: the number of top n-grams for comparison
#Returns the filepath of the language that has the highest number of top 10 matches that are similar to mystery file.
#Note/Hint: depending how you implemented topNCommon() earlier, you should only need to call it once per language, and doing so avoids a possible error
def compareLang(testFile,langFiles,N):
    langMatch = ''
    
    b_ng = set([l[0] for l in topNCommon(testFile, N)]);
    
    Arr1 = [];
    for folders in langFiles:
        tg = set([tup[0] for tup in topNCommon(folders, N)]);
        cross = b_ng.intersection(tg);
        Arr1.append(cross);
        
    Arrays_in = []
    for r in Arr1:
        Arrays_in.append(len(r));

    most = max(Arrays_in);

    i = Arrays_in.index(most);

    langMatch = langMatch + langFiles[i]
        
        
    return (langMatch);




if __name__ == '__main__':
    from os import listdir
    from os.path import isfile, join, splitext
    
    #Test topNCommon()
    path = join('ngrams','english.txt')
    print(topNCommon(path,10))
    
    #Compile ngrams across all 6 languages and determine a mystery language
    path='ngrams'
    fileList = [f for f in listdir(path) if isfile(join(path, f))]
    pathList = [join(path, f) for f in fileList if 'mystery' not in f]#conditional excludes mystery.txt
    print(getAllNGrams(pathList))#list of all n-grams spanning all languages
    
    testFile = join(path,'mystery.txt')
    print(compareLang(testFile, pathList, 20))#determine language of mystery file

