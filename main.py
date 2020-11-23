# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

a = 'python'
print('hello ', a or 'world')

b = ''

print('hello ', b or 'world')

print('fasdfd')

print(r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!''')

#多行文本操作
print(r''' "To be, or not to be":that is the question.
Whether it's nobler in the mind to suffer. ''')

#切片操作
s = 'AABCDEFGHHIJ'
print(s[1:9])

#Python之if语句 条件后的代码块可以是多行，只要一起保存缩进即可（缩进4个空格）
age = 17
if age >= 18:
    print('adult')
    print('1 a\'s age is ', age)
else:
    print('3 as')
print('2 a\'s age is ', age)

#Python之if-elif-else语句
score = 59
if score < 60:
    print('抱歉，考试不及格')
else:
    if score >= 90:
        print('恭喜你，拿到卓越的成绩')
    else:
        if score >= 80:
            print('恭喜你，拿到优秀的成绩')
        else:
            print('恭喜你，考试及格')


score = 100
if score < 60:
    print('抱歉，考试不及格')
elif score >= 90:
    print('恭喜你，拿到卓越的成绩')
elif score >= 80:
    print('恭喜你，拿到优秀的成绩')
else:
    print('恭喜你，考试及格')

#Python之for循环
s = 'ABCD'
for ch in s:
    print(ch) # 注意缩进
L = [75, 92, 59, 68, 99]
sum = 0.0;
for l in L:
    sum += l;
print(sum/5)

#Python之while循环
num = 1
sum = 0
while num <= 100:
    sum = sum + num # 注意缩进
    num = num + 1 # 注意缩进
print(sum) # ==> 5050
last = 10
first = 1
total = 1;
index = first
while index <= last:
    total = total * index
    index+=1
print('total = ', total)

#Python之break跳出循环
index = 1
sum = 0
while True:
    if index > 1000:
        break
    if index % 2 == 0:
        sum += index
    index += 1

print('sum = ', sum)

#Python之continue继续循环
index = 1
sum = 0
while index <= 1000:
    index += 1
    if index % 2 == 1:
        continue
    sum += index


print('sum = ', sum)

#Python之嵌套循环
s1 = 'ABC'
s2 = '123'
s3 = 'xyz'
for x in s1:
    for y in s2:
        for z in s3:
            print(x+y+z)

#Python list 如果我们越界切片的话，不会出现Python运行错误 只会返回空list
names = ['Alice', 'Bob', 'David', 'Ellena']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[5:10])
#在Python中，可以使用-1来表示最后一个元素。
print(names[-1])

L = [95.5, 85, 59, 66, 72]
L.sort(reverse=True)
print(L)
print(L[-3:-1])

#Python向list添加新的元素
names = ['Alice', 'Bob', 'David', 'Ellena']

#1、第一个办法是用append()方法 将元素添加到list的尾部
names.append("Baby1")
print(names)
#2、使用list的insert()方法，insert()方法和append()方法不一样，insert()方法需要两个参数，分别是需要插入的位置，以及需要插入的元素。
names.insert(3,"Baby2")
print(names)

#Python list删除元素
#1、pop()  删除最后一个元素
names.pop()
print(names)

#2、pop(index) 按指定索引删除元素
names.pop(3)
print(names)

#Python替换list中的元素 如果替换一个不存在的下标，则同样会引起Python运行错误。
L = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
L[2] = 'Canlina'
print(L)

L =[89, 72, 88, 79, 99]
L.sort(reverse=True)
print(L)
index = 0
while index < 5:
    if L[index] == 99 :
        L[index] = 'Ellena'
    elif L[index] == 79:
        L[index] = 'David'
    elif L[index] == 88:
        L[index] = 'Candy'
    elif L[index] == 72:
        L[index] = 'Bob'
    elif L[index] == 89:
        L[index] = 'Alice'

    index+=1
print(L)

#tuple 不可变的数组 访问tuple元素的其他方法
#1、count()方法 count()方法用来统计tuple中某个元素出现的次数。
#对于不存在的元素，count方法不会报错，而是返回0，这是合理的，因为元组里面有0个不存在的元素。
T = (1, 1, 2, 2, 3, 3, 1, 3, 5, 7, 9)
print(T.count(1)) # ==> 3
print(T.count(5)) # ==> 1
print(T.count(10)) # ==> 0

#2、index()方法 index()方法可以返回指定元素的下标，当一个元素多次重复出现时，则返回第一次出现的下标位置。
#当指定的元素不存在时，使用index()方法Python会报错。
print(T.index(1)) # ==> 0
#print(T.index(8))

#3、创建单元素的元组，元素后面加一个，
T = (1,)
print(T)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
