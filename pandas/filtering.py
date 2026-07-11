# import pandas as pd

# df = pd.read_csv('data.csv' , index_col = 'Name' )

# tall_pokemon = df[df['Height'] > 2.0 ]


# # in this fies the df[height'] > 2.0 is a boolean series which is used to filter the rows of the dataframe where the height is greater than 2.0 and then we are selecting only the height column using [["Height"]]
# tall_pokemon = df.loc[df['Height'] > 2.0 ,["Height"]]
# print("Tall Pokemon:")
# print(tall_pokemon)




# heavy_pokemon = df.loc[df['Weight'] > 100.0 ,["Weight"]]
# print("Heavy Pokemon:")
# print(heavy_pokemon)


# using the or(|) operator

# in thsi the isin tool is used to check the multiple co0lums of the colun type1


# import pandas as pd

# df = pd.read_csv('data.csv'  )

# #  CLEANING STEP: Remove all accidental spaces from column names
# df.columns = df.columns.str.strip()

# # . Double-check our hard work
# print("Cleaned Columns:", df.columns.tolist())

# # water_poke = df.loc[df['Type 1'].isin(['Water', 'Ice']) ]
# water_poke =  df[df['Type1'].isin(['Water', 'Ice'])]

# print("Water and Ice Type Pokemon:")
# print(water_poke)

# usin and (&) operator


import pandas as pd

df = pd.read_csv('data.csv'  )

# Strip out all the messy leading/trailing spaces from the column headers
df.columns = df.columns.str.strip()

# CLEAN THE DATA: Strip spaces from the type columns
df['Type1'] = df['Type1'].str.strip()
df['Type2'] = df['Type2'].str.strip()


ff_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]

print("Fire and Flying Type Pokemon:")
print(ff_pokemon)
