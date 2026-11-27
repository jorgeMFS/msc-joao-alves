# Desvios do Pré registo 25/11/26

- Quando nenhum controlo do grupo tem Expected_Hazard, centrar a expressão em todos os controlos do grupo. No GSE149029 nenhum controlo tem Expected_Hazard, a centragem dá NaN em tudo e as 19 previsões saem iguais, o que dá ΔtAge zero às 3 famílias. 

- As 3 amostras de fígado do GSE124772 não têm controlos de fígado. Saem do treino e também passam a sair do teste porque não dá para calcular o efeito das intervenções.