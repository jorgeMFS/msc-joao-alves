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


## 2. Escrito

- Foi escrito o código para gerar o `table_Zenodo_full.csv` contendo todos os samples, `metadata_preprocessing_full.Rmd`
  
- Foi adicionado ao código `potencia.Rmd` um segundo cenário.
  
A simulação pretende avaliar se o número de intervenções disponíveis é suficiente para comparar o relógio de mortalidade e o relógio cronológico na previsão dos efeitos reais das intervenções na longevidade (Lifespan_Effect).

Para isso, são gerados dados simulados e o processo de comparação é repetido várias vezes. Em cada simulação, calcula-se a diferença entre as correlações dos dois relógios com os efeitos reais:

ΔR = R(mortalidade) - R(cronológico)

Como cada simulação produz um resultado ligeiramente diferente, obtém-se uma distribuição de valores de ΔR.

*Percentile Range*

O Percentile_Range mede a amplitude dos 95% centrais da distribuição simulada de ΔR, calculada pela diferença entre os percentis 97.5 e 2.5:

Um valor menor indica menor variabilidade na diferença estimada entre os relógios, enquanto um valor maior indica maior incerteza.

Este indicador permite avaliar como o número de intervenções influencia a precisão da comparação. Por exemplo, um número reduzido de intervenções pode produzir um Percentile_Range elevado, dificultando a distinção entre os modelos.

Aplicação ao Desenho Experimental

A simulação será utilizada para avaliar diferentes números de intervenções e diferentes cenários de correlação entre os efeitos previstos e os efeitos reais. O objetivo é determinar se aproximadamente X intervenções permitem comparar os relógios com precisão suficiente.

Os resultados também ajudarão a definir a margem Δ a utilizar no pré-registo e a estabelecer uma regra de decisão antes da análise dos dados reais.

O Percentile_Range mede a incerteza da diferença estimada, enquanto a margem Δ define a diferença máxima entre os relógios que será considerada praticamente irrelevante. Estes conceitos estão relacionados, mas não são equivalentes.

## 3. Executado

- **Comando/notebook:** `experiments/potencia/potencia.Rmd`
- **Resultado:** Tabela de dados simulada com media dos ΔR para 20, 41 e 56 interventions
- **Guardado em:** `results/potencia_results.csv` 

- **Comando/notebook:** `experiments/preprocessing/etadata_preprocessing_full.Rmd`
- **Entrada:** `Data_annotation_absolute_rodents.xlsx`
- **Resultado:** Tabela pre-processada dos metadados provenientes do Zenodo
- **Guardado em:** `table_Zenodo_full.csv`

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

## 7. Plano para a próxima semana
