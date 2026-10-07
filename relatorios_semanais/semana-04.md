<!-- Copiar este ficheiro para semana-NN.md todas as sextas (semana-01.md, semana-02.md, ...). -->

# Semana 04 (2026-10-05 a 2026-10-12)

**Horas dedicadas:** ~10 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (Metodologia) Retido: O Interventions Testing Program (ITP) já avaliou mais de 50 fármacos em genetically heterogenous mice (UM-HET3) e identificou mais de 10 lifespan-extending treatments. Geraram dados RNA-seq de rataos UM-HET3 sujeitos a 20 intervenções ITP e integraram-nos com transcriptomas públicos e dados de sobrevivência e fizeram aging clocks.

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