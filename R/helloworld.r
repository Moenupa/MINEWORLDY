# File:
# Project:

## Hello World =======================================================
print("Hello World!")

## Data Types ========================================================
a = 2 + 2
x = c(1,2,3,4)                  # integer and 1d vector

y = 0:10
z = seq(10)
b = seq(30,0,by=-3)             # ways to do range()

## Remove Data =======================================================
rm(a,x)
rm(list = ls())                 # remove all data

## Types test ========================================================
c = "Hello World!"
x = c(1,2,3,4)
y = 0:10

typeof(y)
is.vector(x)

## Vector ============================================================
v1 = c(T,T,T,T)
v2 = c(1,1,1,1)
v3 = c("c", "a", "bb")          # vector, accept all-same-type data
is.vector(v1)

## Matrix ============================================================
m1 = matrix(c(T, T, F, F, T, F), nrow = 2)
m2 = matrix(c(
    "a", "b",
    "c", "d"),
    nrow = 2,
    byrow = T
)                               # create matrix (default by columns)

## Array =============================================================
a1 = array(c(1:24), c(4,3,2))   # 3D array, accept all-same-type data

vNum = c(1,2,3)
vChar = c("a", "b", "c")
vLog = c(T, F, T)

## DataFrame =========================================================
df1 = cbind(vNum, vChar, vLog)
df2 = as.data.frame(cbind(vNum, vChar, vLog)) # aware of the diffrence

lst1 = list(vNum, vChar, vLog)
