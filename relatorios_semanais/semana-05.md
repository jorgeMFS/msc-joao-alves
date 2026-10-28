# Semana 05 (2026-10-12 a 2026-10-18)

**Horas dedicadas:** ~12 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (Metodologia) Retido: 

**Ideia inical para obter os grupos de controlos**
Como tivemos o problema dos grupos para calcular a mediana dos controlos não estar explícito, surgiu a ideia de calcular o valor D. Ou seja, os modelos são lineares    f(x)=b+w·x. Subtraindo a mediana (m) dos controlos de um grupo, dá f(x-m)=b+w·(x-m), que é igual a f(x-m)=f(x)-w·m. Mudando a referencia dos controlos não altera o declive, então todas as previsões são deslocadas por uma constante.

Então para testar, o objetivo era calcular para cada amostra: D=obtained-expected, no caso D=previsao-Expected_Hazard.log10. Se os valores de D fossem iguais dentro de cada grupo, esse seria o grupo usado. Ordenando o D e fazendo um scatterplot daria para obter esses patamares, revelando os grupos.

No entanto, **Expected_hazard.log10** não é o valor obtido através dos clocks, então não pode ser expected, porque não é calculado pelo f(x)=b+w·x mas sim pelo modelo de Gompertz. Acaba por ser o valor que devia ser o "objetivo" dos clocks.

---

**Kaplan-Meier**

O método Kaplan-Meier estima a probabilidade de um animal sobreviver para além de determinado tempo.

Imagina que acompanhas 100 ratinhos de controlo e 100 tratados com um fármaco. Alguns morrem durante o estudo, enquanto outros são retirados vivos ou chegam ao fim do acompanhamento sem que a sua morte seja observada.

Kaplan–Meier utiliza os tempos de seguimento disponíveis para estimar a curva de sobrevivência de cada grupo, considerando corretamente os animais censurados.

A mediana de sobrevivência é o tempo em que a curva estimada desce até 50%. Essa percentagem é referente à proporção de ratinhos que estaria viva nesse momento.

*Vantagens*
- Permite comparar longevidade entre tratados e controlos
- Tem em conta os ratinhos censurados
- É não paramétrico

*Desvantagem*
- Se por acaso os ratinhos do C2015 viverem mais tempo por alguma razão relacionada com as condições experimentais. Se os ratinhos tratados estão sobretudo no C2015 e os controlos sobretudo no C2016, podemos atribuir ao fármaco uma diferença que se deve ao cohort.

**Cox Proportional Hazard Regression**

O modelo de Cox, tenta perceber quanto é que as váriaveis (sexo, fármaco, cohort) estão associadas ao hazard (probabilidade do ratinho morrer)

Dão uma tabela com as variáveis escolhidas e coeficientes, em que valores próximos de 0 têm pouca ou nenhuma associação ao hazard, valores positivos ou negativos estão positiva- ou negativamente associados. O exp(coeficiente) é parecido mas é mais interpretável, e em vez de 0 ser o valor com pouca associação, é o 1.

No fundo, o Kaplan-Meier dá informação em cada grupo (Sex_Intervention) sobre a probabilidade de um ratinho desse grupo sobreviver além do tempo t., enquanto Cox dá informação sobre se as variáveis estão associadas ou não ao hazard.


## 2. Escrito

- Foi escrito o código para gerar o `table_Zenodo`, `metadata_preprocessing`
- Foi escrito o código da replicação do estudo (`tAge_replication.rmd`), nomeadamente usar apenas o All_Controls para calcular a mediana dos controlos, e gerar os valores de R (Pearson) para a mortalidade com e sem os ratinhos jovens.
- Código `potencia.rmd` em que se cria dados fictícios para 20 fármacos diferentes, com efeito real (Lifespan_Effect), efeitos preditos pelos modelos cronológicos e de mortalidade (Chronological_Effect e Mortality_Effect), através de diferentes valores decorrelções entre os modelos e os valores reais. O resultado são médias de ΔR (R(mortalidade - cronologico), utilizando a correlação de Pearson.

## 3. Executado

- **Comando/notebook:** `experiments/potencia/potencia.rmd`
- **Resultado:** Tabela de dados simulada com media dos ΔR
- **Guardado em:** `results/potencia_results.csv` 

- **Comando/notebook:** `experiments/preprocessing/ITP_preprocessing.rmd`
- **Entrada:** `data/raw/ITP_C2015_Lifespan.xlsx`, `data/raw/ITP_C2016_Lifespan.xlsx`, `data/raw/ITP_C2017_Lifespan.xlsx` e `results/table_zenodo_mpd_id`
- **Resultado:** Tabela pre-processada dos dados ITP provenientes do MPD
- **Guardado em:** `results/table_ITP_Lifespan_Data.csv` 

- **Comando/notebook:** `experiments/preprocessing/metadata_preprocessing.rmd`
- **Entrada:** `data/raw/Data_annotation_absolute_rodents.xlsx` e `results/table_zenodo_mpd_id`
- **Resultado:** Tabela pre-processada dos metadados
- **Guardado em:** `results/tabela_Zenodo.csv` (eventualmente mudar o nome para um nome em inglês e standard em todos os scripts)

- **Comando/notebook:** `experiments/replication/tAge_replication.rmd`
- **Entrada:** `results/tabela_Zenodo.csv` e `results/table_ITP_Lifespan_Data.csv`
- **Resultado:** Valores de R próximos de 1. Valores preditos próximos dos expectados.
- **Guardado em:** `replication/tAge_replication_results.csv`

- **Comando/notebook:** `experiments/interventions/intervention.rmd`
- **Entrada:** `results/table_ITP_Lifespan_Data.csv`
- **Resultado:** Tabela com Mediana (Kaplan-Meier) , P-Value (Log Rank Test), Hazard Ratios e IC 95% (Cox Model): `interventions/interventions.csv`
- **Guardado em:** `interventions/interventions.rmd`
  
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
- survminer  0.5.2

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

- Não se continuou com a ideia de calcular os valores D
- Utilizar todos os controlos para calcular a média.
- Para já, utilizar a Rapamycin Continuous (standby)
- Para o interventions.csv, usar o Kaplan-Meier

## 7. Plano para a próxima semana
