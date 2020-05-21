# @author: WANG Meng
# R Script for <COMP1433 A2Q4>

# (2)
## Read data from txt
age <- as.numeric(readLines("./q4_data/age.txt"))
height <- as.numeric(readLines("./q4_data/height.txt"))

## get linear model
reg <- lm(height ~ age)

## plot and regression line to graph
library(ggplot2)
graph <- ggplot(mapping = aes(age, height)) +
    geom_point(colour = 'blue') +
    geom_abline(
        slope = reg$coefficients[2],
        intercept = reg$coefficients[1],
        colour = 'red'
    ) +
    labs(
        x = "Age (year)",
        y = "Height (meter)",
        title = "Age vs. Height"
    )
ggsave(graph, filename = "Age vs Height.jpg", path = "./q4_data")

# (3)
## make prediction of 3.5 and 8
pred1 <- predict(reg, data.frame(age = 3.5))
pred2 <- predict(reg, data.frame(age = 8))