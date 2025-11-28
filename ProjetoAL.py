import numpy as np

class SolucionadorLinear:
    def __init__(self, A, b):
        self.A = np.array(A, dtype=float)
        self.b = np.array(b, dtype=float)
        self.n = len(b)
    
    def verificar_diagonal_dominante(self):
        
        print("\n--- Verificação de Convergência (Critério das Linhas) ---")
        dominante = True
        
        for i in range(self.n):
            diagonal = abs(self.A[i][i])
            soma_outros = sum(abs(self.A[i][j]) for j in range(self.n) if j != i)
            print(f"Linha {i+1}: |{diagonal}| > {soma_outros}? {'Sim' if diagonal > soma_outros else 'Não'}")
            
            if diagonal <= soma_outros:
                dominante = False
        
        if dominante:
            print(">> A matriz é Diagonal Dominante. Convergência garantida.")
        else:
            print(">> AVISO: A matriz NÃO é estritamente Diagonal Dominante. Risco de divergência.")
        
        return dominante
    
    def gauss_jacobi(self, x0=None, tol=0.01, max_iter=100):
        if x0 is None:
            x0 = np.zeros(self.n)
        
        x = x0.copy()
        print(f"\nIniciando Gauss-Jacobi (Tol={tol})...")
        
        for k in range(max_iter):
            x_novo = np.zeros_like(x)
            for i in range(self.n):
                soma = sum(self.A[i][j] * x[j] for j in range(self.n) if j != i)
                x_novo[i] = (self.b[i] - soma) / self.A[i][i]
            
            if np.linalg.norm(x_novo - x, ord=np.inf) < tol:
                return x_novo, k+1
            
            x = x_novo
        
        return x, max_iter
    
    def gauss_seidel(self, x0=None, tol=0.01, max_iter=100):
        if x0 is None:
            x0 = np.zeros(self.n)
        
        x = x0.copy()
        print(f"\nIniciando Gauss-Seidel (Tol={tol})...")
        
        for k in range(max_iter):
            x_antigo = x.copy()
            for i in range(self.n):
            
                soma = (sum(self.A[i][j] * x[j] for j in range(i)) +  
                        sum(self.A[i][j] * x_antigo[j] for j in range(i+1, self.n)))
                x[i] = (self.b[i] - soma) / self.A[i][i]
            
            if np.linalg.norm(x - x_antigo, ord=np.inf) < tol:
                return x, k+1
        
        return x, max_iter


def ler_sistema():
    print("=== FERRAMENTA GENERALISTA DE SISTEMAS LINEARES ===\n")
    
    n = int(input("Digite o número de equações/incógnitas: "))
    set
    print(f"\nDigite os coeficientes da matriz A ({n}x{n}):")
    A = []
    for i in range(n):
        print(f"Linha {i+1} (valores separados por espaço):")
        linha = list(map(float, input().split()))
        if len(linha) != n:
            print(f"ERRO: Esperava {n} valores, recebeu {len(linha)}. Tente novamente.")
            return ler_sistema()
        A.append(linha)
    
    print(f"\nDigite o vetor b ({n} valores, separados por espaço):")
    b = list(map(float, input().split()))
    if len(b) != n:
        print(f"ERRO: Esperava {n} valores, recebeu {len(b)}. Tente novamente.")
        return ler_sistema()
    
    return A, b


# --- EXEMPLO DE USO ---
if __name__ == "__main__":
    escolha = input("Usar exemplo pré-definido? (s/n): ").lower()
    
    if escolha == 's':
        print("\n=== USANDO EXEMPLO PRÉ-DEFINIDO ===")
        matriz_teste = [[5, 1, 1],
                        [3, 4, 1],
                        [2, 1, 4]]
        vetor_teste = [3000, 5000, 6000]
        print(f"Matriz A:\n{np.array(matriz_teste)}")
        print(f"Vetor b: {vetor_teste}")
    else:
        matriz_teste, vetor_teste = ler_sistema()
    
    solver = SolucionadorLinear(matriz_teste, vetor_teste)
    
    solver.verificar_diagonal_dominante() # 1. Verifica se vai convergir

    res_j, iter_j = solver.gauss_jacobi()    # 2. Resolver por Jacobi
    print(f"\n✓ Resultado Jacobi: {res_j}")
    print(f"  Iterações: {iter_j}")
    
    res_s, iter_s = solver.gauss_seidel()    # 3. Resolver por Seidel
    print(f"\n✓ Resultado Gauss-Seidel: {res_s}")
    print(f"  Iterações: {iter_s}")