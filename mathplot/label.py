# # With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.

# import matplotlib.pyplot as plt
# import numpy as np

# xarray = np.array([1, 2, 3, 4, 5])
# yarray = np.array([2, 4, 6, 8, 10])

# plt.plot(xarray, yarray, marker='o', linestyle='--', color='g', label='y = 2x')

# # With Pyplot, you can use the title() function to set a title for the plot.
# plt.title('Line Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.show()



# # we  can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels.
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.show()