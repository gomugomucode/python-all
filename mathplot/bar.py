

# #  we can create bar fuctions to create the bar chart 

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()


# we can also create vertically

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()


# we can also use the color argument to set the color of the bars:

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# # plt.bar(x, y, color = "red")

# #  we can alos use the hexadecimal color code to set the color of the bars:


# plt.bar(x, y, color = "#4CAF50")

# plt.show()



#  we can also specify the width of the bars by using the width argument:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1 , color = "#FAF200")
plt.show()