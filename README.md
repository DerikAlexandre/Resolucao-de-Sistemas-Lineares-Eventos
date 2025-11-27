Sistemas Lineares Aplicados ao Planejamento de Eventos

Este projeto utiliza métodos numéricos para resolver um sistema linear aplicado ao planejamento ideal de eventos ao longo de 5 anos, considerando restrições de consumo de bebidas e buscando o maior lucro possível.

O código resolve o sistema utilizando três métodos:

🔹 Métodos Implementados
Método	Tipo	Observação
Eliminação de Gauss	Direto	Fornece solução exata dentro da precisão numérica
Gauss-Jacobi	Iterativo	Convergência dependente da matriz
Gauss-Seidel	Iterativo	Convergência mais rápida que Jacobi
📌 Modelo matemático

O planejamento está baseado no seguinte sistema de equações:

5E1 + 1E2 + 1E3 = 3000   (Consumo total de Whisky)
3E1 + 4E2 + 1E3 = 5000   (Consumo total de Cerveja)
2E1 + 1E2 + 4E3 = 6000   (Consumo total de Champagne)


Onde:

E1 = Shows abertos ao público

E2 = Festas corporativas

E3 = Casamentos

O objetivo é encontrar a quantidade ideal de cada evento e calcular o lucro total ao final de 5 anos.

📈 Resultados exibidos pelo programa

O código imprime automaticamente:

✔ Quantidade ideal de cada tipo de evento
✔ Lucro total estimado e lucro médio anual
✔ Número de iterações de Jacobi e Seidel (comparação de desempenho)

▶️ Como executar
python main.py


Não é necessário instalar nenhuma dependência externa — apenas Python.

📚 Objetivo acadêmico

Este projeto foi desenvolvido com fins educacionais para demonstrar a aplicação de Álgebra Linear e Métodos Numéricos na resolução de problemas reais de planejamento e otimização.

Projeto desenvolvido para fins acadêmicos e de estudo em modelagem matemática e computação científica.