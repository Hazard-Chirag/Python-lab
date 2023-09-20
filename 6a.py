fname=input("Enter a filename")
infile=open(fname,"r")
line=int(input("Enter the First N lines to print"))
for x in range(line+1):
    a=infile.readline()
    print(x+1,":",a)
word=input("Enter word to find frequency")
count=0
for line in infile:
    r=line.split()
    count+=r.count(word)
print("The word",word,"aPPEARS ",count,"Number of times")
