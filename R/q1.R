# @author: WANG Meng
# R Script for <COMP1433 A2Q1>

f1 <- function (x=1,n=3) {
    sum = 0
    for (i in 1:n) {
        sum = sum + i*x**i
    }
    return(sum)
}

f2 <- function (x) {
    sum = 0
    if (length(x)==0) {
        return(NA)
    }
    for (i in x) {
        if (i %% 2== 0 || i %% 3== 0) {
            sum = sum + i
        }
    }
    return(sum)
}

f3 <- function (x,n=1) {
    x = sort(x,decreasing=TRUE)
    return(x[n])
}

f4 <- function (x) {
    x = sort(x)
    if (x[1] < 0) {
        return(NA)
    }
    groups = factorial(sum(x))
    for (i in x) {
        groups = groups/factorial(i)
    }
    return(groups)
}
