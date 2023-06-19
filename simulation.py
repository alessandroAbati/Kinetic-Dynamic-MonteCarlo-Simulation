import random
import matplotlib.pyplot as plt
import numpy as np


class chemicalSystem:

	def __init__(self, A, B, k1, k2, Dt):
		self.A = A #concentration of particle A at t=0
		self.B = B #concentration of particle B at t=0
		self.k1 = k1 #rate of A->B
		self.k2 = k2 #rate of B->A
		self.Dt = Dt #time step
		assert k1*Dt < 1, "k1*Dt > 1" #k1Dt should be a probability
		assert k2*Dt < 2, "k2*Dt > 1" #k2Dt should be a probability

	def simulationChemicalReaction(self, t_init, t_max):
		N = self.A + self.B #total concentration of the system
		t = t_init
		concentration_A = []
		concentration_B = []
		while t < t_max:
			for i in range(N):
				if random.uniform(0,1) < self.A/(self.A+self.B):
					if random.uniform(0,1) < k1*Dt:
						self.A -= 1
						self.B += 1
				else:
					if random.uniform(0,1) < k2*Dt:
						self.A += 1
						self.B -= 1
			concentration_A.append(self.A)
			concentration_B.append(self.B)
			t += Dt
		return concentration_A, concentration_B

def analyticalSolutionA(A0, B0, k1, k2, t):
	return (k2/(k1+k2))*(A0+B0)+((A0*k1-B0*k2)/(k1+k2))*np.exp(-(k1+k2)*t)

def analyticalSolutionB(A0, B0, k1, k2, t):
	return (k1/(k1+k2))*(A0+B0)-((A0*k1-B0*k2)/(k1+k2))*np.exp(-(k1+k2)*t)


############################################## MAIN ###################################################
if __name__ == "__main__":
	number_of_simulations = 51
	A0 = 300
	B0 = 150
	k1 = 0.5
	k2 = 0.8
	Dt = 0.02
	t_init = 0
	t_max = 4
	x = np.linspace(t_init, t_max, int(t_max/Dt)) #defines x-axis for plots

	simulation = chemicalSystem(A0, B0, k1, k2, Dt)
	concentrationA, concentrationB = simulation.simulationChemicalReaction(t_init, t_max)
	average_Aconcentration = concentrationA
	average_Bconcentration = concentrationB

	plt.plot(x, [analyticalSolutionA(A0,B0,k1,k2,t) for t in x], label='AnalyticA', color='r')
	plt.axhline(((k2/(k1+k2))*(A0+B0)), label='EquilibriumA', color='grey')
	plt.plot(x, [analyticalSolutionB(A0,B0,k1,k2,t) for t in x], label='AnalyticB', color='b')
	plt.axhline(((k1/(k1+k2))*(A0+B0)), label='EquilibriumB', color='grey')
	plt.scatter(x, concentrationA, c='r',marker='.', label='A', s=2)
	plt.scatter(x, concentrationB, c='b', marker='.', label='B', s=2)
	plt.title(f"Simulation N° 1 of 2 particles chemical reaction")
	plt.xlabel("Time")
	plt.ylabel("Concentration of particles")
	plt.xlim([0,4.5])
	plt.ylim([140,320])
	plt.legend(loc='center left')
	plt.show(block=False)
	plt.pause(1)
	plt.savefig("output/Simulation1.png")
	plt.close()

	for i in range(2,number_of_simulations):
		simulation = chemicalSystem(A0, B0, k1, k2, Dt)
		concentrationA, concentrationB = simulation.simulationChemicalReaction(t_init, t_max)
		for index, (a,b) in enumerate(zip(concentrationA, concentrationB)):
			a0 = average_Aconcentration[index]
			b0 = average_Bconcentration[index]
			average_Aconcentration[index] = ((i-1)/i)*a0+a/i
			average_Bconcentration[index] = ((i-1)/i)*b0+b/i
		plt.plot(x, [analyticalSolutionA(A0,B0,k1,k2,t) for t in x], label='AnalyticA', color='r')
		plt.axhline(((k2/(k1+k2))*(A0+B0)), label='EquilibriumA', color='grey')
		plt.plot(x, [analyticalSolutionB(A0,B0,k1,k2,t) for t in x], label='AnalyticB', color='b')
		plt.axhline(((k1/(k1+k2))*(A0+B0)), label='EquilibriumB', color='grey')
		plt.scatter(x, concentrationA, c='r',marker='.', label='A', s=2)
		plt.scatter(x, concentrationB, c='b', marker='.', label='B', s=2)
		plt.scatter(x, average_Aconcentration, label='AverageA', facecolors='none', edgecolors='r', s=5)
		plt.scatter(x, average_Bconcentration, label='AverageB', facecolors='none', edgecolors='b', s=5)
		plt.title(f"Simulation N° {i} of 2 particles chemical reaction")
		plt.xlim([0,4.5])
		plt.ylim([140,320])
		plt.xlabel("Time")
		plt.ylabel("Concentration of particles")
		plt.legend(loc='center left')
		plt.show(block=False)
		plt.pause(1)
		plt.savefig(f"output/Simulation{i}.png")
		plt.close()

	plt.plot(x, [analyticalSolutionA(A0,B0,k1,k2,t) for t in x], label='AnalyticA', color='r')
	plt.axhline(((k2/(k1+k2))*(A0+B0)), label='EquilibriumA', color='grey')
	plt.plot(x, [analyticalSolutionB(A0,B0,k1,k2,t) for t in x], label='AnalyticB', color='b')
	plt.axhline(((k1/(k1+k2))*(A0+B0)), label='EquilibriumB', color='grey')
	plt.scatter(x, average_Aconcentration, c='r', marker='.', label='AverageA', facecolors='none', edgecolors='r', s=5)
	plt.scatter(x, average_Bconcentration, c='b', marker='.', label='AverageB', facecolors='none', edgecolors='b', s=5)
	plt.title(f"Simulation of 2 particles chemical reaction on average over {number_of_simulations} simulations")
	plt.xlim([0,4.5])
	plt.ylim([140,320])
	plt.xlabel("Time")
	plt.ylabel("Concentration of particles")
	plt.legend(loc='center left')
	plt.show()
