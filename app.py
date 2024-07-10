from numpy import array
from random import *

t = array([int]*15)

for i in range(15):
    t[i] = randint(0,1500)

st.table(t)
