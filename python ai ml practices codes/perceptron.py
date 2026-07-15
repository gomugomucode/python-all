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

class Perceptron:
#   here the num_inputs = 2 mena 2 inputs by default and the weights=[2,1] mena the first inpout weight is  twice as important to the perceptron as the second input.
  def __init__(self, num_inputs=2, weights=[2,1]):
    self.num_inputs = num_inputs
    self.weights = weights
    
    # in thsi function we do weighted sunm calculation
  def weighted_sum(self, inputs):  #the iput are 2 because the num input is 2  in array or list like [2,6]
    # create variable to store weighted sum
    weighted_sum = 0
    for i in range(self.num_inputs):  #here the i in nrange (2) because the  self.num_inputs  value is 2 
      weighted_sum += inputs[i] * self.weights[i]
      # complete this loop
    return weighted_sum 
  

# activation functions are special functions that transform the weighted sum into a desired and constrained output.
#    — 1 for “Yes” and 0 for “No”
  def activation(self, weighted_sum):
    if weighted_sum >= 0:
      return 1
    else :
      return -1


cool_perceptron = Perceptron()
print(cool_perceptron.weighted_sum([24, 55]))


