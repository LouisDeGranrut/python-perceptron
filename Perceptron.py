#Simple Perceptron
import numpy as np
import matplotlib.pyplot as plt

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
	res = target - output
	error.append(res)

def tuneWeights(weights,error,output):
	for i in range(len(weights)):
		weights[i] = weights[i] + error[-1] * output#last error value
	
#PROGRAM###########################################

#Desired Value
target = input("Enter target Value [0,1]: \n")
target = float(target)
#Number of Iterations
iterations = input("Enter number of iterations:\n")
iterations = int(iterations)
print("######################################")
#Neuron's Inputs
inputs = [np.random.randn(),np.random.randn()]
#Weights
weights = [np.random.randn(),np.random.randn()]
#Graph stuff
error = []#stores every error value
it = [0,0]#stores every iterations (from 0 to iterations)

#Processes the Neuron once and prints result
print("Target Value: ", target)
print("Number of Iterations: ", target)
output = Neuron(inputs,weights)
print("Initial Output: ",output)
calculateError(output,target)
print("Initial Error: ", error)
print("######################################")

print("Processing...")

for i in range(iterations):
	output = Neuron(inputs,weights)
	calculateError(output,target)
	tuneWeights(weights,error,output)
	it.append(i)

#Final Results
print("Final Output: ",output)
calculateError(output,target)
print("Final Error: ", error[-1])
print("######################################")
print("Plotting Results...")

plt.plot(it, error)
plt.show()
