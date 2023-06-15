"""
ASSIGNMENT:
Question 4
Let say that the Kinetic / Dynamic Monte-Carlo model parameters are k1=k2=0.2 e Dt=2.
At time t=0, there are 4 type-A particles and 3 type-B particles. The algorithm of the Kinetic / Dynamic Monte-Carlo model is given at the slide #119 of the “Introduction and general concepts” section.
How many type-B particles there are after one time step at t=2?

Note that in this algorithm, N is the total number of particles. It is very important to note that step (4) required N iterations of steps (2) and (3) before incrementing the time by Δt. Also, both step (2) and step (3) require one random number.  To solve this problem, every time you need a random number pick the number in the following list. Start by taking the first number and then take the second, etc. Never reuse twice a random number. You should have enough random number to answer the question.
"""
import random

randomNumberList = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]

#variables definition
k1 = k2 = 0.2
Dt = 2
#concentration of A-type and B-type particles at time t=0
A = 4
B = 3
N = A + B
for i in range(N):
	print(A, B)
	#Step 2: choosing a particle
	if randomNumberList and (randomNumberList.pop(0) < (A/(A+B))):
		print("Particle A choosen")
		if randomNumberList.pop(0) < k1*Dt:
			print("Particle A transformed into particle B")
			A -= 1
			B += 1
		else:
			print("Particle A NOT transformed")
	else:
		print("Particle B choosen")
		if randomNumberList and (randomNumberList.pop(0) < k2*Dt):
			print("Particle B transformed into particle A")
			A += 1
			B -= 1
		else:
			print("Particle B NOT transformed")

print(f"Concentration of particle B: {B}")


