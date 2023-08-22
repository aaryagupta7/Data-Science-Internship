import tkinter as tk
from tkinter import ttk
import numpy as np

#Pre-trained model parameters 
model_params = np.array([-0.02036573, 0.16518516, -0.00198818, 0.00122779, -0.00015017, 0.08780686, 0.69113173])
intercept = -5.18267154

#Sigmoid function for logistic regression
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#Predict diabetes outcome based on health metrics
def predict_diabetes(input_values):
    z = np.dot(input_values, model_params) + intercept
    prediction = sigmoid(z)
    return 1 if prediction > 0.5 else 0

#GUI setup
root = tk.Tk()
root.title('Diabetes Prediction')

#Health Metrics input fields
input_labels = ['Glucose', 'Blood Pressure', 'Skin Thickness', 'Insulin', 'BMI', 'Diabetes Pedigree', 'Age']
input_entries = [ttk.Entry(root) for _ in input_labels]

for label, entry in zip(input_labels, input_entries):
    label_widget = ttk.Label(root, text=label)
    label_widget.pack()
    entry.pack()

#Prediction result label
result_label = ttk.Label(root,text='')
result_label.pack()

def perform_prediction():
    input_values = [float(entry.get()) for entry in input_entries]
    predicted_class = predict_diabetes(input_values)
    prediction_text = 'Likely Diabetic' if predicted_class == 1 else 'Likely Healthy'
    result_label.config(text=prediction_text)

#Prediction Button    
predict_button = ttk.Button(root, text='Predict Diabetes',command=perform_prediction)
predict_button.pack()

#Exit Button
exit_button = ttk.Button(root, text='Exit', command=root.destroy)
exit_button.pack()

root.mainloop()
