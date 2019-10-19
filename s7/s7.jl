using JuMP
using GLPK
using GLPKMathProgInterface

m = Model()
@variable(m, x[1:4] >= 0)
@variable(m, y[1:4] >= 0)
@variable(m, s[1:3] >= 0)
@constraint(m, [i=1:4], x[i] <= 1000)
@constraint(m, [i=1:4], y[i] <= 1000)
@constraint(m, 100 * x[1] + 80 * x[2] + 70 * x[3] + 60 * x[4] + s[1] == 100 * y[1] + 80 * y[2] + 70 * y[3] + 60 * y[4])
@constraint(m, 110 * x[1] + 90 * x[2] + 80 * x[3] + 50 * x[4] + s[2] == 110 * y[1] + 90 * y[2] + 80 * y[3] + 50 * y[4] + s[1] * 1.1)
@constraint(m, 1100 * x[1] + 1120 * x[2] + 1090 * x[3] + 1110 * x[4] + s[3] == 1100 * y[1] + 1120 * y[2] + 1090 * y[3] + 1110 * y[4] + s[2] * 1.1)
@objective(m, Max, 990 * x[1] + 985 * x[2] + 972 * x[3] + 954 * x[4] - 980 * y[1] - 970 * y[2] - 960 * y[3] - 940 * y[4])
println(m)

@time optimize!(m, with_optimizer(GLPK.Optimizer))

println("Objective value: ", objective_value(m))
X = value.(x)
Y = value.(y)
S = value.(s)
println("X: ", X)
println("Y: ", Y)
println("S: ", S)
