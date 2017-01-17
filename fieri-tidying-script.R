##Fieri-Effect: Creating workable data set that combines yelp review data
## with information on episode air date

#After setting working directory to folder with json data set, load required packages
library(jsonlite)
library(tidyverse)
library(tibble)
library(stringr)

#Begin parsing json file and converting to usable data frame for business dataset
yelp <- stream_in(file("yelp_academic_dataset_business.json"))
yelp_flat <- flatten(yelp)
yelp_tbl <- as_data_frame(yelp_flat)

yelp_tbl %>% mutate(categories = as.character(categories)) %>% 
        select(categories)

yelp_tbl <- yelp_tbl %>% select(-starts_with("hours"), -starts_with("attribute"))

yelp_tbl %>% filter(str_detect(categories, "Restaurant"))

#Repeat process for reviews data to prepare for join
yelp_reviews <- read_csv("yelp_academic_dataset_review.csv")
yelp_reviews <- yelp_reviews %>% select(-text, -votes_cool, - votes_funny, -votes_useful)

#Merge reviews and business data sets into one data frame
df_yelp <- left_join(yelp_reviews, yelp_tbl, by = "business_id")

#example of github
