f1 <- function (x=1,n=3) {
    sum = 0
    for (i in 1:n) {
        sum += i*x**i
    }
    return sum
}

f2 <- function (x) {
    sum = 0
    if (length(x)==0) {
        return NA
    }
    for (i in x) {
        if (x % 2 == 0 or x % 3 == 0) {
            sum += i
        }
    }
    return sum
}

f3 <- function (x,n) {
    sort(x,decreasing=TRUE)
    return x[n]
}

f4 <- function (x) {
    sort(x,decreasing=TRUE)
    if (x[length(x)] < 0) {
        return NA
    }
    groups = prod(x[1]:sum(x))
    for (i in 2:length(x)) {
        groups /= prod(1:x[i])
    }
    return groups
}