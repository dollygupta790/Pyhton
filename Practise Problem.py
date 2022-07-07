#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input("Enter number: "))
if(a%2)==0:
    print("number is even ")
else:
    print("number is odd" )


# In[ ]:


a=float(input("enter the number : "))
if a>0:
    print("it is positive")
elif a==0:
    print("it is zero")
else:
    print("it is negative")
    


# In[ ]:


b=int(input("enter the number: "))
a=1
if b<0:
    print("it is negative")
elif b==0:
    print("the factorial 0 of 1 ")
else:
    for i in range(1,b+1):
        a=a*i
    print("the factorial of ",b,"is",a)    


# In[ ]:


n=int(input("Enter the number: "))
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("Reverse number is:",rev)    


# In[ ]:


n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)


# In[4]:


n=int(input("enter the number: "))
a=0
b=1
if n<0:
    print("incorrect input")
elif n==0:
    print(a)
elif n==1:
    print(a)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    print(b)


# In[ ]:


n=int(input("enter the number: "))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print("the number is paridrome")
else:
    print("the number is not paridrome")


# In[3]:


n=int(input("Enter number:"))
a = 0
b = 1
if n < 0: 
    print("Incorrect input") 
elif n == 0: 
    print(a)
elif n == 1: 
    print(a) 
else: 
    for i in range(2,n): 
        c = a + b 
        a = b 
        b = c 
    print(b) 


# In[9]:


for n in range(11):
    for i in range(n):
        print(n,end=" ")
    print("\n")   
    


# In[10]:


def add(x):
    return x+10


# In[11]:


add(55)


# In[14]:


def even_odd(x):
    if (x%2)==0:
        print(x,"is even")
    else:
        print(x,"is odd")
even_odd(10)        


# In[15]:


a=lambda x:x*x*x
print(a(3))


# In[17]:


li=[5,12,23,45]
final_list=list(filter(lambda x:(x%2 ==0),li))
print(final_list)


# In[21]:


li=[5,12,23,45]
final_list=list(map(lambda x:x*2,li))
print(final_list)


# In[20]:


from functools import reduce
li=[5,8,10,20,100]
sum=reduce((lambda x,y:x+y),li)
print(sum)


# In[8]:


class Phone:
    def set_color(self,color):
        self.color=color
        
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print("Making phone call")
    def play_game(self):
        print("Playing games")


# In[9]:


p1=Phone()


# In[11]:


p1.set_color('pink')


# In[12]:


p1.set_cost(500)


# In[13]:


p1.show_color()


# In[15]:


p1.show_cost()


# In[16]:


p1.play_game()


# In[17]:


p1.make_call()


# In[18]:


class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_details(self):
        print("The name of the employe is ",self.name )
        print("The age of the employee is ",self.age)
        print("The salary of the employee is ",self.salary)
        print("The gender of the employee is ",self.gender)


# In[19]:


e1=Employee('Julia',25,1120000,'Female')


# In[20]:


e1.show_details()


# In[21]:


class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_details(self):
        print("I am a vehicle")
        print("The mileage is ",self.mileage)
        print("The cost is ",self.cost)
        


# In[22]:


v1=Vehicle(300,10000)


# In[24]:


v1.show_details()


# In[25]:


class Car(Vehicle):
    def show_car(self):
        print("I am a car")


# In[26]:


c1=Car(200,2000)


# In[27]:


c1.show_details()


# In[28]:


c1.show_car()


# In[34]:


class Car(Vehicle):
    def __init__(self,mileage,cost,tyres,hp):
        super().__init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("I am a car")
        print("Number of the tyres are ",self.tyres)
        print("value of horese poe=wer is",self.hp)


# In[35]:


c1=Car(20,1000,5000,3000)


# In[36]:


c1.show_details()


# In[37]:


c1.show_car_details()


# In[63]:


class Parent1:
    def assign_str1(self,str1):
        self.str1=str1
    def show_str1(self):
        print(self.str1)


# In[64]:


class Parent2:
    def assign_str2(self,str2):
        self.str2=str2
    def show_str2(self):
        print(self.str2)


# In[79]:


class Child(Parent1,Parent2):
    def assign_str3(self,str3):
        self.str3=str3
    def show_str3(self):
        print(self.str3)


# In[81]:


c1=Child()


# In[82]:


c1.assign_str1("Sparta")
c1.assign_str2("This is sparataaaa!!!")
c1.assign_str3("Hello world")


# In[83]:


c1.show_str1()


# In[84]:


c1.show_str2()


# In[85]:


c1.show_str3()


# In[86]:


class Parent():
    def assign_name(self,name):
        self.name=name
    def show_name(self):
        return self.name


# In[87]:


class Child(Parent):
    def assign_age(self,age):
        self.age=age
    def show_age(self):
        return self.age


# In[88]:


class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        return self.gender


# In[89]:


g1=GrandChild()


# In[90]:


g1.assign_name("Naman")
g1.assign_age(16)
g1.assign_gender("Male")


# In[91]:


g1.show_name()


# In[92]:


g1.show_age()


# In[93]:


g1.show_gender()


# In[94]:


a1=10
print(type(a1))


# In[95]:


a1=9
b1=10
a1!=b1


# In[ ]:




