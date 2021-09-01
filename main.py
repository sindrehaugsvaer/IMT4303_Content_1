from nltk.tokenize import word_tokenize

# Retrieved from geeksforgeeks.org: https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

# this will open the file
file = open('text1.txt', encoding='utf8')
read = file.read()
file.seek(0)
print(read)
print("---")

# number of lines
line = 1
for word in read:
    if word == '\n':
        line += 1
print("---")
print("Number of lines in file is: ", line)
print("---")

# create a list to
# store each line as
# an element of list
array = []
for i in range(line):
    array.append(file.readline())

print("each line as element of list")
print(array)
print("---")

# Remove punctuation:
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:
    if ele in punc:
        read = read.replace(ele, " ")
print(read)
print("---")

# to maintain uniformity
read = read.lower()
print(read)
print("---")

# Creating array with all words
oneline = read.replace('\r', '').replace('\n', '')
print("--- oneline")
print(oneline)

allwords=oneline.split(" ")
print("--- allwords")
print(allwords)


#Creating inverted index:
dict = {}
for i in range(line):
    check = array[i].lower()
    for item in allwords:

        if item in check:
            if item not in dict:
                dict[item] = []

            if item in dict:
                dict[item].append(i + 1)
print("--- inverted index!")
print(dict)