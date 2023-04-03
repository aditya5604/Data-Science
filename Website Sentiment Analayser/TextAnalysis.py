from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import nltk


Output_data = pd.read_csv("D:\ADITYA\DATASETS\BlackCoffer\Code\Output Data Structure.csv ")



def remove_items(test_list, item):
 
    res = [i for i in test_list if i != item]
 
    return res

with open('StopWords_Auditor.txt', 'r') as file:
    Auditor = file.read().replace('\n', '')
    Auditor = Auditor.lower()
    Auditor = word_tokenize(Auditor)

with open('StopWords_Currencies.txt', 'r') as file:
    Currency = file.read().replace('\n', ' ')
    Currency = Currency.lower()
    Currency = word_tokenize(Currency)

with open('StopWords_DatesandNumbers.txt', 'r') as file:
    Date_and_Number = file.read().replace('\n', ' ')
    Dates_and_Numbers = Date_and_Number.lower()
    Dates_and_Numbers = word_tokenize(Dates_and_Numbers)

with open('StopWords_Generic.txt', 'r') as file:
    Generic = file.read().replace('\n', ' ')
    Generic = Generic.lower()
    Generic = word_tokenize(Generic)

with open('StopWords_Geographic.txt', 'r') as file:
    Geographic = file.read().replace('\n', ' ')
    Geographic = Geographic.lower()
    Geographic = word_tokenize(Geographic)

with open('StopWords_GenericLong.txt', 'r') as file:
    GenericLong = file.read().replace('\n', ' ')
    GenericLong = GenericLong.lower()
    GenericLong = word_tokenize(GenericLong)

with open('StopWords_Names.txt', 'r') as file:
    Names = file.read().replace('\n', ' ')
    Names = Names.lower()
    Names = word_tokenize(Names)

with open('positive-words.txt', 'r') as file:
    Positive = file.read().replace('\n', ' ')
    Positive = Positive.lower()
    Positive = word_tokenize(Positive)

with open('negative-words.txt', 'r') as file:
    Negative = file.read().replace('\n', ' ')
    Negative = Negative.lower()
    Negative = word_tokenize(Negative)

with open('Garbage.txt', 'r') as file:
    Garbage = file.read().replace('\n', ' ')
    Garbage = Garbage.lower()
    Garbage = word_tokenize(Garbage)

#Concatenate all the lists to create a new list of stopwords.
StopWords =  Auditor + Currency + Dates_and_Numbers + Generic + GenericLong + Geographic + Names

for j in range(37, 151):
    with open('{0}.0.txt'.format(j), 'r') as file:
       data = file.read().replace('\n', '')
    data = data.lower()
    data = word_tokenize(data)
    CleanData = data
    TotalGarbage = 0
    TotalSentence = CleanData.count('.') + 1
    TotalWords = len(CleanData)

    # Code to clean the data of the garbage we scraped earlier.
    for i in data:
       GarbageScore = 0
       if i in Garbage:
            GarbageScore = CleanData.count(i)
            CleanData = remove_items(CleanData, i)
            TotalGarbage = TotalGarbage + GarbageScore
            
    CleanDataofStopWords = CleanData

    #Removing the StopWords

    for i in CleanData:
        if i in StopWords:
            CleanDataofStopWords.remove(i)
   
    WordCount = len(CleanDataofStopWords) #Total Word Count Of Data

    AvgSenLength = WordCount/TotalSentence #Calculate Average Sentence Length
    AvgWordsPerSentence = WordCount/TotalSentence #Calculate Average Words Per SentencE
 
    TotalChar = 0
    SyllableCount = 0
    ComplexWordCount = 0
    Vowel = ['a', 'e', 'i', 'o', 'u']
    #Calculate the  Syllable Count and Complex Word Count
    for i in CleanDataofStopWords:
        TotalChar = TotalChar + len(i)
        word = i
        count = 0
        for i in range(0, len(word)):
            if word[i] in Vowel:
                SyllableCount = SyllableCount + 1
                count = count + 1
                if word[i] == 'e' and i != len(word) - 1 and (word[i+1] == 's' or word[i+1] == 's'):
                    SyllableCount = SyllableCount - 1
                
        if count >= 2:
          ComplexWordCount = ComplexWordCount + 1

    AvgWordLength = TotalChar/WordCount #Calculate Average Word Length
    SyllablePerWord = SyllableCount/WordCount
   
    PositiveScore = 0
    NegativeScore = 0
   #calculate postive and negative score
    for i in CleanDataofStopWords:
        if i in Positive:
            PositiveScore = PositiveScore + 1
        if i in Negative:
            NegativeScore = NegativeScore - 1
        

    #Calculate Polarity score
    PolarityScore = (PositiveScore  + NegativeScore) / (PositiveScore + (NegativeScore*(-1)) + 1)
    #Caculate Subjectivity score
    SubjectivityScore = (PositiveScore + (NegativeScore*-1 ))/WordCount
    #Calculaye Fog Index
    FogIndex = 0.4*(AvgSenLength + (ComplexWordCount/WordCount)*100)
    
    CleanDataofStopWords = ' '.join(CleanDataofStopWords)
    CleanDataofStopWords = word_tokenize(CleanDataofStopWords)
    CleanDataofStopWords = nltk.pos_tag(CleanDataofStopWords)
    PersonalPronouns = 0
    
    for i in CleanDataofStopWords:
        if i[1] == 'PRP':
            PersonalPronouns = PersonalPronouns + 1

    
    Output_data['POSITIVE SCORE'][j-37] = PositiveScore
    Output_data['NEGATIVE SCORE'][j-37] = NegativeScore
    Output_data['SUBJECTIVITY SCORE'][j-37] = SubjectivityScore
    Output_data['POLARITY SCORE'][j-37] = PolarityScore
    Output_data['FOG INDEX'][j-37] = FogIndex
    Output_data['AVG NUMBER OF WORDS PER SENTENCE'][j-37] = AvgWordsPerSentence
    Output_data['COMPLEX WORD COUNT'][j - 37] = ComplexWordCount
    Output_data['SYLLABLE PER WORD'][j - 37] = SyllablePerWord
    Output_data['AVG SENTENCE LENGTH'][j - 37] = AvgSenLength
    Output_data['PERCENTAGE OF COMPLEX WORDS'][j - 37] = (ComplexWordCount/WordCount)*100
    Output_data['AVG WORD LENGTH'][j - 37] = AvgWordLength
    Output_data['WORD COUNT'][j - 37] = WordCount
    Output_data['PERSONAL PRONOUNS'][j - 37] = PersonalPronouns


Output_data = Output_data.drop(['Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25'], axis = 1)
Output_data = Output_data.dropna()                               

Output_data.to_excel('FinalOutput.xlsx')
    
        

    