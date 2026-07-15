#  perceptron is an artificial neuron that can make a simple decision.

class Perceptron:
  def __init__(self, num_inputs=2, weights=[1,1]):
    self.num_inputs = num_inputs
    self.weights = weights

cool_perceptron  = Perceptron()
print(cool_perceptron)