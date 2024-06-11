# Shreya Shravini
# shreyashravini
# Your github user id here

"""
INSTRUCTIONS

Available: May 2nd

Due: May 12th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework3.py file
(b) Must homework3.py commit to your clone of the GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory
(e) Must NOT modify the original data in any way

Failure to do any of these will result in the loss of points
"""

"""
QUESTION 1

In this question, you'll be replicating the graph from Lecture 14, slide 5
which shows the population of Europe from 0 AD to the present day in both
the linear and the log scale. You can find the data in population.csv, and the
variable names are self-explanatory.

Open this data and replicate the graph. 

Clarification: You are not required to replicate the y-axis of the right hand
side graph; leaving it as log values is fine!

Clarification: You are not required to save the figure

Hints: Note that...

- The numpy function .log() can be used to convert a column into logs
- It is a single figure with two subplots, one on the left and the other on
the right
- The graph only covers the period after 0 AD
- The graph only covers Europe
- The figure in the slides is 11 inches by 6 inches
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
df_pop = pd.read_csv("C:/Users/Shreya Work/OneDrive/Documents/GitHub/population.csv")

# Filter data for Europe and after 0 AD
df_europe = df_pop[(df_pop["Entity"] == "Europe") & (df_pop["Year"] >= 0)]

# Calculate log values and adjust population
df_europe["Log_Pop"] = np.log(df_europe["Population (historical estimates)"])
df_europe["Adj_Pop"] = df_europe["Population (historical estimates)"] / 1000000

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2)

# Plot population on linear scale
ax1.plot(df_europe["Year"], df_europe["Adj_Pop"], "b-")
ax1.set_ylabel("Population (in millions)")
ax1.set_xlabel("Year (AD)")
ax1.set_title("Population of Europe from 0 BCE in millions")

# Plot population on log scale
ax2.plot(df_europe["Year"], df_europe["Log_Pop"], "b-")
ax2.set_yscale("log")
ax2.set_ylabel("Population (log, in millions)")
ax2.set_xlabel("Year (AD)")
ax2.set_title("Population of Europe from 0 BCE in millions (log scale)")

# Layout adjustments
ax1.yaxis.set_major_formatter('{x:,.0f}')
ax1.tick_params(axis="y", size=0)
ax2.tick_params(axis="y", size=0)
fig.tight_layout()
fig.set_size_inches(11, 6, forward=True)

# Show the plot
plt.show()



"""
QUESTION 2

A country's "capital stock" is the value of its' physical capital, which includes the 
stock of equipment, buildings, and other durable goods used in the production 
of goods and services. Macroeconomists seem to conisder it important to have 
public policies that encourage the growth of capital stock. Why is that?

In this exercise we will look at the relationship between capital stock and 
GDP. You can find data from the IMF in "capitalstock.csv" and documentation in
"capitalstock documentation.txt".

In this exercise we will only be using the variables that are demarcated in
thousands of 2017 international dollars to adjust for variation in the value 
of nominal national currency. Hint: These are the the variables that 
end in _rppp.

1. Open the dataset capitalstock.csv and limit the dataframe to only 
observations from 2018

2. Construct a variable called "capital_stock" that is the sum of the general
government capital stock and private capital stock. Drop 
observations where the value of capital stock is 0 or missing. (We will be 
ignoring public-private partnership capital stock for the purpose of t
his exercise.)

3. Create a scatterplot showing the relationship between log GDP and log
capital stock. Put capital stock on the y-axis. Add the line of best 
fit. Add labels where appropriate and make any cosmetic adjustments you want.

(Note: Does this graph suggest that macroeconomists are correct to consider 
 capital stock important? You don't have to answer this question - it's 
 merely for your own edification.)

4. Estimate a model of the relationship between the log of GDP 
and the log of capital stock using OLS. GDP is the dependent 
variable. Print a table showing the details of your model and, using comments, 
interpret the coefficient on capital stock. 

Hint: when using the scatter() method that belongs to axes objects, the alpha
option can be used to make the markers transparent. s is the option that
controls size
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.regression.linear_model import OLS

# Read the dataset
df_cap = pd.read_csv("capitalstock.csv")

# Limit observations to 2018
df_cap = df_cap[df_cap["year"] == 2018]

# Create the capital stock variable
df_cap["capital_stock"] = df_cap["kgov_n"] + df_cap["kpriv_n"]

# Drop observations with missing or zero capital stock values
df_filt_cap = df_cap.dropna(subset=["capital_stock", "GDP_rppp"])
df_filt_cap = df_filt_cap[(df_filt_cap["capital_stock"] > 0) & (~df_filt_cap["capital_stock"].isna())]

# Create scatterplot with log transformation
df_filt_cap["log_GDP"] = np.log(df_filt_cap["GDP_rppp"])
df_filt_cap["log_capital_stock"] = np.log(df_filt_cap["capital_stock"])

# Remove infinite values from log transformation
df_filt_cap = df_filt_cap[~df_filt_cap["log_capital_stock"].isinf()]

# Scatter plot with line of best fit
x = df_filt_cap["log_GDP"]
y = df_filt_cap["log_capital_stock"]
m, b = np.polyfit(x, y, deg=1)
gen_line = np.poly1d((m, b))

fig, ax = plt.subplots()
ax.scatter(df_filt_cap["log_GDP"], df_filt_cap["log_capital_stock"], alpha=0.6)
ax.set_title("GDP Growth (log scale) by Capital Stock Growth (log scale, 2017 $ value)")
ax.plot(x, gen_line(x), "b-", linewidth=2)

# OLS Model
df_filt_cap["intercept"] = np.ones(len(df_filt_cap))
model = OLS(endog=df_filt_cap["log_GDP"], exog=df_filt_cap[["intercept", "log_capital_stock"]])
results = model.fit()
print(results.summary())

plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.regression.linear_model import OLS

# Read the dataset
df_cap = pd.read_csv("capitalstock.csv")

# Limit observations to 2018
df_cap = df_cap[df_cap["year"] == 2018]

# Create the capital stock variable
df_cap["capital_stock"] = df_cap["kgov_n"] + df_cap["kpriv_n"]

# Drop observations with missing or zero capital stock values
df_filt_cap = df_cap.dropna(subset=["capital_stock", "GDP_rppp"])
df_filt_cap = df_filt_cap[(df_filt_cap["capital_stock"] > 0) & (~df_filt_cap["capital_stock"].isna())]

# Create scatterplot with log transformation
df_filt_cap["log_GDP"] = np.log(df_filt_cap["GDP_rppp"])
df_filt_cap["log_capital_stock"] = np.log(df_filt_cap["capital_stock"])

# Remove infinite values from log transformation
df_filt_cap = df_filt_cap[~df_filt_cap["log_capital_stock"].isinf()]

# Scatter plot with line of best fit
x = df_filt_cap["log_GDP"]
y = df_filt_cap["log_capital_stock"]
m, b = np.polyfit(x, y, deg=1)
gen_line = np.poly1d((m, b))

fig, ax = plt.subplots()
ax.scatter(df_filt_cap["log_GDP"], df_filt_cap["log_capital_stock"], alpha=0.6)
ax.set_title("GDP Growth (log scale) by Capital Stock Growth (log scale, 2017 $ value)")
ax.plot(x, gen_line(x), "b-", linewidth=2)

# OLS Model
df_filt_cap["intercept"] = np.ones(len(df_filt_cap))
model = OLS(endog=df_filt_cap["log_GDP"], exog=df_filt_cap[["intercept", "log_capital_stock"]])
results = model.fit()
print(results.summary())

plt.show()

"""
The regression results show a coefficient of 0.5271 for the relationship between the 
log of capital stock and GDP. This implies that a one-unit increase in log capital 
stock leads to a 0.5271-unit increase in log GDP. The high significance level, indicated 
by the low p-value, suggests a robust relationship between the two variables. 
Additionally, the high R-squared value of 0.852 indicates that about 85.2% of the 
variation in GDP can be explained by variation in capital stock. This underscores the 
importance of capital stock as a predictor of GDP growth.
"""
