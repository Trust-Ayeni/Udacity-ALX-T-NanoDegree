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




# Project Overview
This project has two parts that demonstrate the importance and value of data visualization techniques in the data analysis process.

>- In Part I, Exploratory data visualization, you will use Python visualization libraries to systematically explore a selected dataset, starting from plots of single variables and building up to plots of multiple variables.
>- In Part II, Explanatory data visualization, you will produce a short presentation that illustrates interesting properties, trends, and relationships that you discovered in your selected dataset. The primary method of conveying your findings will be through transforming your exploratory visualizations from the first part into polished, explanatory visualizations.

>- What do I need to install?
This project uses Python 3 and is designed to be completed through the Jupyter Notebooks IDE. It is highly recommended that you use the Anaconda distribution to install Python, since the distribution includes all necessary Python libraries as well as Jupyter Notebooks. The following libraries are expected to be used in this project:
- NumPy
- pandas
- Matplotlib
- Seaborn

## Why this project?
Data visualization is an important skill that is used in many parts of the data analysis process.

Exploratory data visualization generally occurs during and after the data wrangling process, and is the main method that you will use to understand the patterns and relationships present in your data. This understanding will help you approach any statistical analyses and will help you build conclusions and findings. This process might also illuminate additional data cleaning tasks to be performed.
Explanatory data visualization techniques are used after generating your findings, and are used to help communicate your results to others. Understanding design considerations will make sure that your message is clear and effective. In addition to being a good producer of visualizations, going through this project will also help you be a good consumer of visualizations that are presented to you by others.

## What will I learned?
After completing this project, i was be able to:

- Supplement statistics with visualizations to build understanding of data.
- Choose appropriate plots, limits, transformations, and aesthetics to explore a dataset, allowing you to understand distributions of variables and relationships between features.
- Use design principles to create effective visualizations for communicating findings to an audience.


# Part 1 - Exploratory Data Analysis
In this first part, i conducted an exploratory data analysis on a dataset of my choice. Used Python data science and data visualization libraries to explore the dataset’s variables and understand the data’s structure, oddities, patterns, and relationships.

The analysis in this part is structured, going from simple univariate relationships to multivariate relationships, but it does not need to be clean or perfect. There is no single answer that needs to come out of a given dataset. This part of the project is my opportunity to ask questions about the data and make discoveries. It’s essential to keep in mind that sometimes exploration can lead to dead ends and that it can take multiple steps to dig down to what you’re genuinely looking for.

Here are the steps to follow:

>- 1.1. Choose your Dataset
Download the [Dataset Options file](https://docs.google.com/document/d/e/2PACX-1vQmkX4iOT6Rcrin42vslquX2_wQCjIa_hbwD0xmxrERPSOJYDtpNc_3wwK_p9_KpOsfA6QVyEHdxxq7/pub) that provides an overview of each dataset option and example topics to explore. Below is a compiled list of the datasets you can choose from:

[Ford GoBike System Data:](https://video.udacity-data.com/topher/2020/October/5f91cf38_201902-fordgobike-tripdata/201902-fordgobike-tripdata.csv) This data set includes information about individual rides made in a bike-sharing system covering the greater San Francisco Bay area.

[Flights:](https://community.amstat.org/jointscsg-section/dataexpo/dataexpo2009) The dataset name is "Airline On-Time Performance Data". This dataset reports flights in the United States, including carriers, arrival and departure delays, and reasons for delays, from 1987 to 2008. You can see the database description [here](https://www.transtats.bts.gov/DatabaseInfo.asp?QO_VQ=EFD&Yv0x=D).
`Note that this is a large dataset; there are approximately 120 million records in total, and takes up to 12 GiB storage space.`

[Loan Data from Prosper:](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv&sa=D&ust=1581581520570000) This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. See this [data dictionary](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1554486256024000) to understand the dataset's variables.

[PISA Data:](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud507/pisa2012.csv.zip&sa=D&ust=1581581520574000) PISA is a survey of students' skills and knowledge as they approach the end of compulsory education. This survey examines

- how well students have learned the school curriculum,
- how well prepared they are for life beyond school.
- Around 510,000 students in 65 economies took part in the PISA 2012 assessment of reading, mathematics and science. Of those economies, 44 took part in an assessment of creative problem solving and 18 in an assessment of financial literacy. See this [data dictionary](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud507/pisadict2012.csv&sa=D&ust=1554482573645000) to understand the dataset's variables.


# Generate Explanatory Data Visualizations
Generate explanatory data visualizations to tell a story about the data you explored. The Part_II_slide_deck_template.ipynb template notebook file contains these tasks:

- Use code that you used in your exploration phase to generate selective and polished plots.
- Make sure that you pay attention to aspects of design integrity in your revisions. Use appropriate plot types, transformations, and encoding. All plots in the presentation should have a title, labeled axes (including units, if any), legend, scale, ticks, and optionally grid in the plot.
- You need to provide at least 3 visualizations to convey key insights, along with descriptive comments which accurately depict their purpose.

## Create Slide Deck
Now it's time to create a slide deck by converting the notebook file. You need to prepare the notebook for conversion using the steps below:

>- Add Cell Toolbar - Add a specific Cell Toolbar to each cell in your notebook. To do this, select a cell and click on `View > Cell Toolbar > Slideshow.`

>- Choose Slide Type - Assign each cell a Slide Type. Choose Slide for the markdown cells that you want to appear in the slide show, for example, the cells that describe your visualizations. For the code cells that display the visualization, you can choose Sub-Slide. You can choose Skip for the other code cells that don't display visualizations and are not crucial to the presentation.

>- Convert - Once you're ready to generate your presentation, use nbconvert to export the notebook and set up a server for the slides. In the last code cell, use the following command:
`!jupyter nbconvert <Notebook_name>.ipynb --to slides --post serve --no-input --no-prompt`
The command above should open a tab in your web browser where you can scroll through your presentation. Sub-slides can be accessed by pressing `down` when viewing its parent slide. Make sure you remove all of the quote-formatted guide notes in the template before you finish your presentation!

Later you can stop the Kernel.
