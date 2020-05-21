# @author: WANG Meng
# R Script for <COMP1433 A2Q3 Part A>

pWin = 0.49
pLose = 0.51

## winTimes + loseTime = T (gamble times)
## winTimes - loseTime <= -100 (running out of money)
## winTimes <= T/2 - 50

gamble <- function(T) {
    return(pbinom(T/2-50, size = T, prob = pWin))
}

for (i in c(100,1000,10000,100000)) {
    print(gamble(i))
}