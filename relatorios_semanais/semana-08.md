# Semana 08 (2026-10-9 a 2026-11-15)

**Horas dedicadas:** ~10 h · **Bloco do plano:** LOIO

---

## 1. Lido

- **Lopez-Otin et al. (2023)**, Retido: 
 12 Hallmarks of aging e explicação de todos os mecanismos.

Artigos diversos para a tese 

## 2. Escrito

Mudança da estrutura da tese, foram escritos todos os primary hallmarks of aging e os seus mecanismos

## 3. Executado

- **Comando/notebook:** `src/clocks/hyperparameter_tuning.py`
- **Entrada:** `table_Zenodo_complete.csv`, `Expression_data_absolute_rodents_Scaled.csv`
- **Resultado:** Hiperparametros otimizados de acordo com os procedimentos do estudo para cada dataset
- **Guardado:** `results/hyperparameters_mortality_LODO.csv`

## 4. Números da semana

Os números da semana são os hiperparametros do relógio de mortalidade, que estão guardados em `results/hyperparameters_mortality_LODO.csv`

## 5. Bloqueado

Valores de R do relógio de mortalidade em LOIO e LODo

## 6. Decisões tomadas

- Utilizar Azure para correr os scripts eventualmente, se possível, HPC fornecido pela fct.
  
## 7. Plano para a próxima semana

- Obter predictions do relógio de mortalidade (LODO), calcular R. Fazer o mesmo em LOIO e comparar correlações.
- Acabar a contextualização dos hallmarks of aging e começar outras subsections