def matryoshka(n):
    if n == 1:
        print("Min matryoshka")
    else:
        print("matryoshka top, n=", n)
        matryoshka(n-1)
        print("matryoshka bottom, n=", n)
matryoshka(10)

'''
import graphics as gr

window = gr.GraphWin("Russian game", 1000, 1000)
alpha = 0.11111111111111111111111

def fractal_rectangle(A, B, C, D, deep):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
    B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
    C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
    D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
    fractal_rectangle(A1, B1, C1, D1, deep-1)
    window.getMouse()
    window.close()
fractal_rectangle((50, 50), (950, 50), (950, 950), (50, 950), 100)
'''

def factorial(num):
    assert num>=0, "Factorial <0"
    if num == 0:
        return 1
    return factorial(num-1) * num
print(factorial(5))

def gcf(a, b):
    return a if b == 0 else gcf(b, a%b)
print(gcf(188, 400))

def exp(a, n):# a >= 0
    assert a>=0, "Number is less than 0"
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exp(a * a, n // 2) * a
    else:
        return exp(a, n-1) * a
print(exp(5, 5))

