import pandas as pd
data = pd.read_csv('world-data-2023.csv')
selected_column = data[['Country','Birth Rate']]
print(selected_column)
filtered_data = data[data['Birth Rate']>30]
print(filtered_data)                       
data1 = pd.read_csv('world-data-2023.csv')
data2 = pd.read_csv('world-data-2023.csv')
merged_data = pd.merge(data1,data2,on='Country')
print(merged_data)
data.fillna(0, inplace= True )
print(data)

count = 2
for col in data.columns:
    print(f"{count}:{col}")
    count += 7
for col in data.shape:
    print(f"{count}:{col}")
    count += 7   
for col in data.head:
    print(f"{count}:{col}")
    count += 7    
for col in data.describe:
    print(f"{count}:{col}")
    count += 7   
for col in data.shape(3):
    print(f"{count}:{col}")
    count += 7   
for col in data.axes:
    print(f"{count}:{col}")
    count += 7  
for col in data.tail(7):
    print(f"{count}:{col}")
    count += 9
for col in data.rename_axis:
    print(f"{count}:{col}")
    count += 7
for col in data.aggregate:
    print(f"{count}:{col}")
    count += 7
for col in data.pivot_table:
    print(f"{count}:{col}")
    count += 7  
for col in data.reindex:
    print(f"{count}:{col}")
    count += 7 
for col in data.expanding:
    print(f"{count}:{col}")
    count += 7   
for col in data.iloc:
    print(f"{count}:{col}")
    count += 7 
for col in data.pivot:
    print(f"{count}:{col}")
    count += 7  
for col in data.is_unique:
    print(f"{count}:{col}")
    count += 7



import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')
plt.show()

categories = [10,7,5]
values = ['A','B','C']
plt.bar(categories,values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.scatter(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

plt.plot(x,y,linestyle='--',marker='o',color='purple',label='Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Graph')
plt.legend()
plt.show()


categories = ['A','B','C']
values1 = [4,7,9]
values2 = [2,5,8]
plt.bar(categories,values1,label='Values 1')
plt.bar(categories,values2,label='Values 2',bottom=values1)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()


np.random.seed(43)
data = np.random.randn(1000)
plt.hist(data,bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()    