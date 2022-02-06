# def fibbo(n):
#     a = 0
#     b = 1
#     i = 0
#     while i <=n:
#         print(a)
#         c= a+b
#         a = b
#         b = c
#         i+=1
# print(fibbo(10))
# for i in range(-10,-0,):
#     print(i)
# files = ["youtube.txt", "amazon.pdf", "apple.xls", "flipkart.in"]
# res = []
# for file in files:
#     a= file.split(".")
#     if a == file:
#         pass
#     else:
#         res.append(a[-1])
# def vasu(*args):
#     for i in args:
#         if isinstance(i,str):
#             print(i[::-1])
#         else:
#             a = str(i)
#             print(a[::-1])
# vasu(10,30,'vasu','gurram')
# l = [1,2,3]
# print(*l)
# d = {'a':1,'b':2,'c':3}
# print(*d)
# print({**d})



# using user defined functions
# print 1 to 10
# def count(n):
#     for i in range(1,n):
#         print(i)
# count(10)
# print 10 to 1
# def count1(n):
#     for i in range(10,1,-1):
#         print(i)
# count1(10)
# print -1 to -10
# def count2(n):
#     for i in  range(-1,-n,-1):
#         print(i)
# count2(10)
# print -10 to -1
# def count3 (n):
#     for i in range(-n,-1,1):
#         print(i)
# count3(10)
# count of digits of a string
# def str_count(n):
#     count = 0
#     for i in range(len(n)):
#         count+=i
#     print(count)
# str_count('python')
# count of a string
# def str_count(n):
#     count = 0
#     for i in n:
#         count+=1
#     print(count)
# str_count('python')
# traversing through list
# def list_(n):
#     count =0
#     for i in n:
#         count+=1
#     print(count)
# list_([10,20,30,50])
# print index and its char
# def str_count(n):
#     for index,value in enumerate(n):
#         print(index,value)
# str_count('python')
# using len function
# string reversered order
# def str_count(n):
#     res = ''
#     for i in n:
#         res = i+res
#     print(res)
# str_count('hai')
# def str_count(n):
#     if isinstance(n,str):
#         print(n[::-1])
# str_count('python')
# def str_count(n):
#     for i in (n[::-1]):
#          print(i,end="")
# str_count('vasu')
# print even char in string
# d = 'vasu gurram'
# d1 = {}
# for index,i in enumerate(d):
#     d1[index]=i,index
# print(d1)
# d = ['vasu','gurram','suresh']
# dd = {(item,index):item if len(item)%2==0 for index,item in enumerate(d) }
# print(dd)
# st ='hello'
# s = set(st)
# l = list(s)
# count =0
# d ={}
# for i in l:
#     for j in st:
#         if j == i:
#             count+=1
#             d[i]=count
# print(d)
# def count(n):
#     print(n)
# def sum_ (n,sum=0):
#     if n>10:
#         return
#     c = print(n)
#     sum_(n+1)
#     if c>0:
#         last = c%10
#         sum+=last
#         n = c//10
#         return sum_(n,sum)
#     else:
#         return sum
# print(sum_(12345))
# def re(n):
#     if n>n:
#         pass
#     else:
#         count =0
#         if n%2==0:
#             a =n//10
#             count+=a
#     print(count)
# re(1234555)
# def fact(n,sum=1):
#     count =0
#     if n>1:
#         sum+=sum*1
#         return fact(n-1,sum)
#     return sum
# print(fact(4))
# mul = lambda a,b:a*b
# print(mul(10,30))
# last = lambda item:item[-1]
# print(last('pthon'))
# l = ['vasu','gurram','balaji','suresh']
# def names(num):
#     l= []
#     if type(num)==str and  'a'<=num<='z':
#          chr(ord(num)-32)
# res = map(names,l)
# print(list(res))
# l = [20,-20,-88,77]
# def neg(num):
#     if abs(num)==num:
#         return num
#
# res = map(neg,l)
# print(list(res))
# l = [10,20,5,66,55]
# def seq (num):
#     if enumerate(num) and l[num]==0:
#         return (index**2)
# res= map(seq,l)
# print(res)
# l = ['vasu','gurram','balaji']
# # a = 'happy birthday'
# for i in l:
#     print(i.upper())
# from lower case to upper case letters

# l = ['vasu','gurram','sreenivasulu','adilakshmi']
# def upper_case(num):
#     return num.upper()
# res = map(upper_case,l)
# print(list(res))

# negative numbers to postive numbers
# l = [20,50,-85,-99,100]
# def neg(num):
#     if abs(num)==num:
#         pass
#     elif abs(num)!=num:
#         return abs(num)
# res = map(neg,l)
# print(list(res))
# index sequres of list numbers
# l = [20,55,88,77,55,22,66,888,666]
# def seq (num):
#     while i<len(l):
#         i += 1
#         return i**2
# res = map (seq,l)
# print(list(res))
# l = [20,30,21,30,30,40,4]
# d= []
# for i in l:
#     a = l.pop(-1)
#     d.append(a)
# # print(d)
# d = {'s':2,'d':4,'v':4,'m':9,'l':7}
# h = {}
# for i in d:
#     value = d[i]
#     h[value]=i
# print(h)
# d2 ={}
# for i,j in d.items():
#     d2[j]=i
# print(d2)
d = 'pythonn is interpreted language'
# d1 = {}
# for i in d:
#     count = 0
#     for j in d:
#         if i==j:
#             count+=1
#     d1[i]=count
# print(d1)
# from collections import defaultdict
# dd = defaultdict(int)
# for word  in d:
#     dd[word]+=1
# print(dd)
# l = [12,20,3,-99,33]
# def neg(num):
#     a = []
#     if abs(num)!=num:
#          a.append(abs(num))
#     else:
#         a.append(num)
#     return a
# res = map(neg,l)
# print(list(res))


