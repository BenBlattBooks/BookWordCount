import nltk
import pandas as pd

#This file does not do too much - but shows the form of opening a particular word count file and reading the frequency. If you just want to explore the data a bit start here.


#Opens up one book from Rowling, Collins, and Galbraith (who is also Rowling)
WordsR = pd.read_csv('Words/Rowling/Rowling_1997_HarryPotter1_Words.csv')
WordsC = pd.read_csv('Words/Collins/Collins_TheHungerGames_2008_Words.csv')
WordsG = pd.read_csv('Words/Galbraith/Galbraith_CuckoosCalling_2013_Words.csv')


#Count number of words in each book
LenR=sum(WordsR['Count'])
LenC=sum(WordsC['Count'])
LenG=sum(WordsC['Count'])


#Set Test Word
TestWord="later"

try:
    RWord=100000*float(WordsR.loc[WordsR['Word'] == TestWord]['Count'])/LenR
except TypeError:
    RWord=0
try:
    CWord=100000*float(WordsC.loc[WordsC['Word'] == TestWord]['Count'])/LenC
except TypeError:
    CWord=0
try:
    GWord=100000*float(WordsG.loc[WordsG['Word'] == TestWord]['Count'])/LenG
except TypeError:
    GWord=0

print "Rowling Freq of '"+TestWord+"' per 100,000 Words: "+str(int(RWord))
print "Collins Freq of '"+TestWord+"' per 100,000 Words: "+str(int(CWord))
print "Galbraith Freq of '"+TestWord+"' per 100,000 Words: "+str(int(GWord))
