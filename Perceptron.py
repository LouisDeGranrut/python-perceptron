#Simple Neuron
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

#Desired Value (could be anything)
target = 0.8
#Inputs
inputs = [np.random.randn(),np.random.randn()]
#Weights
weights = [np.random.randn(),np.random.randn()]

#Processes the Neuron once and prints result
for i in range(60):
	output = Neuron(inputs,weights)
	print("Target: ", target)
	print("Output: ",output)
	error = calculateError(output,target)
	print("Error: ", error)
	tuneWeights(weights,error,output)