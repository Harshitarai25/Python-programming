#questions on dictionary
1.....# to update dictionary
d={}
x=int(input("enter the number of elements"))
for i in range(x):
    y=int(input("enter key"))
    d[y]={}
    k=int(input("enter the keys"))
    v=int(input("enter the values"))
    d[y].update({k:v})
print(d)
2.....#to find sum of values in dictionary 
d={}
x=int(input("enter the number of elements"))
for i in range(x):
    k=int(input("enter the keys"))
    v=int(input("enter the values"))
    d.update({k:v})
s=0
for i in d.values():
    s+=i
print(s)
3.....#to find sum of keys in dictionary 
d={}
x=int(input("enter the number of elements"))
for i in range(x):
    k=int(input("enter the keys"))
    v=int(input("enter the values"))
    d.update({k:v})
s=0
for i in d.keys():
    s+=i
print(s)
4.....#to find sum and average of marks of student
d={}
s=0
avg=0
x=int(input("enter the element in outer dictionary"))
y=int(input("enter the element in inner dictionary"))
for i in range(x):
    r=int(input("enter roll no."))
    d[r]={}
    for j in range(y):
        r1=input("enter subject names")
        r2=int(input("enter marks of subject"))
        d[r].update({r1:r2})
print(d)
for i in d.keys():
    for j in d[i].keys():
        s=s+d[i][j]
        avg=s/y
print(s)
print(avg)
5........#to print sorted dictionary
dict={}
x=int(input("enter the number of elements"))
for i in range(x):
    k=int(input("enter the keys"))
    v=int(input("enter the values"))
    dict.update({k:v})
print(sorted(dict))
#6........ to print salary of a employee if salary<25000 then add 10000 in salary
d={}
x=int(input("enter outer dictionary"))
y=int(input("enter inner dictionary"))
for i in range(x):
    k=int(input("employee"))
    d[k]={}
    for j in range(y):
        k1=input("enter name")
        v=int(input("enter salary"))
        if v<25000:
            v=v+10000
    d[k].update({k1:v})
print(d)
#7..... to merge two dictionary in one  
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)
#8...... to convert two list into a dictionary 
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)
#9....check if value exists in dictionary 
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')
#10....to change value of a key in a nested dictionary
dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
dict['emp3']['salary'] = 8500
print(dict)



#questions on list


#1.......reverse a list 
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#2......Replace list’s item with new value if found
list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200
print(list1)
#3....extend nested list by adding sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)
#4.......Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)
#5......remove empty string from list of string
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)
#6....... Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)
#7......Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)
#8......turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)
#9.......Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
#10...... Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)


#questions on string


#1..... to print largest word in python
str=input("Enter any String :")
L = str.split()
max=0
b=""
for i in L:
     if len(i) > max:
           b=i
           max=len(i)
print("Longest word is ",b)
#2.....to accept a string and display it in upper case.
str=input("Enter any String :")
print(str.upper( ))
#3.....to display the unique words from the string.
str=input("Enter any String :")
L=str.split( )
L1=[ ]
for i in L:
     if i not in L1:
         L1.append(i)
str=""
for i in L1:
     str=str+" "+i
print("String with unique words are :",str)
#4..... to accept a string and display the ascii value of each character.
str=input("Enter any String :")
for i in str:
     print("ASCII value of ",i,"is",ord(i))
#5..... to accept a string and replace all spaces by ‘#’ symbol.
str=input("Enter any String :")
str1=""
for i in str:
      if i.isspace():
          str1=str1+'#'
      else:
          str1=str1+i
print("Output String is :",str1)

#6......to accept two strings from the user and display the common words.
tr1=input("Enter first String :")
str2=input("Enter second String :")
L1=str1.split()
L2=str2.split()
for i in L1:
     if i in L2:
         print(i)

#7......to accept a string and count the frequency of each vowel.
str1=input("Enter String :")
print("frequency of vowel 'a' is :",str1.count('a'))
print("frequency of vowel 'e' is :",str1.count('e'))
print("frequency of vowel 'i' is :",str1.count('i'))
print("frequency of vowel 'o' is :",str1.count('o'))
print("frequency of vowel 'u' is :",str1.count('u'))
#8.....to display the smallest word from the string
str=input("Enter any String :")
L = str.split()
min=50
b=""
for i in L:
     if len(i) < min:
           b=i
           min=len(i)
print("Smallest word is : ",b)
#9....to accept a string and display the string in Title case
str=input("Enter any String :")
print(str.title())
#10......to accept a string and display the string with changed case
str=input("Enter any String :")
print(str.swapcase())
#questions on function
#1......to create a function in python
# def demo(name, age):
    print(name, age)
demo("Ben", 25)
#2......Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)
func1(20, 40, 60)
func1(80, 100)
#3......Return multiple values from a function
def calculation(a, b):
    return a + b, a - b
add, sub = calculation(40, 10)
print(add, sub)
#4....Create a function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")
#5...... Create an inner function to calculate the addition in the following way
def outer_fun(a, b):
    square = a ** 2
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
result = outer_fun(5, 10)
print(result)
#6..... Create a recursive function
def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0
res = addition(10)
print(res)
#7.....Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)
display_student("Emma", 26)
showStudent = display_student
showStudent("Emma", 26)
#8.....Generate a Python list of all the even numbers between 4 to 30
print(list(range(4, 30, 2)))
#9......Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
print(max(x))
#10......Find the Max of three numbers
def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(3, 6, -5)



#....questions on file handling and exception handling



#1... Create a text file “intro.txt” in python and ask the user to write a single line of text by user input.
def program1():
    f = open("intro.txt","w")
    text=input("Enter the text:")
    f.write(text)
    f.close()
#2....Create a text file “MyFile.txt” in python and ask the user to 
# write separate 3 lines with three input statements from the user.
def program2():
    f = open("MyFile.txt","w")
    line1=input("Enter the text:")
    line2=input("Enter the text:")
    line3=input("Enter the text:")
    new_line="\n"
    f.write(line1)
    f.write(new_line)
    f.write(line2)
    f.write(new_line)
    f.write(line3)
    f.write(new_line)
    f.close()
#3...program to read the contents of both the files created in the above programs and merge
#  the contents into “merge.txt”. Avoid using the close() function to close the files.
def program3():
    with open("MyFile.txt","r") as f1:
       data=f1.read()
    with open("intro.txt","r") as f2:
        data1=f2.read()
    with open("merge.txt","w") as f3:
        f3.write(data)
        f3.write(data1)
#4..... Count the total number of upper case, lower case, and digits used in the text file “merge.txt”.
def program4():
    with open("merge.txt","r") as f1:
       data=f1.read()
    cnt_ucase =0
    cnt_lcase=0
    cnt_digits=0
    for ch in data:
        if ch.islower():
            cnt_lcase+=1
        if ch.isupper():
            cnt_ucase+=1
        if ch.isdigit():
            cnt_digits+=1
    print("Total Number of Upper Case letters are:",cnt_ucase)
    print("Total Number of Lower Case letters are:",cnt_lcase)
    print("Total Number of  digits are:",cnt_digits)
#5.....Write a program to count a total number of lines and count the total number
#  of lines starting with ‘A’, ‘B’, and ‘C’. (Consider the merge.txt file)
def program5():
    with open("merge.txt","r") as f1:
       data=f1.readlines()
    cnt_lines=0
    cnt_A=0
    cnt_B=0
    cnt_C=0
    for lines in data:
        cnt_lines+=1
        if lines[0]=='A':
            cnt_A+=1
        if lines[0]=='B':
            cnt_B+=1
        if lines[0]=='C':
            cnt_C+=1
    print("Total Number of lines are:",cnt_lines)
    print("Total Number of lines strating with A are:",cnt_A)
    print("Total Number of lines strating with B are:",cnt_B)
    print("Total Number of lines strating with C are:",cnt_C)
#6..... Find the total occurrences of a specific word from a text file:
def program6():
    cnt = 0
    word_search = input("Enter the words to search:")
    with open("merge.txt","r") as f1:
        for data in f1:
            words = data.split()
            for word in words:
                if (word == word_search):
                    cnt+=1
    print(word_search, "found ", cnt, " times from the file")
#7...Read first n no. letters from a text file, read the first line, 
# read a specific line from a text file.
def program7():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       line1=f1.readline()
       print("The first line of file:",line1)
       nchar=f1.read(n)
       print("First n no. of characters:", nchar)
       nline=f1.readlines()
       print("Line n:",nline[n])
#8....Replace all spaces from text with – (dash)
def program8():
    cnt = 0
    n = int(input("Enter no. characters to read:"))
    with open("merge.txt","r") as f1:
       data = f1.read()
       data=data.replace(' ','-')
    with open("merge.txt","w") as f1:
        f1.write(data)
#9...Write a program to know the cursor position and print the
#  text according to below-given specifications:
def program9():
    f = open("merge.txt","r")
    print(f.tell())
    f.seek(4,0)
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print(f.seek(7,0))
    print(f.read(10))
#10... Append the contents in entered by the user in the text file:
def program10():
    text = input("Enter text to append in the file:")
    with open("merge.txt","a") as f1:
        f1.write(text)