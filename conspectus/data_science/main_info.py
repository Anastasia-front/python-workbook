import sweetviz as sv
from pandas_profiling import ProfileReport

import seaborn as sns
import matplotlib.pyplot as plt

# Life cycle of a Data Science project

"""---------------------------------------------------------------------"""

# Data collection

'''
The first stage of the life cycle of a Data Science project is data collection. 
This step is important because the accuracy and reliability of any data analysis 
depends on the quality of the input data. Typically, data is collected from various sources 
such as databases, sensors, APIs, etc. Depending on the project, data 
can be in the form of structured or unstructured text, images, video or audio.
'''

"""---------------------------------------------------------------------"""

# Data cleaning and preparation

'''The data cleansing stage is one of the most important stages in the life cycle of a Data Science project. 
No matter how good a model we have, most depends on our dataset, and there is a good saying: garbage in, garbage out. 
Data cleansing means removing or correcting inaccuracies, errors, duplicates, missing values, or other incorrect data. 
At this stage, you can perform various operations, for example:


- Deduplication: Large datasets may contain duplicate records, which can skew the results. 
For example, the table may have User and Name columns, but each of them will store the same information - the user's name. 
Deduplication ensures data accuracy and reduces data volume.

- Removal of missing values: Missing values in data can occur for a variety of reasons, including input errors, 
refusal of study participants to answer certain questions, or unavailability of data. Missing values can be replaced by means or other imputed values.

- Encoding categorical data: Many data contain categorical data that must be encoded into numerical values for further processing. 
This can be done using different methods, such as one-hot encoding or label encoding.

- Data normalization: Data may contain values that differ by an order of magnitude, such as age and income. 
In order to ensure equal weights for all factors, the data can be normalized using various methods.

This list is not exhaustive, but describes the main problems you may encounter.
'''


"""---------------------------------------------------------------------"""


# Data exploration


'''
EDA (Exploratory Data Analysis) is a fundamental step in statistical modeling and machine learning projects. 
This process helps to understand the basic characteristics of the data before applying more complex algorithms.

The main goals of EDA:

- Determination of the main data characteristics: dataset size, data types (categorical, numerical, time), presence of missing values.

- Data Distribution Analysis: Studying data distribution helps to understand how data is distributed across different variables.

- Identifying correlations and dependencies between variables: Helps identify potential relationships between variables that may be important for modeling.

- Detection of anomalies (Outliers): detection of data that differs from others may indicate errors or special cases.

- Data visualization: using graphical representations to better understand data and its structure.
'''

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


# Tools for EDA:
'''
- Pandas: A Python library for data manipulation and analysis.
- Matplotlib: A Python library for creating static, animated plots and interactive visualizations in Python.
- Seaborn: A Python library based on Matplotlib for creating more attractive and informative statistical plots.
'''



# Example code for EDA:

# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# Loading the dataset

df = sns.load_dataset('iris')

# View the first rows of data

print(df.head())

# Basic statistical characteristics

print(df.describe())

# Check for missing values

print(df.isnull().sum())

# Visualization of the distribution of a variable

sns.histplot(df['sepal_length'], kde=True)
plt.show()

# Visualization of the relationship between variables

sns.pairplot(df, hue='species')
plt.show()

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


# Libraries for EDA automation

'''Automation of the EDA process is becoming increasingly popular thanks to the development of specialized libraries 
that allow to significantly reduce the time of data analysis. Here are three outstanding libraries that provide fast and efficient EDA:
'''

# 1. Pandas Profiling

'''Pandas Profiling is a Python library that allows you to generate an EDA report from a single command. 
It runs on top of the pandas library and provides a detailed report on each variable in the dataset, 
including information about data types, missing values, unique values, quantiles, distribution histograms, corelation and much more.
'''

# from pandas_profiling import ProfileReport
profile = ProfileReport(df, title="Report")
profile

'''
Features:

- Automatic analysis of data types.
- View statistics, including the number of unique values, missing data.
- Data visualization through histograms, correlation matrices, scatter plots, and more.
- Detection of duplicate rows.
'''

# 2. SweetViz

'''SweetViz is a data analysis tool focused on creating attractive visualizations for EDA reports. 
It generates detailed reports that include comparisons between data sets, analysis of the target variable, 
comparisons between data groups, and more.
'''


# import sweetviz as sv
analyze_report = sv.analyze(df)
analyze_report.show_html('report.html', open_browser=False)


'''
Features:

- Comparative analysis between different datasets.
- Automated reports with detailed analysis of the target variable.
- Visualization of associations between variables.
- Interactive reports that are easy to share with colleagues.
'''

"""---------------------------------------------------------------------"""


# Creation of a model

'''This is probably the most interesting, but also the most difficult part of the entire work of a Data Scientist. 
This is where the magic happens and it is only thanks to our data that we can learn to distinguish spam, 
predict the price of a house or unlock the phone with a touch or with our face.
'''

# https://towardsdatascience.com/5-steps-of-a-data-science-project-lifecycle-26c50372b492


'''
Again, before moving on to this step, keep in mind that the data cleaning and exploration step is equally important 
to building useful models. Therefore, do not rush to apply modeling, but pay attention to these stages.

There are several tasks in modeling. We can also train a model to perform a classification to distinguish 
between emails you have received as "Inbox" and "Spam" using logistic regression. We can also predict values 
using linear regression. We can also use modeling to cluster data to understand the logic behind these clusters. 
For example, we group e-commerce customers to understand their behavior on your website. This requires us 
to identify groups of data points with clustering algorithms such as k-means or hierarchical clustering.

Briefly, we use regression and prediction to predict future values, classification to identify, and clustering to group values.

To implement this stage, we already need to know the scikit-learn library (https://scikit-learn.org/stable/), as well as libraries for deep learning 
such as TensorFlow or PyTorch, in case of using a large number of data and more complex models. Also, we must 
be able to evaluate the performance of our model in order to understand which model is better, how it can be improved, etc. 
Accordingly, to evaluate the model, we need some metrics, such as RMSE, MAE or F1 score.
'''


"""---------------------------------------------------------------------"""


# Interpretation (Application)
'''
We are at the last stage of the Data Science project - interpretation of models and data. 
The predictive power of the model lies in its ability to generalize. 
How to explain a model depends on its ability to generalize future data that are currently unknown.

Data interpretation means presenting your data to a layperson in the field. 
We demonstrate results to answer the business questions we asked at the beginning of the project, 
along with actionable insights we found through our own Data Science, our data exploration process. 
This is the main job of a Data Scientist - to benefit the company by making some optimizations 
or getting some insights from the data. For example, offer the product that the user will buy, correctly apply targeted advertising, etc.

Actionable insight is a key outcome. (Дієвий інсайт є ключовим результатом)
We study how to repeat a positive result or prevent a negative result.

Additionally, you need to visualize your results according to your business question. 
It is important to present your results in a way that is useful to the organization, otherwise it will be pointless.

At this stage, only technical skills are not enough. One of the key skills you must have is the ability to tell a clear and effective story. 
If your presentation does not move your audience to action, it means that your communication was ineffective. 
Remember that you will be presenting to an audience without a technical background, so the way you communicate with your audience is key.
'''


"""---------------------------------------------------------------------"""


# Classification of machine learning algorithms
'''
At the stage of building the model, we mentioned some problems and algorithms that exist to solve them. 
For a better understanding of what algorithms actually exist, let's dive into the current classification of algorithms.

https://towardsdatascience.com/machine-learning-algorithms-in-laymans-terms-part-1-d0368d769a7b

'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Learning with a teacher
'''
Supervised learning is a type of machine learning in which the model learns on the basis of pre-marked (labeled) data. 
In other words, for each set of inputs, there is a correct answer that the model tries to predict. 
The model is trained on these marked data tp find patterns and make correct predictions for new, unknown data.

One of the examples of application of supervised learning is the task of classifying e-mail into "spam" or "other messages".
In this case, the model is built on the basis of pre-labeled data, which contains information about samples of spam and normal messages. 
Then, the model learns to recognize patterns and determine whether new messages are "spam" or not.

Another example is real estate price forecasting. The model can be trained on pre-labeled data that contains information about properties, 
features and their sale price. Then, the model learns to recognize the relationship between the characteristics and their price 
in order to predict the price for new houses (real estate).

In both examples, the model is trained on previously labeled data in order to predict correct responses for new, unknown data. 
Tutored learning allows you to create accurate predictions and classifications with a high level of confidence, making it useful 
for a wide range of tasks in different industries.
'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Learning without a teacher

'''
Unsupervised learning is one of the machine learning approaches that allows you to detect hidden dependencies in data 
without using labels or results. The main goal is to find structure in data and clustering, where algorithms identify 
groups of similar elements in a data set that do not have explicit labels.

For example, consider the problem of clustering, where we have a set of images and want to divide them into different groups. 
Instead, there is no information in the dataset about which object belongs to which group. Unsupervised learning algorithms 
such as k-means can be used to cluster images based on their similarity.

Another example is data dimensionality reduction, where we have a large dataset with many features and want to reduce 
the number of features for further analysis. In such a case, dimensionality reduction algorithms such as Principal Component Analysis (PCA) 
can be used to reduce the number of features while retaining as much information as possible.

In summary, unsupervised learning is an approach to machine learning that allows you to find structure in data 
without previously training on a sample of data. This opens up opportunities to discover new dependencies and patterns 
that can be useful in many areas such as recommendation, natural language processing, data analysis, and many others.
'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Recommender systems
'''
Recommender systems are software solutions that analyze data about users and subjects of interest in order to provide 
personalized recommendations to users. Such systems are used in various fields, including e-commerce, media, music, social networks, and more.

Recommender systems use two main approaches: collaborative and content-based. The collaborative approach is based on the history of the user's 
interaction with the system and the analysis of the commonality of these interactions with other users. 
A content-based approach uses information about the properties and characteristics of objects to compare with user preferences.

One example of a recommender system is Netflix. The system analyzes the user's viewing history, their preferences and movie ratings, 
and also analyzes data about the characteristics of the movie itself, such as genre, cast, director, etc. 
Based on this data, the system makes personalized recommendations to users.

Another example is Amazon. Amazon's recommendation system analyzes users' purchase history, their reviews and ratings of the products 
they have purchased. The system also analyzes the properties of the products to compare them with the user's preferences and find products 
that he may be interested in buying.

Recommender systems are an important tool for increasing user satisfaction and increasing company profits. 
They are used in various industries such as e-commerce, media, music, games and others.
'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Reinforcement learning (Навчання з підкріпленням)
'''
Reinforcement learning is one of the main subfields of machine learning, which consists in teaching an agent to interact with the environment 
by maximizing reward or minimizing punishment.

There are no right or wrong answers in reinforcement learning. Instead, the agent interacts with the environment and performs certain actions 
for which it receives rewards or punishments. The agent's goal is to learn a strategy that allows him to maximize his reward in the long run.

One example of the application of reinforcement learning is the game of Go. An agent (for example, a computer program) 
interacts with the environment (Go-board) and must make certain moves, for which it receives points that reflect its success. 
The goal of the agent is to learn how to play Go better in order to earn as many points as possible. 
Google's AlphaGo learned to play the game of Go and defeated one of the best players in the world.

Another example of the application of reinforcement learning is robots that perform various tasks. The robot interacts with the environment 
by performing certain actions and is rewarded or punished depending on how efficiently it performs the task.

Reinforcement learning is a rather complex process because the agent has to solve problems with a long-term perspective, 
where each step can influence subsequent behavior. However, it makes it possible to solve complex tasks for which
there is no simple solution or algorithm.
'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

# Neural networks (deep learning)

'''
Deep Learning is a subfield of machine learning that uses neural networks with many layers to automatically perform tasks 
such as image classification, speech recognition, and natural language processing. Deep learning is based on neural network technology 
that learns abstract characteristics of data by recognizing relationships between input data and output labels. It is widely used 
in many fields such as medicine, finance and others.

Depending on what kind of data we are working with, we have different specific neural networks that can be used more effectively in this task.'''

# An example of a convolutional neural network:
'''
Convolutional Neural Networks (CNN - Згорткові нейронні мережі) are a type of deep learning algorithm that specializes in processing 
mesh-structured data such as images, videos and audio. They are used to automatically process and analyze large amounts of data, 
allowing them to perform tasks such as object recognition in images, image classification, and other related tasks.

The basic idea behind CNN is that they use small filters to convolution an image and get the answers to each of those convolutions. 
Next, with the help of a subsampling (підвибіркa) (pooling) layer, the received answers are reduced, which allows to reduce 
the number of parameters and simplify calculations. Application of these operations allows CNN to recognize objects in images 
with high accuracy and efficiency.

Examples of applications of CNN are image classification, face recognition, motion tracking, and speech recognition. 
In particular, they are widely used in computer vision, recommender systems, robotics, and other areas related to image and video data processing.'''

# An example of a recurrent neural network:
'''
Recurrent neural networks (RNN) are a type of neural network that can analyze sequences of data where each element 
is interconnected with previous elements of the sequence.

One of the main features of RNN is that they store state (memory) from previous input elements and use it to make predictions 
for the next element. This allows them to take context into account, which helps in more accurate forecasting.

RNN are commonly used to work with data sequences such as speech, time series, music. They find applications in various fields, 
including machine translation, speech recognition, text generation, time series forecasting, and more.

One of the most well-known examples of RNN is Long Short-Term Memory (LSTM), which is a special type of RNN. 
It can store information long-term and avoid the problem of missing gradients, which allows it to be very efficient 
in working with sequential data. LSTM is used for a variety of tasks including text autocompletion, text compression, music generation, and more.
'''

"""---------------------------------------------------------------------"""

# Work environment

'''
In addition to the fact that we will be working in the Python programming language environment, 
Data Scientists are comfortable using Jupyter Notebook or Google Colab, rather than a more familiar IDE, such as PyCharm. 
And there are several reasons for this:

- both of these tools provide the ability to execute the code step by step and save and view the results of each step individually. 
This makes it easy to understand what's going on in the code, and to debug and improve the models;

- Jupyter Notebook and Google Colab support many machine learning libraries and frameworks, which greatly simplifies the development 
and training of models. In addition, both tools have the ability to save and reload the state of models, which saves time and effort 
in debugging and optimizing models;

- these tools are free and easily accessible from any device with an internet connection. 
It makes it possible to easily share results and collaborate with colleagues;

- you can also use Jupyter Notebook on remote servers, for example using the SageMaker tool from AWS.


So, Jupyter Notebook and Google Colab are powerful tools for Data Scientists to quickly and efficiently develop, 
train, and debug machine learning models.
'''
"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


# Installation
'''If Google Colab does not require any additional configuration or installation from us, we can easily use it from our disk, 
like a Google document or spreadsheet, we must additionally install this tool for a laptop. If you already have Python installed, 
you can easily install the laptop with pip:
'''

command='pip install notebook'
# and run it accordingly with the following command:
command='jupyter notebook'

'''Another way to install is to use Anaconda. It is a free, open source distribution of Python that includes tools for scientific computing 
and data analysis. It contains more than 1,500 packages, including scientific libraries such as NumPy, pandas, SciPy, scikit-learn,
 and TensorFlow, as well as data visualization tools such as Matplotlib.

Anaconda comes with its own package manager that makes it easy to install, update, and manage packages, as well as additional tools 
like Jupyter Notebook, Spyder, and JupyterLab.

Therefore, installing Anaconda can immediately provide us with all the necessary tools.
'''

"""---------------------------------------------------------------------"""

# Additional materials
'''
5 steps in the life cycle of a Data Science project 
(https://towardsdatascience.com/machine-learning-algorithms-in-laymans-terms-part-1-d0368d769a7b)
Learning with a teacher and without a teacher
article (https://www.ibm.com/blog/supervised-vs-unsupervised-learning/) and video (https://www.youtube.com/watch?v=W01tIRP_Rqs)
Video overview of the main work environments for Data Scientist (https://www.youtube.com/watch?v=5pf0_bpNbkw)
'''