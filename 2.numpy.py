# %%
import numpy as np # konvencija da se pise 'as np'
mylist = [1,2,3]
print(type(mylist))
mynplist = np.array(mylist)
print(type(mynplist))

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
print(np.array(my_matrix))
# %%
np.arange(0,11,2)
# array([ 0,  2,  4,  6,  8, 10])
# %%
np.zeros(5)
# array([0., 0., 0., 0., 0.])
# %%
np.zeros((2,2)) # (row,column)
# array([[0., 0.],
#        [0., 0.]])
# %%
np.ones(5)
# array([1., 1., 1., 1., 1.])
# %%
# sta ona 14. 7:00