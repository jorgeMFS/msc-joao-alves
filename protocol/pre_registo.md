# Pré registo

## Hipótese primária (equivalência, não diferença)

Sob LOIO com folds idênticos, o relógio de mortalidade **não confere capacidade de generalização
adicional** sobre o relógio cronológico, na associação ao nível da intervenção entre o efeito do
composto no relógio e o seu efeito no tempo de vida.

Operacionalmente: o intervalo de confiança da **diferença emparelhada** entre os dois relógios está
contido em [−Δ, +Δ], com **Δ = ______** (preencher a partir de `potencia.md`, antes de ver os dados).

> Isto é um **teste de equivalência**, não um teste de diferença. "Não rejeitar a hipótese nula de
> diferença zero" não demonstra equivalência; é preciso a margem, e a margem é pré-registada.

**Números de referência publicados:** r² ≈ 0,13 (cronológico) e r² ≈ 0,28 (mortalidade).
A previsão da tese é que o segundo colapse para ≈ 0,13 sob LOIO.

## Definição de intervenção

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 56 families (with control).

If interventions containing multiple regimes (e.g. Ercc1 + CR) have to be joined with its components , it will result in 41 families.

## Esquema de validação
GroupKFold com a intervenção como grupo. Hiperparâmetros afinados dentro de cada fold. Os rótulos do relógio de mortalidade são reconstruídos dentro de cada fold sem usar a curva de sobrevivência da intervenção retida.

## Regra de decisão
O intervalo fica todo dentro da margem, e os dois relógios são equivalentes. A tese confirma se.
O intervalo fica todo acima da margem, e o de mortalidade é mesmo melhor.
O intervalo atravessa a margem, e o resultado é inconclusivo.

## Análises secundárias
Dimorfismo sexual com canagliflozina. Substituição ao nível do ensaio (Buyse Molenberghs, só trial level, não há dados individuais emparelhados). Baseline aleatório e transcriptoma completo regularizado.

**Treatments to be tested**

**Intervention**                                      **Family**

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
RaAc_9m                                               Acarbose
RaAc_16m                                              Acarbose
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

Ercc1 delta/- progeria & Hypoxia; 11%                Ercc1; Hypoxia
