import pandas as pd

data = pd.read_csv('IRIS.csv')

selected_columns = data[['sepal_length','sepal_width']]
print(selected_columns)

filtered_data = data[data['petal_length']>6]
print(filtered_data)

grouped_data = data.groupby('sepal_length')['sepal_width'].sum()
print(grouped_data)    

data1 = data[['petal_length','petal_width','species']]   
data2 = data[['sepal_length','sepal_width','species']]

print(data1)
print(data2)

merged_data = pd.merge(data1,data2,on='species')
print(merged_data)

data.fillna(0, inplace=True)
print(data)

def process_value(value):
    processed_value = value * 2
    return processed_value

data['processed_column'] = data['sepal_length'].apply(process_value)
print(data)

pivot_table = pd.pivot_table(data, values='sepal_length',
                            index='sepal_width', columns='species')
print(pivot_table)

data['date_time'] = pd.to_datetime(data['sepal_length'])
data.set_index('date_time',inplace=True)
resampled_data = data.resample('M').sum()
print(resampled_data)


import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)

arr = np.random.random((3,3))
print(arr)

arr1 = np.array([2,3,4])
arr2 = np.array([6,7,8])
result = arr1 + arr2
print(result)

data = np.array([[1,2],[3,4], [5,6]])
sum_along_rows = np.sum(data, axis=0)
sum_along_columns = np.sum(data, axis=1)
print(sum_along_rows)
print(sum_along_columns)

data = np.array([1,2,3,4,5])
print(data[1])
mask = data > 2
filtered_data = data[mask]
print(filtered_data)

data = np.array([1,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,5])
unique_elements = np.unique(data)
element_counts = np.bincount(data)
print(unique_elements)
print(element_counts)

x = np.array([1,2,3,4,5])
y = np.array([2,4,5,6,4])
coefficients = np.polyfit(x,y,1)
slope, intercept = coefficients
print("Slope:",slope)
print("Intercept:",intercept)