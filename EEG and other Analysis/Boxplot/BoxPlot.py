import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\Boxplot\Completion time.csv")

fx = sns.boxplot(x='Stage', y='Time', data=df, hue='Condition')

plt.show()