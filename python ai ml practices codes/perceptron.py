#  perceptron is an artificial neuron that can make a simple decision.

# structure of the perceptron
# class Perceptron:
#   def __init__(self, num_inputs=2, weights=[1,1]):
#     self.num_inputs = num_inputs
#     self.weights = weights

# cool_perceptron  = Perceptron()
# print(cool_perceptron)


# now adding the weighted sum variable o store the data

class Perceptron:
#   here the num_inputs = 2 mena 2 inputs by default and the weights=[2,1] mena the first inpout weight is  twice as important to the perceptron as the second input.
  def __init__(self, num_inputs=2, weights=[2,1]):
    self.num_inputs = num_inputs
    self.weights = weights
    
    # 
  def weighted_sum(self, inputs):
    # create variable to store weighted sum
    weighted_sum = 0
    for i in range(self.num_inputs):
      pass
      # complete this loop
    return weighted_sum 
      
cool_perceptron = Perceptron()

