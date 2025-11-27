Sistemas Lineares aplicados ao Planejamento Estratégico de Eventos

Este projeto calcula a quantidade ideal de eventos que uma empresa deve realizar ao longo de 5 anos para maximizar o lucro, respeitando as restrições do estoque de bebidas.
O problema é modelado como um sistema linear 3×3 e resolvido por três métodos numéricos.

🎯 Objetivo do problema

Determinar quantos eventos de cada tipo podem ser realizados:

Evento	Símbolo	Lucro por evento
Shows abertos ao público	E1	R$ 3.000
Festas corporativas	E2	R$ 5.000
Casamentos	E3	R$ 6.000

O consumo de bebidas por evento gera o sistema:

5E1 + 1E2 + 1E3 = 3000   (Whisky)
3E1 + 4E2 + 1E3 = 5000   (Cerveja)
2E1 + 1E2 + 4E3 = 6000   (Champagne)


A solução fornece a quantidade ideal de cada evento e o lucro total esperado.

🧠 Métodos Numéricos Implementados
Método	Tipo	Característica
Eliminação de Gauss	Direto	Solução exata dentro da precisão numérica
Gauss-Jacobi	Iterativo	Aproxima a solução via iterações sucessivas
Gauss-Seidel	Iterativo	Variação do Jacobi com convergência mais rápida

O programa também compara o desempenho entre Jacobi e Seidel.

📈 Resultados apresentados na execução

O programa exibe automaticamente:

Quantidade ideal de cada evento

Lucro total estimado por 5 anos

Lucro médio anual

Número de iterações de Jacobi e Seidel e comparação de velocidade

Exemplo de resumo visual final:

CONCLUSÃO FINAL — PLANEJAMENTO IDEAL
Shows abertos ao público: XX eventos
Festas corporativas:      XX eventos
Casamentos:               XX eventos

Lucro total estimado: R$ X.XXX.XXX,00
Lucro médio anual:    R$ XXX.XXX,00

▶️ Como executar
python main.py


Nenhuma biblioteca externa é necessária (apenas Python).

📌 Estrutura do repositório
main.py  → Implementação dos métodos numéricos + relatório final

🔬 Finalidade

Projeto desenvolvido com fins educacionais para demonstrar:

Modelagem matemática de problemas reais

Resolução de sistemas lineares via métodos numéricos

Comparação entre métodos diretos e iterativos