# Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

data.head()

print(data.head())
