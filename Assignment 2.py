#!/usr/bin/env python
# coding: utf-8

# 
# # Merna Mansour
# # Assignment 2
# #Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[4]:


st = 'Print only the words that start with s in this sentence'


# In[6]:


#Code here
x=st.split(' ')
y=[]
for i in x:
    if i[0]=='s':
        print(i)
        


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[10]:


l3=[]
for i in range(0,10):
    if i%2==0:
        l3.append(i)
l3


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[12]:


#Code Here
l2=[]
l4=[]
for i in range(1,51):
    l2.append(i)
for i in l2:
    if i%3==0:
        l4.append(i)
l4


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[7]:


st = 'Print every word in this sentence that has an even number of letters'


# In[10]:


#Code in this cell
word=st.split(' ')
word
for i in word:
    if len(i)%2==0:
        print('{}, is even'.format(i))


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[16]:


#Code in this cell
for i in range(1,101):
    if (i%3==0) and (i%5==0):
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[22]:


st = 'Create a list of the first letters of every word in this string'


# In[23]:


#Code in this cell
y=st.split(' ')
k=[]
k=[i[0] for i in y]
k
    


# ### Great Job!

# In[ ]:


# Write a Python program to print the numbers 
# of a specified list after removing even numbers from it.
x= int(input())
l=[]
for i in range(0,x,1):
    nums=int(input('please enter the {} number'.format(i+1)))
    l.append(i)
for i in l:
    if i%2==0:
        l.remove(i)
l


# In[ ]:


# Write a Python program to get the difference between 
#the two lists.
# l1 =  [1,2,3]
#[4,6,8]
# Expected output = [3,4,5]
l1=[1,2,3]
l2=[4,6,8]
l3=[]
for i in range(0,3,1):
    x=l2[i]-l1[i]
    l3.append(x)
l3


# In[ ]:


# Print the following pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
s=1
for i in range(0,5+1):
    for s in range(i):
        print(s+1, end=' ')
    print('')


# In[ ]:




