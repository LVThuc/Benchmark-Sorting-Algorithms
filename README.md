
# Single-system

## Classical information

### Classical states and probability vectors
- A system $X$ is a classical system that contains information.
- Let $\Sigma$ be a finite and nonempty set representing all possible states of $X$.
- Each state in $\Sigma$ can occur with a certain probability, resulting in a **probabilistic state**.
- A probabilistic state can be represented by a **column vector** $\vec{p}$ with:
  1. Non-negative entries.
  2. Entries' sum equal to 1.
- Such vectors allow us to define **operations** on the system as **matrix-vector multiplication**.
#### Example
- Let $X$ be the result of flipping a coin.  
- $\Sigma = \{0, 1\}$, where 0 = heads and 1 = tails.  
- The probabilistic state is:  
  $p = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$

### Measuring probabilistic states
- A measurement on a probabilistic state collapses it into a specific deterministic state, chosen from the set $\Sigma$ according to the given probabilities. The probability vector of this state only has one $1$ and all other entries as $0$. For example:
$$
p = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}
$$
