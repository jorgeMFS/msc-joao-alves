<!-- Copiar este ficheiro para semana-NN.md todas as sextas (semana-01.md, semana-02.md, ...). -->

# Semana 04 (2026-10-05 a 2026-10-12)

**Horas dedicadas:** ~10 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (Metodologia) Retido: 
# Pipeline

**Expression data → RLE → Scaling → Control subtraction → Relative targets → Model**

## RLE — Relative Log Expression

**O quê?**
Método de normalização da expressão génica que compara a expressão de cada gene com uma referência.

**Para quê?**
Corrigir diferenças técnicas entre amostras, como diferenças no número total de reads, para que estas não sejam confundidas com diferenças biológicas.

**Exemplo:**

* Amostra A → 1 milhão de reads
* Amostra B → 2 milhões de reads

* A → 1 000 reads
* B → 2 000 reads

Parece que o gene está **2× mais expresso em B**, mas na realidade B simplesmente tem o dobro das reads. O RLE ajuda a corrigir este tipo de diferença técnica, permitindo comparar a expressão de forma relativa.

**Ideia principal:**
Garantir que diferenças na expressão entre amostras refletem sobretudo diferenças biológicas e não diferenças técnicas.

**No código:**
Seria no `tAge_preprocessing` mas eu usei os dados já scaled

---

## Scaling

**O quê?**
Standardização dos valores das features, normalmente através de:

(x - mean) / SD

**Para quê?**
Colocar os genes/features numa escala comparável, evitando que valores com escalas maiores tenham demasiado peso no modelo.

**Resultado:**
Valores centrados em aproximadamente 0, com SD ≈ 1.

**No código:**
Seria no `tAge_preprocessing` mas eu usei os dados já scaled

Yugene é uma alternativa usada no artigo mas não faz parte do pipeline que é replicado no nosso estudo.
**Yugene** - Transformação dos valores de expressão baseada na distribuição dos genes dentro de cada amostra.
---

## Control Subtraction

**O quê?**
Subtrai à expressão de cada amostra o valor de referência do grupo Control.

**Para quê?**
Transformar expressão absoluta em **expressão relativa ao controlo** e reduzir diferenças basais entre grupos.

**Exemplo:**
sample − median(control)

**No código:**
`subtract\_by()`
---

## Relative Targets / Centering

**O quê?**
O mesmo princípio do control subtraction, mas aplicado ao **target** em vez da expressão.

**Para quê?**
Transformar o target absoluto num valor relativo à referência, permitindo ao modelo aprender o **desvio relativamente ao esperado**.

**No código:**
`center_by`
---

## Relative Clock

**Absolute clock:**
Prevê o valor absoluto, por exemplo: idade = 70.

**Relative clock:**
Prevê a diferença relativamente à referência, por exemplo: +10.

**Para quê?**
Focar o modelo na diferença biológica relativamente ao grupo de referência, em vez de simplesmente prever o valor absoluto.

---

## 2. Escrito

- Foi escrito o código completo da replicação do estudo (`tAge_replication.rmd`)


## 3. Executado


- **Comando/notebook:** `experiments/replication/tAge_replication.rmd`
- **Entrada:** (`data/raw/Expression_data_absolute_rodents_Scaled.csv`, e `results/table_Zenodo.csv`, 161 amostras)
- **Resultado:** Valores de R (Pearson) mais altos para o grupo de todos os controlos (0.90, 0.75 e 0.97)
- **Guardado em:** `replication/tAge_replication_results.csv/` e `replication/tAge_replication.png`

A versão do sklearn usada na replicação é 1.9.1

## 4. Números da semana

- Samples: 161
- Controlos: 55

Em relação aos resultados da replicação, é provável que o estudo tenha usado todos os controlos como um só grupo para calcular a mediana.
Os valores da correlação de Pearson obtidos referente a esse grupo são:

- Mortality_Mouse_Multitissue: 0.90
- Mortality_Rodents_Liver: 0.75
- Mortality_Rodents_Multitissue: 0.97


## 5. Bloqueado


## 6. Decisões tomadas

Entre as três intervenções da Rapamycin (Continuous, Start-Stop, Cycle) não se tinha a certeza de qual era utilizada na tabela do Zenodo. Sendo assim foi calculada a média de age dos ratinhos na tabela do ITP para comparar com a esperança média de vida, chegou-se à conclusão que o valor mais 

## 7. Plano para a próxima semana

Confirmar que intervenções usar
Remover rapamycin start-stop e continuous
Corrigir código Rmd e .py