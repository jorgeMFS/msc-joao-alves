# Pré registo

## Hipótese primária (diferença, não equivalência)

Sob LOIO com folds idênticos, o relógio de mortalidade **não confere capacidade de generalização
adicional** sobre o relógio cronológico, na associação ao nível da intervenção entre o efeito do
composto no relógio e o seu efeito no tempo de vida.

Operacionalmente: o intervalo de confiança da **diferença emparelhada** entre os dois relógios está
contido em [−Δ, +Δ], com **Δ = ______** (preencher a partir de `potencia.md`, antes de ver os dados).

> Isto é um **teste de equivalência**, não um teste de diferença. "Não rejeitar a hipótese nula de
> diferença zero" não demonstra equivalência; é preciso a margem, e a margem é pré-registada.

**Números de referência publicados:** r² ≈ 0,13 (cronológico) e r² ≈ 0,28 (mortalidade).
A previsão da tese é que o segundo colapse para ≈ 0,13 sob LOIO.

---
Dado que para definir Δ, obtivemos uma margem demasiado permissiva (0.56, enquanto a diferença entre o R_Mortality e R_Chronological = 0.17), tivemos de optar por outra estratégia, já que reduzir o Δ para 0.17 tornaria o teste exigente demais (seriam necessárias mais de 500 famílias). Por isso passámos a testar a diferença:

O objetivo é avaliar se o relógio de mortalidade apresenta melhor capacidade preditiva em LODO do que em LOIO, ou seja, se a exclusão de intervenções relacionadas reduz a associação entre as previsões do relógio e o tempo de vida real.

Operacionalmente: comparamos a diferença emparelhada entre as correlações r_LODO - r_LOIO, nas mesmas 56 famílias. Consideramos que existe evidência de uma vantagem de LODO quando o limite inferior do intervalo de confiança de 90% é superior a zero.
Isto é um teste unilateral de superioridade. Não procuramos demonstrar equivalência entre os métodos, mas determinar se LODO apresenta uma correlação superior à de LOIO.

**Números de referência publicados:** r ≈ 0.53 (LODO/Lifepsan) e r ≈ 0.36 (LOIO/Lifespan)


## Definição de intervenção

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 56 families (with control).

If interventions containing multiple regimes (e.g. Ercc1 + CR) have to be joined with its components , it will result in 41 families.

## Esquema de validação
LOIO com a intervenção como família, em que combinações de intervenções saem juntamente com os seus componentes. Para equivalência é usado o intervalo a 90%, calculado por bootstrap das famílias (sorteadas com reposição e recalculada a diferença de cada vez). GroupKFold com a intervenção como grupo. Hiperparâmetros afinados dentro de cada fold. Os rótulos do relógio de mortalidade são reconstruídos dentro de cada fold sem usar a curva de sobrevivência da intervenção retida.
Vão ser usados 20, 41 ou 56 grupos de intervenções.
- 20: corresponde às 20 intervenções ITP
- 41: corresponde aos blocos, porque cada combinação sai com os seus componentes
- 56: corresponde a todas as famílias, ou seja, cada intervenção pertence a uma ou mais famílias (e.g. RaAc percence a Rapamycin e a Acarbose)

## Regra de decisão
• Teste com menor número de simulções com o lower bound inferior a zero, já que este apresentará a maior potência

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

Ercc1 delta/- progeria & Hypoxia; 11%                Ercc1; Hypoxia
