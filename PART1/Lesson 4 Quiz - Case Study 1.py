### The Data Analysis Process - Case Study 1 ###

## Assessing Data ##

import pandas as pd

df_red = pd.read_csv('winequality-red.csv', sep=';')
df_white = pd.read_csv('winequality-white.csv', sep=';')

#How many samples of red wine are there?#
#How many samples of white wine are there?#
#How many columns are in each dataset?#
#Which features have missing values?#
df_red.info()
df_white.info()

#How many duplicate rows are in the white wine dataset?#
#Are duplicate rows in these datasets significant/ need to be dropped?#
sum(df_white.duplicated())

#How many unique values of quality are in the red wine dataset?#
#How many unique values of quality are in the white wine dataset?#
df_red.nunique()
df_white.nunique()

#What is the mean density in the red wine dataset?#
mean = df_red['density'].mean()
print(mean)

--------------------------------------------------------------------------------
## Appending Data ##
# import numpy and pandas
import pandas as pd
import numpy as np

# load red and white wine datasets
red_df = pd.read_csv('winequality-red.csv', sep=';')
white_df = pd.read_csv('winequality-white.csv', sep=';')
red_df.info()
white_df.info()

# create color array for red dataframe
color_red = np.repeat("red",1599)

# create color array for white dataframe
color_white = np.repeat("white", 4898)

red_df['color'] = color_red
red_df.head()
white_df['color'] = color_white
white_df.head()

# append dataframes
wine_df = red_df.append(white_df, ignore_index=True)

# view dataframe to check for success
wine_df.head()

wine_df.to_csv('winequality_edited.csv', index=False)

--------------------------------------------------------------------------------
## Appending Data (cont'd)##
"""
Add a new cell below the first code cell (where you imported packages and
loaded data) to fix the problematic column label in the red dataframe.
Use Pandas' rename function to change the total_sulfur-dioxide column label
to total_sulfur_dioxide. You can check out this Stack Overflow page to help
you.
(https://stackoverflow.com/questions/20868394/changing-a-specific-column-name-
in-pandas-dataframe)
Then, rerun all the cells below that to append the dataframes and save your
successfully combined dataset!
"""

red_df.rename(columns={'total_sulfur-dioxide':'total_sulfur_dioxide'},
inplace=True)

--------------------------------------------------------------------------------
## Exploring with Visuals ##
"""
Use the notebook below to perform exploratory data analysis on your newly
combined dataframe. Create some visuals to answer these quiz questions below
the notebook.
-   Based on histograms of columns in this dataset, which of the following feature
    variables appear skewed to the right? Fixed Acidity, Total Sulfur Dioxide, pH,
    Alcohol 
    
    Answer is: fixed_acidity and alcohol
    
    
-   Based on scatterplots of quality against different feature variables, which
    of the following is most likely to have a positive impact on quality?
    Volatile Acidity, Residual Sugar, pH, Alcohol
    
    Answer is: alcohol
    
"""
# Load dataset
import pandas as pd
% matplotlib inline

wine_df = pd.read_csv('winequality_edited.csv')
wine_df.head()

# Histograms for Various Features
wine_df['fixed_acidity'].plot(kind='hist');
wine_df['total_sulfur_dioxide'].plot(kind='hist');
wine_df['pH'].plot(kind='hist');
wine_df['alcohol'].plot(kind='hist');

# Scatterplots of Quality Against Various Features
wine_df.plot(x='quality', y='volatile_acidity', kind='scatter');
wine_df.plot(x='quality', y='residual_sugar', kind='scatter');
wine_df.plot(x='quality', y='pH', kind='scatter');
wine_df.plot(x='quality', y='alcohol', kind='scatter');

--------------------------------------------------------------------------------
## Conclusions Using Groupby ##
"""
In the notebook below, you're going to investigate two questions about this
data using Pandas' groupby function. Here are tips for answering each
question:
Q1: Is a certain type of wine (red or white) associated with higher quality?
Q2: What level of acidity (pH value) receives the highest average rating?
Acidity Levels:
High: Lowest 25% of pH values
Moderately High: 25% - 50% of pH values
Medium: 50% - 75% of pH values
Low: 75% - max pH value
"""
# Load `winequality_edited.csv`
import pandas as pd

df = pd.read_csv('winequality_edited.csv')

# Is a certain type of wine associated with higher quality?
# Find the mean quality of each wine type (red and white) with groupby
df.groupby('color').mean().quality

# What level of acidity receives the highest average rating?
# View the min, 25%, 50%, 75%, max pH values with Pandas describe
df.describe().pH

# Bin edges that will be used to "cut" the data into groups
bin_edges = [2.27, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values

# Labels for the four acidity level groups
bin_names = ['High', 'Moderately_High', 'Medium', 'Low'] # Name each acidity

# Creates acidity_levels column
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
df.head()

# Find the mean quality of each acidity level with groupby
df.groupby('acidity_levels').mean().quality


# Save changes for the next section
df.to_csv('winequality_edited.csv', index=False)

--------------------------------------------------------------------------------
## Pandas Query ##

# selecting malignant records in cancer data
df_m = df[df['diagnosis'] == 'M']
df_m = df.query('diagnosis == "M"')

# selecting records of people making over $50K
df_a = df[df['income'] == ' >50K']
df_a = df.query('income == " >50K"')

--------------------------------------------------------------------------------
## Drawing Conclusions Using Query ##
"""
Q1: Do wines with higher alcoholic content receive better ratings?
To answer this question, use query to create two groups of wine samples:
1. Low alcohol (samples with an alcohol content less than the median)
2. High alcohol (samples with an alcohol content greater than or equal to the
median)
Then, find the mean quality rating of each group.
Q2: Do sweeter wines (more residual sugar) receive better ratings?
Similarly, use the median to split the samples into two groups by residual
sugar and find the mean quality rating of each group.
"""
# Load `winequality_edited.csv`
import pandas as pd
df = pd.read_csv('winequality_edited.csv')


# get the median amount of alcohol content
df.alcohol.median()

# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < 10.3')

# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= 10.3')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True

# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.quality.mean(), high_alcohol.quality.mean()

# Do sweeter wines receive better ratings?
# get the median amount of residual sugar
df.residual_sugar.median()

# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < 3')

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar >= 3')

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # should be True

# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean()

--------------------------------------------------------------------------------
## Matplotlib Example ##
"""
Before we jump into the making of this plot, let's walk through a simple example
using Matplotlib to create a bar chart.
Now that we've made some conclusions, we can create visualizations to display our findings regarding 
the association between wine quality and different properties of wine.
"""
import matplotlib.pyplot as plt
% matplotlib inline

plt.bar([1, 2, 3], [224, 620, 425]);

# plot bars
plt.bar([1, 2, 3], [224, 620, 425])

# specify x coordinates of tick labels and their labels
plt.xticks([1, 2, 3], ['a', 'b', 'c']);

# plot bars with x tick labels
plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c']);

plt.bar([1, 2, 3], [224, 620, 425], tick_label=['a', 'b', 'c'])
plt.title('Some Title')
plt.xlabel('Some X Label')
plt.ylabel('Some Y Label');
--------------------------------------------------------------------------------
## Plotting with Matplotlib ##
# Import necessary packages and load `winequality_edited.csv`
import matplotlib.pyplot as plt
% matplotlib inline
import pandas as pd

df = pd.read_csv('winequality_edited.csv')

#1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol
# wine samples. This first one is filled out for you.

# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()

# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');

#2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high
# residual sugar wine samples.

# Use query to select each group and get its mean quality
median = df['residual_sugar'].median()
low = df.query('residual_sugar < {}'.format(median))
high = df.query('residual_sugar >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()

# Create a bar chart with proper labels
locations = [1,2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Residual Sugar')
plt.xlabel('Residual Sugar Content')
plt.ylabel('Average Quality Rating');

#3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# Use groupby to get the mean quality for each acidity level
acidity_level_quality_means = df.groupby('acidity_levels').quality.mean()
acidity_level_quality_means

# Create a bar chart with proper labels
locations = [4, 1, 2, 3]  # reorder values above to go from low to high
heights = acidity_level_quality_means

# labels = ['Low', 'Medium', 'Moderately High', 'High']
labels = acidity_level_quality_means.index.str.replace('_', ' ').str.title() # alternative to commented out line above

plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Acidity Level')
plt.xlabel('Acidity Level')
plt.ylabel('Average Quality Rating');

# Bonus: Create a line plot for the data in #3
# You can use pyplot's plot function for this.
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot

plt.plot(labels, heights, color='green', linestyle='solid', marker='o',
markerfacecolor='blue', markersize=12);
--------------------------------------------------------------------------------
'''
Plotting Wine Type and Quality with Matplotlib
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
% matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

wine_df = pd.read_csv('winequality_edited.csv')


'''
Create arrays for red bar heights white bar heights¶
Remember, there's a bar for each combination of color and quality rating. 
Each bar's height is based on the proportion of samples of that color with that quality rating.

1. Red bar proportions = counts for each quality rating / total # of red samples
2. White bar proportions = counts for each quality rating / total # of white samples
'''

# get counts for each rating and color
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
color_counts

# get total counts for each color
color_totals = wine_df.groupby('color').count()['pH']
color_totals

# get proportions by dividing red rating counts by total # of red samples
red_proportions = color_counts['red'] / color_totals['red']
red_proportions

# get proportions by dividing white rating counts by total # of white samples
white_proportions = color_counts['white'] / color_totals['white']
white_proportions

'''
Plot proportions on a bar chart
Set the x coordinate location for each rating group and and width of each bar.
'''
 
# Oh, that won't work because we're missing a red wine value for a the 9 rating. 
# Even though this number is a 0, we need it for our plot. 
# Run this then run the codes below.
red_proportions['9'] = 0
red_proportions


ind = np.arange(len(red_proportions))  # the x locations for the groups
width = 0.35       # the width of the bars


# plot bars
red_bars = plt.bar(ind, red_proportions, width, color='r', alpha=.7, label='Red Wine')
white_bars = plt.bar(ind + width, white_proportions, width, color='w', alpha=.7, label='White Wine')

# title and labels
plt.ylabel('Proportion')
plt.xlabel('Quality')
plt.title('Proportion by Wine Color and Quality')
locations = ind + width / 2  # xtick locations
labels = ['3', '4', '5', '6', '7', '8', '9']  # xtick labels
plt.xticks(locations, labels)

# legend
plt.legend()





