# mystring = 'abcdefghigk'
# print(mystring[::])
# print(mystring[2:5])
# print(mystring[::3])
# print(mystring[2:6:2])
# print(mystring[::-4])
# print(mystring[::])

values = 'abcvhru'
res1 = ''
res2=''
a,b,c="name1","hello",343
print(a,b,c)
kk=list(values)
for i in range(len(list(values))//2):
    # print((len(values)-1)//2,i,"data")
    # if((len(values)-1)//2  == i):
    #     print(32233)
    #     kk=values.split(f'{values[i]}')
    #     kk.insert(1,values[i])
    #     print(kk)
        
    # temp = values[i]
    # temp1 = values[len(values)- i -1]
    # values[i]=temp1
    # values[(len(values)- i -1)] = temp
    kk[i]=values[-(i+1)]
    kk[-(i+1)]=values[i]



        # print((len(values)-1)//2)
    # print(values[(i==((len(values)-1))//2)])
    # if  (len(values))//2==i:
    #     # print(i)
    #     # print(res2+res1)
    #     break
    # res1 = res1 + values[i]
    # res2 = res2 + values[len(values)- i -1]
    # res1 = res1 + values[i]
print(''.join(kk))
name = 'raj%s'
n1 ='ram%shh%d%s'
n2="hiiii"
print(name%n1)
print(n1%("hello",323,"hi"))
print(f'{n2}data')