# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas
pandas.__version__


# %%
type(1)


# %%
type(1.0)


# %%
5 ** 2 # exponent


# %%
5 % 2 # ostatak modulo


# %%
'eej'


# %%
print('ejj')


# %%
print("My name is {}, my number is {}".format("Jose", 1))
print("My name is {x}, my number is {y}".format(x="Jose", y=1))


# %%
myList = ['a', 'b', 'c']
myList.append('d')
print(myList[2])
print(myList[-1])


# %%
myTouple = (1,2,3)
myTouple2 = 1,2,3
print(myTouple)
print(myTouple2)


# %%
for x in range(2,5): # 2 - koliko pocetnih da preskoci, 5 - koliko komada, krece od 0
    print(x)


# %%
def moja_funkcija():
    '''
    dokumentacija moje funkcije
    '''
    print('moja func')
moja_funkcija()
# %%
# kasnije cemo korisitit
lambda var: var*2
# %%
