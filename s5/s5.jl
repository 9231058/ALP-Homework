using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[0:5] >= 0)
@constraint(m, x[0] * 2 + x[3] * 2 + x[4] * 3 + x[5] <= 25000)
@constraint(m, x[1] <= 5000)
@constraint(m, x[2] + x[3] <= 5000)
@constraint(m, x[4] + x[5] <= 3000)
@constraint(m, 3 * x[0] == x[1] + x[3] + x[4])
@constraint(m, x[0] == x[2] + x[5])
@objective(m, Max, x[1] * 10 + x[2] * 20 + x[3] * 20 + x[4] * 30 + x[5] * 30 - x[0] * 25 - x[2] - x[3] - x[4] * 2 - x[5] * 6)
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
println("X: ", X)
