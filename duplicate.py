

fl1=open("manju.txt","w")

textadded=["hello manju how ar you","how i am doing good","they going to the school","Write this into file","You are doing awesome"]
textadded1=["hello manju how ar you","how i am doing good","they going to the school","Write this into file","You are doing awesome"]
textadded2=["hello manju how ar you","how i am doing good","they going to the school","Write this into file","You are doing awesome"]
textadded3=["hello manju how ar you","how i am doing good","they going to the school","Write this into file","You are doing awesome"]
fl1.writelines(textadded)
fl1.writelines(textadded1)
fl1.writelines(textadded2)
fl1.writelines(textadded3)
fl1.close()

fl2=open("manju.txt","r")
long_string=fl2.read()
arr=long_string.split(" ")
#print arr
count={}
for word in arr:
   if word not in count:
   	count[word]=0
   
   count[word]+=1
for word in count:
	print ('{0} word has occured {1}'.format(word,count[word]))


