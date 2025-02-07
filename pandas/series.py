# pandas is library which is used data analysis, manipulation and visualization.It provides two primary data structures.

import pandas as pd

# series is like a column in spreadsheet, consists of data and index
data = pd.Series([10,20,30,40])
print(data)

# custom Index

data = pd.Series([10, 20, 30, 40], index = ['a', 'b', 'c', 'd'])
print(data)
