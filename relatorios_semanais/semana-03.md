<!-- Copiar este ficheiro para semana-NN.md todas as sextas (semana-01.md, semana-02.md, ...). -->

# Semana 02 (2026-09-28 a 2026-10-04)

**Horas dedicadas:** ~10 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (Abstract até pág. 6) Retido: O Interventions Testing Program (ITP) já avaliou mais de 50 fármacos em genetically heterogenous mice (UM-HET3) e identificou mais de 10 lifespan-extending treatments. Geraram dados RNA-seq de rataos UM-HET3 sujeitos a 20 intervenções ITP e integraram-nos com transcriptomas públicos e dados de sobrevivência e fizeram aging clocks.

## 2. Escrito

- Foi escrito o código completo da replicação do estudo (`tAge_replication.rmd`)

## 3. Executado


- **Comando/notebook:** `experiments/replication/tAge_replication.rmd`
- **Entrada:** (`data/raw/Expression_data_absolute_rodents_Scaled.csv`, e `results/table_Zenodo.csv`, 161 amostras)
- **Resultado:** Valores de R (Pearson) mais altos para o grupo de todos os controlos (0.90, 0.75 e 0.97)
- **Guardado em:** `replication/tAge_replication_results.csv/` e `replication/tAge_replication.png`


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

No script `tAge_replication` não é usada a tabela dos metadados completa, apenas com as amostras das intervenções estudadas.
É provável que o estudo tenha usado todos os controlos como um só grupo para calcular a mediana, já que foram obitdos os maiores valores de R de Pearson para esse grupo, sendo assim, esse será o grupo de controlos adotado.

## 7. Plano para a próxima semana

Confirmar que intervenções usar
Remover rapamycin start-stop e continuous
Corrigir código Rmd e .py