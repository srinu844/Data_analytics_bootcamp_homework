import scipy.stats as st
from scipy.stats import linregress
import matplotlib.pyplot as plt

def linear_regress(x_values,y_values):
    correlation = st.pearsonr(x_values, y_values)
    print(f"The correlation between both factors is {round(correlation[0],2)}")
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    regress_values = x_values * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    plt.annotate(line_eq,(6,10),fontsize=15,color="black")
    plt.scatter(x_values,y_values,marker = 'o',edgecolors ='red',title = )
    plt.plot(x_values,regress_values,"r-",color = 'blue')
    print(f"The r-squared is: {rvalue}")
    plt.show()