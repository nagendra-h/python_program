# mystring = 'abcdefghigk'
# print(mystring[::])
# print(mystring[2:5])
# print(mystring[::3])
# print(mystring[2:6:2])
# print(mystring[::-4])
# print(mystring[::])

values = 'abcvhr'
res1 = ''
res2=''
for i in range(len(values)-1,-1,-1):
    # print(len(values)2)
    # print(i)
    # if  (len(values))//2==i:
    #     print(i)
    #     print(res2+res1)
    #     break
    # res1 = res1 + values[i]
    # res2 = res2 + values[len(values)- i -1]
    res1 = res1 + values[i]
print(res1)