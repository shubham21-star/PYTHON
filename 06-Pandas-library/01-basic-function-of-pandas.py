# importing lib
import pandas as pd
import numpy as np

# method 1 : from a dictionary
df= pd.DataFrame({
    'Name' : ['Alice', 'Bob' , 'Carol'],
    'Age' : [25, 30, 22],
    'Score' : [88, 72, 95]
})

# method 2 : from csv file
df = pd.read_csv('student.csv')

# method 3 : from numpy array   
arr = np.array