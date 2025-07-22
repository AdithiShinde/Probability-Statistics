import pandas as pd
import matplotlib.pyplot as plt
netflix=pd.read_csv('C:/Users/shind/OneDrive/Desktop/p and s')
column2=netflix['show_id']
column8=netflix['release_year']
column9=netflix['rating']
column5=netflix['type']
summary=(netflix.groupby('type').size().to_frame('rating').reset_index())
plt.figure(figsize=(10,5))
width=0.9
plot=plt.pie(summary['rating'],labels=summary['type'],autopct='%1.1f%%')
plt.title('Netflix shows')
plt.show()