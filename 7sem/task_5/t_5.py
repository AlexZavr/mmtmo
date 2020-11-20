from math import exp, factorial
import numpy as np

N = 2
limit = 2
lam = 3
v = 0.5
mu = 1 / v

alpha = lam / mu
print('alpha:', alpha)


def p1n(_n):
    return ((alpha ** (_n + 1) * sum([alpha ** i for i in range(N - _n + 1)])) /
            (sum([alpha ** i for i in range(N + 1)]))) * p_0_0


def pkn(_k):
    return (alpha ** (_k + N) /
            (factorial(_k) * sum([alpha ** i for i in range(N + 1)]))) * p_0_0


# а) вероятность того, что у раздаточного окна инструментальной кладовой никого из рабочих нет,
# и дежурный кладовщик свободен от выдачи
# \ p(0,0)
t_1 = sum([alpha ** (-i) for i in range(N + 1)])
t_2 = sum([(N - i + 1) * alpha ** (-i) for i in range(1, N + 1)])
p_1_0 = (alpha * t_1) / ((N + 1) * exp(alpha) + t_2)

p_0_0 = p_1_0 / alpha
print('Вероятность того, что у раздаточного окна инструментальной кладовой никого из рабочих нет, и дежурный '
      'кладовщик свободен от выдачи:\n', p_0_0)

# б) вероятности того, что на раздаче инструмента будет занято 1,2,3,...,7 кладовщиков
p_1_1 = ((alpha ** 2 * sum([alpha ** i for i in range(N - 1 + 1)])) / sum([alpha ** i for i in range(N + 1)])) * p_0_0
p_1_2 = ((alpha ** 3 * sum([alpha ** i for i in range(N - 2 + 1)])) / sum([alpha ** i for i in range(N + 1)])) * p_0_0

p = [
    [p_1_0],
    [p_1_1],
    [p_1_2]
]

for i in range(N + 1):
    for k in range(2, 8):
        p[i].append((alpha ** (k + N) / (factorial(k) * sum([alpha ** i for i in range(N + 1)]))) * p_0_0)

p = np.array(p)
p_k = [p.transpose()[k].sum() for k in range(7)]
print('\nВероятности того, что на раздаче инструмента будет занято 1,2,3,...,7 кладовщиков:\n')
for k in range(7):
    print('p(', k + 1, ', n) = ', p_k[k], ', где n = 0,1,2.', sep='')
# в) вероятности того, что очередь не будет превышать N человек при условии,
# что на раздаче инструмента будет занято 1,2,3,...,7 кладовщиков
# \ p(1,0), p(2,0), p(3,0), p(4,0), p(5,0), p(6,0), p(7,0).
# \ p(1,1), p(2,1), p(3,1), p(4,1), p(5,1), p(6,1), p(7,1).
# \ p(1,2), p(2,2), p(3,2), p(4,2), p(5,2), p(6,2), p(7,2).
print('\nВероятности того, что очередь не будет превышать N человек при условии, что на раздаче инструмента будет '
      'занято 1,2,3,...,7 кладовщиков:\n')
for n in range(N + 1):
    for k in range(len(p[n])):
        print('p(', k + 1, ', ', n, ') = ', round(p[n][k], 4), sep='')
    print()

# г) среднее число занятых кладовщиков
# \ h_
h_ = sum([p1n(n) for n in range(N + 1)]) + \
     sum([k * sum([pkn(k) for _ in range(N + 1)]) for k in range(2, 150)])
print('М.о. числа занятых кладовщиков:', h_)

# д) среднее число рабочих, ожидающих в очереди
# \ b_
b_ = sum([n * p1n(n) for n in range(N + 1)]) + \
     sum([sum([n * pkn(k) for n in range(N + 1)]) for k in range(2, 150)])
print('М.о. числа рабочих, ожидающих в очереди:', b_)

# е) среднее время пребывания рабочих в очереди в ожидании выдачи инструмента
# \ w = b_ / lam
w_ = b_ / lam
print('М.о. времени пребывания рабочих в очереди:', w_)

# среднее число кладовщиков с условием
a = 90 / 100
s = p_0_0
k = 0
while s < a:
    s += p_k[k]
    k += 1

print('В среднем необходимых', k + 1,
      'кладовщиков, чтобы обеспечить обслуживание рвбочих в заданных условиях с гарантийной веоятностью не ниже 0.9')
