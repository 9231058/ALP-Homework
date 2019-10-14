using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[1:2, 1:2, 1:2] >= 0) # number of product that are generated [line][month][product]
@variable(m, s[1:2, 1:2] >= 0)
@constraint(m, x[1, 1, 1] * 0.15 + x[1, 1, 2] * 0.12 <= 800)
@constraint(m, x[2, 1, 1] * 0.16 + x[2, 1, 2] * 0.14 <= 2000)
@constraint(m, x[1, 2, 1] * 0.15 + x[1, 2, 2] * 0.12 <= 400)
@constraint(m, x[2, 2, 1] * 0.16 + x[2, 2, 2] * 0.14 <= 1200)
@constraint(m, 500 + x[1, 1, 1] + x[2, 1, 1] == s[1, 1] + 5000)
@constraint(m, 750 + x[1, 1, 2] + x[2, 1, 2] == s[2, 1] + 2000)
@constraint(m, s[1, 1] + x[1, 2, 1] + x[2, 2, 1] == s[1, 2] + 8000)
@constraint(m, s[2, 1] + x[1, 2, 2] + x[2, 2, 2] == s[2, 2] + 4000)
@constraint(m, s[1, 2] >= 1000)
@constraint(m, s[2, 2] >= 1000)
@objective(m, Min, 5 * (x[1, 1, 1] * 0.15 + x[1, 1, 2] * 0.12 + x[2, 1, 1] * 0.16 + x[2, 1, 2] * 0.14 + x[1, 2, 1] * 0.15 + x[1, 2, 2] * 0.12 + x[2, 2, 1] * 0.16 + x[2, 2, 2] * 0.14) + 0.2 * (s[1, 1] + s[2, 1]))
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
S = value.(s)
println("X: ", X)
println("S: ", S)
