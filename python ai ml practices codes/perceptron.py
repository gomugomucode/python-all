#  perceptron is an artificial neuron that can make a simple decision.

# structure of the perceptron
# class Perceptron:
#   def __init__(self, num_inputs=2, weights=[1,1]):
#     self.num_inputs = num_inputs
#     self.weights = weights

# cool_perceptron  = Perceptron()
# print(cool_perceptron)


# Perceptron steps : 
# 1 . weighted sum calculation
# 2. Activation Function


# now adding the weighted sum variable o store the data

# class Perceptron:
# #   here the num_inputs = 2 mena 2 inputs by default and the weights=[2,1] mena the first inpout weight is  twice as important to the perceptron as the second input.
#   def __init__(self, num_inputs=2, weights=[2,1]):
#     self.num_inputs = num_inputs
#     self.weights = weights
    
#     # in thsi function we do weighted sunm calculation
#   def weighted_sum(self, inputs):  #the iput are 2 because the num input is 2  in array or list like [2,6]
#     # create variable to store weighted sum
#     weighted_sum = 0
#     for i in range(self.num_inputs):  #here the i in nrange (2) because the  self.num_inputs  value is 2 
#       weighted_sum += inputs[i] * self.weights[i]
#       # complete this loop
#     return weighted_sum 
  

# # activation functions are special functions that transform the weighted sum into a desired and constrained output.
# #    — 1 for “Yes” and 0 for “No”
#   def activation(self, weighted_sum):
#     if weighted_sum >= 0:
#       return 1
#     else :
#       return -1


# cool_perceptron = Perceptron()

# weighted_sum = cool_perceptron.weighted_sum([24, 55])
# print(weighted_sum)

# print(cool_perceptron.activation(weighted_sum))



# above we just pass 2 valse and weight and it ell yes or no in binary  but if we have to work in larger data set then we have to train the preception  so for that we are going to train the preceptron 


# # importing the matplot and random
# import matplotlib.pyplot as plt
# import random

# # creating a  generate_training_set function with argument num_points
# def generate_training_set(num_points):
# 	x_coordinates = [random.randint(0, 50) for i in range(num_points)]   #here storing the xcoordinate for i range  numpoint  and generating random number everytime
# 	y_coordinates = [random.randint(0, 50) for i in range(num_points)]
# 	training_set = dict()

# 	# in this step we ar making a pair of x,y by using the zip which combine x and y value 
# 	for x, y in zip(x_coordinates, y_coordinates):
# 		# here 45 is jus aan random number we can use any 
# 		if x <= 45-y:
# 			training_set[(x,y)] = 1
# 		elif x > 45-y:
# 			training_set[(x,y)] = -1
# 	return training_set

# # creating an training_set object 
# training_set = generate_training_set(30)

# # creating an empty array of x y plus minus
# x_plus = []
# y_plus = []
# x_minus = []
# y_minus = []

# # here accessing the value of x and y from the training set 
# for data in training_set:
# 	# checking the label 1 or -1 so we can store teh value in plus or minus simultaneously 
# 	if training_set[data] == 1:
# 		x_plus.append(data[0])
# 		y_plus.append(data[1])
# 	elif training_set[data] == -1:
# 		x_minus.append(data[0])
# 		y_minus.append(data[1])
    
# # creating the figure from mathplot
# fig = plt.figure()
# ax = plt.axes(xlim=(-25, 75), ylim=(-25, 75))

# plt.scatter(x_plus, y_plus, marker = '+', c = 'green', s = 128, linewidth = 2)
# plt.scatter(x_minus, y_minus, marker = '_', c = 'red', s = 128, linewidth = 2)

# plt.title("Training Set")

# plt.show()



# now training errors in preceptron

# Every time the output mismatches the expected label, we say that the perceptron has made a training error

# training error = actual label − predicted label


# class Perceptron:
#   def __init__(self, num_inputs=2, weights=[1,1]):
#     self.num_inputs = num_inputs
#     self.weights = weights
    
#   def weighted_sum(self, inputs):
#     weighted_sum = 0
#     for i in range(self.num_inputs):
#       weighted_sum += self.weights[i]*inputs[i]
#     return weighted_sum
  
#   def activation(self, weighted_sum):
#     if weighted_sum >= 0:
#       return 1
#     if weighted_sum < 0:
#       return -1
    
#   def training(self, training_set):
#     for inputs in training_set:
#     #    creating a  variable called prediction and assign it the correct label value using .activation(), .weighted_sum(), and inputs in a single statement.
#       prediction = self.activation(self.weighted_sum(inputs))  
      
# 	#   Creating a variable named actual and assign it the actual label for each inputs in training_set.
#       actual = training_set[inputs]
      
# 	#   Creating a variable called error and assign it the value of actual - prediction.
#       error = actual - prediction
       

     
# cool_perceptron = Perceptron()
# print(cool_perceptron.weighted_sum([24, 55]))
# print(cool_perceptron.activation(52))



# preceptron algorithim is a supervised learning algorithm that can be used for binary classification tasks. It works by finding a linear decision boundary that separates the two classes in the training data. The algorithm iteratively adjusts the weights of the perceptron based on the training errors until it converges to a solution that correctly classifies the training data.

# The most important part of the algorithm is the update rule where the weights get updated:

# weight=weight+(error∗input)


lines = []

class Perceptron:
  def __init__(self, num_inputs=2, weights=[1,1]):
    self.num_inputs = num_inputs
    self.weights = weights
    
  def weighted_sum(self, inputs):
    weighted_sum = 0
    for i in range(self.num_inputs):
      weighted_sum += self.weights[i]*inputs[i]
    return weighted_sum
  
  def activation(self, weighted_sum):
    if weighted_sum >= 0:
      return 1
    if weighted_sum < 0:
      return -1
    
  def training(self, training_set):
    foundLine = False
    while not foundLine:
      total_error = 0

      for inputs in training_set:
        prediction = self.activation(self.weighted_sum(inputs))
        actual = training_set[inputs]
        error = actual - prediction
        total_error += abs(error)

        # in thsi loop we are updating the weights of the perceptron based on the training errors. The weights are adjusted by adding the product of the error and the corresponding input value to each weight. This update rule allows the perceptron to learn from its mistakes and improve its classification performance over time.
        for i in range(self.num_inputs):
          self.weights[i] += error*inputs[i]

        #   until total error is 0 we keep on training the perceptron and when the total error is 0 we found the line and we can stop the training
      if total_error == 0:
        foundLine = True
        


cool_perceptron = Perceptron()
small_training_set = {(0,3):1, (3,0):-1, (0,-3):-1, (-3,0):1}
print(cool_perceptron.training(small_training_set))