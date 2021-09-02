# Inspired by geeksforgeeks: https://www.geeksforgeeks.org/create-inverted-index-for-file-using-python/

# this will open the file
file = open('text1.txt', encoding='utf8')
read = file.read()
file.seek(0)
print("--- Raw file read: ---")
print(read)

# number of lines
line = 1
all_docs_list = [1]
for word in read:
    if word == '\n':
        line += 1
        all_docs_list.append(line)
print("--- Line count: ---")
print("Number of lines in file is: ", line)
print("All docs list: ", all_docs_list)

# create a list to store each line as an element of list
array = []
for i in range(line):
    array.append(file.readline())

print("--- List with each line as element: ---")
print(array)

# Remove punctuation:
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
for ele in read:
    if ele in punc:
        read = read.replace(ele, " ")
print("--- Punctuation removed: ---")
print(read)

# to maintain uniformity
read = read.lower()
print("--- Only lower case: ---")
print(read)

# Transforming into one line
oneline = read.replace('\r', '').replace('\n', '')
print("--- Transformed to one line: ---")
print(oneline)

# Creating list with all words
allwords=oneline.split(" ")
print("--- Created list with all words ---")
print(allwords)

# Removing "no go" words or phrases, like ''. Others can be added to the nogo-list.
nogo = ['']
for word in list(allwords):  # iterating on a copy
    if word in nogo:
        allwords.remove(word)
print("--- All words, without '': ---")
print(allwords)

# Remove duplicates
allwordsnoduplicate = []
for i in allwords:
  if i not in allwordsnoduplicate:
    allwordsnoduplicate.append(i)
print("--- List of all words, no duplicates: ---")
print(allwordsnoduplicate)

#Creating inverted index where each document is represented as a line in the text:
inverted_index = {} #Dictionary
for i in range(line):
    check = array[i].lower()
    for item in allwordsnoduplicate:

        if item in check:
            if item not in inverted_index:
                inverted_index[item] = []

            if item in inverted_index:
                inverted_index[item].append(i + 1)

print("=== TASKS: ===")
print("--- INVERTED INDEX! ---")
print(inverted_index)

# Boolean queries
print("=== BOOLEAN QUERIES ===")
print("--- Please enter two words, and the program will find out what lines they are in ---")

while True:
    First_term = input("Enter the first word: ")
    if First_term not in inverted_index.keys():
        print("Word not in text, sorry. Try another word.")
        continue
    else:
        break

while True:
    Second_term = input("Enter the second term: ")
    if Second_term not in inverted_index.keys():
        print("Word not in text, sorry. Try another word.")
        continue
    else:
        and_query = set(inverted_index[First_term]).intersection(
            inverted_index[Second_term])
        and_list = list(and_query)
        print("Documents with both terms: ")
        print(and_list)

        or_query = set(inverted_index[First_term]).union(
            inverted_index[Second_term])
        or_list = list(or_query)
        print("Documents with either term: ")
        print(or_list)

        #NOT query
        #Creating sets to use the difference operator
        set_list_first = set(inverted_index[First_term]) #set of docs where first term is represented
        set_list_second = set(inverted_index[Second_term]) #set of docs where second term is represented
        set_all = set(all_docs_list) #set of all docs available
        not_query_first = (set_all - set_list_first) #creating a set of all docs where first term is not represented
        not_query_second = (set_all - set_list_second) #creating a set of all docs where first term is not represented
        print("Documents without first term: ", list(not_query_first)) #Printing list
        print("Documents without second term: ", list(not_query_second)) #Printing list
        break