"Funções sem retorno de valor (es)"

def exibe_mensagem():
    print("Primeira função em Python")


exibe_mensagem()


def exibe_mensagem_custom(mensagem):  # mensagem: parâmetro formal (é definido na criação da função)
    print(mensagem)


msg = "Mensagem do Prof. Daniel"
exibe_mensagem_custom(msg)

# msg: parâmetro real (é definido na chamada da função)
# passagem de parâmetros: parâmetro real substitui o parâmetro formal


def soma_numeros(num1, num2):
    soma = num1 + num2
    print("Soma=", soma)


x = 5
y = 13
soma_numeros(x, y)

"Funções com retorno de valor (es)"


def soma_numeros_ret(num1, num2):
    soma = num1 + num2
    return (soma)

x = 7
y = 12

print("Soma=", soma_numeros_ret(x, y))

s = soma_numeros_ret(x, y)

# In[18]:


print(s)


# In[12]:


def calcula_soma_media(a, b):
    soma = a + b
    media = (a + b) / 2
    return (soma, media)


# In[13]:


x = 6
y = 12

calcula_soma_media(x, y)

# In[14]:


s, m = calcula_soma_media(x, y)

# In[15]:


print(s)

# In[16]:


print(m)


# In[20]:


def par_impar(n):
    if (n % 2 == 0):
        return (1)
    else:
        return (0)


# In[23]:


t = 12

res = par_impar(t)

if (res == 1):
    print("O número é par")
else:
    print("O número é ímpar")


# In[24]:


def verifica_maior(x, y):
    if (x > y):
        print("Maior=", x)
    else:
        print("Maior=", y)


# In[25]:


num1 = 5
num2 = 8

verifica_maior(num1, num2)


# In[26]:


def verifica_maior_ret(x, y):
    if (x > y):
        return (x)
    else:
        return (y)


# In[28]:


num1 = 5
num2 = 8

print("Maior=", verifica_maior_ret(num1, num2))

maior = verifica_maior_ret(num1, num2)

# In[29]:


dobro = maior * 2
print(dobro)


# In[30]:


def valida_CPF(cpf):
    sdfkjklf
    sdlfkjkdf
    sdlfklkjlsf
    sdflfjsdfl

    if (digitos_verif_cpf == digitos_calculados):
        return (1)
    else:
        return (0)


# In[ ]:


cpf = input("Digite seu cpf")
if (valida_CPF(cpf) == 1):
    print("CPF válido")
else:
    print("CPF inválido")
