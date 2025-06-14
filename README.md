# Single-System

## Classical information

### Classical states and probability vectors
- A system $X$ is a classical system that contains information.
- Let $\Sigma$ be a finite and nonempty set representing all possible states of $X$.
- Each state in $\Sigma$ can occur with a certain probability, resulting in a **probabilistic state**.
- A probabilistic state can be represented by a **column vector** $p$ with:
  1. Non-negative entries.
  2. Entries' sum equal to 1.
- Such vectors allow us to define **operations** on the system as **matrix-vector multiplication**.

##### Example
- Let $X$ be the result of flipping a coin.
- $\Sigma = \{\text{head, tail}\}$.

- The probabilistic state is:

$$
p = \begin{bmatrix} 0.5 \\
0.5 \end{bmatrix}
$$

where the components correspond to $\text{head}$ and $\text{tail}$ respectively.

### Measuring probabilistic states
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
