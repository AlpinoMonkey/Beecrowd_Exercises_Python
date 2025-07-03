nome = input("")
salariof = float(input(""))
totaldevendase = float(input(""))
comissao = 0.15
salariocomissao = totaldevendase * comissao
salario = salariocomissao + salariof
print("TOTAL = R$ %.2f"%salario)