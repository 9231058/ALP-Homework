using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[1:2] >= 0)
@variable(m, y[0:3] >= 0)
@constraint(m, y[0] <= 0.3 * x[1] + 0.2 * x[2])
@constraint(m, y[1] <= 0.3 * x[1] + 0.2 * x[2])
@constraint(m, y[2] <= 0.2 * x[1] + 0.25 * x[2])
@constraint(m, y[3] <= 0.15 * x[1] + 0.20 * x[2])
@constraint(m, 0.3 * x[1] + 0.2 * x[2] - y[1] + 0.25 * y[0] + 0.3 * y[1] >= 3000)
@constraint(m, 0.2 * x[1] + 0.25 * x[2] - y[2] + 0.15 * y[0] + 0.3 * y[1] + 0.4 * y[2] >= 3000)
@constraint(m, 0.15 * x[1] + 0.2 * x[2] - y[3] + 0.2 * y[0] + 0.2 * y[1] + 0.3 * y[2] + 0.5 * y[3] >= 2000)
@constraint(m, 0.05 * x[1] + 0.15 * x[2] + 0.1 * y[0] + 0.2 * y[1] + 0.3 * y[2] + 0.5 * y[3] >= 1000)
@constraint(m, x[1] + x[2] + y[0] + y[1] + y[2] + y[3] <= 20000)
@objective(m, Min, 50 * x[1] + 70 * x[2] + 25 * (y[0] + y[1] + y[2] + y[3]))
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
Y = value.(y)
println("X: ", X)
println("Y: ", Y)
