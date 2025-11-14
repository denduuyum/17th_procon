from problem import Problem
import problem
a = [\
     [1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0],
     [0, 1, 2, 3, 4],
     [5, 6, 7, 8, 9],
     [6, 7, 8, 9, 0]
    ]
N = 5
problem.rotate(a, 5, 1, 1, 3)
for i in range(N):
    for j in range(N):
        print(a[i][j], end = ' ')
    print()

print(problem.eval_score(a, 5))
