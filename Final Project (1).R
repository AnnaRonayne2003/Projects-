
library(dplyr)
library(tidyverse)
sport <- read.csv("C:/Users/annar/Downloads/revenuesport - sportsref_download.xls (1).csv", header=TRUE)

sport$points <- sport$AST*2+sport$PTS
sport_new <- sport[c('RK','NAME','Pos','points','REB','PF','SALARY')]
sport_new$SALARY

sport_new$SALARY <- gsub("\\$|,", "", sport_new$SALARY)

# Convert to integer
sport_new$SALARY <- as.integer(sport_new$SALARY)

sport_new



sport_new <- sport_new %>%
  mutate(Position_Category = case_when(
    Pos %in% c("PG", "SG", "G") ~ "Guard",
    Pos %in% c("SF", "PF", "F") ~ "Forward",
    Pos == "C" ~ "Center",
    TRUE ~ "Other"  
  ))

sport_new <- sport_new %>%
  select(-Pos)

sport_new

# Convert Position_Category to a factor (important for categorical blocking)
sport_new$Position_Category <- as.factor(sport_new$Position_Category)


sport_new$log_salary <- log(sport_new$SALARY)

# Fit the RCBD model including additional metrics
model <- lm(log_salary ~ Position_Category + points + REB + PF, data = sport_new)

# Perform ANOVA
anova_table <- anova(model)

# Display the ANOVA table
print(anova_table)

# Summary of the model (optional)
summary(model)
levels(sport_new$Position_Category)

  
  # Example of plotting with an equation in R
#plot(1:10, 1:10)
#text(5, 5, expression(log(salary)[ij] == mu + tau[i] * Position_Category[i] + beta[1] * Points[j] + beta[2] * REB[j] + beta[3] * PF[j] + epsilon[ij]), pos=4)

#warnings()
  
#pair <- pairs(model)

#print(pair)

#library(emmeans)

#noodles.rcb.means.treatment <- emmeans(model,"Position_Category")
#summary(noodles.rcb.means.treatment)
#pairs(noodles.rcb.means.treatment)

cor(sport_new[, c("log_salary", "points", "REB", "PF")])



ggplot(sport_new, aes(x = points, y = log_salary)) +
  geom_point() +
  geom_smooth(method = "lm", col = "blue") +
  labs( x = "Points per Game", y = "Log Salary")

boxplot(log_salary ~ Position_Category, data = sport_new,
        main = "Boxplot of Salary by Position Category",
        xlab = "Position Category",
        ylab = "Salary",
        col = "darkred",
        border = "black")


library(emmeans)

treatmeans <- emmeans(model, "Position_Category")

pairs(treatmeans)
sport_new <- sport_new %>%
  mutate(
    Guard = ifelse(Position_Category %in% c("Guard"), 1, 0),
    Forward = ifelse(Position_Category %in% c("Forward"), 1, 0)
  )


model2 <- lm(log_salary ~ points + Guard + Forward, data = sport_new)

# Summarize the model to view the results
summary(model2)


plot(model)
plot(model2)


sport_new$Forward

ggplot(sport_new, aes(x = points, y = log_salary, color = Position_Category)) +
  geom_point(size = 3, alpha = 0.8)  +
  labs(x = "Points", y = "Log Salary", title = "Log Salary vs. Points by Position") +
  scale_color_viridis_d() +
  theme_minimal()


