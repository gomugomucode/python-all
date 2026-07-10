import pandas as pd

df = pd.read_csv('data.csv' , index_col = 'Name')

# tall_pokemon = df[df['Height'] > 2.0 ]

tall_pokemon = df.loc[df['Height'] > 2.0 ,["Height"]]
print("Tall Pokemon:")
print(tall_pokemon)