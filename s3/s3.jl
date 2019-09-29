using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[1:4] >= 0)
@constraint(m, [i=1:4], x[i] <= 0.4)
@constraint(m, sum(x[i] for i=1:4) <= 1)
@constraint(m, x[1] * 3 + x[2] * 4 + x[3] * 7 + x[4] * 9 <= 6)
@constraint(m, x[1] * 6 + x[2] * 8 + x[3] * 10 + x[4] * 9 >= 8)
@objective(m, Max, x[1] * 13 + x[2] * 8 + x[3] * 12 + x[4] * 14)
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
println("X: ", X)
