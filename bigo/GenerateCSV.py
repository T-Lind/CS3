import pandas as pd
import random


max_val = 2_147_483_647
num_items = 10_000_000

data = pd.DataFrame([[random.randint(-max_val, max_val)] for _ in range(num_items)])
data.to_csv('numerical_data.csv', mode='a', index=False, header=False)
