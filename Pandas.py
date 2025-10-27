import pandas as pd


data = {
    'Name': ['saniya', 'Bharat', 'Mane', 'Shubham', 'Shubhangi'],
    'Age': [20, 47, 2, 24, 43],
    'Salary': [50000, 54000, 46000, 61000, 58000]
}
df = pd.DataFrame(data)
print("1. Original DataFrame:\n", df)


print("\n2. Head of DataFrame:\n", df.head(3))


print("\n3. Info of DataFrame:")
print(df.info())


print("\n4. Describe DataFrame:\n", df.describe())


print("\n5. Select 'Name' column:\n", df['Name'])


print("\n6. Filter Age > 25:\n", df[df['Age'] > 25])


df['Bonus'] = df['Salary'] * 0.10
print("\n7. New Column 'Bonus' Added:\n", df)


sorted_df = df.sort_values(by='Salary', ascending=False)
print("\n8. Sorted by Salary (Descending):\n", sorted_df)


grouped = df.groupby('Age')['Salary'].mean()
print("\n9. GroupBy Age (Average Salary):\n", grouped)


df.to_csv('employees.csv', index=False)
print("\n10. DataFrame saved to 'employees.csv'")
