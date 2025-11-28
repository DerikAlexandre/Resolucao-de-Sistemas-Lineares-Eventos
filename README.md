📝 README — Sistema Linear Aplicado à Definição de Metas de Eventos
🎯 Objetivo do Projeto

Este projeto aplica conceitos de Cálculo Numérico e Sistemas Lineares para resolver um problema real de uma produtora de eventos.
Com base no consumo de bebidas (whisky, cerveja e champagne) e nos lucros obtidos por cada tipo de evento, determina-se:

Quantos shows,

Quantas festas corporativas,

Quantos casamentos

devem ser realizados ao longo de 5 anos para maximizar o lucro total da empresa, respeitando as limitações de estoque.

Para isso, foram aplicados três métodos numéricos:

Eliminação de Gauss (método direto)

Gauss-Jacobi (iterativo)

Gauss-Seidel (iterativo)

📁 Estrutura do Repositório
✔ ProjetoALEvento.py — Solucionador dedicado ao problema

Como parte integrante deste relatório e demonstrando a aplicação prática dos conceitos, foi desenvolvido um algoritmo em Python que replica fielmente o caso real da produtora de eventos, resolvendo o sistema linear:

A⋅x=b

O script:

Calcula automaticamente E1, E2 e E3 (shows, festas e casamentos)

Apresenta os resultados dos três métodos (Gauss, Jacobi e Seidel)

Compara a velocidade de convergência

Determina o lucro total estimado e o lucro médio anual

Esse arquivo representa a aplicação prática do estudo de caso.

✔ ProjetoAL.py — Ferramenta universal para sistemas lineares

Além do caso aplicado, desenvolvemos uma biblioteca generalista capaz de resolver qualquer sistema linear n×n.

O arquivo inclui:

Função para testar diagonal dominante automaticamente

Implementações modulares de:

Eliminação de Gauss

Gauss-Jacobi

Gauss-Seidel

Entrada flexível para qualquer matriz A e vetor b

Sistema de detecção de divergência

Função para gerar relatórios das iterações

Essa ferramenta permite que outros problemas de engenharia, economia, administração e otimização sejam resolvidos sem precisar reescrever os métodos.

🧮 Sistema Matemático Utilizado

O sistema do caso real é representado por:

\[
A =
\begin{bmatrix}
5 & 1 & 1 \\
3 & 4 & 1 \\
2 & 1 & 4
\end{bmatrix}
,\quad
b =
\begin{bmatrix}
3000 \\
5000 \\
6000
\end{bmatrix}
\]

Sendo:

E1 = Shows

E2 = Festas Corporativas

E3 = Casamentos

📊 Resultados Obtidos

Os métodos convergem aproximadamente para:

E1 ≈ 200 shows

E2 ≈ 800 festas corporativas

E3 ≈ 1200 casamentos

Lucro total aproximado:

R$ 11.800.000,00 a 12.000.000,00
(dependendo da precisão e do método)

🚀 Tecnologias Utilizadas

Python 3.10+

NumPy

Execução recomendada via VSCode, PyCharm ou Jupyter Notebook

📌 Conclusão

O projeto demonstra a importância dos métodos numéricos para tomada de decisão, transformando dados reais em informações estratégicas.
Combinando métodos diretos e iterativos, é possível analisar custos, prever limites e definir metas de produção de forma otimizada.