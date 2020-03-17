##############################################################################################
# 1. Importing original data set of Stack Overflow 2018 Developer Survey

original_data <- read.csv("Stack_Overflow_2018_Developer_Public_Survey.csv")

# 1.1. Randomly choosing 1000 rows from the original data (*default seed)

random_sample <- original_data[sample(1:nrow(original_data), 1000),]

##############################################################################################
# 2. Performing basic descriptive statistics on the random sample

sink('random_sample_summary.txt')
summary(random_sample)
sink()

##############################################################################################
# 3. Data visualization of all the yearly salaries in the random sample

hist(random_sample$Yearly.Salary.in.USD, main = "Salary Distribution Amongst Stock Overflow Developer Survey Respondents", ylab = "Number of Respondents", xlab = "Yearly Salary ($)")

##############################################################################################
# 4. Analysis of the shared variability between "Open Source" and "Yearly Salary in USD" 

developer_opinion <- plot(random_sample$Open.Source, random_sample$Yearly.Salary.in.USD, main = "Stock Overflow Developer Survey: Respondent Yearly Salary ($) vs Stance on Open Source Software", ylab = "Yearly Salary ($)", xlab = "Stance on open source software", col=7:6)

developer_opinion_no <- developer_opinion$stats[,1]
developer_opinion_yes <- developer_opinion$stats[,2]

sink('final_analysis.txt')
print('    Min. Lower Qu. Median Upper Qu. Max')
print(developer_opinion_no)
print(developer_opinion_yes)
sink()
