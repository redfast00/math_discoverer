from z3 import EnumSort, Solver, Function, Const, sat
import itertools


R, values = EnumSort('R', ('alpha', 'beta', 'gamma'))

plus = Function('plus', R, R, R)
multiply = Function('multiply', R, R, R)

neutral_plus = Const('neutral_plus', R)
neutral_multiply = Const('neutral_multiply', R)

solver = Solver()

for a, b, c in itertools.product(values, repeat=3):
    # (R, +) is a commutative monoid with identity element 0:
    #     (a + b) + c = a + (b + c)
    #     0 + a = a + 0 = a
    #     a + b = b + a
    solver.add(plus(plus(a, b), c) == plus(a, plus(b, c)))
    solver.add(plus(neutral_plus, a) == a)
    solver.add(plus(a, neutral_plus) == a)
    solver.add(plus(a, b) == plus(b, a))

    # (R, ⋅) is a monoid with identity element 1:
    #     (a⋅b)⋅c = a⋅(b⋅c)
    #     1⋅a = a⋅1 = a
    solver.add(multiply(multiply(a, b), c) == multiply(a, multiply(b, c)))
    solver.add(multiply(neutral_multiply, a) == a)
    solver.add(multiply(a, neutral_multiply) == a)

    # Multiplication left and right distributes over addition:
    #     a⋅(b + c) = (a⋅b) + (a⋅c)
    #     (a + b)⋅c = (a⋅c) + (b⋅c)
    solver.add(multiply(a, plus(b, c)) == plus(multiply(a, b), multiply(a, c)))
    solver.add(multiply(plus(a, b), c) == plus(multiply(a, c), multiply(b, c)))

    # (This is not done for algebraic graphs)
    # Multiplication by 0 annihilates R:
    #     0⋅a = a⋅0 = 0
    # solver.add(multiply(neutral_plus, a) == neutral_plus)
    # solver.add(multiply(a, neutral_plus) == neutral_plus)

# Neutral element for addition and multiplication are the same
solver.add(neutral_plus == neutral_multiply)

# Might as well add alpha as neutral
solver.add(neutral_plus == values[0])

status = solver.check()

if status == sat:
    print(solver.model())
else:
    print(status)
