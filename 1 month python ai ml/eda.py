# # EDA  = Exploratory Data Analysis


from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_csv('.csv')

encoder = LabelEncoder()

df.target = encoder.fit_transform(df.target)




import matplotlib.pyplot as plt
plt.pie(df['Type1'].value_counts(), labels=df['Type1'].value_counts().index, autopct='%1.1f%%')
plt.title('Distribution of Type1')
plt.show()