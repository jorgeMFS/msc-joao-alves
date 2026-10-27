# Pré registo

## Hipótese primária (diferença, não equivalência)
Dado que para definir Δ, obtivemos uma margem demasiado permissiva (0.56, enquanto a diferença entre o R_Mortality e R_Chronological = 0.17), tivemos de optar por outra estratégia, já que reduzir o Δ para 0.17 tornaria o teste exigente demais (seriam necessárias mais de 500 famílias). Por isso passámos a testar a diferença:

O objetivo é avaliar se o relógio de mortalidade apresenta melhor capacidade preditiva em LODO do que em LOIO, ou seja, se a exclusão de intervenções relacionadas reduz a associação entre as previsões do relógio e o tempo de vida real.

Operacionalmente: comparamos a diferença emparelhada entre as correlações r_LODO - r_LOIO, nas mesmas 56 famílias. Consideramos que existe evidência de uma vantagem de LODO quando o limite inferior do intervalo de confiança de 90% é superior a zero.
Isto é um teste unilateral de superioridade. Não procuramos demonstrar equivalência entre os métodos, mas determinar se LODO apresenta uma correlação superior à de LOIO.

**Números de referência publicados:** 
*Para o relógio de mortalidade*
r ≈ 0.53 (LODO/Lifespan)

*Para o relógio cronológico*
r ≈ 0.36 (LODO/Lifespan)


## Definição de intervenção

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 56 families (with control).



## Esquema de validação
- LODO tira do treino um dataset inteiro.
- LOIO exclui o dataset D e, nos outros datasets, a família F e as que partilham componente com ela (por exemplo, para a RaAc saem também a Rapamycin e a Acarbose). Para diferença é usado o intervalo a 90%, calculado por bootstrap das famílias (sorteadas com reposição e recalculada a diferença de cada vez). 
Hiperparâmetros afinados dentro de cada fold. Os rótulos do relógio de mortalidade são reconstruídos dentro de cada fold sem usar a curva de sobrevivência da intervenção retida.

Vão ser usadas 56 grupos de intervenções.
- 56: corresponde a todas as famílias, ou seja, cada intervenção pertence a uma ou mais famílias (e.g. RaAc não percence a "Rapamycin" e a "Acarbose" mas sim a uma família "Rapamycin-Acarbose", embora saia do treino quando se prevê ou a "Rapamycin" ou "Acarbose")

## Regra de decisão
Para CI 90% = [X,Y]:
- Se X > 0 : O relógio de mortalidade perde desempenho quando não vê a intervenção
- Se X < 0 : Não se pode concluir que o relógio de mortalidade perde desempenho quando não vê a intervenção

## Análises secundárias
Dimorfismo sexual com canagliflozina. Substituição ao nível do ensaio (Buyse Molenberghs, só trial level, não há dados individuais emparelhados). Baseline aleatório e transcriptoma completo regularizado.

## Potência

### Tabela 1 — Resultados das simulações

| nint | corr_LOIO_Lifespan | corr_between_models | Mean_delta_r | Percentile_Range_CI95 | Percentile_Range_CI90 | r_LODO | r_LOIO | n_LB_under_zero |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 56 | 0.36 | 0.80 | 0.164020 | 0.300515 | 0.246189 | 0.519664 | 0.355645 | 272 |
| 56 | 0.36 | 0.90 | 0.169677 | 0.228532 | 0.185943 | 0.524125 | 0.354448 | 53 |
| 56 | 0.36 | 0.95 | 0.166113 | 0.176487 | 0.141065 | 0.524728 | 0.358615 | 0 |
| 56 | 0.45 | 0.80 | 0.079275 | 0.284216 | 0.237093 | 0.529329 | 0.450054 | 693 |
| 56 | 0.45 | 0.90 | 0.080601 | 0.209259 | 0.172293 | 0.531803 | 0.451201 | 518 |
| 56 | 0.45 | 0.95 | 0.081251 | 0.152672 | 0.128928 | 0.529227 | 0.447976 | 278 |
| 56 | 0.53 | 0.80 | -0.002080 | 0.273406 | 0.229461 | 0.527792 | 0.529871 | 951 |
| 56 | 0.53 | 0.90 | 0.000011 | 0.204405 | 0.165872 | 0.530182 | 0.530172 | 941 |
| 56 | 0.53 | 0.95 | 0.000157 | 0.144280 | 0.122973 | 0.526080 | 0.525924 | 930 |

### Tabela 2 — Potência estatística

| nint | corr_LOIO_Lifespan | corr_between_models | n_LB_under_zero | potencia |
|---:|---:|---:|---:|---:|
| 56 | 0.36 | 0.80 | 272 | 0.728 |
| 56 | 0.36 | 0.90 | 53 | 0.947 |
| 56 | 0.36 | 0.95 | 0 | 1.000 |
| 56 | 0.45 | 0.80 | 693 | 0.307 |
| 56 | 0.45 | 0.90 | 518 | 0.482 |
| 56 | 0.45 | 0.95 | 278 | 0.722 |
| 56 | 0.53 | 0.80 | 951 | 0.049 |
| 56 | 0.53 | 0.90 | 941 | 0.059 |
| 56 | 0.53 | 0.95 | 930 | 0.070 |

Rows com corr_LOIO_Lifespan = 0.53 são a taxa de falsos positivos, não de potência

---

**Treatments to be tested**

**Intervention**                                      **Family** (25)

17aE2_16m                                             17-alpha-estradiol
17aE2_20m                                             17-alpha-estradiol
BD                                                    BD
bGPA                                                  bGPA
Cana                                                  Cana
Capt                                                  Capt
CC                                                    CC
DMAG                                                  DMAG
GGA                                                   GGA
Leu                                                   Leu
MIF098                                                MIF098
Min                                                   Min
MitoQ                                                 MitoQ
NR                                                    NR
PB125                                                 PB125
RaAc_9m                                               Acarbose, Rapamycin
RaAc_16m                                              Acarbose, Rapamycin
Rapa_Continuous                                       Rapamycin
Sul                                                   Sul
Syr                                                   Syr

Protandim; 1200ppm                                    Protandim
SRT2104; 1330ppm                                      SRT2104
Metformin 1%; every other week                        Metformin
Metformin 1%; 2 consecutive weeks per month           Metformin
Spermidine; 3mM                                       Spermidine
Acarbose; 1000ppm                                     Acarbose
D-Glucosamine; 10,000ppm                              D-Glucosamine
Rapamycin; 14ppm                                      Rapamycin
Rapamycin; 42ppm                                      Rapamycin
17-alpha-estradiol; 14.4ppm                           17-alpha-estradiol

CR; 20% from 6m                                       CR
CR; 30% from 5 weeks                                  CR
CR; 40%                                               CR
CR; 40% from 2m                                       CR
CR; 40% from 6m                                       CR
CR, 12h during day; 30%                               CR
CR, 12h during night; 30%                             CR
CR, 2h during day; 30%                                CR
CR, 2h during night; 30%                              CR
CR, spread; 30%                                       CR
HF diet + CR; 30% from 5 weeks                        HF diet; CR
HF diet; 60% kcal fat/g                               HF diet
HF diet; from 12 months                               HF diet
HF diet; from 5 weeks                                 HF diet
Ketogenic diet; from 12 months                        Ketogenic diet
Late-life CR; 40%                                     CR
Low amino acid diet; from 6 months                    Low amino acid diet
Low BCAA diet                                         Low BCAA diet
Low isoleucine diet; from 6 months                    Low isoleucine diet

HF diet & exercise; from 5 weeks                      HF diet; Exercise

Exercise; from 5 weeks                                Exercise

Akt1 +/-                                              Akt1
Ames dwarf                                            Ames dwarf
BubR1 +/L1002P                                        BubR1
BubR1 H/H                                             BubR1
BubR1 H/L1002P                                        BubR1
Dgat1 -/-                                             Dgat1
Ercc1 delta/- progeria                                Ercc1
G2 Terc -/-                                           Terc
GHRKO                                                 GHRKO
Little                                                Little
Lmna G609G/G609G progeria                             Lmna
Lmna LCS/LCS                                          Lmna
Myc +/-                                               Myc
Nqo1 and Cyb5r3 overexpression                        Nqo1; Cyb5r3
PAPP-A KO                                             PAPP-A
S6K1 -/-                                              S6K1
Sirt1 -/-                                             Sirt1
Slc6a6 -/-                                            Slc6a6
Snell dwarf                                           Snell dwarf
nmrHas2 overexpression                                nmrHas2
Kl KO                                                 Kl

G2 Terc -/- & Rapamycin; 42ppm                       Terc; Rapamycin
Ercc1 delta/- progeria & Rapamycin; 14ppm            Ercc1; Rapamycin

Sirt1 -/- & CR; 40% from 2m                          Sirt1; CR
Sirt1 +/- & CR; 40% from 2m                          Sirt1; CR
Lmna G609G/G609G progeria & Methionine restriction   Lmna; Methionine restriction
Ercc1 delta/- progeria & CR; 30%                     Ercc1; CR

Ercc1 delta/- progeria & Hypoxia; 11%                Ercc1; Hypoxia - É retirado porque não tem controlos
