# Pré registo (preencher na semana 1, antes de qualquer análise)

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
