# INTORODUCTION

## The Final Step: Cleaning Data
In this lesson, you will work on the third step of the data wrangling process, cleaning your data. Here you will focus on two main items that you identified in your assessment in the prior lesson:

- Quality
- Tidiness
- Clean Data

While there are ways to clean data manually using spreadsheet programs and text editors, the best way to clean data is to code it yourself. This requires three steps:

>- Define - define how you will clean the issue in words
>- Code - convert your definitions into executable code
>- Test - test your data to ensure your code was implemented correctly


>- Next, i'll take your assessments for the last lesson and define, code, and test cleaning operations for each.


## Lesson Outline

Data wrangling process:

- Gather
- Assess
- Clean (this lesson)

>- Cleaning data is the third step in data wrangling. It is where I'll fix the quality and tidiness issues that I'll identified in the assess step. In this lesson, I'll clean all of the issues I identified in Lesson 3 using Python and pandas.

This lesson is structured as follows:

- You'll get remotivated (if you aren't already) to clean the dataset for lessons 3 and 4: Phase II clinical trial data that compares the efficacy and safety of a new oral insulin to treat diabetes to injectable insulin
- You'll learn about the data cleaning process: defining, coding, and testing
- You'll address the missing data first (and learn why it is usually important to address these completeness issues first)
- You'll tackle the tidiness issues next (and learn why this is usually the next logical step)
- And finally, you'll clean up the quality issues

This lesson will consist primarily of Jupyter Notebooks, of which there will be two types: one quiz notebook that you'll work with throughout the whole lesson (i.e. my work will carry over from page to page) and three solution notebooks. I'll pop in and out to introduce the larger conceptual bits.

>- I will leverage the most common cleaning functions and methods in the pandas library to clean the nineteen quality issues and four tidiness issues identified in Lesson 3. Given your pandas experience and that this isn't a course on pandas, these functions and methods won't be covered in detail. Regardless, with this experience and your research and documentation skills, i am confident that leaving this course i'll be able to clean any form of dirty and/or messy data that comes your way in the future.


>- The same Phase II clinical trial dataset for a new oral insulin called Auralin in Lesson 3 (Assessing Data) is used here again in Lesson 4 (Cleaning Data). The same dataset preview video and disclaimer text are included here, as well.



## Learning About Our Dataset


>- Diabetes
The increasing prevalence of diabetes in the 21st century is a problem. Patients have symptoms like

- unusual thirst
- frequent urination
- extreme fatigue
- Diabetes can also lead to more serious complications like stroke, blindness, loss of limbs, kidney failure, and even heart attack.


# Discovery of Insulin
In the 1920s, insulin was discovered by Frederick Banting. Most of the food we eat is turned to glucose, or sugar, for our bodies to use for energy. The pancreas, an organ near the stomach, makes a hormone called insulin, to help glucose get into the cells of our bodies. When you have diabetes, your body either doesn't make enough insulin or can't use its own insulin as well as it should. And this causes sugars to build-up in the blood.

With Banting's discovery of insulin, pharmaceutical companies began large-scale production of insulin. Although it doesn't cure diabetes, it's one of the biggest discoveries in medicine. When it came, it was like a miracle.


# Challenges with Insulin
The default method of administration is by a needle, multiple times a day. Insulin pumps are a more recent invention. These are insulin delivering devices that are semi-permanently connected to a diabetic's body.

# The Future: Oral Insulin?
Wouldn't it be great if diabetics could take insulin orally? This is an active area of research, but historically the roadblock is getting insulin through the stomach's thick lining.


>- Our dataset: Auralin and Novodra Trials
We will be looking at the phase two clinical trial data of 350 patients for a new innovative oral insulin called Auralin - a proprietary capsule that can solve this stomach lining problem.

>- Phase two trials are intended to:

- Test the efficacy and the dose response of a drug
- Identify adverse reactions
- In this trial, half of the patients are being treated with Auralin, and the other 175 being treated with a popular injectable insulin called Novodra. By comparing key metrics between these two drugs, we can determine if Auralin is effective.

# Why do we need Data Cleaning?
Healthcare data is notorious for its errors and disorganization, and its clinical trial data is no exception. For example, human errors during the patient registration process mean we can have

- duplicate data
- missing data
- inaccurate data
You're going to take the first step in fixing these issues by assessing this data sets quality and tidiness, and then cleaning all of these issues using Python and Pandas. Our goal is to create a trustworthy analysis.

>- DISCLAIMER: This Data Isn't "Real"
The Auralin and Novodra are not real insulin products. This clinical trial data was fabricated for the sake of this course. When assessing this data, the issues that you'll detect (and later clean) are meant to simulate real-world data quality and tidiness issues.

That said:

- This dataset was constructed with the consult of real doctors to ensure plausibility.
- This clinical trial data for an alternative insulin was inspired and closely mimics this real clinical trial for an inhaled insulin called Afrezza.
- The data quality issues in this dataset mimic real, common data quality issues in healthcare data. These issues impact the quality of care, patient registration, and revenue.
- The patients in this dataset were created using this fake name generator and do not include real names, addresses, phone numbers, emails, etc.



## Manual vs. Programmatic Cleaning

>- Manual Data Cleaning includes:

Retyping incorrect data
Copying and pasting columns and rows
However, manual cleaning is inefficient, error-prone, and demoralizing. So never clean manually.


>- Programmatic Data Cleaning uses code to:

Automate cleaning tasks
Minimize repetition
Save time
Data wrangling takes a tremendous amount of time for the data professional, so doing anything that saves time is great.



## Getting Ready To Clean
The very first thing to do before any cleaning occurs is to make a copy of each piece of data. All of the cleaning operations will be conducted on this copy so you can still view the original dirty and/or messy dataset later. Copying DataFrames in pandas is done using the copy method. If the original DataFrame was called df, the soon-to-be clean copy of the dataset could be named df_clean.

df_clean = df.copy()
Note that simply assigning a DataFrame to a new variable name leaves the original DataFrame vulnerable to modifications, as explained in the answers to this Stack Overflow question: "Why should I make a copy of a DataFrame in pandas?"


# The Cleaning Process
Programmatic data cleaning is a separate process within data wrangling. It has three steps:

- Defining
- Coding
- Testing

>- Define
The first step is to define a data cleaning plan in writing by converting your assessments into cleaning tasks by writing little how-to guides. This plan also serves as documentation so that your work can be reproduced.

>- Code
Second, you'll translate these words to code and actually run it.

>- Test
Finally, you'll test your dataset often using code to make sure your cleaning code worked. This is like a revisiting the assess step.

- An Example
Note: a copy of the original dataset was not made before cleaning in the following example, though one should have been.


Here's a concrete example of the data cleaning process: defining, coding, and testing. So

- Gather
We imported the pandas library and read the animals.csv file into a DataFrame called df.

- Assess
Visual assessment was done in pandas and two quality issues were noted:

>- bb before every animal name
>- ! instead of . for decimal in body weight and brain weight

- Clean

>- Step 1: Define
- Defining uses verbs. It's a call to action to fix the issue we observed:

- Remove 'bb' before every animal name
- Replace ! with . in body weight and brain columns

>- Step 2: Code
This is actually doing the task listed in the Define step. For this course, we will use the pandas library.

## Remove 'bb' before every animal name
df['Animal'] = df['Animal'].str[2:]

## Replace ! with . in body weight and brain columns
df['Body Weight (kg)'] = df['Body Weight (kg)'.str.replace('!','.')
df['Brain weight (g)'] = df['Brain weight (g)'.str.replace('!','.')

>- Step 3: Test
The testing step is about making sure our code worked. The simplest way to do so is to visually assess your data set. That works for this data set because it's pretty small but we can also use programmatic assessments like search statements and pandas built in testing methods.


## Address Missing Data First

When checking data quality, it is usually best to deal with completeness issues first. For missing data this means:

- Concatenate
- Join
- Impute, if possible
It's important to do this upfront so that subsequent data cleaning will not have to be repeated.

# Clinical Trial Dataset
In the clinical trial dataset, we identified three completeness issues:

- treatments table
- missing HbA1c changes
- missing records (280 instead of 350)
- patients table
- Missing demographic information (address - contact columns)
Unfortunately, we can't do anything about the missing demographic information because we have no way of accessing that information until those patients come back. But let's deal with the other missing data with the exercise on the next page.


## Cleaning for Tidiness

Address Tidiness After Structural Issues and Before Content Issues
After addressing missing data the next logical step is cleaning for tidiness. Statistician, Hadley Wickham, is the pioneer of tidy data, and in his paper, 'Tidy data' (The Journal of Statistical Software, vol. 59, 2014), he makes these key points:

- Tidy datasets are easy to manipulate
- Tidy datasets with data quality issues are almost always easier to clean than untidy datasets with the same issues
- This means it's generally best to clean structural issues first, like tidiness, and then clean content issues, like quality.

# Clinical Trial Dataset
In the oral insulin clinical trial dataset, we found four sections of the dataset that were not tidy:

- Tidiness
- Contact column in patients table should be split into phone number and email
- Three variables in two columns in treatments table (treatment, start dose and end dose)
- Adverse reaction should be part of the treatments table
- Given name and surname columns in patients table duplicated in treatments and adverse_reactions tables
You'll learn how to fix these four issues next.

# Next Steps
Once the missing data and tidiness issues are cleaned, all that remains is cleaning the remaining data quality issues.

There were a lot of data quality issues in this dataset:

# Quality
- patients table
- zip code is a float not a string
- zip code has four digits sometimes
- Tim Neudorf height is 27 in instead of 72 in
- full state names sometimes, abbreviations other times
- Dsvid Gustafsson
- Missing demographic information (address - contact columns)
- Erroneous datatypes (assigned sex, state, zip_code, and birthdate columns)
- Multiple phone number formats
- Default John Doe data
- Multiple records for Jakobsen, Gersten, Taylor
- kgs instead of lbs for Zaitseva weight
- treatments table
- missing HbA1c changes
- the letter u in starting and ending doses for Auralin and Novodra
- lowercase given names and surnames
- missing records (280 instead of 350)
- Erroneous datatypes (auralin and novodra columns)
- Inaccurate HbA1c changes (4s mistaken as 9s)
- Nulls represented as dashes (-) in auralin and novodra columns
- adverse_reactions table
- lowercase given names and surnames
Next, you'll use a variety of common pandas functions to clean them all.

>- This is a hefty task but you can do it!


## Is Auralin Effective?

# Comparing Key Metrics
After assessing and cleaning the clinical trial data set we are ready to determine if the proposed new oral insulin, Auralin, compared to the injectable insulin Novodra.

- Adverse Reactions
For Auralin to pass this Phase II clinical trial it must be deemed safe, and the adverse reactions to it is encouraging.


# Adverse Reactions
|treatment	| adverse_reaction|
| --- | --- |	
|Auralin cough|	1|
|headache	|1|
|hypoglycemia|	10|
|nausea	|1|
|throat irritation|	2|
|Novodra cough|	1|
|headache|	2|
|hypoglycemia|	10|
|injection site discomfort|	6|
|nausea|	1|

>- These adverse_reactions were actually previously standalone, but we joined this to the treatments table to allow for this analysis. Between the two drugs, Auralin and Novodra, the counts of each adverse reaction are pretty similar. One exception is throat irritation for Auralin, the oral insulin which is expected because this pill is taken orally and passes by the throat before it gets to the stomach. Another is injection site discomfort for Novodra which is the injectable insulin because that's a common known adverse reaction for injectable insulin because of needles. This one of the reasons why we want oral insulin in the first place.

These counts are more clear in these horizontal bar charts.



Adverse Reaction Count Bar Charts for Auralin and Novodra
Pre-trial Post-trial Mean Insulin Dose Change.
Dose change is important because if the new oral insulin requires a higher dosage to be effective, the manufacturer might not bring this to market because it wouldn't be financially feasible.

The dosage information was hidden in two columns in the treatments table, auralin and novodra, with start dose and end dose in each column, and the treatment value in each column header. We converted this to a tidy format and separated out the start_dose and end_dose by melting the treatment variable down to its own column. This allowed us to run a mean dose change analysis:

Mean Dosage Change
treatment	
Auralin	-8.325714
Novodra	0.377143Again, the results here are good for Auralin. Patients that were treated with Auralin required on average, 8 more units of insulin to establish a safe, steady blood sugar level compared to Novodra patients who on average required 0.4 units less of insulin. Auralin requiring 8 more units, is expected because we knew that oral insulin has a tougher time getting into the bloodstream through the stomach lining, and eight units more isn't a big a deal.
Mean Insulin Unit Change for Auralin and Novodra
HbA1c Change
HbA1 change is our key indicator for diabetes control. Most patients in this trial start around 7.9 percent so if we can establish that Auralin causes a reduction in HbA1c that's similar to the current injectable insulin standard, that's a success. We can measure that through a confidence interval But first we need to establish the difference in means.

Before Cleaning
Before cleaning, Novodra had a massive advantage in HbA1C reduction, 0.71 compared to 0.35 for Auralin.

treatment	
Auralin	0.344872
Novodra	0.714731
Pre-trial/Post-trial Mean HbA1c Change (Unclean Data)
After Cleaning
After cleaning, the difference is much smaller



treatment	
Auralin	0.387657
Novodra	0.40491
Pre-trial/Post-trial Mean HbA1c Change (Clean Data)
These results are encouraging but clinical trial results require more rigorous statistical analysis.

Confidence Interval
The confidence interval refers to the range of values that a parameter is likely to fall in with a specific probability. We want the upper limit of the confidence interval of the differences in means to be less than 0.4, meaning that if the difference in means is less than 0.4, we can be highly confident that our results are meaningful.

Before cleaning, the upper limit of the confidence interval is 0.43 which means that Auralin would not have passed the Phase II clinical trial. But after cleaning the HbA1C reduction is pretty similar the upper limit of the confidence interval is 0.03.

before_CI_upper_limit	after_CI_upper_limit
0.43	0.03
0.03 is significantly lower than 0.4, which means that Auralin oral insulin is similarly effective to Novodra injectable insulin.

Good News!
Our oral insulin, Auralin passed Phase II clinical trials! This is a big deal because the probability of success for Phase II trials is 31%. A successful Phase II trial means we have a good chance of making it past Phase III and the regulatory review process to make it to market. If it does, this oral insulin would be an enormous breakthrough in treating Type I and Type II diabetes patients, as freedom from daily injections would liberate patients, reduce missed doses and therefore reduce irritating and sometimes serious complications from diabetes.

Great job assessing and cleaning this data!

More Reading
Confidence intervals are an important measure o the validity of our results. Learn more about Confidence Intervals:







## New Terms

| Terms    | Definition |
| --- | --- |
|Imputing	| Filling in missing data with other values|


# More Reading
Want to learn more about imputation? Read this: [here](https://en.wikipedia.org/wiki/Imputation_(statistics))