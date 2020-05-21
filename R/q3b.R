# @author: WANG Meng
# R Script for <COMP1433 A2Q3 Part B>

relation <- function(T) {
    N = 100 - 0.02 * T
}
plot(
    relation,
    main="Q3Task2: Relationship of gambling times and expected fortune",
    xlab="T: Gamble Times",
    ylab="N: Expected Fortune $N",
    xlim=c(0, 120000)
)