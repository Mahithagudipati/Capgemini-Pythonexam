def wordcounter(s):
    word_list={}
    for word in s:
        if word in word_list:
            word_list[word]+=1
        else:
            word_list[word]=1
    return word_list

def main():
    s=input("Enter a sentence : ").split()
    print(wordcounter(s))
main()
