# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here
    with open("./story.txt", "r") as file:
      contents = file.read()
    print(contents)
    
    


def count_words():
    count= dict()
    text = read_file_content("./story.txt").split()
    # [assignment] Add your code here
    for word in text:
        if word in count:
            count[word] +=1
        else:
            count[word] = 1
        return count
        print(count_words())