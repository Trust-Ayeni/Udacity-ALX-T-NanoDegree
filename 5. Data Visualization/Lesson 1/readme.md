# Data Visualization in Data Analysis

## Course Prerequisite
To successfully complete and fully engage in the entire coursework, you should have the following skills before start:

>- You can use Anaconda to manage packages and environments for use with Python
>- You can use Jupyter notebook to combine explanatory text, math equations, code, and visualizations in one sharable document
>- You have basic Python skill: use NumPy and Pandas to wrangle, explore, analyze, and visualize data
>- You are familiar with basic statistics and probability concepts such as linear regression, the normal distribution


## Motivation for Data Visualization

### Summary Statistics vs. Visualizations
Summary statistics like the mean and standard deviation can be great for attempting to quickly understand aspects of a dataset, but they can also be misleading if you make too many assumptions about how the data distribution looks.

Anscombe's Quartet Example
Consider we have the following four datasets of x, y pairs. You can download the data using the button below. A link to a Google Sheet with the data is also available [here](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fs3.amazonaws.com%2Fvideo.udacity-data.com%2Ftopher%2F2018%2FSeptember%2F5b982e04_anscombes-quartet%2Fanscombes-quartet.xlsx&wdOrigin=BROWSELINK)
or [here](https://docs.google.com/spreadsheets/d/17Ec80nOP79w4qHIQhX8FXAGOpUhkU89Do9sEZP2Xgkg/edit#gid=0)

### Beyond Anscombe's Quartet
More recently, [Alberto Cairo](http://albertocairo.com/) created the [Datasaurus](https://www.autodesk.com/research/publications/same-stats-different-graphs) dataset, 
which is **amazingly insightful and artistic** but is built on the same idea that you just discovered. 
You can find the full dataset and the visualizations on the **Datasaurus** link.

#### Supporting Materials
[Alberto Cairo](https://video.udacity-data.com/topher/2019/November/5dc49f25_albertocairo.com/albertocairo.com.pdf)

[Datasaurus dataset](https://video.udacity-data.com/topher/2019/November/5dc49fcf_samestats-differentgraphs/samestats-differentgraphs.pdf)


### Exploratory vs. Explanatory Analyses
There are two main reasons for creating visuals using data:

- Exploratory analysis is done when you are searching for insights. These visualizations don't need to be perfect. You are using plots to find insights, but they don't need to be aesthetically appealing. You are the consumer of these plots, and you need to be able to find the answer to your questions from these plots.
- Explanatory analysis is done when you are providing your results for others. These visualizations need to provide you the emphasis necessary to convey your message. They should be accurate, insightful, and visually appealing.
The five steps of the data analysis process:

>- Extract - Obtain the data from a spreadsheet, SQL, the web, etc.
>- Clean - Here, we could use exploratory visuals.
>- Explore - Here, we use exploratory visuals.
>- Analyze - Here, we might use either exploratory or explanatory visuals.
>- Share - Here is where explanatory visuals live.

## Python Data Visualization Libraries
In this course, you will make use of the following libraries for creating data visualizations:

- Matplotlib: a versatile library for visualizations, but it can take some coding effort to put together common visualizations.
- Seaborn: built on top of matplotlib, adds a number of functions to make common statistical visualizations easier to generate.
- pandas: while this library includes some convenient methods for visualizing data that hook into matplotlib, we'll mainly use it for its main purpose as a general tool for working with data.

All together, these libraries will allow you to visualize data in a balance of productivity and flexibility for both exploratory and explanatory analyses.

### A Quick Note about Library Versions
Some of the things you see in this course might not work the same depending on which version of the Python packages you have. For clarity, as of August 2018, here are the library versions that were used to create the course materials:

>- NumPy: Workspaces use v1.12.1, content created with v1.14.0
>- pandas: Workspaces use v0.20.3, content created with v0.22.0
>- Matplotlib: Workspaces use v2.1.0, content created with v2.1.2
>- Seaborn: Workspaces and content both created with v0.8.1












