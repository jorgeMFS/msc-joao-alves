# Pré registo
## Nota
Todas as correlações usadas são de Pearson

## Hipótese primária (diferença, não equivalência)
Dado que para definir Δ, obtivemos uma margem demasiado permissiva (0.59, enquanto a diferença entre o R_Mortality e R_Chronological = 0.17), tivemos de optar por outra estratégia, já que reduzir o Δ para 0.17 tornaria o teste exigente demais (seriam necessárias mais de 500 famílias). Por isso passámos a testar a diferença:

O objetivo é avaliar se o relógio de mortalidade apresenta melhor capacidade preditiva em LODO do que em LOIO, ou seja, se a exclusão de intervenções relacionadas reduz a associação entre as previsões do relógio e o tempo de vida real.

Operacionalmente: comparamos a diferença emparelhada entre as correlações r_LODO - r_LOIO, nas mesmas 56 famílias. Consideramos que existe evidência de uma vantagem de LODO quando o limite inferior do intervalo de confiança de 90% é superior a zero.
Isto é um teste unilateral de superioridade. Não procuramos demonstrar equivalência entre os métodos, mas determinar se LODO apresenta uma correlação superior à de LOIO.

**Números de referência publicados:** 
*Para o relógio de mortalidade*
r ≈ 0.53 (LODO/Lifespan)

*Para o relógio cronológico*
r ≈ 0.36 (LODO/Lifespan)

## Definição de intervenção

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 57 families, however, the dataset containing Ercc1 + Hypoxia (GSE219203) doesn't have any controls, thus this dataset is withdrawn from LOIO when the model is predicting a family with Ercc1. The dataset is still present in the model training.

## Modelo e Hiperparâmetros
- O modelo a ser usado é uma regressão linear Elastic Net, em que os hiperparâmetros (alpha e l1_ratio) vão ser tuned através do GridSearchCV, usando GroupKFold = 5 por cada fold. Para escolher os melhores hiperparâmetros, é escolhido o modelo com maior R^2 médio das validações cruzadas.
- O grid usado no gridsearch vai ter o seguinte formato:
-"alpha": np.logspace(-5, 2, 15)
-"l1_ratio": [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1]

## Esquema de validação
- LODO tira do treino um dataset inteiro.
- LOIO exclui o dataset D (onde está o que vai ser predito) e, nos outros datasets, a família F e as que partilham componente com ela (por exemplo, para a RaAc saem também a Rapamycin e a Acarbose). O intervalo de confiança de 90% será calculado através de 10 000 reamostragens bootstrap emparelhadas ao nível das famílias. Em cada reamostragem, serão selecionadas as mesmas famílias para LODO e LOIO, com reposição, sendo recalculadas ambas as correlações e a respetiva diferença. 
Hiperparâmetros afinados dentro de cada fold. Usamos o Expected_Hazard.log10 do paper, já que este depende apenas do grupo de cada amostra (e as amostras F já saem do treino)

- Vão ser usados 57 grupos de intervenções, que corresponde a todas as famílias, ou seja, cada intervenção pertence a uma família, podendo pertencer a um ou dois componentes (e.g. RaAc não percence a "Rapamycin" e a "Acarbose" mas sim a uma família "Rapamycin-Acarbose", embora saia do treino quando se prevê ou a "Rapamycin" ou "Acarbose").
- Apenas uma das 57 famílias não tem controlo (Ercc1 + Hypoxia), por isso esta fica fora dosfolds, embora continue no treino do modelo, por isso na prática ficam 56 famílias avaliáveis, totalizando 81 folds para o LOIO.

## Regra de decisão
- Intervenções com os mesmos componentes principais são agrupadas numa única família, mesmo quando diferem na dose ou duração (por exemplo, 17aE2_16m e 17aE2_20m). As combinações de dois componentes constituem uma única família, mantendo-se cada componente identificado separadamente. A tabela com as intervenções distribuídas em famílias e componentes é `protocol/interventions_families_components.csv`.

As variantes pertencentes à mesma família serão agregadas num único ponto através de uma média simples dos respetivos efeitos dos grupos (mesmo dataset, intervenção, estirpe e sexo), de modo a obter uma estimativa única do efeito no tempo de vida por família.

O efeito de cada intervenção na longevidade será quantificado através do log(Estimate.Lifespan.99.9th_percentile_tratados / Estimate.Lifespan.99.9th_percentile_controlos), comparando os animais tratados com os respetivos controlos (mesmo dataset, estirpe e sexo). O ΔtAge é calculado nos mesmos grupos e agregado da mesma forma que o efeito no tempo de vida.

Vão ser utilizadas como covariáveis o tecido e idade no efeito do relógio.

Os 5 controlos do dataset `GSE149029` têm 1092 dias como máximo observado (Dollé et al. 2011 https://doi.org/10.3402/pba.v1i0.7219)

- Para cada família, será calculado um único efeito no tempo de vida, que servirá de referência para avaliar a associação entre os efeitos previstos pelos relógios e os efeitos reais das intervenções.


Para CI 90% = [X,Y]:
- Se X > 0 : O relógio de mortalidade perde desempenho quando não vê a intervenção.
- Se X =< 0 : Não se pode concluir que o relógio de mortalidade perde desempenho quando não vê a intervenção.

## Controlo do efeito da dimensão de treino

Para verificar que uma potencial diferença de desempenho entre o LOIO e LODO não se deva ao LOIO excluir mais samples do treino que o LODO, vai ser também treinado um segundo LODO retirando aleatoriamente o mesmo número de amostras tratadas que o LOIO perdeu. Essa remoção aleatória é feita entre famílias sem relaçao a F. Esta remoção vai ser repetida 1000x, em que o modelo é novamente treinado, calculando o R em cada iteração, obtendo-se um CI90% que vai ser utilizado.
  
## Comparação secundária entre os relógios
Para testar se o relógio de mortalidade (LOIO) tem melhor desempenho que o relógio cronológico a estatística passa a ser:

Δr = r_mortality - r_chronological

Depois passa-se a calcular o IC 90% através de um bootstrap (N = 10000) com emparelhamento entre famílias e verifica-se se o limite superior é inferior a 0.17 (0.53 - 0.36 = 0.17)

Para CI 90% = [X,Y]:
- Se X > 0.17 : O desempenho do relógio de mortalidade é superior ao desempenho do relógio cronológico
- Se X =< 0.17 : Não podemos dizer que o desempenho do relógio de mortalidade  é superior ao desempenho do relógio cronológico

## Análises secundárias
Dimorfismo sexual com canagliflozina. Substituição ao nível do ensaio (Buyse Molenberghs, só trial level, não há dados individuais emparelhados). Baseline aleatório e transcriptoma completo regularizado.

## Potência

Foram realizadas 1000 simulações independentes para cada cenário de correlação entre o LOIO e o Lifespan (0.36, 0.45, 0.53). Em cada simulação, foram gerados dados para 56 famílias, de acordo com as correlações definidas para cada cenário de correlação entre LOIO e LODO (0.8, 0.9 e 0.95). Para cada simulação, foi realizado um bootstrap emparelhado com 1000 reamostragens das famílias, com reposição, utilizando as mesmas famílias em LODO e LOIO em cada reamostragem. A partir da distribuição bootstrap da diferença entre as correlações de Pearson (r_LODO − r_LOIO), foi calculado o intervalo de confiança de 90%. A taxa de rejeição é a proporção das simulações em que o limite inferior foi superior a zero.

### Tabela 1 — Resultados das simulações

| nint | corr_LOIO_Lifespan | corr_between_models | Mean_delta_r | Percentile_Range_CI95 | Percentile_Range_CI90 | r_LODO | r_LOIO | n_LB_under_zero |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 56 | 0.36 | 0.80 | 0.164020 | 0.300515 | 0.246189 | 0.519664 | 0.355645 | 272 |
| 56 | 0.36 | 0.90 | 0.169677 | 0.228532 | 0.185943 | 0.524125 | 0.354448 | 53 |
| 56 | 0.36 | 0.95 | 0.166113 | 0.176487 | 0.141065 | 0.524728 | 0.358615 | 0 |
| 56 | 0.45 | 0.80 | 0.079275 | 0.284216 | 0.237093 | 0.529329 | 0.450054 | 693 |
| 56 | 0.45 | 0.90 | 0.080601 | 0.209259 | 0.172293 | 0.531803 | 0.451201 | 518 |
| 56 | 0.45 | 0.95 | 0.081251 | 0.152672 | 0.128928 | 0.529227 | 0.447976 | 278 |
| 56 | 0.53 | 0.80 | -0.002080 | 0.273406 | 0.229461 | 0.527792 | 0.529871 | 951 |
| 56 | 0.53 | 0.90 | 0.000011 | 0.204405 | 0.165872 | 0.530182 | 0.530172 | 941 |
| 56 | 0.53 | 0.95 | 0.000157 | 0.144280 | 0.122973 | 0.526080 | 0.525924 | 930 |

### Tabela 2 — Potência estatística

| nint | corr_LOIO_Lifespan | corr_between_models | n_LB_under_zero | taxa_rejeicao |
|---:|---:|---:|---:|---:|
| 56 | 0.36 | 0.80 | 272 | 0.728 |
| 56 | 0.36 | 0.90 | 53 | 0.947 |
| 56 | 0.36 | 0.95 | 0 | 1.000 |
| 56 | 0.45 | 0.80 | 693 | 0.307 |
| 56 | 0.45 | 0.90 | 518 | 0.482 |
| 56 | 0.45 | 0.95 | 278 | 0.722 |
| 56 | 0.53 | 0.80 | 951 | 0.049 |
| 56 | 0.53 | 0.90 | 941 | 0.059 |
| 56 | 0.53 | 0.95 | 930 | 0.070 |