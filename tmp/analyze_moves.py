#%%
# import pandas as pd
# df30 = pd.read_csv("~/rubik_moves_30.csv", sep=";", index_col=0)
# df35 = pd.read_csv("~/rubik_moves_35.csv", sep=";", index_col=0)
# df = pd.concat((df30,df35), axis=1)

# new_cols = [str(x) for x in sorted([int(x) for x in df.columns.values])]
# df = df[new_cols]
# df.to_csv("~/rubik_moves_total.csv", sep=";")

#%%
import pandas as pd
#df = pd.read_csv("~/rubik_3x3_moves_total.csv", sep=";", index_col=0)
df = pd.read_csv("~/rubik_moves.csv", sep=";", index_col=0)
df_desc = df.describe()
df_desc.loc[["50%","mean","max"]].transpose().plot(grid=True)

#df[4].plot(kind='hist', bins=20, density=1, stacked=False)

