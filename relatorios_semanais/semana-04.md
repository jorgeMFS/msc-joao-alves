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

## 2. Escrito

- Foi escrito o código da replicação do estudo (`tAge_replication.rmd`), no caso o cálculo do valor D (D=obtained-expected).

## 3. Executado

- **Comando/notebook:** `experiments/replication/tAge_replication.rmd`
- **Resultado:** valores de D muito dispersos
- **Guardado em:** `replication/calculod.csv` e `replication/tAge_replication.Rmd`

A versão do sklearn usada na replicação é 1.9.1

## 4. Números da semana

- Samples: 161
- Controlos: 55

Em relação aos resultados da replicação, nomeadamente para descobrir que grupo de controlos foi utilizado, ainda não se chegou a nenhuma conclusão, visto que os valores de D variam imenso.

## 5. Bloqueado

Descobrir que grupos de controlos foram utilizados no estudo. Descobrir que regime de rapamycin foi utilizado no estudo.

## 6. Decisões tomadas

Passar a calcular-se o D (D=obtained-expected) no script de replicação.

## 7. Plano para a próxima semana

Confirmar que regime de rapamycin usar
Confirmar que grupos de controlos usar