#!/usr/bin/env python
# coding: utf-8

# ### <div align='center'> Graphing with MatplotLib</div>
# 
# 

# **Problem 1: Plot the graph of the function $y=xe^{-x}$ defined on the interval $[0,3]$, using blue solid line. The tangent line at the very top of the curve has equation $y=e^{-1}$. Draw the tangent line use a red dashed line. Put a black dot at the tangent point point $(1,e^{-1})$. Set $y$ axis limits from 0 to 0.5. Use the graph title "The graph of $y=xe^{-x}$".** 

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,3,20)
y = x*np.exp(-x)
z = np.exp(-x)
plt.axis([0,3,0,0.5])
plt.plot(x,y,'b')
plt.plot(x,z,'r--')
plt.scatter(1,np.exp(-1), color='black')
plt.title("The graph of $y=xe^{-x}$")


# **Problem 2: Draw an equilateral triangles of side length 1, with one side parallel to the $x$-axis. Make sure the equilaterial triangle indeed looks like equilaterial.** 
# 

# In[80]:


x = [2,4,3,2]
y = [1,1,3,1]
plt.plot(x,y)


# **Problem 3: Draw a circle of radius 1, and point a dot at the center of the circle. Label the center by  putting a letter "O" next to the dot. Make sure the circle is circular.**
# 

# In[25]:


b = np.linspace(0, 2*np.pi, 30)
x=np.cos(b)
y = np.sin(b)
plt.figure(figsize=(4,4), dpi=100)
plt.plot(x,y,'b+-')
plt.plot(0,0, 'ok')
plt.text(0.05,0, 'o', fontname='wave', fontsize=20) 
plt.show()


# In[197]:


b = np.linspace(0, 2*np.pi, 30)
x=np.cos(b)
y = np.sin(b)
plt.figure(figsize=(4,4), dpi=100)
plt.plot(x,y,'b+-')
plt.plot((x+2),(y), 'ok')
plt.axis('scaled')
plt.show()


# **Problem 4. Plot the graphs of the functions $y=\sin x$ and $y=\cos x$ over the interval $[0,7]$. Put a black dot at each of their intersections. Label the two curve by their function names $\sin x$ and $\cos x$**
# 

# In[84]:


x = np.linspace(0,7,50)
y= np.sin(x)
z= np.cos(x)
plt.plot(x,y,'bo-',label='$sinx$')
plt.plot(x,z,'r--',label='$cosx$')
plt.legend()
intersect = np.argwhere(np.diff(np.sign(y - z))).flatten()
plt.plot(x[intersect], y[intersect], 'ko')
#Find out when sin(x)=cos(x)#


# **Problem 5. Plot a figure with two subplots of the same size. The one on top contains two identical circles putting side by side and are tangent to each other. The one on the bottom contains two identical equilaterial triangles putting side by side with one common tangent vertex. Give each subplot a meaningful title using fontname abadi.**  

# In[223]:


b = np.linspace(0, 2*np.pi, 30)
x=np.cos(b)
y = np.sin(b)
plt.figure(figsize=(4,4), dpi=100)
plt.plot(x,y,'k')
plt.plot((x+2),(y), 'k')
plt.axis('scaled')
plt.title('two circles',fontdict={'fontname': 'abadi', 'fontsize': 10})
plt.show()
x = [-1,3,2,1,0,-1]
y = [-1,-1,1,-1,1,-1]
plt.xticks([-1,0,1,2,3])
plt.yticks([-1,-0.5,0,0.5,1])
plt.title('two trianges',fontdict={'fontname': 'abadi', 'fontsize': 10})
plt.plot(x,y)
#So the font doesn't- it says the font is not in the font family


# In[ ]:





# ### **Problem 6. Plot a figure with 3x3 subplots, each containing the graph of the squiggle_xy(a, b, c, d) defined below with parameters (a,b,c,d) of your choice. Label each curve by its parameter tuple. Keep the boxes of each subplot, but do not show the tick marks. Give a meaningful title for the whole figure.**   

# In[225]:


import numpy as np
import matplotlib.pyplot as plt

def squiggle_xy(a, b, c, d, i=np.arange(0.0, 2*np.pi, 0.01)):
    return np.sin(i*a)*np.cos(i*b), np.sin(i*c)*np.cos(i*d)
plt.plot(*squiggle_xy(2,3,2.4,5.8)) #Changes the parameters (2,3,2.4,5.8) to see how the curve changes
plt.title('$sinx$ and $cosx$ squiggle art')
plt.show()
for i in range(1,10):
    plt.subplot(3,3,i)
    plt.plot(*squiggle_xy(2,3,2.4,5.8), 'r-')
    plt.xticks([])
    plt.yticks([])
    plt.title('tuple {}'.format(str(i)),fontsize=7)


# #### 
