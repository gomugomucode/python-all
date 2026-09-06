# import matplotlib.pyplot as plt
# import seaborn as sns

# # sns.defaullt_theme()

# #  here the  tips is the dataset which is used to plot the graph
# # #  it has  data like this 

# #      total_bill   tip     sex smoker   day    time  size
# # 0         16.99  1.01  Female     No   Sun  Dinner     2
# # 1         10.34  1.66    Male     No   Sun  Dinner     3
# # 2         21.01  3.50    Male     No   Sun  Dinner     3
# # 3         23.68  3.31    Male     No   Sun  Dinner     2
# # 4         24.59  3.61  Female     No   Sun  Dinner     4

# tips = sns.load_dataset("tips")

# # sns.relplot(data = tips, x = "total_bill", y = "tip")


# #  create  a scatter plot
# # sns.scatterplot(data = tips, x = "total_bill", y = "tip")


# #  create the histogram plot
# sns.histplot(data = tips, x = "total_bill", y = "tip")

# plt.show()

# # print(tips)




import seaborn as sns
import matplotlib.pyplot as plt

# Apply default styling
# sns.set_theme()

# Your code snippet
dots = sns.load_dataset("dots")


# sns.relplot(
#     data=dots, kind="line",
#     x="time", y="firing_rate", col="align",
#     hue="choice", size="coherence", style="choice",
#     facet_kws=dict(sharex=False),
# )


sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)


sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate",
    hue="align", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)



# Display the plot
plt.show()

# print(dots.head(20))
