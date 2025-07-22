import pandas as pd
import matplotlib.pyplot as plt
netflix = pd.read_csv('C:/Users/shind/OneDrive/Desktop/netflix_titles.csv')
print(netflix)
column = netflix['show_id']
column2 = netflix['release_year']
print(column.head(6), column2.head(6))
summary = netflix.groupby('type').size().reset_index(name='count')
plt.figure(figsize=(10, 5))
colors = ['green', 'yellow', 'black', 'red', 'blue']
plt.bar(summary['type'], summary['count'], color=colors)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Count of Netflix Titles by Type')
plt.show()