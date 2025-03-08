filename = "The Adventures of Sherlock Holmes.txt"

with open(filename) as file: #2.1
    text=file.read()
    
print("The book is " + str(len(text)) + " characters long.")

with open(filename) as file: #2.2
    text=file.read().replace("'"," ")
    
words=text.split()
print("The book has " + str(len(words)) + " words.")

import re #2.3
with open(filename) as file:
    text=file.read()
    
    found_the = re.findall("[tT]he", text)
    found_and = re.findall("[aA]nd", text)
    found_i = re.findall("I", text)
    
total_the=0
total_and=0
total_i=0

for a in found_the:
    total_the+=1
for b in found_and:
    total_and+=1
for c in found_i:
    total_i+=1
    
print("'the' appears " + str(total_the) + " times.")
print("'and' appears " + str(total_and) + " times.")
print("'I' appears " + str(total_i) + " times.")