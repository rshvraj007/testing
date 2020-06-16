#!/usr/bin/env python
# coding: utf-8

# # Z-Distribution

# In[2]:


from scipy import stats as rr
Z0=float(input("Enter the input value for unit distribution: "))
print(f"probability P(Z<=Z0) for input {Z0} is : {rr.norm.cdf(Z0)}")


# In[3]:


A=float(input("Enter the Score value for unit distribution: "))
print(f"value of Z0 for which P(Z<=Z0)={A} is : {rr.norm.ppf(A)}")


# # Chi-square Distribution

# In[4]:


from scipy import stats as rr
X=float(input("Enter the input value for chisquare distribution: "))
dof=int(input("Enter degree of freedom: "))
chi_pro=rr.chi2.cdf(X,dof)
print(f"Chisquare probability for {X} is: {chi_pro}")


# In[5]:


A=float(input("Enter the Score value for chisquare distribution: "))
dof=int(input("Enter degree of freedom: "))
X=rr.chi2.ppf(A,dof) 
print(f"Value of y0 for which chisquare probability is equal to {A}: {Z0}")


# # T-Distribution

# In[9]:


T=float(input("Enter input value for T-distribution: "))
dof=int(input("Enter degree of freedom: "))
t_prob=rr.t.cdf(T,dof)
print(f"probability of T<=T0 is: {t_prob}")


# In[11]:


from scipy import stats as rr
A=float(input("Enter T-score for T-distribution: "))
dof=int(input("Enter degree of freedom: "))
T=rr.t.ppf(A,dof)
print(f"Value of T0 for which P(T<=T0)={A} is: {T}")


# # F-Distribution

# In[13]:


F=float(input("Enter value for F-distribution: "))
dof1=int(input("Enter degree of freedom v1: "))
dof2=int(input("Enter degree of freedom v2: "))
f_prob=rr.f.cdf(F,dof1,dof2)
print(f"probability of F<=F0 is: {f_prob}")


# In[15]:


A=float(input("Enter f-score: "))
dof1=int(input("Enter degree of freedom v1: "))
dof2=int(input("Enter degree of freedom v2: "))
z0=rr.f.cdf(A,dof1,dof2)
print(f"probability of F<=F0 is: {F}")


# In[ ]:




