#Simple Neural Network
import numpy as np
###########LEARNING############

#A Neuron with 2 inputs
def Neuron(inputs,weights):
	sum = 0
	for i in range(len(inputs)):
		sum += (inputs[i]*weights[i])
	return sigmoid(sum)

#Activation Function
#returns the Neuron's Output
def sigmoid(x):
	return 1/(1+np.exp(-x))

#Calculates the error
def calculateError(output, target):
	return target - output

def tuneWeights(weights,error,output):
	for i in range(len(weights)):
		weights[i] = weights[i] + error * output
	


#PROGRAM###########################################

#Desired Value
target = input("Enter target Value:\n")
target = int(target)
#Number of Iterations
iterations = input("Enter number of iterations:\n")
iterations = int(iterations)
#Neuron's Inputs
inputs = [np.random.randn(),np.random.randn()]
#Weights
weights = [np.random.randn(),np.random.randn()]

#Processes the Neuron once and prints result
print("Target Value: ", target)
print("Number of Iterations: ", target)
output = Neuron(inputs,weights)
print("Initial Output: ",output)
error = calculateError(output,target)
print("Initial Error: ", error)

print("Processing...")

for i in range(iterations):
	output = Neuron(inputs,weights)
	tuneWeights(weights,error,output)
print("Final Output: ",output)
error = calculateError(output,target)
print("Final Error: ", error)
