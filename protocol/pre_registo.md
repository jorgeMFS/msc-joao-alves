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
(preencher)

## Esquema de validação
GroupKFold com a intervenção como grupo. Hiperparâmetros afinados dentro de cada fold. Os rótulos do relógio de mortalidade são reconstruídos dentro de cada fold sem usar a curva de sobrevivência da intervenção retida.

## Regra de decisão
(o que se conclui em cada um dos desfechos possíveis, escrito antes de ver os dados)

## Análises secundárias
Dimorfismo sexual com canagliflozina. Substituição ao nível do ensaio (Buyse Molenberghs, só trial level, não há dados individuais emparelhados). Baseline aleatório e transcriptoma completo regularizado.

**Treatments to be tested**

As there are many interventions with minor changes (e.g. rapamycin regimes or diet), each group will only count as a single family. Following this step, this will result in 56 families (with control).
If interventions containing multiple regimes (e.g. Ercc1 + CR) have to be joined with its components , it will result in 41 families.

*ITP Samples Compounds* (20)
-17aE2_16m
-17aE2_20m
-BD
-bGPA
-Cana
-Capt
-CC
-DMAG
-GGA
-Leu
-MIF098
-Min
-MitoQ
-NR
-PB125
-RaAc_9m
-RaAc_16m
-Rapa_Continuous
-Sul
-Syr

*Compound* (10)
Protandim; 1200ppm
SRT2104; 1330ppm
Metformin 1%; every other week
Metformin 1%; 2 consecutive weeks per month
Spermidine; 3mM
Acarbose; 1000ppm
D-Glucosamine; 10,000ppm
Rapamycin; 14ppm
Rapamycin; 42ppm
17-alpha-estradiol; 14.4ppm

*Diet* (19)
CR; 20% from 6m
CR; 30% from 5 weeks
CR; 40%
CR; 40% from 2m
CR; 40% from 6m
CR, 12h during day; 30%
CR, 12h during night; 30%
CR, 2h during day; 30%
CR, 2h during night; 30%
CR, spread; 30%
HF diet + CR; 30% from 5 weeks
HF diet; 60% kcal fat/g
HF diet; from 12 months
HF diet; from 5 weeks
Ketogenic diet; from 12 months
Late-life CR; 40%
Low amino acid diet; from 6 months
Low BCAA diet
Low isoleucine diet; from 6 months

*Diet + Exercise* (1)
HF diet & exercise; from 5 weeks

*Exercise* (1)
Exercise; from 5 weeks

*Genotype* (21)
Akt1 +/-
Ames dwarf
BubR1 +/L1002P
BubR1 H/H
BubR1 H/L1002P
Dgat1 -/-
Ercc1 delta/- progeria
G2 Terc -/-
GHRKO
Little
Lmna G609G/G609G progeria
Lmna LCS/LCS
Myc +/-
Nqo1 and Cyb5r3 overexpression
PAPP-A KO
S6K1 -/-
Sirt1 -/-
Slc6a6 -/-
Snell dwarf
nmrHas2 overexpression
Kl KO

*Genotype + Compound* (2)
G2 Terc -/- & Rapamycin; 42ppm
Ercc1 delta/- progeria & Rapamycin; 14ppm

*Genotype + Diet* (4)
Sirt1 -/- & CR; 40% from 2m
Sirt1 +/- & CR; 40% from 2m
Lmna G609G/G609G progeria & Methionine restriction
Ercc1 delta/- progeria & CR; 30%

*Genotype + Hypoxia* (1)
Ercc1 delta/- progeria & Hypoxia; 11%
