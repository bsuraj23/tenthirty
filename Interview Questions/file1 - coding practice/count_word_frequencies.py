# Write code to read a text file and count word frequencies.
from collections import Counter

def count_word_frequencies(newfile):
    try:
        with open(newfile,'r',encoding='utf-8') as file:
            text=file.read().lower()   #read content and convert to lowercase
            words=text.split()          #split into words
            word_counts=Counter(words)   #count word frequiences
            return word_counts
    except FileNotFoundError:
        print("Error: File not found")
        return {}

if __name__=="__main__":
    newfile="sample.txt"        
    counts=count_word_frequencies(newfile)
    for word, freq in counts.items():
        print(f"{word}:{freq}")
        
#if you want to run the code you need to create the file which you given in this code 'sample.txt'
#to check the file directory use 'dir' command in the terminal it will show the path, if the file is not there in the path you need to change
#the path or you need to move the file to current path