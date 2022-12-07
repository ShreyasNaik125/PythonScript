import os as s
import ctypes
def readfile(string):
    with open(f"{string}","r") as file:
        content = file.read()
        print(f"{content}")

def writefile(string,const):
    with open(f"{string}","r") as file:
        file.write(f"const")

def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1,n+1):
        c = a+b
        print(c)
        a=b
        b=c

def infinity():
    i = 10
    while i>=1:
        print(i)
        i+=1

def fact(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    print(f)


def add(n,i):
    c = n+i
    print(c)


def sub(n,i):
    c = n-i
    print(c)

def div(n,i):
    c = n/i
    print(c)

def product(n,i):
    c = n*i
    print(c)

def opensite(n):
    s.system(f"start chrome {n}")

def shutdown():
    s.system("shutdown /p")

def changewallpaper(n):
    wallpaper_path = f'{n}'
    ctypes.windll.user32.SystemParametersInfoW(20,0,wallpaper_path,3)