#python Dictionary
# academy = {
#     "13_room":"python",
#     "12_room":"c#",
#     "11_room":"cyber security",
#     "10_room":["chief ceo","secretare"]
# }
# print(academy.keys())
# print(academy.get("13_room"))
# print(academy['10_room'][1])
#
# academy2 = dict(
#     name = "Bobir Akilhonov",
#     age = 41,
#     country = "Tashkent"
#
# )
# #academy2.copy()
# #academy2.popitem()
# #print(academy2.keys())
# #academy2.update({"name" : "Alish"})
# print(academy2)
#
# academy3 = academy2.copy()
# print(academy3)

# nested dict
# item = {
#     'tree1':{
#        'type':'yablonya',
#     'age':100,
#     'color_leaves':'brown'
# },
# 'tree2':{
#     'type':'ogurechniy',
#     'age':150,
#     'color_leaves':'white'
# },
#     'tree3':{
#         'type':'arbuzniy',
#         'age':300,
#         'color_leaves':'orange'
#     }
# }
# print(item['tree2']['age'])
# print(item['tree2']['color_leaves'])

# car = {
#   "brand": "Форд",
#   'model': 'Мустанг',
#   'year': 1964
# }
# car.update({"model" : "shelby"})
# print(car.get('model'))
# #print(car)
# car.update({"color" : "green"})
# #car.pop('model')
# #car.clear()
# print(car)

# a = 50
# b = 150
# if a > b:
#   print('b bolshe a')
# else:
#   print('a bolshe b ')

# i = 1
# while i <= 10:
#     print(i)
#     i +=1
# else:
#     print('error')

#     if i == 7:
# #       break
#         continue
#     i = i + 1
#     print(i)


#i = 1
#while i <= 10:
   # print(i)
  #  i += 1
    # i = i + 1
    # if i == 3:
    #    # break
    #    continue
    # print(i)
#else:
 # print('ERROR')
#
# N = int(input('write your number'))
# i = 0
# while i ** 2 !<= N:
#     print(i ** 2)
#     i += 1

# user = int(input("Enter your number: "))
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# while a <= user:
#     a = a * 2
#     b = b + 1
# else:
#     print("wdcoinpicpwcldk")
# print(b - 1, a // 2)

# a =['qovin', 'tarvuz','snikers','chips','cola']
# b = [1,2,3,4,5,6,7,8,9,10]
# # c = a + b
# # for x in c:
# #     print(x)
# for x in b:
#         print(x)

#1
#a = (1,2,3,4,5,6,7,8,9,10)
# print(a[0])
# print(a[0])
# print(a[-1])
# print(len(a))

# #5
# a = (1,2,3,4,5,6,7,8)
# def name(*org):
#     if a[0] == org[0]:
#         print("True")
#     else:
#         print('False')
#     if a[-1] == org[-1]:
#             print("True")
#     else:
#           print("False")
# name(1,9)

#a = [1,2,3,4,5,6]
#print(a[0:-3])

# a = (8,2)
# if a[0] / a[-1] != float:
#     print("True")
# else:
#     print("False")

# a = ["academy"]
# s = []
# for i in a:
#     #print( "", i,  "")
#     s+= i
# print(s)

# a = {
#     'year': '2025',
#     'month': '12',
#     'day': '31',
# }

# print(a['year']+'-'+a['month']+'-'+a['day'])

#a = (0)
#a = (100)
#for i in range(1,101):
#for i in range(-100,1):
#while a <= 100:
#    print(i)
#  print(a)
#  a+=3
#  a-=1
# while a == 0:
#     print(a)
#     a-=1

# a = [1,2,3,4,5,6,]
# print(a[4:6])

# slovar = {
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4,
# }
# for i in slovar.values():
#     i=i*2
#     print(i)

# a = "abcdef"
# print(a[::2])

# a = [1,2,3,4,5]
# a.reverse()
# print(a)

# a = 10
# while a <= 1000:
#     print(a)
#     a += 5

# a = ("abcdeabc")
# b = list(a)
# print(a[0:5])


# a = [1,-2,3,-4,5,-6,7,-8,9,-10]
# for i in a:
#     if i > 0:
#      print(i)

# a = [1.856,2.125,3.32,4.1,5.34]
# for i in a:
#     i = int(i)
#     print(i)

# slovar = {
#     'a':1,
#     'b':2,
#     'c':3,
#     'd':4,
# }
# for i in slovar:
#     print(slovar[i])
#print(slovar['a'],slovar['b'],slovar['c'],slovar['d'])


# a = [1,2,3]
# b = [4,5,6]
# print(a + b )``

# dct1 = {
#     'a' : 1,
#     'b' : 2
# }
# dct2 = {
#     'c':3,
#     'd':4

# }

# dct1.update(dct2 )
# print(dct1)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}
# for i in b:
#     a.symmetric_difference(i)
# print(jh)    

# for i in range(6,1,-1):
# #    print(" " * ((9 - i) // 2) + str(i) * i)
#     print(" " * ((9 - i) // 2) + str("x") * i)
# #    print(str(i) * i)
# a = [
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45],
#     [51, 52, 53, 54, 55]
# ]
# for i in a:
#     print(a[0][2])
    

# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# b = []
# print(b = a)


# events = [
#   {
#     'date':  '2019-12-29',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name4'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name5'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name6'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name7'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name8'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name9'
#   },
# ]
# events = [
#             {
#     'date':  '2019-12',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-11',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-11',
#     'event': 'name4'
#   },
#   {
#     'date':  '2020-10',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-10',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-11',
#     'event': 'name5'
#   },
#   {
#     'date':  '2020-11',
#     'event': 'name6'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name7'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name8'
#   },
#   {
#     'date':  '2020-12',
#     'event': 'name9'
#   },
# ]

# MyBox = {}
# for event in events:
#    for event in events:
    # date = event['date']
    # event_n = event['event']
    # if date not in MyBox:
    #     MyBox[date] = [event_n]
    # else:
    #     MyBox[date].append(event_n)
#         name = event['date']
#         event_n = event['event']
#         if name not in MyBox:
#             MyBox[name] = [event_n]
#         else:
#             MyBox[name].append(event_n)

# print(MyBox)

    # event = date['event']
    # date_n = date['date']
    # if event not in MyBox:
    #     MyBox[event] = [date_n]
    # else:
    #     MyBox[event].append(date_n)
    # print(MyBox)

# lst = ['abcd','ab','c','de','bc']
# b = filter(lambda word: word  , lst)
# print(list(b))

# num = 10

# def funcy():
# #    num = 4
# #    global num
#     num -= 2
#     return num

# print(funcy())

# def get_Info(txt, func):
#   print(func(txt))
  
# def func(name):
#   return 'user name is ' + name
  
# get_Info('john', func)
# print(func(name))

a =(2,3,4,1)
a.count()
print(a)



















