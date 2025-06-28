# Multiple-System

## Classical information

### Cartesians product and classical compound system
- Let $X, Y$ be systems with classical states sets: $\Sigma , \Gamma$ .
- The classical states set of the compound system $(X,Y)$ is the Cartesian product of $\Sigma$ and $\Gamma$, defined as

$$
\Sigma \times \Gamma = \\{ (a, b) : a \in \Sigma \text{ and } b \in \Gamma \\}
$$
- In another word, it create a new system $(X,Y)$ where the classical states which contains all distinc pair of states, where the first state picked from $\Sigma$, second state picked from $\Gamma$. Each pair $\(\sigma,\gamma\)$ represent a state where $X$ is in state $\sigma$ and $Y$ is in state $\gamma$.
##### Example
- If $\Sigma = \\{0, 1\\}$ and $\Gamma = \\{ A, B, C, D \\}$, then

$$
\Sigma \times \Gamma = \\{ (0, A), (0, B), (0, C), (0, D), (1, A), (1, B), (1, C), (1, D) \\}
$$

This description generalizes to more than two systems in a natural way.
Suppose $X_1, \dots, X_n$ are systems having classical state sets $\Sigma_1, \dots, \Sigma_n$, respectively.

The classical state set of the n-tuple $(X_1, \dots, X_n)$, viewed as a single compound system, is the Cartesian product

$$
\Sigma_1 \times \dots \times \Sigma_n = \\{ ((a_1, \dots, a_n)) : a_1 \in \Sigma_1, \dots, a_n \in \Sigma_n \\}
$$

##### Example

If $\Sigma_1 = \Sigma_2 = \Sigma_3 = \\{0, 1\\}$, then the classical state set of $(X_1, X_2, X_3)$ is

$$
\Sigma_1 \times \Sigma_2 \times \Sigma_3 = \\{ (0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1) \\}
$$

$$\Sigma \times \Gamma = \\{ (a,b) : a \in \Sigma \text{ and } b \in \Gamma \\}.$$

It is often convenient to write a classical state of the form $(a_{n-1} \dots a_0)$ as a string $a_{n-1} \dots a_0$ for the sake of brevity, especially in the case of alphabet(english alphabet, binary alphabet, hexa alphabet). For example, suppose that $X_0, \dots, X_9$ are bits.

$$\Sigma_0 = \Sigma_1 = \dots = \Sigma_9 = \\{0,1\\}$$

There are $2^{10} = 1024$ classical states of system $(X_9, \dots, X_0)$

$$\Sigma_9 \times \Sigma_8 \times \dots \times \Sigma_0 = \\{0,1\\}^{10}$$

Written as strings, these classical states look like this:

$0000000000$ 

$0000000001$

$0000000010$

$0000000011$

$0000000100$

$\vdots$

$1111111111$

For the classical state $0000000110$, for instance, we see that $X_1$ and $X_2$ are in the state $1$, while all other systems are in the state $0$.

### Probabilistic compound states
- A measurement on a probabilistic state collapses it into a specific deterministic state from $\Sigma$, chosen according to the given probabilities. 
- The post-measurement state is represented by a standard basis vector (one entry 1, others 0).
- We denote these basis states using ket notation like this $\lvert a \rangle$, $\lvert b \rangle$.

##### Example
For the coin flip system $X$ with initial state 

$$
p = \begin{bmatrix} 0.5 \\
0.5 \end{bmatrix}
$$

- Measurement yields:

$$
\begin{cases}
\lvert \text{head} \rangle = \begin{bmatrix} 1 \\
0 \end{bmatrix} & \text{with probability } 0.5 \\
\lvert \text{tail} \rangle = \begin{bmatrix} 0 \\
1 \end{bmatrix} & \text{with probability } 0.5
\end{cases}
$$
  
- The initial probabilistic state can be expressed as:
 
$$
0.5 \lvert \text{head} \rangle + 0.5 \lvert \text{tail} \rangle
$$
  
After the measurement, the state either becomes $\lvert \text{head} \rangle$ or $\lvert \text{tail} \rangle$, and is no longer a probabilistic state.
 
### Classical Operations

#### Deterministic Operations
- For a classical system with states $\Sigma$, a deterministic operation is a function 
$f: \Sigma \to \Sigma$, represented by matrices $M$ where:

$$
M \lvert a \rangle = \lvert f(a) \rangle \quad \forall a \in \Sigma
$$

- Any operation $M$ can be expressed as:

- with $\langle a \rvert$ is the row vector of a state, we have

$$
M = \sum_{a \in \Sigma} \lvert f(a) \rangle \langle a \rvert
$$
- That is, mapping from a state into other states from $\Sigma$
- These matrices have:
  1. Exactly one 1 per column
  2. All other entries 0

**Example ($\Sigma = \{0,1\}$):**
- Identity:
  
$$
  M_2 = \begin{bmatrix} 1 & 0 \\
  0 & 1 \end{bmatrix} \quad (f(a)=a)
$$
  
- NOT gate:
  
$$
  M_3 = \begin{bmatrix} 0 & 1 \\
   1 & 0 \end{bmatrix} \quad (f(a)=\neg a)
$$
  
- Constant 0:
  
$$
  M_1 = \begin{bmatrix} 1 & 1 \\
  0 & 0 \end{bmatrix} \quad (f(a)=0)
$$
  
- Constant 1:

$$
  M_4 = \begin{bmatrix} 0 & 0 \\
   1 & 1 \end{bmatrix} \quad (f(a)=1)
$$

#### Probabilistic Operations
- Represented by **stochastic matrices**:
  1. All entries are real non-negative number
  2. Column sums $= 1$ (each column is a probability vector)

**Example:**

$$
\begin{bmatrix} 1 & 0.5 \\
0 & 0.5 \end{bmatrix}
$$

- Input $0$: Output stays $0$
- Input $1$: Output becomes $0$ or $1$ with 50% probability each

#### Composition of Operations
$$
\text{Apply } M_1 \text{ then } M_2 \equiv M_2 M_1
$$

The composition is the same for three or more operations, the operations are sorted by order of applying from right to left.

## Quantum Information

### Quantum State Vectors
- Represented by complex vectors:
  
$$
\lvert \psi \rangle = \begin{bmatrix}\alpha_1 \\
\vdots \\
\alpha_n\end{bmatrix}
$$

- The sum of the absolute values squared of the entries of a quantum state vector is $1$.
- Equivalent to  $\lVert \lvert \psi \rangle \rVert = \sqrt{\sum|\alpha_k|^2} = 1$ (Euclidean norm)
- Thus quantum state vectors are unit vectors.

**Qubit:**
- Qubit is a quantum system whose classical states set is $\{0,1\}$
- Classical states vectors of classical bit are also quantum state vectors of a qubit: 

$$
\lvert 0 \rangle = \begin{bmatrix}1\\
0\end{bmatrix}, \lvert 1 \rangle = \begin{bmatrix}0\\
1\end{bmatrix}
$$

- Qubit can also be a state that's superposition between 0 and 1 which are Superposition states:

$$
\lvert + \rangle = \frac{1}{\sqrt{2}}\lvert 0 \rangle + \frac{1}{\sqrt{2}}\lvert 1 \rangle
$$

$$
\lvert - \rangle = \frac{1}{\sqrt{2}}\lvert 0 \rangle - \frac{1}{\sqrt{2}}\lvert 1 \rangle
$$

### Measurement (Born Rule)
When measuring state $\lvert \psi \rangle$:
- The quantum state collapses into a deterministic state with each classical state of the system appearing with probability equal to the **absolute value squared** of the entry in the quantum state vector corresponding to that classical state:

$$
P(\text{outcome } a) = |\langle a \lvert \psi \rangle|^2 = |\alpha_a|^2
$$

- **Absolute value squared** behaves like the probability of each state, thus the sum of absolute value squares must be 1 for every quantum state vector.

**Example:**
- For $\lvert + \rangle$:

$$
P(0) = |\langle 0 \lvert + \rangle|^2 = \frac{1}{2}, \quad P(1) = |\langle 1 \lvert + \rangle|^2 = \frac{1}{2}
$$

- For $\lvert - \rangle$:

$$
P(0) = |\langle 0 \lvert - \rangle|^2 = \frac{1}{2}, \quad P(1) = |\langle 1 \lvert - \rangle|^2 = \frac{1}{2}
$$

### Unitary Operations
- As we see, $\lvert + \rangle$ and $\lvert - \rangle$ behave identically when measuring, thus we have to resort to operations to differentiate them.
- Operations on quantum states are represented by **unitary matrices**, thus it's called unitary operations.

- **Unitary matrix** are square matrices with complex entries that satisfy:

$$
UU^\dagger = U^\dagger U = I
$$

- $U^\dagger = \overline{U^T} = U^{-1}$ are *conjugate transpose* of $U$ and we can conclude that it's equal to its inverse if it satisfies the above equation.

- The multiplication of a unitary matrix with a vector preserves the norm of the vector, thus preserving the quantum status.
- It can be understood as a mapping operation from one quantum state to another.

**Examples of Unitary Matrices on a Qubit:**
1. Pauli matrices:

$$
X = \begin{bmatrix}0 & 1 \\
1 & 0\end{bmatrix}, \quad Z = \begin{bmatrix}1 & 0 \\
0 & -1\end{bmatrix}
$$

2. Hadamard:

$$
H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1 \\
1 & -1\end{bmatrix}
$$

Hadamard operation is the way to distinguish $\lvert + \rangle$ and $\lvert - \rangle$ as:

$$
H \lvert + \rangle = \lvert 0 \rangle, \quad H \lvert - \rangle = \lvert 1 \rangle
$$

3. Phase gates:

$$
S = \begin{bmatrix}1 & 0 \\
0 & i\end{bmatrix}, \quad T = \begin{bmatrix}1 & 0 \\
0 & e^{i\pi/4}\end{bmatrix}
$$

#### Compositions of qubit unitary operations
- Similar to compositions of classical operations, applying multiple operations on a quantum state is also represented as matrix multiplication from right to left.

**Example:**

Apply $H$, then $S$, then $H$ again:


$$ 
R = 
H S H = 
\begin{bmatrix}
  \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
  \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
  \end{bmatrix}
  \begin{bmatrix}
  1 & 0 \\
  0 & i
  \end{bmatrix}
  \begin{bmatrix}
  \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
  \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
  \end{bmatrix} =
  \begin{bmatrix}
  \frac{1+i}{2} & \frac{1-i}{2} \\
  \frac{1-i}{2} & \frac{1+i}{2}
  \end{bmatrix}
$$


This example is interesting because if we square it:

$$
R^2 = 
\begin{bmatrix}
\frac{1+i}{2} & \frac{1-i}{2} \\
\frac{1-i}{2} & \frac{1+i}{2}
\end{bmatrix}^2=
\begin{bmatrix}
0 & 1 \\
1 & 0 
\end{bmatrix}
$$

Thus $R = HSH$ is also called the square root of the NOT operation.
