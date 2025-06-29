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
- Just like classical states, a compound system of two or more probabilistic system are viewed as one single probabilistic system as the result of cartesian product of individual systems.
- Probabilistic system come along with a probability vector which describe the probability of each entries of the states set.
- To express the probabilistic state of a compound system $(X, Y)$ using probability vectors in Dirac notation, it is written as:

$$
\sum_{(a,b)\in\Sigma\times\Gamma} p_{ab}|ab\rangle.             
$$
- Because each arrangement of individual systems and their states results in a different compound system, we typically follow a convention for ordering them: The order of the system is determined by its placement in the operation. The order of states within a system is lexicographical(alphabetical).
##### Example
- $X$ and $Y$ are two bits, $\Sigma = \Gamma = \\{0,1\\}$, the probabilistic states $(X,Y)$ is:
  
Pr((X,Y)=(0,0)) = 0.5

Pr((X,Y)=(0,1)) = 0

Pr((X,Y)=(1,0)) = 0

Pr((X,Y)=(1,1)) = 0.5
- The probability vector:
  
$$
p = \begin{bmatrix} 0.5 \\
0 \\
0 \\
0.5 \end{bmatrix}
$$

#### Independence of two(and more) systems
- Two individual systems $X$, $Y$ forming a compound system $(X,Y)$ are independent if:

- The condition for independence is met if there exist two probability vectors for the individual systems:

$$|\phi\rangle = \sum_{a\in\Sigma} q_a|a\rangle \quad \text{and} \quad |\psi\rangle = \sum_{b\in\Gamma} r_b|b\rangle,$$

- The joint probability $p_{ab}$ can be factored as the product of the individual probabilities $q_a$ and $r_b$ for all $a \in \Sigma$ and $b \in \Gamma$:

$$p_{ab} = q_a r_b$$

- Independence of systems can be concisely expressed through the **tensor product**. If a compound probabilistic state, $|\pi\rangle$, can be formed by taking the tensor product of individual probability vectors, $|\phi\rangle$ for system $X$ and $|\psi\rangle$ for system $Y$, then these systems are independent.

- Given individual probability vectors:

$$
|\phi\rangle = \sum_{a\in\Sigma} \alpha_a|a\rangle \quad \text{and} \quad |\psi\rangle = \sum_{b\in\Gamma} \beta_b|b\rangle
$$

- The tensor product is defined as the compound state:

$$
|\phi\rangle \otimes |\psi\rangle = \sum_{(a,b)\in\Sigma\times\Gamma} \alpha_a \beta_b |ab\rangle
$$

- If the joint state $|\pi\rangle$ is a **product state**, meaning the systems are independent, it can be written as:

$$
|\pi\rangle = |\phi\rangle \otimes |\psi\rangle 
$$

- An independence system is a product system as it's can be formed from two individual systems. If not independence, we call it correlation systems.
- A compound system with more than two individual systems are similar to compound system of two, 
#### Measuring Compound Probabilistic System
- Measurement of whole compound system is straightforward like single system where states collapsed into one classical state in the states set of system according to the probability of the state.
- Partial measurement of a compound system, let's have $(X,Y)$ as a compound system of states $\Sigma, \Gamma$,
- The probability to observe a particular classical state $\alpha \in \Sigma$ when just $X$ is measured is

$$
\mathrm{Pr}(X = a) = \sum_{b \in \Gamma} \mathrm{Pr}((X, Y) = (a, b))
$$

- There may still exist uncertainty about the classical state of $Y$, depending on the outcome of the measurement:

$$
\mathrm{Pr}(Y = b \mid X = a) = \frac{\mathrm{Pr}((X, Y) = (a, b))}{\mathrm{Pr}(X = a)}
$$
- On the compound probability vector, the measurement reduced the system into another system conditioned on the outcome of $X=a$

$$
\Ket{\pi_a} = \frac{\sum_{b \in \Gamma} p_{ab} \Ket{b}}{\sum_{c \in \Gamma} p_{ac}}
$$

###### Example
$X$ is $\Sigma = \\{0, 1\\}$, $Y$ is $\Gamma = \\{1, 2, 3\\}$, the probabilistic state of $(X, Y)$ is

$$|\psi\rangle = \frac{1}{2}|0, 1\rangle + \frac{1}{12}|0, 3\rangle + \frac{1}{12}|1, 1\rangle + \frac{1}{6}|1, 2\rangle + \frac{1}{6}|1, 3\rangle.$$
or
$$
p = \begin{bmatrix} 
\frac{1}{2} \\
0 \\
\frac{1}{12} \\
\frac{1}{12} \\
\frac{1}{6}\\
\frac{1}{6}
\end{bmatrix}
$$
- We have

$$
\Pr(X=0) = \frac{1}{2} + \frac{1}{12} = \frac{7}{12}
$$

$$
\Pr(X=1) = \frac{1}{12} + \frac{1}{6} + \frac{1}{6} = \frac{5}{12}
$$

- Conditioned on X being 0, the probabilistic state of Y becomes

$$
\frac{\frac{1}{2}|1\rangle + \frac{1}{12}|3\rangle}{\frac{7}{12}} = \frac{6}{7}|1\rangle + \frac{1}{7}|3\rangle,
$$

- and conditioned on the measurement of X being 1:

$$
\frac{\frac{1}{12}|1\rangle + \frac{1}{6}|2\rangle + \frac{1}{6}|3\rangle}{\frac{5}{12}} = \frac{1}{5}|1\rangle + \frac{2}{5}|2\rangle + \frac{2}{5}|3\rangle.
$$
#### Operations on compound probabilistic system
- Operation on a compound probabilistic system $(X,Y)$ can be represent as stochastic matrices as of single systems.

$$
\begin{pmatrix}
1 & \frac{1}{2} & \frac{1}{2} & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & \frac{1}{2} & \frac{1}{2} & 1
\end{pmatrix}
= \frac{1}{2}
\begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1
\end{pmatrix}
\+ \frac{1}{2}
\begin{pmatrix}
1 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 1 & 0 & 1
\end{pmatrix}
$$
- The matrix above is the operations on two bits $(X,Y)$ with probability $\frac{1}{2}$ to set $X$ to $Y$ and vice versa.
- Compound operations on a compound system $(X,Y)$ from two independence operation on independent system are defined as the tensor product of the stochastic matrix.



$$
\begin{pmatrix}
\alpha_{11} & \cdots & \alpha_{1m} \\
\vdots & \ddots & \vdots \\
\alpha_{m1} & \cdots & \alpha_{mm}
\end{pmatrix}
\otimes
\begin{pmatrix}
\beta_{11} & \cdots & \beta_{1k} \\
\vdots & \ddots & \vdots \\
\beta_{k1} & \cdots & \beta_{kk}
\end{pmatrix}
$$

$$
\=
\begin{pmatrix}
\alpha_{11}\beta_{11} & \cdots & \alpha_{11}\beta_{1k} & \cdots & \alpha_{1m}\beta_{11} & \cdots & \alpha_{1m}\beta_{1k} \\
\vdots & \ddots & \vdots & & \vdots & \ddots & \vdots \\
\alpha_{11}\beta_{k1} & \cdots & \alpha_{11}\beta_{kk} & \cdots & \alpha_{1m}\beta_{k1} & \cdots & \alpha_{1m}\beta_{kk} \\
\vdots & & \vdots & \ddots & \vdots & & \vdots \\
\alpha_{m1}\beta_{11} & \cdots & \alpha_{m1}\beta_{1k} & \cdots & \alpha_{mm}\beta_{11} & \cdots & \alpha_{mm}\beta_{1k} \\
\vdots & \ddots & \vdots & & \vdots & \ddots & \vdots \\
\alpha_{m1}\beta_{k1} & \cdots & \alpha_{m1}\beta_{kk} & \cdots & \alpha_{mm}\beta_{k1} & \cdots & \alpha_{mm}\beta_{kk}
\end{pmatrix}
$$
##### Example

$$
\begin{pmatrix}
1 & \frac{1}{2} \\
0 & \frac{1}{2}
\end{pmatrix}
$$

Suppose this operation is performed on a bit X, and a NOT operation is (independently) performed on a second bit Y.
The combined operation on the compound system $(X, Y)$ then has this matrix representation:

$$
\begin{pmatrix}
1 & \frac{1}{2} \\
0 & \frac{1}{2}
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\=
\begin{pmatrix}
0 & 1 & 0 & \frac{1}{2} \\
1 & 0 & \frac{1}{2} & 0 \\
0 & 0 & 0 & \frac{1}{2} \\
0 & 0 & \frac{1}{2} & 0
\end{pmatrix}
$$
## Quantum Informations
- Quantum states vector are alike to probabilistic states vector aside from the complex entries.
- Tensor product of Quantum states vector are also Quantum states vector and are called product states. This is because Euclidean Norm are multiplicative respectively to tensor product. $(1*1=1)$
- Quantum states that are not product states are a compound system with correlated individual systems, these systems are entangled with each other.
##### Example
This is an entangled system.

$$
\frac{1}{\sqrt{2}} |00\rangle + \frac{1}{\sqrt{2}} |11\rangle
$$
### Some familiar states
$$
|\phi^+\rangle = \frac{1}{\sqrt{2}}|00\rangle + \frac{1}{\sqrt{2}}|11\rangle
$$

$$
|\phi^-\rangle = \frac{1}{\sqrt{2}}|00\rangle - \frac{1}{\sqrt{2}}|11\rangle
$$

$$
|\psi^+\rangle = \frac{1}{\sqrt{2}}|01\rangle + \frac{1}{\sqrt{2}}|10\rangle
$$

$$
|\psi^-\rangle = \frac{1}{\sqrt{2}}|01\rangle - \frac{1}{\sqrt{2}}|10\rangle
$$

The states above are called Bell states
The content of the images shows the definitions of the four Bell states and the set notation for collecting them. Here's how to write them out:

The four Bell states are defined as:
The collection of all four Bell states is:

$$
\\{|\phi^+\rangle, |\phi^-\rangle, |\psi^+\rangle, |\psi^-\rangle\\}
$$

The above set is known as the Bell basis. Every quantum states vectors of two qubit can be represented as a linear combination of Bell basis' vectors.

- GHZ state

$$
\frac{1}{\sqrt{2}}|000\rangle + \frac{1}{\sqrt{2}}|111\rangle
$$

- W state

$$
\frac{1}{\sqrt{3}}|001\rangle + \frac{1}{\sqrt{3}}|010\rangle + \frac{1}{\sqrt{3}}|100\rangle
$$-

### Measurements of quantum states
- Measuring the entire compound system of quantum states collapses it into deterministic states, with probabilities equal to the squares of the corresponding entries.
- Given a compound quantum states $(X,Y)$ with $(\Sigma, \Gamma)$ as classical states set.
  
$$
|\psi\rangle = \sum_{(a,b) \in \Sigma \times \Gamma} \alpha_{ab} |ab\rangle
$$

- The probability for each outcome a of measuring independently the system $X$ is

$$
\sum_{b \in \Gamma} |\langle ab | \psi \rangle|^2 = \sum_{b \in \Gamma} |\alpha_{ab}|^2
$$

We can first express the vector $$|\psi\rangle$$ as

$$
|\psi\rangle = \sum_{a \in \Sigma} |a\rangle \otimes |\phi_a\rangle,
$$

where

$$
|\phi_a\rangle = \sum_{b \in \Gamma} \alpha_{ab} |b\rangle.
$$

The probability for the standard basis measurement of $X$ to give each outcome $a$ is as follows:

$$
\sum_{b \in \Gamma} |\alpha_{ab}|^2 = \| |\phi_a\rangle \|^2.
$$

And, as a result of the standard basis measurement of $X$ giving the outcome $a$, the quantum state of the pair $(X, Y)$ together becomes:

$$
|a\rangle \otimes \frac{|\phi_a\rangle}{\|||\phi_a\rangle\||}
$$
###### Example
As an example, consider the state of two qubits \((X,Y)\) from the beginning of the section:

$$
|\psi\rangle=\frac{1}{\sqrt{2}}|00\rangle-\frac{1}{\sqrt{6}}|01\rangle+\frac{i}{\sqrt{6}}|10\rangle+\frac{1}{\sqrt{6}}|11\rangle.
$$

To understand what happens when the first system \(X\) is measured, we begin by writing

$$
|\psi\rangle=|0\rangle\otimes\left(\frac{1}{\sqrt{2}}|0\rangle-\frac{1}{\sqrt{6}}|1\rangle\right)+|1\rangle\otimes\left(\frac{i}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle\right).
$$

We now see, based on the description above, that the probability for the measurement to result in the outcome 0 is

$$
\left\|\frac{1}{\sqrt{2}}|0\rangle-\frac{1}{\sqrt{6}}|1\rangle\right\|^{2}=\frac{1}{2}+\frac{1}{6}=\frac{2}{3},
$$

in which case the state of \((X,Y)\) becomes

$$
|0\rangle\otimes\frac{\frac{1}{\sqrt{2}}|0\rangle-\frac{1}{\sqrt{6}}|1\rangle}{\sqrt{\frac{2}{3}}}=|0\rangle\otimes\left(\frac{\sqrt{3}}{2}|0\rangle-\frac{1}{2}|1\rangle\right);
$$

and the probability for the measurement to result in the outcome 1 is

$$
\left\|\frac{i}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle\right\|^{2}=\frac{1}{6}+\frac{1}{6}=\frac{1}{3},
$$

in which case the state of \((X,Y)\) becomes

$$
|1\rangle\otimes\frac{\frac{i}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle}{\sqrt{\frac{1}{3}}}=|1\rangle\otimes\left(\frac{i}{\sqrt{2}}|0\rangle+\frac{1}{\sqrt{2}}|1\rangle\right).
$$

---

The same technique, used in a symmetric way, describes what happens if the second system \(Y\) is measured rather than the first. This time we rewrite the vector \(|\psi\rangle\) as

$$
|\psi\rangle=\left(\frac{1}{\sqrt{2}}|0\rangle+\frac{i}{\sqrt{6}}|1\rangle\right)\otimes|0\rangle+\left(-\frac{1}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle\right)\otimes|1\rangle.
$$

The probability that the measurement of \(Y\) gives the outcome 0 is

$$
\left\|\frac{1}{\sqrt{2}}|0\rangle+\frac{i}{\sqrt{6}}|1\rangle\right\|^{2}=\frac{1}{2}+\frac{1}{6}=\frac{2}{3},
$$

in which case the state of \((X,Y)\) becomes

$$
\frac{\frac{1}{\sqrt{2}}|0\rangle+\frac{i}{\sqrt{6}}|1\rangle}{\sqrt{\frac{2}{3}}}\otimes|0\rangle=\left(\frac{\sqrt{3}}{2}|0\rangle+\frac{i}{2}|1\rangle\right)\otimes|0\rangle;
$$

and the probability that the measurement outcome is 1 is

$$
\left\|-\frac{1}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle\right\|^{2}=\frac{1}{6}+\frac{1}{6}=\frac{1}{3},
$$

in which case the state of \((X,Y)\) becomes

$$
\frac{-\frac{1}{\sqrt{6}}|0\rangle+\frac{1}{\sqrt{6}}|1\rangle}{\sqrt{\frac{1}{3}}}\otimes|1\rangle=\left(-\frac{1}{\sqrt{2}}|0\rangle+\frac{1}{\sqrt{2}}|1\rangle\right)\otimes|1\rangle.
$$
### Unitary operations
The combined action of independent unitary operations $\(U_1, \ldots, U_n\)$ applied to systems $\(X_1, \ldots, X_n\)$ is represented by their tensor product:

$$
U_1 \otimes \cdots \otimes U_n
$$

For example, applying a unitary \(V\) to system \(Y\) while leaving system \(X\) unchanged is represented by:

$$
I \otimes V
$$

where $\(I\)$ is the identity matrix.
##### Example
For qubits $X$ and $Y$, applying a Hadamard gate to $X$ while leaving $Y$ unchanged is represented by:

For qubits $X$ and $Y$, applying a Hadamard gate to $X$ while leaving $Y$ unchanged is represented by:

$$
H \otimes I \= 
\begin{pmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}}
\end{pmatrix} 
\otimes 
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\=
\begin{pmatrix}
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} & 0 \\
0 & \frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\
\frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}} & 0 \\
0 & \frac{1}{\sqrt{2}} & 0 & -\frac{1}{\sqrt{2}}
\end{pmatrix}
$$
