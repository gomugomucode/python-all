# # import matplotlib

# # print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np



# # fig, ax = plt.subplots()             # Create a figure containing a single Axes.
# # ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
# # plt.show()                           # Show the figure.


# # fig = plt.figure()             # an empty figure with no Axes
# # fig, ax = plt.subplots()       # a figure with a single Axes
# # fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# # # a figure with one Axes on the left, and two on the right:
# # fig, axs = plt.subplot_mosaic([['left', 'right_top'],
# #                                ['left', 'right_bottom']])

# # plt.show()

# # np.random.seed(19680801)  # seed the random number generator.
# # data = {'a': np.arange(50),
# #         'c': np.random.randint(0, 50, 50),
# #         'd': np.random.randn(50)}
# # data['b'] = data['a'] + 10 * np.random.randn(50)
# # data['d'] = np.abs(data['d']) * 100

# # fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# # ax.scatter('a', 'b', c='c', s='d', data=data)
# # ax.set_xlabel('entry a')
# # ax.set_ylabel('entry b')
# # plt.show()





# # matplotlib  pyplot


# import matplotlib.pyplot as plt
# import numpy as np

# # creating the numpy array containing the horizontal and verticla points

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# # plotting the points using the plot()

# # plot function is used to draw the line between two points 

# # plt.plot(xpoints, ypoints)   

# # if u  want to draw the axis not the line in the graph or plot then pass 'o' in the plot function  

# # Draws only circles at (0, 0) and (6, 250) without a connecting line
# plt.plot(xpoints, ypoints, 'o')



# # if u Want both the line and the dots in the graph or plot then pass 'o' in the plot function  
# # You can combine a marker 'o' with a line '-' to get both:

# # Draws both the dots and the line connecting them
# # plt.plot(xpoints, ypoints, marker='o')

# # If you want to change the appearance of the line and the marker, you can use the fmt argument:
# plt.plot(xpoints, ypoints, 'o:r')

# plt.show()



# plotting multiple points in a graph or plot


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()


# import matplotlib.pyplot as plt 
# import numpy as np  

# ypoints = np.array([3, 8, 1, 10])  
# plt.plot(ypoints, marker = 'o') 
# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# # The 'o:r' format string specifies that the points should be marked with circles ('o'), connected by a red line (':r').
# # here the 'o' is for the marker, ':' is for the line style (dashed), and 'r' is for the color red.

# # plt.plot(ypoints, 'o:r')

# plt.plot(ypoints, '*:r')
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# xarray = np.array([1, 2, 3, 4, 5])
# yarray = np.array([2, 4, 6, 8, 10])

# plt.plot(xarray, yarray, marker='o', linestyle='--', color='g', label='y = 2x')
# plt.title('Line Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

# ms = marker size

plt.plot(ypoints, marker = 'o', ms = 20)


#  for the marker color we can use mec = marker edge color

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')


# we can use marker face color  to set the color inside the edge of the markers
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')


plt.show()

