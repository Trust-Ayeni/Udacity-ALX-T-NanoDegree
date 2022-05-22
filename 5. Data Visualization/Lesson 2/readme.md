# Design of Visualizations

## Lesson Overview
Before making visualizations, it is important to understand how visualizations are designed, and what makes a visualization "good" or "bad." Explanatory visualizations utilize specific design principles in order to clearly and accurately convey findings. Design principles can also be useful in the exploratory phase of the data analysis process.

In this lesson, you'll learn about the following topics related to the design of data visualizations.

- What makes a bad visual?
- Levels of measurement and types of data
- Continuous vs. discrete data
- Identifying data types
- What experts say about visual encodings
- Chart Junk
- Data-to-ink ratio
- Design integrity
- Using color and designing for color blindness
- Shape, size, and other tools

## Course Outline
You have already completed the first lesson. Let's see where we are in the overall course:

>- Data Visualization in Data Analysis
>- **Design of Visualizations**
>- Univariate Exploration of Data
>- Bivariate Exploration of Data
>- Multivariate Exploration of Data
>- Explanatory Visualizations
>- Visualization Case Study
>- Project - Communicate Data Findings


Visuals can be bad if they:

- Don't convey the desired message.
- Are misleading.

This seems straightforward, but often visuals are created that do one or both of these unintentionally. There is an entire book that was published aimed at misleading visuals: [How to Lie with Statistics](http://faculty.neu.edu.cn/cc/zhangyf/papers/How-to-Lie-with-Statistics.pdf).

## Levels of Measurement & Types of Data

### The Four Levels of Measurement
In order to choose an appropriate plot type or method of analysis for your data, you need to understand the types of data you have. One common method divides the data into four levels of measurement:

- **Qualitative** or categorical types (non-numeric types)
1. **Nominal data**: pure labels without inherent order (no label is intrinsically greater or less than any other)
2. **Ordinal data**: labels with an intrinsic order or ranking (comparison operations can be made between values, but the magnitude of differences are not be well-defined) 

- **Quantitative** or numeric types
3. **Interval data**: numeric values where absolute differences are meaningful (addition and subtraction operations can be made)
4. **Ratio data**: numeric values where relative differences are meaningful (multiplication and division operations can be made)

All quantitative-type variables also come in one of two varieties: **discrete and continuous.**
>- **Discrete** quantitative variables can only take on a specific set values at some maximum level of precision.
>- **Continuous** quantitative variables can (hypothetically) take on values to any level of precision.

Distinguishing between continuous and discrete can be a little tricky – a rule of thumb is if there are few levels, and values can't be subdivided into further units, then it's discrete. Otherwise, it's continuous. If you have a scale that can only take natural number values between 1 and 5, that's discrete. A quantity that can be measured to two digits, e.g. 2.72, is best characterized as continuous, since we might hypothetically be able to measure to even more digits, e.g. 2.718. A tricky case like test scores measured between 0 and 100 can only be divided down to single integers, making it initially seem discrete. But since there are so many values, such a feature is usually considered as continuous.

When exploring your data, the most important thing to consider first is whether your data is qualitative or quantitative. In later lessons, you will see how this distinction impacts your choice of plots.

### Likert Scale
One form of data you might encounter is response data to a **Likert scale** like the ones below.





