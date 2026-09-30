<!-- Primeira entrada, parcialmente preenchida como exemplo. Copiar o TEMPLATE.md
     para semana-02.md na próxima sexta. Apagar os comentários. -->

# Semana 01 (2026-09-13 a 2026-09-20)

**Horas dedicadas:** ~6 h · **Bloco do plano:** 1, portão de viabilidade (sem código de modelação)

---

## 1. Lido

As três leituras da semana 1 (`docs/reading-list.md`: §A1, §C1, §C0).

- **Tyshkovskiy et al. (2026)**, *Nature*, o artigo posto à prova. Retido: o carimbo do relógio de mortalidade vem das curvas de sobrevivência dos fármacos do ITP, e a validação deixou de fora tecidos, conjuntos de dados e espécies, **nunca uma intervenção inteira**.
- Documentação do GIT, tAge, repository do GitHub.

## 2. Escrito

Tabelas com fármacos e dados relativos

## 3. Executado

- **Nada de modelação**, por desenho. A semana 1 é portão de viabilidade e o código de modelação só abre depois de o pré-registo estar fechado.
- **Feito:** descarregados os ficheiros do Zenodo e os metadados do GEO; inspecionadas as colunas para ver se as amostras trazem identificação de fármaco.
- Foi criada uma tabela de ligação (table_zenodo_mpd_id) para padronizar nomenclatura dos fármacos entre os dados do Zenodo e do ITP, a partir dessa lista no ITP foi feito o download dos cohorts que continham esses fármacos.
- Foi descoberta a forma de como o diff é calculado. Encontra-se na metodologia do tAge, e refere que foi centrado na mediana do grupo escolhido (controlo).

## 4. Números da semana

### Dados sobre cada intervenção 
Tabela sampleinfo