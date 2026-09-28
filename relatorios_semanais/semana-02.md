<!-- Copiar este ficheiro para semana-NN.md todas as sextas (semana-01.md, semana-02.md, ...). -->

# Semana 02 (2026-09-21 a 2026-09-27)

**Horas dedicadas:** ~7 h · **Bloco do plano:** (ex.: 2-4, reproduzir valor publicado)

---

## 1. Lido

- **[Gladyshev-Lab]** (README.md). Retido: O diff dos modelos .pkl é calculado através da diferença de expressão entre o fármaco e a mediana dos controlos do grupo.
-

## 2. Escrito

- Foi criada a tabela table_ITP_Lifespan_Data que inclui todos os samples do ITP dos cohorts que vão ser utilizados numa só tabela.
- Foi criada a tabela table_Zenodo que exclui da tabela proveniente do Zenodo os samples que não são do ITP e altera a nomenclatura dos fármacos, seguindo a tabela de ligação, para que a nomenclatura dos fármacos seja igual em todas as tabelas. A esta tabela foi adicionada uma coluna Group que junta as colunas Sex e Cohort, já que o split_by() do tAge apenas aceita uma coluna, como pode ser visto em https://github.com/Gladyshev-Lab/tAge/blob/main/R/preprocessing.R.

## 3. Executado

O que correu de facto, com números. Se não correu nada, escrever "nada". É uma resposta legítima e informativa.

- **Comando/notebook:** `...`
- **Entrada:** (ficheiro, N amostras)
- **Resultado:** (o número, não a impressão)
- **Guardado em:** `results/...`
- Foi removido o cohort C2011, visto que o 17aE2 do ITP não existe no Zenodo e não existem mais fármacos em comum.

## 4. Números da semana

Tabelas table_ITP_Lifespan_Data e table_Zenodo

## 5. Bloqueado

Finalizar pre-processamento de dados

- [ ] ...

## 6. Decisões tomadas

Foram retirados os cohorts C2011 e C2020, visto que não há transcriptomas de nenhum animal dessas cohorts. O Cana, referente ao Canagliflozin nos dados é referente à cohort C2016 (7mo) e não aos fármacos utilizados em C2020.

## 7. Plano para a próxima semana

- [ ] Testar se os scripts dão os mesmos resultados que estão no excel
