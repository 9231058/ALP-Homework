# In The Name of God
# =======================================
# [] File Name : ip.py
#
# [] Creation Date : 16-01-2020
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================

from ortools.linear_solver import pywraplp


def main():
    # Create the mip solver with the CBC backend.
    solver = pywraplp.Solver('IntegerProgrammingExample',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    a3 = solver.IntVar(0.0, solver.infinity(), 'a3')
    a5 = solver.IntVar(0.0, solver.infinity(), 'a5')
    a7 = solver.IntVar(0.0, solver.infinity(), 'a7')
    a9 = solver.IntVar(0.0, solver.infinity(), 'a9')

    constraint = solver.Constraint(-solver.infinity(), 17)
    constraint.SetCoefficient(a3, 3)
    constraint.SetCoefficient(a5, 5)
    constraint.SetCoefficient(a7, 7)
    constraint.SetCoefficient(a9, 9)

    objective = solver.Objective()
    objective.SetCoefficient(a3, 1/5)
    objective.SetCoefficient(a5, 1/3)
    objective.SetCoefficient(a7, 1)
    objective.SetCoefficient(a9, 1)
    objective.SetMaximization()

    solver.Solve()
    print(f'Maximum objective function value = {solver.Objective().Value()}')
    print()
    for variable in [a3, a5, a7, a9]:
        print('%s = %d' % (variable.name(), variable.solution_value()))


if __name__ == '__main__':
    main()
