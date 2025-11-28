import numpy as np

def imprimir_resultados(metodo, solucao, iteracoes=None):
    print(f"\n--- Método: {metodo} ---")
    # A ordem das variáveis é: E1 (Shows), E2 (Festas), E3 (Casamentos)
    print(f"Shows (E1): {solucao[0]:.4f}")
    print(f"Festas Corp (E2): {solucao[1]:.4f}")
    print(f"Casamentos (E3): {solucao[2]:.4f}")
    
    if iteracoes:
        print(f"Iterações realizadas: {iteracoes}")
    
    # Função Objetivo: L = 3000*E1 + 5000*E2 + 6000*E3
    lucro = 3000*solucao[0] + 5000*solucao[1] + 6000*solucao[2]
    print(f"Lucro Estimado: R$ {lucro:,.2f}")

# --- DADOS DO PROBLEMA (Extraídos do PDF) ---
# Sistema: Ax = b
# 5E1 + 1E2 + 1E3 = 3000
# 3E1 + 4E2 + 1E3 = 5000
# 2E1 + 1E2 + 4E3 = 6000

A = np.array([[5, 1, 1],
              [3, 4, 1],
              [2, 1, 4]], dtype=float)

b = np.array([3000, 5000, 6000], dtype=float)

# Configurações iniciais para métodos iterativos
x_inicial = np.array([0, 0, 0], dtype=float)
tolerancia = 0.01
max_iteracoes = 100

print("=== RESOLUÇÃO DO ESTUDO DE CASO: PRODUTORA DE EVENTOS ===")

# 1. Solução Exata (Eliminação de Gauss / Numpy Solve)
solucao_exata = np.linalg.solve(A, b)
imprimir_resultados("Direto (Eliminação de Gauss)", solucao_exata)

# 2. Método de Gauss-Jacobi
def gauss_jacobi(A, b, x0, tol, max_iter):
    x = x0.copy()
    n = len(b)
    
    for k in range(max_iter):
        x_novo = np.zeros_like(x)
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_novo[i] = (b[i] - s1) / A[i][i]
        
        if np.linalg.norm(x_novo - x, ord=np.inf) < tol:
            return x_novo, k+1
        x = x_novo
    return x, max_iter

sol_jacobi, iter_jacobi = gauss_jacobi(A, b, x_inicial, tolerancia, max_iteracoes)
imprimir_resultados("Gauss-Jacobi", sol_jacobi, iter_jacobi)

# 3. Método de Gauss-Seidel
def gauss_seidel(A, b, x0, tol, max_iter):
    x = x0.copy()
    n = len(b)
    
    for k in range(max_iter):
        x_antigo = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - s1) / A[i][i] # Atualiza imediatamente
        
        if np.linalg.norm(x - x_antigo, ord=np.inf) < tol:
            return x, k+1
    return x, max_iter

sol_seidel, iter_seidel = gauss_seidel(A, b, x_inicial, tolerancia, max_iteracoes)
imprimir_resultados("Gauss-Seidel", sol_seidel, iter_seidel)