import pandas as pd
df=pd.read_excel('data.xlsx')
print("First few rows")
print(df.head())
print("\n Summary statistics:")
print(df.describe())
filtered_data=df[df['Age']>30]
print("\n Filtered data(Age>30):")
print(filtered_data)
sorted_data=df.sort_values(by='salary',ascending=False)
print("\nSorted data(by Salary):")
print(sorted_data)
df['Bonus']=df['salary']*0.1
print("\n Data with new column(Bonus)")
print(df)
df.to_excel('Output.xlsx',index=False)
print("\n Data written to output.xlsx")
