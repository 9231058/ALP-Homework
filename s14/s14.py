# In The Name of God
# =======================================
# [] File Name : s14.py
#
# [] Creation Date : 12-01-2020
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================
from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver('ch5_5_2_p1',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # acres planted with wheat
    a1 = solver.NumVar(0, 28, 'A1')
    # acres planted with corn
    a2 = solver.NumVar(0, 30, 'A2')
    # hours of labor that are purchased
    l = solver.NumVar(0, 350, 'L')

    print('Number of variables =', solver.NumVariables())

    # Create a linear constraint, 6A1 + 10A2 - L <= 0
    c1 = solver.Constraint(-solver.infinity(), 0, 'c1')
    c1.SetCoefficient(a1, 6)
    c1.SetCoefficient(a2, 10)
    c1.SetCoefficient(l, -1)

    # Create a linear constraint, A1 + A2 <= 45
    c2 = solver.Constraint(0, 45, 'c2')
    c2.SetCoefficient(a1, 1)
    c2.SetCoefficient(a2, 1)

    print('Number of constraints =', solver.NumConstraints())

    # Create the objective function
    objective = solver.Objective()
    objective.SetCoefficient(a1, 150)
    objective.SetCoefficient(a2, 200)
    objective.SetCoefficient(l, -10)
    objective.SetMaximization()

    solver.Solve()

    print('Solution:')
    print('Objective value =', objective.Value())
    print('A1 =', a1.solution_value())
    print('A2 =', a2.solution_value())
    print('L =', l.solution_value())

    # please note that non-zero dual price indicates zero slack
    print('C1 (dual price) =', c1.dual_value())
    print('C2 (dual price) =', c2.dual_value())

if __name__ == '__main__':
    main()
