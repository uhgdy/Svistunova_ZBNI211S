import json
#1
def fact(x):
    if (x <= 1):
        return 1
    else:
        return (x * fact(x-1))

#2
def filter_even(li):
    return list(filter(lambda x : x % 2 == 0, li))

#3
def square(li):
    return list(map(lambda x : x**2, li))

#4
def bin_search(li, element):
    l = 0
    r = len(li) - 1
    k = -1
    while(l <= r):
        m = (l+r)//2
        if(li[m]<element):
            l = m + 1
        elif(li[m]>element):
            r = m - 1
        else:
            k = m
            break
    return k

#5
def is_palindrome(string):
    s = ''.join(filter(str.isalpha, string)).lower()
    i = 0
    j = len(s)-1
    pal = "YES"
    while (i<j) and pal:
        if(s[i]!=s[j]):
            pal = "NO"
        i += 1
        j -= 1
    return pal

#6
def calculate(path2file):
    string=""
    with open(path2file) as file:
        array = [row.strip() for row in file]
    for s in array:
        arr=s.split("    ")
        x=arr[1]+arr[0]+arr[2]
        string = string + str(eval(x)) + ","
    string = string[:-1]
    return string

#7
def substring_slice(path2file_1, path2file_2):
    string=""
    with open(path2file_1) as file:
        array_1 = [row.strip() for row in file]
    with open(path2file_2) as file:
        array_2 = [row.strip() for row in file]
    for i in range(len(array_1)):
        s = array_2[i].split(" ")
        st = array_1[i]
        string = string + st[int(s[0]):int(s[1])]+" "
    string = string[:-1]
    return string

#8
def decode_ch(sting_of_elements):
    periodic_table = json.load(open('periodic_table.json'))
    s=""
    t=""
    for i in range(len(sting_of_elements)-1):
      if(sting_of_elements[i+1].islower()!=True and sting_of_elements[i].islower()!=True):
          t=sting_of_elements[i]
          s=s+periodic_table[t]
          t=""
      elif(sting_of_elements[i+1].islower()==True and sting_of_elements[i].islower()!=True):
          t=sting_of_elements[i]+sting_of_elements[i+1]
          s=s+periodic_table[t]
          t=""
    if(sting_of_elements[-1].islower()!=True):
      s=s+periodic_table[sting_of_elements[-1]]
    return s

#9
class Student:

    def __init__(self, name, surname, grades = [3,5,5]):
        self.name = name
        self.surname = surname
        self.fullname = name + " " + surname
        self.grades = grades

    def greeting():
        return ("Hello, I am Student")
    
    def mean_grade(self):
        return sum(self.grades)/len(self.grades)

    def is_otlichnik(self):
        buf = float(self.mean_grade())
        if (buf >= 4.5):
            return "YES"
        else:
            return "NO"

    def __add__(self, other):
        x = self.name
        y = other.name
        return x + "is friends with " + y

    def __str__(self):
        return self.fullname

#10
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

#buf = input("Password: ")

#try:
#    buf = int(buf)
#    if buf != 12345:
#        raise MyError("invalid password")
#except ValueError:
#    print("Error type of value!")
#except MyError as mr:
#    print(mr)
#else:
#    print(buf)
