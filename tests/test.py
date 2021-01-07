import pandas as pd

path = '../data/current_data.csv'
data = pd.read_csv(path, sep=';')
data.columns = ['Position', 'Opening', 'Closing', '0', '0']
x = pd.to_numeric(data['Position'].to_numpy())
y_open = data['Opening'].to_numpy()
y_close = data['Closing'].to_numpy()

print(type(x[1]))
