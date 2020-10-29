import math
 
from functools import partial
from functools import reduce 


height_weight_age = [70, # inches
                    170,# pounds
                    40 ] # years

grades = [95, # exam1
          80, # exam2
          75, # exam3
          62 ] # exam4

u = [1,0,0]
v = [0,1,0]
w = [0,0,1]

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]

print(vector_add(v,w))

def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]
print(vector_subtract(v,w))


def vector_sum(vectors):
    result = vectors[0] # start with the first vector
    for vector in vectors[1:]: 
        result = vector_add(result, vector)
    return result
vectors = (u,v,w)
print(vector_sum(vectors))

def vector_sum(vectors):
    return reduce(vector_add, vectors)
print(vector_sum(vectors))

vector_sum = partial(reduce, vector_add(v,w))
print(vector_sum)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]
c=99.9
print(scalar_multiply(c,v))


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))
#print(vector_mean(vectors))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
print(dot(v,w))