import math

# Valores retirados da pesquisa
# Sistema de equações (Tabela 1 do PDF):
# 5E1 + 1E2 + 1E3 = 3000  (B1 - Whisky/Fardos)
# 3E1 + 4E2 + 1E3 = 5000  (B2 - Cerveja/Fardos)
# 2E1 + 1E2 + 4E3 = 6000  (B3 - Champagne/Fardos)

A = [[5.0, 1.0, 1.0],
     [3.0, 4.0, 1.0],
     [2.0, 1.0, 4.0]]

# Vetor b (Estoque)
b = [3000.0, 5000.0, 6000.0]

lucros = [3000.0, 5000.0, 6000.0]

print("====================================================")
print("SISTEMA LINEAR PARA DEFINICAO DE META DE EVENTOS")
print("====================================================")

def copiar_matriz(matriz):
    return [linha[:] for linha in matriz]

def multiplicar_vetor(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def norma_infinito(vetor): 
    return max(abs(x) for x in vetor)

def subtrair_vetores(v1, v2): 
    return [a - b for a, b in zip(v1, v2)]
 

# MÉTODO 1 — GAUSS 
def eliminacao_gauss(A, b):
    n = len(b) 
    Ab = copiar_matriz(A)
    for i in range(n):
        Ab[i].append(b[i])

    for i in range(n): # Eliminação Progressiva (transformar matriz em triangular superior)
        max_row = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > abs(Ab[max_row][i]):
                max_row = k
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i] # Trocando a linha atual com a linha do maior pivô

        for j in range(i + 1, n): 
            if Ab[i][i] == 0: continue # Se o pivo for = 0, ele pulaa
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i, n + 1):
                Ab[j][k] -= factor * Ab[i][k]

    x = [0.0] * n # Substituição Regressiva
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n]
        for j in range(i + 1, n):
            x[i] -= Ab[i][j] * x[j]
        x[i] /= Ab[i][i]
    
    return x

print("\n=== MÉTODO 1 — ELIMINAÇÃO DE GAUSS ===")
solucao_gauss = eliminacao_gauss(A, b)
lucro_gauss = multiplicar_vetor(lucros, solucao_gauss)
print(f"E1 (Shows): {solucao_gauss[0]:.2f}")
print(f"E2 (Festas Corporativas): {solucao_gauss[1]:.2f}")
print(f"E3 (Casamentos): {solucao_gauss[2]:.2f}")
print(f"Lucro Total (5 anos): R$ {lucro_gauss:,.2f}")


# MÉTODO 2 — GAUSS-JACOBI 
def gauss_jacobi(A, b, x0, tol=1e-4, max_iter=100):
    n = len(b)
    x = x0[:]
    x_novo = [0.0] * n
    iteracoes = []

    for k in range(max_iter):
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - soma) / A[i][i]

        erro = norma_infinito(subtrair_vetores(x_novo, x))
        iteracoes.append((k + 1, x_novo[:], erro))

        if erro < tol:
            return x_novo, iteracoes
        
        x = x_novo[:]
    return x_novo, iteracoes


print("\n=== MÉTODO 2 — GAUSS-JACOBI ===")
x0 = [0, 0, 0]  # estimativa inicial neutra
solucao_jacobi, iter_jacobi = gauss_jacobi(A, b, x0)
print(f"Convergiu em {len(iter_jacobi)} iterações")
print(f"E1: {solucao_jacobi[0]:.2f}")
print(f"E2: {solucao_jacobi[1]:.2f}")
print(f"E3: {solucao_jacobi[2]:.2f}")


# MÉTODO 3 — GAUSS-SEIDEL 
def gauss_seidel(A, b, x0, tol=1e-4, max_iter=100):
    n = len(b)
    x = x0[:]
    iteracoes = []

    for k in range(max_iter):
        x_anterior = x[:]
        for i in range(n):
            soma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - soma) / A[i][i]

        erro = norma_infinito(subtrair_vetores(x, x_anterior))
        iteracoes.append((k + 1, x[:], erro))

        if erro < tol:
            return x, iteracoes
    return x, iteracoes


print("\n=== MÉTODO 3 — GAUSS-SEIDEL ===")
x0 = [0, 0, 0]
solucao_seidel, iter_seidel = gauss_seidel(A, b, x0)
print(f"Convergiu em {len(iter_seidel)} iterações")
print(f"E1: {solucao_seidel[0]:.2f}")
print(f"E2: {solucao_seidel[1]:.2f}")
print(f"E3: {solucao_seidel[2]:.2f}")


print("\n=== COMPARAÇÃO DE VELOCIDADE ===")
print(f"Gauss-Jacobi: {len(iter_jacobi)} iterações")
print(f"Gauss-Seidel: {len(iter_seidel)} iterações")
print(f"Gauss-Seidel foi {len(iter_jacobi) / len(iter_seidel):.2f}x mais rápido!")

print("==========================================")
print("=== META IDEAL DE EVENTOS PARA 5 ANOS ===")
print("==========================================")
print(f"- Shows abertos ao público {round(solucao_gauss[0])} eventos")
print(f"- Festas corporativas {round(solucao_gauss[1])} eventos")
print(f"- Casamentos {round(solucao_gauss[2])} eventos")
print("\n--> Lucro total estimado em 5 anos: R$ {:,.2f}".format(lucro_gauss))
print("--> Lucro médio anual: R$ {:,.2f}".format(lucro_gauss / 5))
print("=========================================================")

input("\nPressione ENTER para sair")