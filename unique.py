def unique(x):
i=0
d=0
y=[]
while(i<len(x)):
d=0
f=x[i] in y
if (f==false):
y.append(x[i])
i=i+1
return y
print unique(["py","py","qw","qwqwqwqwq","ui","UI"])
