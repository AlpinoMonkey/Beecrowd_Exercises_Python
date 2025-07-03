A , B , C = input().split()
A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
areatrianguloretangulo = (A*C)/2
areacirculo = pi * (C**2)
areatrapezio = ((A+B)*C)/2
areaquadrado = B**2
arearetangulo = A*B
print("TRIANGULO: %.3f"%areatrianguloretangulo)
print("CIRCULO: %.3f"%areacirculo)
print("TRAPEZIO: %.3f"%areatrapezio)
print("QUADRADO: %.3f"%areaquadrado)
print("REATNGULO: %.3f"%arearetangulo)