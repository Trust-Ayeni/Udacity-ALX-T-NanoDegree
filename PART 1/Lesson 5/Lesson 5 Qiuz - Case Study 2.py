'''Prior to MY 2013, SmartWay was based on the greenhouse gas 
and air pollution scores found in an earlier
version of the Green Vehicle Guide.'''


### The Data Analysis Process - Case Study 2 ###

## Assessing Data ##
"""
Using Pandas, explore all_alpha_08.csv and all_alpha_18.csv in the Jupyter
notebook below to answer quiz questions below the notebook about these
characteristics of the datasets:
number of samples in each dataset
number of columns in each dataset
duplicate rows in each dataset
datatypes of columns
features with missing values
number of non-null unique values for features in each dataset
what those unique values are and counts for each
"""

import pandas as pd

fuel_08_df = pd.read_csv('all_alpha_08.csv')
fuel_18_df = pd.read_csv('all_alpha_18.csv')


print(fuel_08_df.shape)
print(fuel_18_df.shape)


fuel_08_df.isnull().sum()
fuel_18_df.isnull().sum()


fuel_08_df.duplicated().sum()
fuel_18_df.duplicated().sum()


fuel_08_df.dtypes
fuel_18_df.dtypes


fuel_08_df.SmartWay.nunique()
fuel_18_df.SmartWay.nunique()


fuel_08_df["Sales Area"].nunique()
fuel_18_df["Cert Region"].nunique()


fuel_08_df.Trans.nunique()
fuel_18_df.Trans.nunique()

fuel_08_df.Trans.unique()
fuel_18_df.Trans.unique()

fuel_08_df.Fuel.unique()
fuel_18_df.Fuel.unique()
--------------------------------------------------------------------------------
## Cleaning Column Labels ##
"""
1. Drop extraneous columns
Drop features that aren't consistent (not present in both datasets) or aren't
relevant to our questions. Use Pandas' drop function.
(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.
html)
Columns to Drop:
From 2008 dataset: 'Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'
From 2018 dataset: 'Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'
2. Rename Columns
Change the "Sales Area" column label in the 2008 dataset to "Cert Region" for
consistency.
Rename all column labels to replace spaces with underscores and convert
everything to lowercase. (Underscores can be much easier work with in Python
than spaces. For example, having spaces wouldn't allow you to use df.column_name
instead of df['column_name'] to select columns or use query(). Being consistent
with lowercase and underscores also helps make column names easy to remember.)
"""
# load datasets
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv')
df_18 = pd.read_csv('all_alpha_18.csv')

# view 2008 dataset
df_08.head(1)
# view 2018 dataset
df_18.head(1)

# Drop Extraneous Columns
# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1,
inplace=True)

# confirm changes
df_08.head(1)

# drop columns from 2018 dataset
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1,
inplace=True)

# confirm changes
df_18.head(1)

# Rename Columns
# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area':'Cert Region'}, inplace=True)
# confirm changes
df_08.head(1)

# replace spaces with underscores and lowercase labels for 2008 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
# confirm changes
df_08.head(1)
# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x: x.strip().lower().replace(" ","_"), inplace=True)
# confirm changes
df_18.head(1)

# confirm column labels for 2008 and 2018 datasets are identical
df_08.columns == df_18.columns
# make sure they're all identical like this
(df_08.columns == df_18.columns).all()

# save new datasets for next section
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
--------------------------------------------------------------------------------
## Filter, Drop Nulls, Dedupe ##
"""
1. Filter
For consistency, only compare cars certified by California standards. Filter
both datasets using query to select only rows where cert_region is CA. Then,
drop the cert_region columns, since it will no longer provide any useful
information (we'll know every value is 'CA').
2. Drop Nulls
Drop any rows in both datasets that contain missing values.
3. Dedupe
Drop any duplicate rows in both datasets.
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')

# view dimensions of dataset
df_08.shape
# view dimensions of dataset
df_18.shape

# Filter by Certification Region
# filter datasets for rows following California standards
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')

# confirm only certification region is California
df_08['cert_region'].unique()
# confirm only certification region is California
df_18['cert_region'].unique()

# drop certification region columns form both datasets
df_08.drop(['cert_region'], axis=1, inplace=True)
df_18.drop(['cert_region'], axis=1, inplace=True)

df_08.shape
df_18.shape

# Drop Rows with Missing Values
# view missing value count for each feature in 2008
df_08.isnull().sum()
# view missing value count for each feature in 2018
df_18.isnull().sum()

# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)

# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()
# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()

# Dedupe Data
# print number of duplicates in 2008 and 2018 datasets
print(sum(df_08.duplicated()))
print(sum(df_18.duplicated()))

# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)

# print number of duplicates again to confirm dedupe - should both be 0
print(sum(df_08.duplicated()))
print(sum(df_18.duplicated()))

# save progress for the next section
df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
--------------------------------------------------------------------------------
## Fixing Data Types ##
"""
In the next three sections, you'll make the following changes to make the
datatypes consistent and practical to work with.
Fix cyl datatype
2008: extract int from string.
2018: convert float to int.
Fix air_pollution_score datatype
2008: convert string to float.
2018: convert int to float.
Fix city_mpg, hwy_mpg, cmb_mpg datatypes
2008 and 2018: convert string to float.
Fix greenhouse_gas_score datatype
2008: convert from float to int.
"""
--------------------------------------------------------------------------------
## Fixing Data Types Pt. 1 ##
"""
2008: extract int from string
2018: convert float to int
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')

# check value counts for the 2008 cyl column
df_08['cyl'].value_counts()

# Read this to help you extract ints from strings in Pandas for the next step.
# https://stackoverflow.com/questions/35376387/extract-int-from-string-in-pandas
# Extract int from strings in the 2008 cyl column
df_08['cyl'] = df_08['cyl'].str.extract('(\d+)').astype(int)

# Check value counts for 2008 cyl column again to confirm the change
df_08['cyl'].value_counts()

# convert 2018 cyl column to int
df_18['cyl'] = df_18['cyl'].astype(int)

df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
--------------------------------------------------------------------------------
## Fixing Data Types Pt. 2 ##
"""
2008: convert string to float
2018: convert int to float
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')

# try using Pandas to_numeric or astype function to convert the
# 2008 air_pollution_score column to float -- this won't work
df_08['air_pollution_score'].astype(float)

# Figuring out the issue
# Looks like this isn't going to be as simple as converting the datatype.
# According to the error above, the value at row 582 is "6/4" - let's check
# it out.

df_08[df_08.air_pollution_score == '6/4']


# It's not just the air pollution score!
# The mpg columns and greenhouse gas scores also seem to have the same problem -
# maybe that's why these were all saved as strings! This is a little tricky, so
# I'm going to show you how to do it with the 2008 dataset, and then you'll try
# it with the 2018 dataset.

# First, let's get all the hybrids in 2008
hb_08 = df_08[df_08['fuel'].str.contains('/')]
hb_08
# hybrids in 2018
hb_18 = df_18[df_18['fuel'].str.contains('/')]
hb_18

# create two copies of the 2008 hybrids dataframe
df1 = hb_08.copy()  # data on first fuel type of each hybrid vehicle
df2 = hb_08.copy()  # data on second fuel type of each hybrid vehicle

# Each one should look like this
df1

# columns to split by "/"
split_columns = ['fuel', 'air_pollution_score', 'city_mpg', 'hwy_mpg',
'cmb_mpg', 'greenhouse_gas_score']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# this dataframe holds info for the FIRST fuel type of the hybrid
# aka the values before the "/"s
df1

# this dataframe holds info for the SECOND fuel type of the hybrid
# aka the values before the "/"s
df2

# combine dataframes to add to the original dataframe
new_rows = df1.append(df2)

# now we have separate rows for each fuel type of each vehicle!
new_rows

# drop the original hybrid rows
df_08.drop(hb_08.index, inplace=True)

# add in our newly separated rows
df_08 = df_08.append(new_rows, ignore_index=True)

# check that all the original hybrid rows with "/"s are gone
df_08[df_08['fuel'].str.contains('/')]
df_08.shape

# Repeat this process for the 2018 dataset
# create two copies of the 2018 hybrids dataframe, hb_18
df1 = hb_18.copy()
df2 = hb_18.copy()

# Split values for fuel, city_mpg, hwy_mpg, cmb_mpg
# You don't need to split for air_pollution_score or greenhouse_gas_score here
# because these columns are already ints in the 2018 dataset.

# list of columns to split
split_columns = ['fuel','city_mpg','hwy_mpg','cmb_mpg']

# apply split function to each column of each dataframe copy
for c in split_columns:
    df1[c] = df1[c].apply(lambda x: x.split("/")[0])
    df2[c] = df2[c].apply(lambda x: x.split("/")[1])

# append the two dataframes
new_rows = df1.append(df2)

# drop each hybrid row from the original 2018 dataframe
# do this by using Pandas drop function with hb_18's index
df_18.drop(hb_18.index, inplace=True)

# append new_rows to df_18
df_18 = df_18.append(new_rows, ignore_index=True)

# check that they're gone
df_18[df_18['fuel'].str.contains('/')]
df_18.shape

# Now we can comfortably continue the changes needed for air_pollution_score!
# Here they are again:
# 2008: convert string to float
# 2018: convert int to float

# convert string to float for 2008 air pollution column
df_08.air_pollution_score = df_08.air_pollution_score.astype(float)

# convert int to float for 2018 air pollution column
df_18.air_pollution_score = df_18.air_pollution_score.astype(float)

df_08.to_csv('data_08.csv', index=False)
df_18.to_csv('data_18.csv', index=False)
--------------------------------------------------------------------------------
## Fixing Data Types Part 3 ##
"""
In this last section, you'll fix datatypes of columns for mpg and greenhouse
gas score.
"""
# Fix city_mpg, hwy_mpg, cmb_mpg datatypes
# 2008 and 2018: convert string to float

# load datasets
import pandas as pd
df_08 = pd.read_csv('data_08.csv')
df_18 = pd.read_csv('data_18.csv')

# convert mpg columns to floats
mpg_columns = ['city_mpg','hwy_mpg','cmb_mpg']
for c in mpg_columns:
    df_18[c] = df_18[c].astype(float)
    df_08[c] = df_08[c].astype(float)

# Fix greenhouse_gas_score datatype
# 2008: convert from float to int
# convert from float to int
df_08['greenhouse_gas_score'] = df_08['greenhouse_gas_score'].astype(int)

# All the dataypes are now fixed! Take one last check to confirm all
# the changes.
df_08.dtypes
df_18.dtypes
df_08.dtypes == df_18.dtypes

# Save your new CLEAN datasets as new files!
df_08.to_csv('clean_08.csv', index=False)
df_18.to_csv('clean_18.csv', index=False)
--------------------------------------------------------------------------------
## Exploring With Visuals ##
'''Use clean_08.csv and clean_18.csv. You should've created these data 
files in the previous section: Fixing Data Types Pt 3.'''

import pandas as pd
%matplotlib inline

# load datasets
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


df_08.greenhouse_gas_score.hist();


df_18.greenhouse_gas_score.hist();


df_08.cmb_mpg.hist();


df_18.cmb_mpg.hist();


df_08.plot(x="displ", y="cmb_mpg", kind="scatter");


df_18.plot(x="displ", y="cmb_mpg", kind="scatter");


df_08.plot(x="greenhouse_gas_score", y="cmb_mpg", kind="scatter");


df_18.plot(x="greenhouse_gas_score", y="cmb_mpg", kind="scatter");


--------------------------------------------------------------------------------
## Conclusions & Visuals ##
# load datasets
import pandas as pd
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')
import matplotlib.pyplot as plt
% matplotlib inline

# Q1: Are more unique models using alternative sources of fuel? By how much?
'''Let's first look at what the sources 
of fuel are and which ones are alternative sources.'''
df_08.fuel.value_counts()

df_18.fuel.value_counts()


'''Looks like the alternative sources of fuel available in 2008 are CNG and ethanol, 
and those in 2018 ethanol and electricity. 
(You can use Google if you weren't sure which ones are alternative sources of fuel!)'''

# how many unique models used alternative sources of fuel in 2008
alt_08 = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08


# how many unique models used alternative sources of fuel in 2018
alt_18 = df_18.query('fuel in ["Ethanol", "Electricity"]').model.nunique()
alt_18



plt.bar(["2008", "2018"], [alt_08, alt_18])
plt.title("Number of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");

'''Since 2008, the number of unique models using alternative sources of fuel increased by 24. 
We can also look at proportions.'''

# total unique models each year
total_08 = df_08.model.nunique()
total_18 = df_18.model.nunique()
total_08, total_18

prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18

plt.bar(["2008", "2018"], [prop_08, prop_18])
plt.title("Proportion of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Proportion of Unique Models");



# Q2: How much have vehicle classes improved in fuel economy?
'''Let's look at the average fuel economy for each vehicle class for both years.'''
veh_08 = df_08.groupby(['veh_class']).cmb_mpg.mean()
veh_08

veh_18 = df_18.groupby('veh_class').cmb_mpg.mean()
veh_18

# how much they've increased by for each vehicle class
inc = veh_18 - veh_08
inc


# only plot the classes that exist in both years
inc.dropna(inplace=True)
plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');



# Q3: What are the characteristics of SmartWay vehicles? Have they changed
# over time?
'''We can analyze this by 
filtering each dataframe by SmartWay classification and exploring these datasets.'''

# smartway labels for 2008
df_08.smartway.unique()

# get all smartway vehicles in 2008
smart_08 = df_08.query('smartway == "yes"')

# explore smartway vehicles in 2008
smart_08.describe()

'''Use what you've learned so for to further explore this dataset on 2008 smartway vehicles.'''
# smartway labels for 2018
df_18.smartway.unique()

# get all smartway vehicles in 2018
smart_18 = df_18.query('smartway in ["Yes", "Elite"]')

smart_18.describe()


# Q4: What features are associated with better fuel economy?
'''You can explore trends between cmb_mpg and the other features in this dataset, 
or filter this dataset like in the previous question and explore the properties of that dataset. 
For example, you can select all vehicles that have the top 50% fuel economy ratings like this.'''
top_08 = df_08.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()

top_18 = df_18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()
--------------------------------------------------------------------------------
## Merging Datasets ##
'''Types of Merges
So far, we've learned about appending dataframes. 
Now we'll learn about pandas Merges, a different way of combining dataframes. 
This is similar to the database-style "join." If you're familiar with SQL, 
this comparison with SQL may help you connect these two.

Here are the four types of merges in pandas. 
Below, "key" refers to common columns in both dataframes that we're joining on.

1. Inner Join - Use intersection of keys from both frames.
2. Outer Join - Use union of keys from both frames.
3. Left Join - Use keys from left frame only.
4. Right Join - Use keys from right frame only.
'''


"""
1. Rename 2008 columns to distinguish from 2018 columns after the merge
To do this, use Pandas' rename() with a lambda function. See example here. In
the lambda function, take the first 10 characters of the column label and and
concatenate it with _2008. (Only take the first 10 characters to prevent really
long column names.)
The lambda function should look something like this: lambda x: x[:10] + "_2008"
In your rename, don't forget to specify the parameter columns= when you add the
lambda function!
2. Perform inner merge
To answer the last question, we are only interested in how the same model of
car has been updated and how the new model's mpg compares to the old model's
mpg.
Perform an inner merge with the left on model_2008 and the right on model.
See documentation for Pandas' merge here.
(https://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-
dataframe-joining-merging)
"""
# load datasets
import pandas as pd
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')

# rename 2008 columns
df_08.rename(columns=lambda x: x[:10] + "_2008", inplace=True)

# view to check names
df_08.head()

# merge datasets
df_combined = df_08.merge(df_18, left_on='model2008', right_on='model', how='inner')

# view to check merge
df_combined.head()

df_combined.to_csv('combined_dataset.csv', index=False)

--------------------------------------------------------------------------------
## Results with Merged Dataset ##
"""
Q5: For all of the models that were produced in 2008 that are still being
produced now, how much has the mpg improved and which vehicle improved the
most?
Here are the steps for answering this question.
1. Create a new dataframe, model_mpg, that contain the mean combined mpg values
in 2008 and 2018 for each unique model
To do this, group by model and find the mean cmb_mpg_2008 and mean cmb_mpg for
each.
2. Create a new column, mpg_change, with the change in mpg
Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg
3. Find the vehicle that improved the most
Find the max mpg change, and then use query or indexing to see what model it
is!
"""
# load dataset
import pandas as pd
df = pd.read_csv('combined_dataset.csv')
df.head()


'''To do this, group by `model` and 
find the mean `cmb_mpg_2008` and mean `cmb_mpg` for each.'''

model_mpg = df.groupby('model').mean()[['cmb_mpg2008', 'cmb_mpg']]


model_mpg.head()

# 2. Create a new column, `mpg_change`, with the change in mpg
'''Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg'''

model_mpg['mpg_change'] = model_mpg['cmb_mpg'] - model_mpg['cmb_mpg2008']

model_mpg.head()


# 3. Find the vehicle that improved the most
'''Find the max mpg change, and then use query or indexing to see what model it is!'''
max_change = model_mpg['mpg_change'].max()
max_change


model_mpg[model_mpg['mpg_change'] == max_change]


# Pandas also has a useful [`idxmax`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html) 
# function you can use to find the index of the row containing a column's maximum value!

idx = model_mpg.mpg_change.idxmax()
idx


model_mpg.loc[idx]