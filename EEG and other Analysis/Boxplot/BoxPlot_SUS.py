import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv(r"C:\Users\User\Desktop\MU\4th year\SMART\Capstone\Analysis\Boxplot\SUS.csv")

fx = sns.boxplot(x='Assesment', y='Score', data=df, hue='Condition')

plt.show()