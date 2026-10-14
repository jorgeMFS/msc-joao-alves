# Semana 05 (2026-10-12 a 2026-10-18)

**Horas dedicadas:** ~10 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (Metodologia) Retido: 

**Ideia inical para obter os grupos de controlos**
Como tivemos o problema dos grupos para calcular a mediana dos controlos não estar explícito, surgiu a ideia de calcular o valor D. Ou seja, os modelos são lineares    f(x)=b+w·x. Subtraindo a mediana (m) dos controlos de um grupo, dá f(x-m)=b+w·(x-m), que é igual a f(x-m)=f(x)-w·m. Mudando a referencia dos controlos não altera o declive, então todas as previsões são deslocadas por uma constante.

Então para testar, o objetivo era calcular para cada amostra: D=obtained-expected, no caso D=previsao-Expected_Hazard.log10. Se os valores de D fossem iguais dentro de cada grupo, esse seria o grupo usado. Ordenando o D e fazendo um scatterplot daria para obter esses patamares, revelando os grupos.

No entanto, **Expected_hazard.log10** não é o valor obtido através dos clocks, então não pode ser expected, porque não é calculado pelo f(x)=b+w·x mas sim pelo modelo de Gompertz. Acaba por ser o valor que devia ser o "objetivo" dos clocks.


## 2. Escrito

- Foi escrito o código para gerar o `table_Zenodo`, `metadata_preprocessing`
- Foi escrito o código da replicação do estudo (`tAge_replication.rmd`), nomeadamente usar apenas o All_Controls para calcular a mediana dos controlos, e gerar os valores de R (Pearson) para a mortalidade com e sem os ratinhos jovens.

## 3. Executado

- **Comando/notebook:** `experiments/preprocessing/metadata_preprocessing.rmd`
- **Resultado:** Tabela pre-processada dos metadados
- **Guardado em:** `results/tabela_Zenodo.csv` (eventualmente mudar o nome para um nome em inglês e standard em todos os scripts)

- **Comando/notebook:** `experiments/replication/tAge_replication.rmd`
- **Resultado:** Valores de R próximos de 1. Valores preditos próximos dos expectados.
- **Guardado em:** `replication/tAge_replication_results.csv`
  
**Versões de ficheiros e packages** 
Do MPD (https://phenome.jax.org/projects/ITP1)

- ITP_C2015_Lifespan.xlsx                             (14-10-2026)
- ITP_C2016_Lifespan.xlsx                             (14-10-2026)
- ITP_C2017_Lifespan.xlsx                             (14-10-2026)

Do Zenodo Version v2 (https://zenodo.org/records/22166800)

- Expression_data_absolute_rodents_Scaled.csv         (14-10-2026)
- Data_annotation_absolute_rodents.xlsx               (14-10-2026)   md5:c4f51562c38ab278dbb3b4b8fb7f64cc
- Expression_data_absolute_rodents_Scaled.csv         (14-10-2026)   md5:3b182622809b1361a6266f119102d017
- EN_Chronoage_Mouse_Multitissue_scaleddiff.pkl       (14-10-2026)   md5:c31d3b5ea8af7aa0891aee12d95109b5
- EN_Chronoage_Rodents_Liver_scaleddiff.pkl           (14-10-2026)   md5:a73012b22b5f4bc9881edd1ac2b0cb72
- EN_Chronoage_Rodents_Multitissue_scaleddiff.pkl     (14-10-2026)   md5:19fee9e782b4eda36ab13a459fcdb3db
- EN_Mortality_Mouse_Multitissue_scaleddiff.pkl       (14-10-2026)   md5:43ee221e8cbe8577107f1a74230891e0
- EN_Mortality_Rodents_Liver_scaleddiff.pkl           (14-10-2026)   md5:cd76d203c42f88a7580707c36a7e4a0b 
- EN_Mortality_Rodents_Multitissue_scaleddiff.pkl     (14-10-2026)   md5:26cc9e089e45bf978205738e56f190fb

- here       1.0.2
- readxl     1.5.0.1
- stringr    1.6.0
- reticulate 1.47.0
- tAge       1.5.0
- Biobase    2.72.0
- ggplot2    4.0.3

A versão do sklearn usada na replicação é 1.9.1

O ficheiro `data_annotation_absolute_rodents.csv` usado foi o md5:c4f51562c38ab278dbb3b4b8fb7f64cc (importante distinguir, pois um ficheiro mais antigo continha alterações)

## 4. Números da semana

Valores de R (Pearson) para mediana calculada com All_Controls para cada modelo:
É calculada a correlação com todos os samples (n=161) ou com apenas os ratinhos mais velhos (n=150)

**Modelos**                       **R(n=161)**     **R(n=150)**
*Mortality_Mouse_Multitissue*     0.90             0.68
*Mortality_Rodents_Liver*         0.75             0.32
*Mortality_Rodents_Multitissue*   0.97             0.89

## 5. Bloqueado

## 6. Decisões tomadas

Não se continuou com a ideia de calcular os valores D
Utilizar todos os controlos para calcular a média.
Para já, utilizar a Rapamycin Continuous (standby)

## 7. Plano para a próxima semana
