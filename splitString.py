def split1(str1):
    
    lst2=[]
    for i in range(len(str1)):
        if str1[i] == " ":
            lst2.append(i)
    lst2.append(len(str1))
    lst3=[None]*len(lst2)
    c=0
    for i in range(len(lst2)):
        n=lst2[i]
        lst3[i]=str1[c:n]
        c=n+1


    return lst3
            
            
  
str1='Hello I am A Splitted String'


result=split1(str1)

print(result)