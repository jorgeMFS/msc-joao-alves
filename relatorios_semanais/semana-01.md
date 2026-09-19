<!-- Primeira entrada, parcialmente preenchida como exemplo. Copiar o TEMPLATE.md
     para semana-02.md na próxima sexta. Apagar os comentários. -->

# Semana 01 (2026-09-13 a 2026-09-20)

**Horas dedicadas:** ~6 h · **Bloco do plano:** 1, portão de viabilidade (sem código de modelação)

---

## 1. Lido

As três leituras da semana 1 (`docs/reading-list.md`: §A1, §C1, §C0).

- **Tyshkovskiy et al. (2026)**, *Nature*, o artigo posto à prova. Retido: o carimbo do relógio de mortalidade vem das curvas de sobrevivência dos fármacos do ITP, e a validação deixou de fora tecidos, conjuntos de dados e espécies, **nunca uma intervenção inteira**.
- **Prentice (1989)**: critérios operacionais para um marcador substituir um desfecho. Retido: são condições fortes, e "correlaciona" não é uma delas.
- **CAST (1989)**: dois antiarrítmicos suprimiram a arritmia e duplicaram a mortalidade. Retido: é o contra-exemplo que justifica a tese existir. Prever não é substituir.
- Documentação do GIT, tAge, repository do GitHub.

## 2. Escrito

Tabelas com fármacos e dados relativos

## 3. Executado

- **Nada de modelação**, por desenho. A semana 1 é portão de viabilidade e o código de modelação só abre depois de o pré-registo estar fechado.
- **Feito:** descarregados os ficheiros do Zenodo e os metadados do GEO; inspecionadas as colunas para ver se as amostras trazem identificação de fármaco.
- Foi criada uma tabela de ligação para padronizar nomenclatura dos fármacos entre os dados do Zenodo e do ITP.
- Foi descoberta a forma de como o diff é calculado. Encontra-se na metodologia do Tyshkovskiy et al. (2026), e refere que foi utilizado uma ANOVA, com o tecido e idade cronológica como covariáveis para calcular a diferença média estimada da idade transcriptómica entre o grupo tratado e o grupo de controlo.

## 4. Números da semana

| Quantidade | Valor | Semana anterior |
|---|---:|---:|
| Amostras de fígado no Zenodo | 170 | - |
| Amostras com fármaco identificado | 106 | - |
| Intervenções com transcriptoma **e** sobrevivência | ? | - |
| N do LOIO (= linha acima) | ? | - |

> A terceira linha é o número que decide a tese. Se for baixo (< 8 a 10), a simulação de potência da pergunta 3 do portão vai dizer que o intervalo de confiança é largo de mais, e a pergunta tem de ser reformulada **nesta semana**.

### Dados sobre cada intervenção

| Intervention                                       |        Year | No of Males | No of Females |
| -------------------------------------------------- | ----------: | ----------: | ------------: |
| Control                                            |             |          26 |            28 |
| 17-DMAG; 30ppm                                     |        2015 |           2 |             3 |
| Minocycline; 300ppm                                |        2015 |           2 |             3 |
| Mito Q; 100ppm                                     |        2015 |           3 |             3 |
| Late-life Rapamycin; 42ppm                         |        2015 |           3 |             2 |
| b-GPA; 3300ppm                                     |        2015 |           3 |             1 |
| Canagliflozin; 180ppm                              | 2016 e 2020 |           6 |             6 |
| Candesartan cilexetil CC; 30ppm                    |        2016 |           3 |             2 |
| Geranylgeranylacetone GGA; 600ppm                  |        2016 |           2 |             3 |
| Nicotinamide riboside NR; 1000ppm                  |        2016 |           2 |             2 |
| MIF098; 240ppm                                     |        2016 |           3 |             1 |
| 1,3-butanediol BD; 100000ppm                       |        2017 |           2 |             3 |
| Captopril; 180ppm                                  |        2017 |           3 |             3 |
| L-Leucine; 40000ppm                                |        2017 |           3 |             3 |
| PB125; 100ppm                                      |        2017 |           3 |             3 |
| Middle-aged Rapamycin; 14.7ppm & Acarbose; 1000ppm |        2017 |           3 |             3 |
| Rapamycin; 14.7ppm & Acarbose; 1000ppm             |        2017 |           3 |             3 |
| Sulindac; 5ppm                                     |        2017 |           2 |             3 |
| Syringaresinol; 300ppm                             |        2017 |           3 |             3 |
| Middle-aged 17-alpha-estradiol; 14.4ppm            |        2011 |           3 |             0 |
| Late-life 17-alpha-estradiol                       |        2016 |           2 |             0 |


## 5. Bloqueado

- [ ] Confirmar com os orientadores o que conta como "uma intervenção": composto, composto × dose, ou composto × idade de início. Fixa o N do LOIO e **não pode mudar depois** de escrito no pré-registo.

## 6. Decisões tomadas

- **Decidido:** nada ainda. **Porquê:** a definição de intervenção depende do que a tabela de amostras mostrar.

## 7. Plano para a próxima semana

- [ ] Fechar `results/tabela_amostras.csv` com as 170 linhas.
- [ ] Cruzar com o ITP1 e produzir `results/intervencoes.csv`.
- [ ] Correr a simulação de potência e escrever `protocol/potencia.md`.
- [ ] Se o portão passar, escrever `protocol/pre_registo.md` e só então abrir código.
