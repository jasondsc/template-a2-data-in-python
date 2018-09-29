# Loading and accessing data in Python

We're interested in enabling reproducible statistical analyses; we're therefore going to focus on both accessing our data as well as executing statistical analyses programmatically. In this assignment, we'll work through accessing data in a standardized fashion using the [Python programming language](https://www.python.org/). 

### Why Python?
Although there are a [wide](https://julialang.org/) [variety](https://www.mathworks.com/products/matlab.html) of programming languages available for data analysis, we've chosen to focus on Python. We've made this choice since Python has several important characteristics:

* It's free and open source software (FOSS), meaning that it's accessible without a subscription plan
* It's a great general purpose scripting language, used in a wide variety of industries today
* It has a [strong ecosystem for scientific analyses](https://www.scipy.org/)

For statistics, the other very popular language to know is [R](https://www.r-project.org/)&mdash;I highly recommend you check it out, even though we won't be using it in this course. 

## How to get started
To get a working python environment, please install Miniconda into the computational [environment you set up in A1](https://github.com/reprocourse/template-a1-setup). Specifically, please make sure to install the Python 3.7 build as there are significant differences between the two Python versions; if you're interested, you can learn more about some of these [differences here](https://devopedia.org/python-2-vs-3). 

Once you have installed Miniconda, you will have access to a working Python environment. First, we'll be using `pip` &mdash;a python package management system&mdash; to install several packages we'll need to execute the assignment. From an open terminal, you can execute the following commands

```
pip ipython
pip numpy
pip pandas
```

Notice that these commands are executed outside of the Python environment! Now we can start Python using the following command:

```
ipython
```

## Accessing data
For this assignment, we'll be using the classic [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). We'll ask you to load the dataset and provide some descriptive statistics.
I've started the code for you in the associated [`descriptive_statistics.py`](https://github.com/reprocourse/template-a2-data-in-python/blob/master/descriptive_statistics.py) file.

## Calculating descriptive statistics
In your copy of the repository, please extend the [`descriptive_statistics.py`](https://github.com/reprocourse/template-a2-data-in-python/blob/master/descriptive_statistics.py) code to include calculating descriptive statistics in either `numpy` **or** `pandas`.

## How to submit
When you are ready to submit, [please open a pull request](https://help.github.com/articles/creating-a-pull-request/) on your copy of the repostiory with the modified  [`descriptive_statistics.py`](https://github.com/reprocourse/template-a2-data-in-python/blob/master/descriptive_statistics.py) code and the table below completed:

| Iris type | Mean Sepal Length| Standard Deviation of Sepal Length |
|-----------|:----------------:|:----------------------------------:|
| Setosa    | 5.005999999999999  | 0.348946987377739 | 
| Versicolor    | 5.936 | 0.5109833656783752 | 
| Virginica    | 6.587999999999998 | 0.6294886813914925 | 
