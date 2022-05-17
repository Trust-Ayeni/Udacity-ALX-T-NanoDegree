## Assessing Data
Assessing your data is the second step in the data wrangling process. When assessing, you're inspecting your data set for two things:

### Data quality issues: Data that has quality issues have issues with content like missing, duplicate, or incorrect data. This is called dirty data.
Lack of tidiness: Data that has specific structural issues that slow you down when cleaning and analyzing, visualizing, or modeling your data later.

### Assess Data
You can search for these issues in two ways:

1. Visually by scrolling

2. Programmatically using code

![Assessing Data](/images/Capture.PNG)

When you detect an issue, document it to make cleaning easier.

In this lesson, we will assess a pre-gathered data set that's full of issues and find them either visually or using the functions in Python's pandas library.

You'll leave this lesson with an eagle eye for unclean data.


## Lesson Outline
Data wrangling process:

>- Gather

>- Assess (this lesson)

>- Clean

Assessing your data is the second step in data wrangling. When assessing, we're like a detective at work, inspecting your dataset for two things: data quality issues (i.e. content issues) and lack of tidiness (i.e. structural issues).

Assessing is the precursor to cleaning. we can't clean something that you don't know exists! In this lesson, we'll learn to identify and categorize common data quality and tidiness issues. This lesson is the shortest and most "hands-off" code-wise of all four in the course because of the passive nature of assessing relative to gathering and cleaning. We have tried to include quizzes wherever possible.

This lesson will be structured as follows:
>- We'll get motivated to assess (and later clean) the dataset for lessons 3 and 4: Phase II clinical trial data that compares the efficacy and safety of a new oral insulin to treat diabetes

>- We'll learn to distinguish between dirty data and messy data

>- We'll assess the data visually and programmatically to identify:

    -- Data quality issues

    -- Tidiness issues

>- We'll learn about data quality dimensions and categorize each of the data quality issues identified above into its appropriate dimension






### Learning About Our Dataset


#### Diabetes
The increasing prevalence of diabetes in the 21st century is a problem. Patients have symptoms like

>- unusual thirst

>- frequent urination

>- extreme fatigue

>- Diabetes can also lead to more serious complications like stroke, blindness, loss of limbs, kidney failure, and even heart attack.

#### Discovery of Insulin
In the 1920s, insulin, was discovered by Frederick Banting. Most of the food we eat is turned to glucose, or sugar, for our bodies to use for energy. The pancreas, an organ near the stomach, makes a hormone called insulin, to help glucose get into the cells of our bodies. When you have diabetes, your body either doesn't make enough insulin or can't use its own insulin as well as it should. And this causes sugars to build-up in the blood.

With Banting discovery of insulin, pharmaceutical companies began large-scale production of insulin. Although it doesn't cure diabetes, it's one of the biggest discoveries in medicine. When it came, it was like a miracle.


#### Challenges with Insulin
The default method of administration is by a needle, multiple times a day. Insulin pumps are a more recent invention. These are insulin delivering devices that are semi-permanently connected to a diabetics body.

>- The Future: Oral Insulin?
Wouldn't it be great if diabetics could take insulin orally? This is an active area of research, but historically the roadblock is getting insulin through the stomach's thick lining.

>- Our dataset: Auralin and Novodra Trials
We will be looking at the phase two clinical trial data of 350 patients for a new innovative oral insulin called Auralin - a proprietary capsule that can solve this stomach lining problem.


Phase two trials are intended to:
>- Test the efficacy and the dose response of a drug
>- Identify adverse reactions
>- In this trial, half of the patients are being treated with Auralin, and the other 175 being treated with a popular injectable insulin called Novodra. By comparing key metrics between these two drugs, we can determine if Auralin is effective.


#### Why do we need Data Cleaning?
Healthcare data is notorious for its errors and disorganization, and its clinical trial data is no exception. For example, human errors during the patient registration process means we can have

>- duplicate data
>- missing data
>- inaccurate data
You're going to take the first step in fixing these issues by assessing this data sets quality and tidiness, and then cleaning all of these issues using Python and Pandas. Our goal is to create a trustworthy analysis.


>- **DISCLAIMER**: This Data Isn't `Real`
The Auralin and Novodra are not real insulin products. This clinical trial data was fabricated for the sake of this course. When assessing this data, the issues that you'll detect (and later clean) are meant to simulate real-world data quality and tidiness issues.


#### That said:
>- This dataset was constructed with the consultation of real doctors to ensure plausibility.

>- This clinical trial data for an alternative insulin was inspired and closely mimics this real clinical trial for a new inhaled insulin called Afrezza.

>- The data quality issues in this dataset mimic real, common data quality issues in healthcare data. These issues impact quality of care, patient registration, and revenue.

>- The patients in this dataset were created using this fake name generator and do not include real names, addresses, phone numbers, emails, etc.


####
Let's explicitly define the terms dirty data and messy data.

>- Dirty data which has issues with its content is often called low-quality data and can include things like inaccurate data, corrupted data, and duplicate data.
>- Messy data has issues with its structure. It is often referred to as untidy.

>- Tidy data means each variable forms a column, each observation forms a row and each type of observational unit forms a table. Any other arrangement is messy which is the exact term that Hadley Wickham, the inventor of the tidy data format uses in his tidy data paper.



### What is the Difference Between Assessing and Exploring?

Data wrangling is about:

>- Gathering the right data
>- Assessing the data's quality and structure
>- Modifying the data to make it clean
However, your assessments and modification will not make your analysis, visualizations, or models better. It just makes them work.


### Exploratory Data Analysis (EDA) is about:

1. Exploring the data with simple visualizations that summarize the data's main characteristics
2. Augmenting the data, for example, removing outliers and feature engineering


### Assessing
In the context of this dataset, assessing is everything you just identified, like spotting:

- Missing HbA1c changes
- Poorly formatted zip codes (e.g., four digits and float data type instead of five digits and string or object data type)
- Multiple state formats (e.g., NY and New York)
- Incorrect patient height values (e.g., 27 inches instead of 72 inches)

Assessing is also identifying structural (tidiness) issues that make analysis difficult.

The discovery of these data quality and ensure that the analysis can be executed, which for this clinical trial data includes calculated average patient metrics (e.g. age, weight, height, and BMI) and calculating the confidence interval for the difference in HbA1c change means between Novodra and Auralin patients.

### Exploring
>- In the context of this dataset, exploring might include using summary statistics like count on the state column or mean on the weight column to see if patients from certain states or of certain weights are more likely to have diabetes, which we can use to exclude certain patients from the analysis and make it less biased

>- In the context of a clinical trial, exploring is less likely to happen given that clinical trials are expensive and include a lot of pre-planning. So exploring this dataset would likely happen before the clinical trial was conducted.


>- Data quality dimensions help guide your thought process while assessing and also cleaning. The four main data quality dimensions are:

1. Completeness: do we have all of the records that we should? Do we have missing records or not? Are there specific rows, columns, or cells missing?

2. Validity: we have the records, but they're not valid, i.e., they don't conform to a defined schema. A schema is a defined set of rules for data. These rules can be real-world constraints (e.g. negative height is impossible) and table-specific constraints (e.g. unique key constraints in tables).

3. Accuracy: inaccurate data is wrong data that is valid. It adheres to the defined schema, but it is still incorrect. Example: a patient's weight that is 5 lbs too heavy because the scale was faulty.

4. Consistency: inconsistent data is both valid and accurate, but there are multiple correct ways of referring to the same thing. Consistency, i.e., a standard format, in columns that represent the same data across tables and/or within tables is desired.

>- These are listed in decreasing order of severity, meaning that the dimension listed first, completeness, is the most important.
Regarding the other data quality research mentioned in the video, the additional dimensions are specific cases of these four dimensions listed above. Example: currency, defined as follows: the degree to which data is current with the world that it models. Currency can measure how up-to-date data is. Currency is a specific case of accuracy in data in the sense that out-of-date data is (usually) valid but wrong. In other words, our definition of accuracy can include currency.



#### Sources of Dirty Data
- `Dirty data` = `low quality data` = `content issues`

There are lots of sources of dirty data. Basically, anytime humans are involved, there's going to be dirty data. There are lots of ways in which we touch data we work with.

- We're going to have user entry errors.

- In some situations, we won't have any data coding standards, or where we do have standards they'll be poorly applied, causing problems in the resulting data

- We might have to integrate data where different schemas have been used for the same type of item.

- We'll have legacy data systems, where data wasn't coded when disc and memory constraints were much more restrictive than they are now. Over time systems evolve. Needs change, and data changes.

- Some of our data won't have the unique identifiers it should.

- Other data will be lost in transformation from one format to another.

- And then, of course, there's always programmer error.

- And finally, data might have been corrupted in transmission or storage by cosmic rays or other physical phenomenon. So hey, one that's not our fault.

>- Sources of Messy Data
Messy data = untidy data = structural issues

>- Messy data is usually the result of poor data planning. Or a lack of awareness of the benefits of tidy data. Fortunately, messy data is usually much more easily addressable than most of the sources of dirty data mentioned above.




Term Review

| Terms    | Definition |
| --- | --- |
| - Dirty Data	        |    Data that has issues with data content including missing data invalid data, inaccurate date or inconsistent data |
| - Messy Data	        |    Data that has issues with its structure (columns, rows or table) |
| - Accuracy		|    Quality dimension focused on whether the data is incorrect |
| - Completeness	|    Quality dimension focused on whether we have all of the records we should |
| - Consistency		|    Quality dimension focused on whether the data conforms to a standardized format |
| - Validity		|    Quality dimension focused on whether the data conforms to a defined schema |
| - Directed Visual Assessment	|  Systematically looking through each table of data in a Jupyter notebook or spreadsheet |
| -Non-directed Visual Assessment	|  Scrolling through the data looking for interesting and relevant issues | 


### Assess: Summary
Assessing is the second step in the data wrangling process:

- Gather
- Assess
- Clean

You can assess data for:

- Quality: issues with content. Low quality data is also known as dirty data.
- Tidiness: issues with structure that prevent easy analysis. Untidy data is also known as messy data. Tidy data requirements:
	- Each variable forms a column.
	- Each observation forms a row.
	- Each type of observational unit forms a table.
...using two types of assessment:

>- Visual assessment: scrolling through the data in your preferred software application (Google Sheets, Excel, a text editor, etc.).
>- Programmatic assessment: using code to view specific portions and summaries of the data (pandas' head, tail, and info methods, for example).



