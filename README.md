# Kinetic/Dynamic Monte-Carlo Simulation
 Simple example of Kinetic/Dynamic Monte-Carlo simulation of 2 molecules chemical reaction.

 ![KineticMonteCarloSimulation](https://github.com/alessandroAbati/Kinetic-Dynamic-MonteCarlo-Simulation/assets/136715422/3534a9d8-8cad-4b05-a135-93b234fb9442)

### Introduction
This project introduces a basic Monte Carlo simulation model for investigating a chemical reaction between molecules A and B. The simulation utilizes random sampling to mimic complex systems and employs the kinetic-dynamic Monte Carlo method to capture the dynamic behavior of molecule concentrations over time.

To validate the simulation, analytical solutions for the molecule concentrations are provided as reference benchmarks. The project incorporates multiple simulations to account for system variability and calculates the average concentration profiles. As the number of simulations increases, the average profiles tend to converge towards the analytical solution, indicating the reliability of the simulation model.

In summary, this project demonstrates the power of Monte Carlo simulations in approximating complex natural processes. It showcases proficiency in mathematical modeling, statistical analysis, and computational simulation, emphasizing the convergence of simulation results towards analytical solutions.

### Theory
Let's consider the abstract chemical equations
$\ce{A ->[k_1] B}$ and $\ce{B ->[k_2] A}$
where some molecule $A$ can transform into a molecule $B$ with the rate $k_1$ and $B$ can transform back to $A$ with the rate $k_2$.
They can be written as an ordinary equation (in a matrix form):
```math
\frac{d}{dt} \begin{pmatrix} A \\ B \end{pmatrix} = \begin{pmatrix}
-k_1 & k_2 \\
k_1 & -k_2
\end{pmatrix}
\begin{pmatrix} A \\ B \end{pmatrix}
```

With analytical solution:
```math
A(t) = \frac{k_2}{k_1+k_2}(A_0+B_0) + \frac{A_0 k_1 - B_0 k_2}{k_1+k_2} e^{-(k_1+k_2)t}
\hspace{30pt}
B(t) = \frac{k_1}{k_1+k_2}(A_0+B_0) - \frac{A_0 k_1 - B_0 k_2}{k_1+k_2} e^{-(k_1+k_2)t}
```
where $A_0$ e $B_0$ are the initial concentration of $A$ and $B$.
As we can see, for $t \rightarrow \infty$:
```math
A(t) \rightarrow \frac{k_2}{k_1+k_2}(A_0+B_0) \hspace{50pt} B(t) \rightarrow \frac{k_1}{k_1+k_2}(A_0+B_0)
```
which are the equilibrium density of the molecules.

### Algorithm
Let's try to sample these processes with some random processes.
We have a molecule A that suddenly turns into a molecule B with some rate and viceversa; so, there is a probability that given a time interval $\Delta t$ the transformation happens. Thus, let's consider $\Delta t$ small enough so that $\Delta t k_1 < 1$ and $\Delta t k_2 < 1$ so we can consider $\Delta t k_1$ as the probability for molecule $A$ to transform into $B$ in $\Delta t$ and $\Delta t k_2$ as the probability for molecule $B$ to transform into $A$ in $\Delta t$.
So we can define the following algorithm:
1. We pick randomly a molecule in the system of $N = A(t) + B(t)$ molecules; practically we can do that considering that $\frac{A}{A+B}$ is the probability that if i pick a random molecule in the system that molecule will be an A-type one. So we can say that we have chosen an A-type molecule if $random.uniform(0,1) < \frac{A}{A+B}$ and a B-type molecule otherwise.
2. (a) If molecule A was chosen, it is transformed into a B molecule provided $random.uniform(0,1) < k_1 \Delta t$; then, $A = A - 1$ and $B = B + 1$. <br />
(b) If molecule B was chosen, it is transformed into a A molecule provided $random.uniform(0,1) < k_2 \Delta t$; then, $A = A + 1$ and $B = B - 1$.
3. We repeat (1) and (2) for all the molecules in the system ($N$ times) and the physical time $t$ is incremented by $\Delta t$: $t = t + \Delta t$.
4. We repeat (1), (2) and (3) until $t=t_{max}$.

### Prerequisites
Make sure you have the following dependencies installed:

- Python 3.x
- matplotlib
- numpy

### How to Use
1. Clone the repository or download the source code.

2. Open the Python script chemical_reaction_simulation.py in your preferred Python editor.

3. Modify the following parameters to customize the simulation:

    - A0 and B0: Initial concentrations of molecules A and B.
    - k1 and k2: Rates of conversion between A and B.
    - Dt: Time step size for the simulation.
    - t_max: Maximum simulation time.
    - number_of_simulations: Number of simulations to run.
4. Run the script. The simulation will generate concentration profiles for molecules A and B over time.

5. The plots will show the simulated concentration profiles for A and B, along with the analytical solutions and equilibrium concentrations. You can observe how the average concentration profiles tend to converge towards the analytical solutions as the number of simulations increases.

### References
This project is based on the section *Introduction and general concepts* of the Coursera course *Simulation and modeling of natural processes* (https://www.coursera.org/learn/modeling-simulation-natural-processes).
