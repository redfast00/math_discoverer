# Math discoverer

Discovers semiring-like structures

```
$ python3 solver.py
[neutral_plus = alpha,
 neutral_multiply = alpha,
 plus = [(alpha, alpha) -> alpha,
         (alpha, gamma) -> gamma,
         (gamma, gamma) -> gamma,
         (gamma, alpha) -> gamma,
         else -> beta],
 multiply = [(alpha, alpha) -> alpha,
             (alpha, gamma) -> gamma,
             (gamma, alpha) -> gamma,
             else -> beta]]

```
