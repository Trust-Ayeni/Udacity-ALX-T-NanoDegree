# (FIFA19 Data Exploration and Explanation)
## by (Ayeni Trust)


## Dataset

> This dataset contains comprehensive information for every player in the FIFA 19 database's most recent version. There are 18207 observations and 89 characteristics in all. Age, Nationality, Overall, Potential, Club, Value, Wage, Preferred Foot, International Reputation, Weak Foot, Skill Moves, Work Rate, Position, Jersey Number, Joined, Loaned From, Contract Valid Until, Height, Weight, Skills... are among the FIFA 2019 player qualities mentioned.

### About Dataset
> Source
You can download the dataset from [here](https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset?resource=download)

> Context
Football analytics

> Content
Detailed attributes for every player registered in the latest edition of FIFA 19 database.

> Acknowledgments
Data scraped from https://sofifa.com/

> Inspiration
Inspired by this dataset: https://www.kaggle.com/thec03u5/fifa-18-demo-player-dataset



## Summary of Findings

> I started with some basic descriptive statistics and discovered that `75%` of the participants in the sample are under the age of `29`. The oldest player is `45` years old, while the youngest is only `16` years old. The most valued player is `€118,500,000`, while the lowest valued player is `€10,000`. The average weekly income is `€9583`, while the highest-paid player gets `€565000`. Then I looked at the distributions of some of the variables, such as `Age`, and `Weight`. The age distribution was somewhat favorably biased, which was fascinating to see.

> I went on to look for connections. The following are some of my significant findings: Weight has a negative relationship with acceleration. `Age` has a negative link with a player's potential, `Wage` has a positive correlation with `Release clause`, and `Potential` has a positive correlation with `Release clause`, as one would assume. `Wage` and `value` have a favorable relationship. Aside from the primary factors of interest, I looked at the skill set of players and discovered that `dribbling` ability has a substantial correlation with `finishing` ability.

## Key Insights for Presentation

> I also investigated how important the Age feature and acceleration may be in terms of a player's work rate. It's evident today that as a person matures, so does his acceleration, but in other circumstances, a player's age has no effect on his work rate. Players with a work rate of High/High, High/Medium, or Low/Low have a higher acceleration, while those with a work rate of Low/Low have a lower acceleration. 


## Resources
- Dataset from [here](https://www.kaggle.com/datasets/javagarm/fifa-19-complete-player-dataset?resource=download)