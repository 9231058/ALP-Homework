# In The Name of God
# =======================================
# [] File Name : s13.py
#
# [] Creation Date : 12-01-2020
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('ch3_3_9_p8',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # raw material
    x0 = solver.NumVar(0, 3000, 'x_0')
    # product 1 sold
    x1 = solver.NumVar(0, 1200, 'x_1')
    # product 1 processed
    xp1 = solver.NumVar(0, solver.infinity(), 'xp_1')
    # product 2 sold
    x2 = solver.NumVar(0, 300, 'x_2')
    # product 2 processed
    xp2 = solver.NumVar(0, solver.infinity(), 'xp_2')
    # product 3 sold
    x3 = solver.NumVar(0, solver.infinity(), 'x_3')
    # product 4 sold
    x4 = solver.NumVar(0, solver.infinity(), 'x_4')
    # product 5 sold
    x5 = solver.NumVar(0, 1000, 'x_5')
    # product 6 sold
    x6 = solver.NumVar(0, 800, 'x_6')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint, x1 + xp1 <= x0 * 4, 0 <= x0 * 4 - x1 -xp1
    ct = solver.Constraint(0, solver.infinity(), 'product-1')
    ct.SetCoefficient(x1, -1)
    ct.SetCoefficient(xp1, -1)
    ct.SetCoefficient(x0, 4)

    # Create a linear constraint, x2 + xp2 <= x0 * 2, 0 <= x0 * 2 - x2 -xp2
    ct = solver.Constraint(0, solver.infinity(), 'product-2')
    ct.SetCoefficient(x2, -1)
    ct.SetCoefficient(xp2, -1)
    ct.SetCoefficient(x0, 2)

    # Create a linear constraint, x3 <= x0 * 1, 0 <= x0 * 1 - x3
    ct = solver.Constraint(0, solver.infinity(), 'product-3')
    ct.SetCoefficient(x3, -1)
    ct.SetCoefficient(x0, 1)

    # Create a linear constraint, x4 <= xp1 * 1, 0 <= xp1 * 1 - x4
    ct = solver.Constraint(0, solver.infinity(), 'product-4')
    ct.SetCoefficient(x4, -1)
    ct.SetCoefficient(xp1, 1)

    # Create a linear constraint, x5 <= xp2 * 0.8, 0 <= xp2 * 0.8 - x5
    ct = solver.Constraint(0, solver.infinity(), 'product-5')
    ct.SetCoefficient(x5, -1)
    ct.SetCoefficient(xp2, 0.8)

    # Create a linear constraint, x6 <= xp2 * 0.3, 0 <= xp2 * 0.3 - x6
    ct = solver.Constraint(0, solver.infinity(), 'product-6')
    ct.SetCoefficient(x6, -1)
    ct.SetCoefficient(xp2, 0.3)

    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function
    objective = solver.Objective()
    objective.SetCoefficient(x0, -4 * 4 + -2 * 4 + -1 * 2 - 6)
    objective.SetCoefficient(x1, 7)
    objective.SetCoefficient(x2, 6)
    objective.SetCoefficient(x3, 4)
    objective.SetCoefficient(xp1, -1)
    objective.SetCoefficient(x4, 3)
    objective.SetCoefficient(xp2, -0.8 * 5 + -0.3 * 5 + -0.8 * 4 + -0.3 * 3)
    objective.SetCoefficient(x5, 20 + 4)
    objective.SetCoefficient(x6, 35 + 3)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('x0 =', x0.solution_value())
    print('x1 =', x1.solution_value())
    print('xp1 =', xp1.solution_value())
    print('x2 =', x2.solution_value())
    print('xp2 =', xp2.solution_value())
    print('x3 =', x3.solution_value())
    print('x4 =', x4.solution_value())
    print('x5 =', x5.solution_value())
    print('x6 =', x6.solution_value())


if __name__ == '__main__':
    main()
