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


#python set
# add(item) 添加
# update() 批量添加 update([1,2])
# remove(item) 删除 元素不存在时会报错的
# Enter a code
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
S = set([1, 3, 5, 7, 9,11])

for l in L:
    if l in S:
        S.remove(l)
    else:
        S.add(l)
print(S)

# 不会报错的删除 discard()
name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
name_set.discard('Jenny')
print(name_set) # ==> set(['Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
name_set.discard('Jenny')
print(name_set) # ==> set(['Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl']
# 清除所有元素的方法clear()
name_set = set(['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
print(name_set) # ==> set(['Jenny', 'Ellena', 'Alice', 'Candy', 'David', 'Hally', 'Bob', 'Isen', 'Karl'])
name_set.clear()
print(name_set) # ==> set([])

#集合的子集和超集  issubset、issuperset
#set提供方法判断两个set之间的关系，比如两个集合set，判断其中一个set是否为另外一个set的子集或者超集。
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# 判断s1是否为s2的子集
print(s1.issubset(s2)) # ==> True
# 判断s2是否为s1的超集
print(s2.issuperset(s1)) # ==> True
#判断集合是否重合  isdisjoint 可以快速判断两个集合是否有重合，如果有重合，返回False，否则返回True。
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s1.isdisjoint(s2)) # ==> False，因为有重复元素1、2、3、4、5

#python 求和函数 sum()
i = 1
L = []
while i<= 100:
    L.append(i*i)
    i+=1
# print(sum(L))

#python 函数可变参数 *args 当做 tuple 使用
def fn_1(*args):
    print(args)

fn_1('a','b','c')

# 对于可变关键字参数，一般使用**kwargs来表示。Python会把可变关键字参数当作dict去处理
def info(**kwargs):
    print('name: {}, gender: {}, age: {}'.format(kwargs.get('name'), kwargs.get('gender'), kwargs.get('age')))

info(name = 'Alice', gender = 'girl', age = 16)

#对于一个拥有必需参数，默认参数，可变参数，可变关键字参数的函数，定义顺序是这样的
def func(param1, param2, param3 = None, *args, **kwargs):
    print(param1)
    print(param2)
    print(param3)
    print(args)
    print(kwargs)

func(100, 200, 300, 400, 500, name = 'Alice', score = 100)


def func(**args):
    i =0
    while i < len(args.get('name')):
        print("names : {} gender :{} age :{}".format(args.get('name')[i],args.get('gender')[i],args.get('age')[i]))
        i += 1
func(name = ['hei1','hei2','hei3'] , gender = ['boy','girl','boy'] , age = [99,98,19])

print("----------------- CLASS -----------------------------")


##### Python 对象 定义  class 类名:
class Person(object):   pass

xiaohong = Person()
xiaohong.name = 'xiaohong'
xiaohong.sex = 'girl'
xiaohong.age = 13

print(xiaohong.name)
print(xiaohong.sex)
print(xiaohong.age)

### 定义类的时候  添加一个特殊的__init__()方法，当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性
##需要注意的是，__init__() 方法的第一个参数必须是 self（也可以用别的名字，但建议使用习惯用法），后续参数则可以自由指定，和定义函数没有任何区别
##定义类后，就可以相应的实例化对象了，需要注意的是，在实例化的时候，需要提供除self以外的所有参数。
class Person(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


xiaoming = Person('Xiao Ming', 'boy', 13)
print(xiaoming.sex1)

###Python 类属性 是所有的实例共享
class Animal(object):
    count = 0
    def __init__(this,name,age):
        this.name = name
        this.age = age
        Animal.count += 1
dog = Animal('dog',1)
print('name : {} age :{}'.format(dog.name,dog.age))
print(Animal.count) # ===> 1
cat = Animal('cat',2)
print(Animal.count) # ===> 2


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
