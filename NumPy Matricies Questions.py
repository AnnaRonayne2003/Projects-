#!/usr/bin/env python
# coding: utf-8

# ### <div align='center'> NumPy Matricies</div>
# 

# **Problem 1: Create the following numpy array**
# ```
# array([[0., 1., 2., 3., 4.],
#        [0., 1., 2., 3., 4.],
#        [0., 1., 2., 3., 4.],
#        [0., 1., 2., 3., 4.],
#        [0., 1., 2., 3., 4.]])
# ```
# 

# In[10]:


import numpy as np
np.zeros((5,5))+np.arange(5)


# **Problem 2: Construct a matrix C with `C[i,j] = 1/(x[i]+y[j])`.**
# 

# In[11]:


x = np.linspace(1,2,6)
y = np.linspace(1,2,6)
# Write your code below
1/(x.reshape(-1,1)+y)


# **Problem 3: Each row of X and Y is the coordinates of a 2D-point. Construct the matrix D, such that `D[i,j]` is the distance between `X[i]` and `Y[j]`.**
# 

# In[12]:


X = np.random.randn(5,2)
Y = np.random.randn(4,2)
# Write you code below
np.sqrt(np.sum((np.expand_dims(X,1)-Y)**2,2))


# **Problem 4. Generate a random matrix of 5x5, with roughly half of the entries 0, and the remaining entries are integers chosen from 1,2 and 3.**
# 

# In[13]:


# Write your code here
np.random.randint(1,4,(5,5))*(np.random.rand(5,5)<0.5)


# **Problem 5. Generate a random 5x5 matrix whose entries above the main diagonal are positive, while the entries below the main diagonal are all negative.**  

# In[14]:


# Write your code here
#np.set_printoptions(precision=2)
np.random.rand(5,5)*(2*np.triu(np.ones((5,5)))-np.ones((5,5)))


# **Problem 6. Muptiple each row of X whose index is given in I by 2.**

# In[15]:


A = np.random.rand(4,4)
print(A)
I = [0,1,1,2]
# Write your code below
A[I] *=2
A


# **Problem 7. Sort X so that the entries of the first column of X are in an increasing order.**
# 

# In[16]:


X = np.random.randn(5,5)
# Write your code below
print(X)
X[np.argsort(X[:,0])]


# **Problem 8. Find the row vector in X that is closest to the first row vector (but not the first row itself).**

# In[17]:


X = np.random.rand(10,2)
print(X)
X[1:][np.argmin(np.sum((X[1:]-X[0:1])**2,1))]


# **Problem 9. Swap the first two rows in X.**

# In[18]:


X = np.random.rand(5,5)
# Write your code here
print(X)
X[:2]=X[[1,0]]
X


# **Problem 10. Extract all the 3x3 blocks from X.**
# 

# In[4]:


###### 
import numpy as np
X = np.random.rand(5,5)
print(X)
# Write your code below
np.array([X[i:i+3,j:j+3] for i in range(2) for j in range(2)])


# **Problem 11. Generate the following array:**
# ```
# array([[ 0,  1,  2,  3],
#        [ 1,  2,  3,  4],
#        [ 2,  3,  4,  5],
#        [ 3,  4,  5,  6],
#        [ 4,  5,  6,  7],
#        [ 5,  6,  7,  8],
#        [ 6,  7,  8,  9],
#        [ 7,  8,  9, 10],
#        [ 8,  9, 10, 11],
#        [ 9, 10, 11, 12]])
# ```

# In[20]:


# Write your code here
np.fromfunction(lambda i,j: i+j, (10,4))


# **Problem 12. Create a random 5x5 symmetric matrix whose entries are integers between 0 and 10.**

# In[21]:


# Write your code below
A=np.random.randint(0,11,(5,5))
np.maximum(A,A.T)


# **Problem 13. Find the average values of X in all 3x3 sliding windows.**

# In[22]:


X=np.arange(25).reshape(5,5)
# Write your code below
np.array([[X[i:i+3,j:j+3].mean() for j in range(5-3)] for i in range(5-3)])


# **Problem 14. Delete the repeated rows from X.**

# In[23]:


np.random.seed(0)
X = np.random.randint(0,3,(10,2))
print(X)
# Write your code below
np.unique(X, axis=0)


# **Problem 15. Delete the repeated rows from X without changing the oder in which each row appears.**

# In[24]:


np.random.seed(0)
X = np.random.randint(0,3,(10,2))
# Write your code below
np.array([list(u) for u in dict.fromkeys([tuple(x) for x in X]).keys()])


# **Problem 16. Create a 6x6 matrix with values 1,2,3,4,5 just below the diagonal.**

# In[25]:


# Write your code below
np.diag(range(1,6),-1)


# **Problem 17. Each row of X is the coordinates of a point in 3D-space. Find the distances between these points and the center of the these points.**
# 

# In[26]:


# Write your code below
X = np.random.randn(5,3)
np.sqrt(np.sum((X-X.mean(0))**2,1))


# **Problem 18. Replace all entries of X that are below the average by $-1$.**

# In[27]:


X = np.random.randn(5,5)
print(X)
X[X<X.mean()]= -1
X


# **Problem 19. Replace the largest 5 entries of X by the corresponding values in V.**

# In[28]:


X = np.random.rand(10)
print(X)
V=np.array([1,2,3,4,5])
# Write your code below
I = np.argpartition(-X,5)[:5]
X[I[np.argsort(-X[I])]] = V
X


# **Problem 20. Reverse the order of the last row of X, keeping the other rows unchanged.** 

# In[29]:


X = np.arange(25).reshape(5,5)
print(X)
# Write your code below
X[-1] = X[-1][::-1]
X


# In[ ]:





# In[ ]:




