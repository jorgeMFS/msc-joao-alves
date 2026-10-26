# Semana 06 (2026-10-19 a 2026-10-25)

**Horas dedicadas:** ~12 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Schaum et al.]** (Abstract e Introdução) Retido: 
Os DEGs na early life têm overlap com os DEGs na late life.
O envelhecimento provoca alterações progressivas na expressão genética, com diferenças no momento de início e na intensidade entre órgãos.
Foram identificadas trajetórias de expressão genética associadas à disfunção mitocondrial, à proteostase, à matriz extracelular e à resposta imunitária.
Os tecidos adiposos apresentam alterações associadas à inflamação relativamente cedo, incluindo acumulação de células imunitárias.
A expressão do gene Igj, associado a células plasmáticas, aumenta com a idade em 11 dos 17 órgãos estudados.
Foram encontradas correlações entre a expressão genética nos órgãos e os níveis de proteínas no plasma, sugerindo possíveis ligações entre alterações locais e envelhecimento sistémico.
Os padrões moleculares do envelhecimento são parcialmente comuns entre órgãos, mas diferem na sua evolução e intensidade.

- **[CAST (1989)]**  Retido: 
O estudo CAST avaliou se a supressão de arritmias ventriculares com medicamentos antiarrítmicos melhorava a sobrevivência após um enfarte do miocárdio.
Apesar de a encainida e a flecainida reduzirem as arritmias, a mortalidade foi superior nos doentes tratados com estes fármacos, comparativamente ao placebo (7,7% vs. 3,0%).
A melhoria de um marcador intermédio não implica necessariamente um benefício clínico, podendo até coexistir com efeitos prejudiciais.
A eficácia de um tratamento deve, por isso, ser avaliada pelo seu impacto nos outcomes clínicos relevantes, como a sobrevivência, e não apenas pela melhoria de marcadores substitutos.

## 2. Escrito

- Foi escrito o código para gerar o `table_Zenodo_full.csv` contendo todos os samples, `metadata_preprocessing_full.Rmd`
  
- Foi adicionado ao código `potencia.Rmd` um segundo cenário.
  
A simulação pretende avaliar se o número de intervenções disponíveis é suficiente para comparar o relógio de mortalidade e o relógio cronológico na previsão dos efeitos reais das intervenções na longevidade (Lifespan_Effect).

Para isso, são gerados dados simulados e o processo de comparação é repetido várias vezes. Em cada simulação, calcula-se a diferença entre as correlações dos dois relógios com os efeitos reais:

ΔR = R(mortalidade) - R(cronológico)

Como cada simulação produz um resultado ligeiramente diferente, obtém-se uma distribuição de valores de ΔR.

*Percentile Range*

O Percentile_Range mede a amplitude dos 95% centrais da distribuição simulada de ΔR, calculada pela diferença entre os percentis 97.5 e 2.5 (na prática, qual o valor maximo de diferença em que os relogios continuam a ser iguais):

Um valor menor indica menor variabilidade na diferença estimada entre os relógios, enquanto um valor maior indica maior incerteza.

Este indicador permite avaliar como o número de intervenções influencia a precisão da comparação. Por exemplo, um número reduzido de intervenções pode produzir um Percentile_Range elevado, dificultando a distinção entre os modelos.

Aplicação ao Desenho Experimental

A simulação será utilizada para avaliar diferentes números de intervenções e diferentes cenários de correlação entre os efeitos previstos e os efeitos reais. O objetivo é determinar se aproximadamente X intervenções permitem comparar os relógios com precisão suficiente.

Os resultados também ajudarão a definir a margem Δ a utilizar no pré-registo e a estabelecer uma regra de decisão antes da análise dos dados reais.

O Percentile_Range mede quanto a diferença varia de simulação para simulação
---
Foi escrito o `model_results_chronoage_vs_mortality.csv` com os valores preditos de todos os modelos pelos 161 samples.
Foi escrito o `drug_effects.csv` com o efeito dos fármacos por modelo. Isto é a média da previsão das amostras do fármaco menos a média dos controlos (660 dias).

Foi escrito o `potencia_corr_modelos`. Neste script ao invés de se utilizar o MASS::mvrnorm, passou a utilizar-se o chol(), porque os valores gerados pelo mvrnorm dependiam da máquina, mesmo usando o mesmo seed. Neste script passou-se a utilizar as colunas: Clock_LODO e Clock_LOIO, porque o objetivo passou a ser testar os valores máximos em que os relógios seriam considerados equivalentes. Para isso também se parou de adicionar noise a estas colunas, já que são valores observados. Fez-se um bootstrap em cada uma das 1000 simulações.

---

1. Porque abandonámos a comparação original entre os relógios?
Inicialmente, pretendíamos avaliar se o relógio cronológico e o relógio de mortalidade eram equivalentes, definindo uma margem de equivalência Δ, que representa a maior diferença entre os relógios que ainda consideraríamos aceitável.

Para definir Δ, simulámos um cenário de referência com 56 famílias. A largura do intervalo a 90% (percentis 5–95) foi de aproximadamente 0.56. O problema é que a diferença entre as correlações publicadas dos dois relógios era apenas 0.17 (0.53 - 0.36). Assim, uma margem de 0.56 seria demasiado permissiva, podendo levar-nos a concluir que os relógios eram equivalentes mesmo quando existia uma diferença relevante. Reduzir Δ para 0.17 exigiria mais de 500 famílias para demonstrar equivalência nas condições simuladas.

2. Nova abordagem: comparar LODO e LOIO
Passámos a comparar o desempenho do relógio de mortalidade com as duas estratégias de validação, usando as mesmas 56 famílias de intervenções.

Em 36 famílias, as previsões LODO e LOIO são exatamente iguais. Por exemplo, o BD só existe no dataset do ITP e não partilha componentes com outras intervenções, ou seja, exluindo o dataset ITP ou Intervention BD vai dar o mesmo reusltado para ambos. Em contrapartida, a CR aparece em oito datasets. O LODO exclui apenas um deles, enquanto o LOIO exclui também a CR dos restantes sete; por isso, os modelos e as previsões diferem.

As restantes 20 famílias incluem intervenções que aparecem em vários datasets ou que partilham componentes com intervenções de outros datasets.

Como 36 famílias têm previsões idênticas, grande parte da variabilidade comum cancela-se na comparação emparelhada. Definimos a diferença como:

Δr = r_LODO-r_LOIO

Se o limite inferior do intervalo de confiança a 90% (que é um IC bilateral, mas equivale a um 95% unilateral) desta diferença for superior a zero, existe evidência de que LODO apresenta uma correlação superior. Esta abordagem não precisa de uma margem de equivalência Δ.
1. Como funciona a nova simulação de potência?
O objetivo é estimar a frequência com que o teste deteta uma diferença relevante entre as duas estratégias.
Etapa 1 — Gerar 1000 conjuntos de dados simulados
Em cada simulação, geramos valores para três variáveis — lifespan, LODO e LOIO — para 56 famílias, respeitando uma matriz de correlações definida previamente:
- Correlação entre lifespan e LODO: 0.53.
- Correlação entre lifespan e LOIO: 0.36.
Estes valores vêm dos resultados publicados como referência e representam uma diferença esperada de 0.17. Não são calculados a partir de cada conjunto de dados simulado.

Também variamos a correlação entre as previsões LODO e LOIO (0.8, 0.9 e 0.95) para avaliar como a semelhança entre os métodos afeta a potência.

Repetimos a simulação 1000 vezes porque um único conjunto de dados não permite estimar de forma fiável a frequência com que o teste deteta a diferença.
Etapa 2 — Aplicar bootstrap 1000 vezes em cada simulação
Em cada conjunto de dados simulado, fazemos 1000 reamostragens bootstrap das 56 famílias, com reposição. Em cada reamostragem, calculamos a correlação entre lifespan e cada método e, depois, a diferença entre as duas correlações.

É essencial utilizar as mesmas famílias reamostradas para LODO e LOIO, preservando a comparação emparelhada.

As 1000 reamostragens permitem estimar a distribuição da diferença e construir um intervalo de confiança a 90%, entre os percentis 5 e 95. Assim, cada simulação produz um intervalo que nos permite avaliar se o teste detetaria uma vantagem de LODO.
Etapa 3 — Estimar a potência
Em cada uma das 1000 simulações, verificamos se o limite inferior do intervalo de confiança a 90% é superior a zero.
- Se for superior a zero: o teste deteta evidência de que LODO tem uma correlação maior do que LOIO.
- Se não for superior a zero: o teste não consegue demonstrar essa superioridade nessa simulação. Isto não significa que LOIO seja melhor.
A potência estimada é a proporção de simulações em que o limite inferior fica acima de zero. Por exemplo, se isso acontecer em 900 das 1000 simulações, a potência estimada é de 90%.
1. O que esperamos aprender com os diferentes cenários?
Quanto maior for a correlação entre as previsões LODO e LOIO, mais semelhantes tendem a ser os métodos e maior pode ser a precisão da comparação entre eles.

Deste modo, avaliamos se o teste tem potência suficiente para detetar uma diferença relevante, considerando diferentes graus de semelhança entre os dois métodos.
---



## 3. Executado

- **Comando/notebook:** `experiments/potencia/potencia.Rmd`
- **Resultado:** Tabela de dados simulada com media dos ΔR para 20, 41 e 56 interventions
- **Guardado em:** `results/potencia_results.csv` 

- **Comando/notebook:** `experiments/preprocessing/metadata_preprocessing_full.Rmd`
- **Entrada:** `Data_annotation_absolute_rodents.xlsx`
- **Resultado:** Tabela pre-processada dos metadados provenientes do Zenodo
- **Guardado em:** `table_Zenodo_full.csv`

- **Comando/notebook:** `experiments/model_results/model_results_chronoage_vs_mortality.Rmd`
- **Entrada:** `Expression_data_absolute_rodents_Scaled.csv` e `table_Zenodo.csv`
- **Resultado:** Efeito de cada fármaco, por modelo.
- **Guardado em:** `drug_effects.csv`

- **Comando/notebook:** `experiments/model_results/model_results_chronoage_vs_mortality.Rmd`
- **Entrada:** `Expression_data_absolute_rodents_Scaled.csv` e `table_Zenodo.csv`
- **Resultado:** Dados preditos por cada modelo, por sample
- **Guardado em:** `model_results_chronoage_vs_mortality.csv`

- **Comando/notebook:** `experiments/potencia/potencia_corr_modelos.Rmd`
- **Entrada:** `results/drug_effects.csv`
- **Resultado:** Versão 2 do `Potencia.Rmd` com a correlação entre os modelos e os dados reais substituída pela correlação real entre os modelos de mortalidade e cronologia. chol() ao invés do mvrnorm e bootstraps por cada simulação. Realização de um teste unilateral de diferença.
Os valores de correlação entre o modelo
- **Guardado em:** `results/potencia_results_corr_between_models.csv`

## 4. Números da semana

Percentile_Range da diferença entre as correlações dos relógios de mortalidade e cronológico com os efeitos reais, para diferentes correlações entre o efeito previsto pelo modelo e o efeito real e diferentes números de intervenções.

**Correlation between Model and Real Effect**             **Percentile_Range(n=20)**      **Percentile_Range(n=41)**      **Percentile_Range(n=56)**

0                                                          0.783169                       0.527381                        0.461194
0.3                                                        0.741868                       0.506527                        0.471088
0.6                                                        0.628226                       0.419577                        0.353729
0.9                                                        0.402218                       0.250039                        0.219747


  
## 5. Bloqueado

## 6. Decisões tomadas

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 56 families (with control).
If interventions containing multiple regimes (e.g. Ercc1 + CR) have to be joined with its components, it will result in 41 families.
Parou de se utilizar o MASS no `potencia_corr_modelos` para se usar o chol(), porque os dados gerados pelo MASS dependiam da máquina em que estavam a ser gerados, mesmo com o mesmo seed.

## 7. Plano para a próxima semana
