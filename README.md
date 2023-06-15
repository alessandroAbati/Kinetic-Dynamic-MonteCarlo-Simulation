# Kinetic/Dynamic MonteCarlo Simulation
 Simple example of Kinetic/Dynamic Monte-Carlo simulation of 2 particles chemical reaction.
 
 ![monteCarloSimulation](https://github.com/alessandroAbati/Kinetic-Dynamic-MonteCarlo-Simulation/assets/136715422/9ccb0fc3-d9d1-4941-8a5b-a131b9f7fb0c)

 This project introduces a Monte Carlo simulation model for investigating natural processes, specifically focusing on a chemical reaction involving two particles, A and B. This project not only showcases the application of Monte Carlo simulation as a computational tool but also highlights the convergence of simulation results towards the analytical solution.

Monte Carlo simulations utilize random sampling to mimic and analyze complex systems. In this project, the simulation model employs the kinetic-dynamic Monte Carlo method to capture the dynamic behavior of particle concentrations during the chemical reaction. By simulating numerous random events based on defined probabilities, the model generates concentration profiles for particles A and B over time.

To verify the accuracy of the simulation, the code also provides analytical solutions for the particle concentrations. These solutions are obtained by solving the differential equations that govern the chemical reaction. The analytical solutions serve as reference benchmarks for comparison with the simulation results.

The project extends beyond a single simulation run and incorporates multiple simulations to capture the system's variability. The average concentration profiles over these simulations are calculated and plotted. As the number of simulations increases, the average concentration profiles tend to converge towards the analytical solution. The convergence occurs because the random fluctuations in individual simulations tend to cancel each other out when averaged over multiple runs. The aggregate behavior of the system, reflected in the average concentration profiles, aligns more closely with the expected deterministic behavior described by the analytical solution.

By demonstrating the convergence of the average concentration profiles towards the analytical solution, the project highlights the power of Monte Carlo simulations in approximating complex natural processes. It underscores the ability to derive meaningful insights from the statistical behavior observed across multiple simulation runs and reinforces the reliability of the simulation model.

Overall, this project showcases proficiency in mathematical modeling, statistical analysis, and computational simulation. It exemplifies the application of Monte Carlo methods to gain a deeper understanding of natural processes and emphasizes the convergence of simulation results towards analytical solutions.

# Theory:
Let's consider the chemical equation: $\ce{A ->[k_1] B} $
