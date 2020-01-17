# In The Name of God
# =======================================
# [] File Name : s20.py
#
# [] Creation Date : 16-01-2020
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('ch10_10_4_p3',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    x1 = solver.NumVar(0, solver.infinity(), 'x_1')
    x2 = solver.NumVar(0, 5, 'x_2')

    print('Number of variables =', solver.NumVariables())

    ct = solver.Constraint(0, 1, 'c1')
    ct.SetCoefficient(x1, 2)
    ct.SetCoefficient(x2, -1)

    ct = solver.Constraint(0, 6, 'c2')
    ct.SetCoefficient(x1, 1)
    ct.SetCoefficient(x2, 6)


    print('Number of constraints =', solver.NumConstraints())

    objective = solver.Objective()
    objective.SetCoefficient(x1, 4)
    objective.SetCoefficient(x2, 3)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    for v in [x1, x2]:
        print(f'{v.name()} = {v.solution_value()}')


if __name__ == '__main__':
    main()
