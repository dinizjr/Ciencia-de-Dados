
# coding: utf-8

# # Biblioteca NumPy
# é comum ser criado alias para o import.

# In[13]:


import numpy as np


# ## Criando arrays a partir de listas
# 

# In[4]:


lista = [1,2,3,4]


# In[7]:


lista


# In[14]:


arr = np.array(lista)


# In[15]:


arr


# In[16]:


type(arr)


# ## Criando Matrizes a partir de listas

# In[17]:


matriz_lista = [[1,2,3], [4,5,6], [7,8,9]]


# In[18]:


matriz_lista


# In[19]:


arr = np.array(matriz_lista)


# In[20]:


arr


# # Principais métodos da NumPy
# ## Método arange()
# 
# semelhante ao range do Python, porém devolve um array com os elementos que estão dentro do intervalo selecionado.
# 
# 

# In[23]:


np.arange(0, 10)


# In[25]:


np.arange(0,10,2)


# In[26]:


np.arange(0,-101,-10)


# ## Métodos zeros()
# Retorna uma matriz com a dimensão informada preenchida com zeros.

# In[27]:


np.zeros(3)


# In[28]:


np.zeros(4,dtype=int)


# In[30]:


np.zeros((3,3), dtype=int)


# In[32]:


np.zeros((3,3,2), dtype=int)


# In[34]:


np.ones(3)


# In[35]:


np.ones(3, dtype=int)


# In[36]:


np.ones((3,4))


# ## Método Linspace()
# Cria uma sequência de números igualmente espaçados entre os limites dados

# In[37]:


np.linspace(0,50,5, dtype=int) 


# In[38]:


np.linspace(0,100,10, dtype=int)


# # Sub-biblioteca random
# 
# ## Método rand()
# Retorna uma matriz com a dimensão informada, preenchida com números aleatórios entre 0 e 1 seguindo uma distribuição uniforme(a probabilidade e o mesmo para todos números)

# In[39]:


np.random.rand(5)


# In[41]:


np.random.rand(3,4)


# É possível incluir operações na criação de números aleatórios

# In[43]:


np.random.rand(5) ** 2


# In[47]:


np.random.rand(2,2) * 10


# ## Método randn()
# Retorna uma matriz com a dimensão informada, preenchida com números aleatórios seguindo uma distribuição normal(qualquer número)

# In[48]:


np.random.randn(5)


# In[50]:


np.random.randn(3,4) * 10


# ## Método randint()
# Retorna um array com números aleatórios inteiros entre o intervalo informado ou uma matriz tridimensional preenchida com números aleatórios inteiros entre o intervalo informado.

# In[51]:


np.random.randint(1,10)


# In[52]:


np.random.randint(1,10,15)


# In[53]:


np.random.randint(1,1000,5) * 10


# # Métodos a etributos do objeto NumPy Array
# ## Método reshape
# Reorganiza um array em uma dimensão diferente da original

# In[54]:


arr = np.random.rand(10)


# In[55]:


arr


# In[56]:


arr.reshape(2,5)


# In[57]:


arr.shape


# In[61]:


arr.reshape(5,2).reshape(2,5)


# ### fez o reshape e desfez

# In[62]:


arr_int = np.random.randint(0,100,50)


# In[63]:


arr_int


# In[64]:


arr_int.reshape(5,10)


# ## Método max()

# In[69]:


arr_int.max()


# ## Método argmax()
# Retorna o índice

# In[70]:


arr_int.argmax()


# ## Método min()

# In[73]:


arr_int.min()


# ## Método argmin()

# In[74]:


arr_int.argmin()


# ## Atributo shape
# Retorna o formato (dimensões) do array

# In[75]:


arr = np.random.randint(0,100,10)


# In[76]:


arr


# In[77]:


arr.shape


# In[78]:


arr = arr.reshape(2,5)


# In[79]:


arr


# In[80]:


arr.shape

