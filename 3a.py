def determine(sentence):
    word=sentence.split()
    wordcount=len(word)
    lower,upper,digit=0,0,0
    for i in sentence:
        if(i>='A' and i<='Z'):
            upper+=1
        elif(i>='a' and i<='z'):
            lower+=1
        elif(i>='0' and i<='9'):
            digit+=1
    print("Number of digits: ",digit)
    print("Number of words: ",wordcount)
    print("Number of Uppercase: ",upper)
    print("Number of Lowercase: ",lower)

sentence=input("Enter a sentence")
determine(sentence)