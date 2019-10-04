using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[1:4] >= 0, Int)
@variable(m, y[1:4] >= 0, Int)
@constraint(m, x[1] + y[1] + x[4] + y[4] + y[3] >= 12)
@constraint(m, x[2] + y[2] + x[1] + y[1] + y[4] >= 8)
@constraint(m, x[3] + y[3] + x[2] + y[2] + y[1] >= 6)
@constraint(m, x[4] + y[4] + x[3] + y[3] + y[2] >= 15)
@objective(m, Min, sum(x[i] * 48 for i=1:4) + sum(y[i] * 84 for i=1:4))
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
Y = value.(y)
println("X: ", X)
println("Y: ", Y)
