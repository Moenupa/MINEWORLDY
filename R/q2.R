# @author: WANG Meng
# R Script for <COMP1433 A2Q2>

# (1) import data and put into dataframe
scores <- read.csv("./q2_data/scores.csv",sep = ',',header = TRUE)

# (2) statistics
## mean median min max and standard deviation
cat("The statistics for science scores are:\n",
    "\tmean = ", mean(scores$Science), ";\n",
    "\tstandard deviation = ", sd(scores$Science), ";\n",
    "\tmedian score = ", median(scores$Science), ";\n",
    "\tminimum score = ", min(scores$Science), ";\n",
    "\tmaximum score = ", max(scores$Science), ".\n", sep = ""
)

# (3) normalize
normalize <- function(col) {
    col_mean <- mean(col)
    col_sd <- sd(col)
    for (i in 1:length(col)) {
        col[i] = (col[i]-col_mean)/col_sd
    }
    return(col)
}
scores$Math <- normalize(scores$Math)
scores$Science <- normalize(scores$Science)
scores$English <- normalize(scores$English)

# (4) first name and last name split
scores[["First Name"]] <- sapply(strsplit(as.character(scores$StuName),' '), "[", 1)
scores[["Last Name"]] <- sapply(strsplit(as.character(scores$StuName),' '), "[", 2)

# (5) overall scores
scores$Grade <- scores$Math+scores$Science+scores$English
stuNum <- length(scores$Grade)
sort_grade <- sort(scores$Math+scores$Science+scores$English)
for (i in 1:length(scores$Grade)) {
    if (which(scores$Grade[i]==sort_grade) < stuNum/2) {
        if (which(scores$Grade[i]==sort_grade) < stuNum/4) {
            scores$Grade[i] <- "D"
        } else {
            scores$Grade[i] <- "C"
        }
    } else {
        if (which(scores$Grade[i]==sort_grade) >= stuNum*3/4) {
            scores$Grade[i] <- "A"
        } else {
            scores$Grade[i] <- "B"
        }
    }
}

# (6) write to csv file
write.csv(scores,"./q2_data/newscores.csv",row.names = FALSE)
