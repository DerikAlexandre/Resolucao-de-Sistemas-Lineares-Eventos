# 📝 Sistema Linear Aplicado à Definição de Metas de Eventos

## Objetivo do Projeto

Este projeto, desenvolvido como parte da disciplina de **Álgebra Linear**, utiliza conceitos de **Cálculo Numérico** e **Sistemas Lineares** para resolver um caso real de uma produtora de eventos.

Com base no consumo de bebidas (whisky, cerveja e champagne) e nos lucros de cada tipo de evento, determina-se:

- **Quantos shows**
- **Quantas festas corporativas**
- **Quantos casamentos**

devem ser realizados ao longo de **5 anos**, visando **maximizar o lucro total** da empresa e respeitando as restrições de estoque.

Foram aplicados três métodos numéricos:

- 🔹 *Eliminação de Gauss* (método direto)  
- 🔹 *Gauss-Jacobi* (iterativo)  
- 🔹 *Gauss-Seidel* (iterativo)

---

## 📁 Estrutura do Repositório

### ✔ `ProjetoALEvento.py` — Solucionador dedicado ao caso real

Script responsável por resolver o sistema linear:

Ax = b

Ele:

- Calcula automaticamente **E1, E2 e E3**  
- Apresenta resultados por **Gauss, Jacobi e Seidel**  
- Compara a velocidade de convergência  
- Mostra **lucro total** e **lucro anual médio**

---

### ✔ `ProjetoAL.py` — Ferramenta universal n×n

Biblioteca generalista para resolver **qualquer sistema linear n × n**.

Inclui:

- ✔ Função para testar **diagonal dominante**
- ✔ Métodos:
  - Eliminação de Gauss  
  - Gauss-Jacobi  
  - Gauss-Seidel  
- ✔ Verificação automática de divergência  
- ✔ Geração de relatórios de iteração  
- ✔ Entrada flexível de qualquer matriz A e vetor b  

Ideal para outros problemas de engenharia, economia, física e otimização.

---

## Sistema Matemático Utilizado

O sistema utilizado no estudo de caso é:

<p align="center">
  <img width="320" height="120" src="https://github.com/user-attachments/assets/a71a1c55-4177-4dfd-a211-536bfc48a390" />
</p>

Onde:

- **E1** → Shows  
- **E2** → Festas Corporativas  
- **E3** → Casamentos  

---

## 📊 Resultados Obtidos

Os métodos convergiram aproximadamente para:

| Variável | Quantidade |
|---------|------------|
| **E1 (Shows)** | **≈ 200** |
| **E2 (Festas Corporativas)** | **≈ 800** |
| **E3 (Casamentos)** | **≈ 1200** |

**Lucro total estimado:**  
**R$ 11.800.000,00 a R$ 12.000.000,00**

*(variação depende do método e tolerância)*

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **NumPy**
- Execução recomendada:
  - VSCode  
  - PyCharm  
  - Jupyter Notebook  

---

## 📌 Conclusão

O projeto demonstra a importância dos métodos numéricos estudados em **Álgebra Linear** para a tomada de decisões reais.  
A combinação entre métodos diretos e iterativos permitiu transformar dados históricos em **informações estratégicas**, definindo metas de produção viáveis e lucrativas.

---

## 👨‍💻 Desenvolvedores

| Nome | Função |
|------|--------|
| **DERIK ALEXANDRE ALVES DE ANDRADE** |
| **KAIC SOARES DE SOUZA** |
| **KATHELEAN SUYANE NORBERTO** |
| **PEDRO NOGUEIRA** | 
| **SAMUEL ABREU DO É** |
---
