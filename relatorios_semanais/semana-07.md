# Semana 07 (2026-11-26 a 2026-11-01)

**Horas dedicadas:** ~10 h · **Bloco do plano:** LOIO

---

## 1. Lido

- **Prentice et al. (1989)**, Retido: 
 Prentice (1989) propõe uma definição restritiva de endpoint substituto: o marcador tem de capturar todo o efeito do tratamento sobre o desfecho, ou seja, dado o valor do marcador, o tratamento não pode ter efeito adicional no desfecho.
Isto implica que o efeito do tratamento tem de passar integralmente pelo marcador. Se o tratamento afetar o desfecho por outras vias que contornem o marcador (por exemplo, toxicidade ou outro mecanismo), o marcador falha como substituto, mesmo que esteja fortemente associado ao desfecho.
Por isso, a associação entre marcador e desfecho não basta, e a validade de um substituto depende dos tratamentos comparados (um marcador pode servir para uns fármacos e não para outros).
Relevância para a tese: fundamenta a distinção entre predição e substituição, e a necessidade de testar se os relógios acompanham o efeito de intervenções novas.


- **Moqri et al. (2024)**, (Até Application of different data sources) Retido: 
  Cada vez há mais interesse em procurar por biomarcadores para quantificar o aging e se estes biomarcadores servem como surrogate endpoints.
  Ainda não existe consenso em como estes devem ser validados


- **Yaneske et al. (2017)**, Retido: 
Ageing can be classified in two different ways, chronological ageing and biological ageing. While
chronological age is a measure of the time that has passed since birth, biological (also known as transcriptomic)
ageing is defined by how time and the environment affect an individual in comparison to other individuals of the
same chronological age. Recent research studies have shown that transcriptomic age is associated with certain genes,
and that each of those genes has an effect size. Using these effect sizes we can calculate the transcriptomic age of an
individual from their age-associated gene expression levels. The limitation of this approach is that it does not consider
how these changes in gene expression affect the metabolism of individuals and hence their observable cellular
phenotype.
  

## 2. Escrito

Pré-registo completo, com informações sobre como calcular os efeitos reais das intervenções, como agrupar os folds, etc.
Estrutura inicial da tese, assim como 2.1 Aging

## 3. Executado

- **Comando/notebook:** `src/clocks/loio.py`
- **Entrada:** `table_Zenodo_complete.csv`
- **Resultado:** Folds a ser usados no LOIO
  
- **Comando/notebook:** `src/clocks/lodo.py`
- **Entrada:** `table_Zenodo_complete.csv`
- **Resultado:** Folds a ser usados no LODO

## 4. Números da semana

LOIO: 81 folds
LODO: 63 folds

## 5. Bloqueado

## 6. Decisões tomadas

- Escolher estrutura da tese (Introduction, Background, Sota...)

## 7. Plano para a próxima semana

- Confirmar se o modelo perde desempenho com o LOIO
- Escrever maioria do background