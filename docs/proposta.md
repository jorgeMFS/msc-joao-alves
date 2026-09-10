# Proposta de dissertação

**Mestrando** João Alves · Mestrado em Bioinformática Clínica, ano letivo 2026/2027
**Orientadores** Jorge Miguel Silva (Investigador Auxiliar, IEETA) · Gabriela Moura (Professora Associada, DCM / iBiMED)

> Este ficheiro é o resumo estruturado da proposta submetida. O documento original
> (`Proposta-Relogios-UA-João.docx`) é a versão de referência; as figuras estão em `figuras/`.

---

## O problema

A idade cronológica é um indicador imperfeito do estado fisiológico. Os **relógios de
envelhecimento**: modelos que estimam idade biológica a partir de metilação do ADN ou expressão
génica, quantificam essa diferença, e o desvio entre idade estimada e cronológica associa-se a
maior morbilidade e mortalidade.

Isso motivou a proposta de os usar como **instrumento de avaliação de intervenções geroprotetoras**:
o efeito de um tratamento seria aferido pela redução na idade biológica estimada, dispensando o
seguimento até ao desfecho. O interesse é evidente, porque avaliar o efeito na longevidade humana
excede o horizonte de qualquer ensaio.

**Mas a validade depende de um pressuposto não trivial:** que uma alteração induzida no marcador
reflete uma alteração no processo que se pretende modificar. Uma intervenção pode agir sobre os
marcadores sem afetar o mecanismo de envelhecimento. Discriminar entre os dois cenários é o objeto
desta dissertação.

### Predizer não é substituir

A capacidade **preditiva** está estabelecida, 14 relógios em 18.859 adultos da Generation Scotland
predizem robustamente doença incidente e mortalidade (Mavrommatis et al., 2025).

Um **substituto** exige mais: que o efeito do tratamento no marcador prediga o efeito do tratamento
no desfecho, e não apenas que marcador e desfecho estejam associados na ausência de intervenção.
É a formalização de Prentice (1989), substancialmente mais forte que a associação observacional.

> **O precedente: CAST, 1989.** A encainida e a flecainida suprimiram a arritmia ventricular -
> melhoria inequívoca do marcador, e elevaram a mortalidade total de **3,0 para 7,7 %** (RR 2,5),
> e a morte por arritmia ou paragem cardíaca não fatal de **1,2 para 4,5 %** (RR 3,6).
> O marcador respondia ao tratamento **sem mediar** o seu efeito no desfecho.
> Ver `figuras/figura2_cast.png`.

O quadro de validação de referência do campo (Moqri et al., 2024, Biomarkers of Aging Consortium)
é, na totalidade, epidemiologia observacional: nenhum dos cinco tipos de validação corresponde a
substituição, nenhuma das doze recomendações menciona aleatorização, e o próprio documento admite
que o caminho para endpoints substitutos ainda não existe.

### A oportunidade

O **NIA Interventions Testing Program (ITP)** fornece o que falta em humanos: desde 2004 testa
compostos em ratinhos geneticamente heterogéneos **UM-HET3**, em três sítios com protocolos
idênticos, medindo o desfecho verdadeiro, o tempo de vida.

Tyshkovskiy et al. (2026) sequenciaram 170 fígados do ITP, construíram relógios transcriptómicos, e
reportaram a correlação entre o efeito das intervenções no relógio e no tempo de vida. Validaram
deixando de fora **tecidos, conjuntos de dados e espécies, nunca uma intervenção inteira**.

Como os rótulos de treino derivam das curvas de sobrevivência das próprias intervenções, a
correlação publicada mede **interpolação entre conjuntos de dados**, não **extrapolação para
tratamentos novos**: que é precisamente a operação de um endpoint substituto.

---

## Os esquemas de validação

Ver `figuras/figura3_esquemas_validacao.png`.

| Esquema | Deixa de fora | Estado |
|---|---|---|
| LOFO | um fold | ✓ feito |
| LOTO | um tecido | ✓ feito |
| LODO | um conjunto de dados | ✓ feito |
| LOSO | uma espécie | ✓ feito |
| **LOIO** | **uma intervenção inteira** | **✗ nunca feito, é a tese** |

### A previsão pré-registada, com os números publicados

| Relógio | r² publicado | Sob LOIO |
|---|---:|---:|
| Cronológico (não vê a sobrevivência) | ≈ 0,13 | - |
| Mortalidade (rótulo do próprio tratamento) | ≈ 0,28 | **previsão: colapsa para ≈ 0,13** |

A tese prevê que a vantagem do relógio de mortalidade **desapareça** quando vê um fármaco pela
primeira vez.

---

## Objetivos

**Geral.** Avaliar a validade dos relógios transcriptómicos de envelhecimento como endpoints
substitutos para intervenções geroprotetoras, no modelo murino do ITP.

1. **[PRIMÁRIO] Generalização para intervenções não observadas.** Validação cruzada agrupada por
   intervenção (LOIO), comparando o relógio de mortalidade com o cronológico.
   A quantidade primária **não é o erro na estimativa de idade**: é a associação, **ao nível da
   intervenção e fora da amostra**, entre o efeito do composto no relógio e o seu efeito no tempo de
   vida, avaliada pela **diferença emparelhada** entre os dois relógios sob folds idênticos.
   **A hipótese é de equivalência, com margem pré-registada** fixada na semana 1 a partir da análise
   de potência, não do resultado observado.
2. **Dimorfismo sexual.** Testar se a assinatura do relógio reproduz o dimorfismo sexual do efeito
   no tempo de vida, com a **canagliflozina** (sequenciada nos dois sexos, benefício apenas em
   machos) como caso de maior potência, e os pares de idade de início como contraste dentro do sexo.
   Convergente e exploratório, assenta num único composto.
3. **Substituição ao nível do ensaio.** Quadro meta-analítico de Buyse-Molenberghs, com correção de
   erro de medição, intervalos de confiança, efeito-limiar, e diagnóstico de estabilidade por
   reamostragem.
4. **Especificidade de módulo.** Desagregar relógios de via (inflamatório, mitocondrial, metabólico)
   por mecanismo de intervenção. **Exploratório, só se o primário e a potência o justificarem.**
5. **Nulos.** Comparar contra um nulo estocástico, para distinguir um resultado negativo por
   qualidade dos dados de um resultado negativo por propriedade do objeto.

---

## Componente de aprendizagem automática

É a competência central que o mestrando desenvolve. Não se limita a aplicar modelos existentes:
retreina-os e interroga sistematicamente a sua capacidade de generalização.

**O regime de dimensionalidade define todo o desenho.** ~20.000 genes como variáveis de entrada
contra **poucas dezenas de unidades independentes ao nível que importa**. Neste regime um modelo com
demasiada capacidade memoriza a identidade de cada intervenção em vez de aprender o sinal biológico.
Daí: modelos lineares regularizados (**elastic net**, **ridge**) e representações de baixa dimensão
(*scores* de módulo), **não** redes profundas. Justificar e demonstrar esta escolha é parte do trabalho.

**O cerne está na escolha do esquema de validação cruzada, porque é ela que decide que pergunta se
está realmente a responder:**

| Agrupar por | Mede | É |
|---|---|---|
| indivíduo | generalização entre indivíduos | **predição** (o habitual) |
| **intervenção** | generalização para um tratamento nunca visto | **substituição** |

Mesmo conjunto de dados, mesmo modelo, agrupamento diferente. **A diferença entre os dois resultados
é exatamente a distância entre prever e servir de endpoint.**

Inclui ainda: afinação **aninhada** dos hiperparâmetros dentro de cada fold para evitar fuga;
reprodução dos modelos publicados a partir do código e pesos; baselines (preditor estocástico,
transcriptoma completo regularizado); e calibração da significância por **testes de permutação que
respeitam a estrutura de dependência dos dados**.

**Ecossistema.** Python com scikit-learn sobre os modelos do pacote tAge; R para a análise de substituição.

---

## Dados e recursos

Todo o trabalho é computacional, sobre dados públicos já localizados. Não requer geração
experimental nem contacto com terceiros.

| Recurso | Identificador |
|---|---|
| Transcriptomas e modelos | Zenodo `10.5281/zenodo.18763485` |
| RNA-seq cru | GEO SuperSeries `GSE292885` |
| Sobrevivência ao nível do animal | Mouse Phenome Database, projeto ITP1 (NIH U24-AG066346) |
| Relógios | pacote `tAge` |
| Substituição | pacote `Surrogate` (CRAN) |

---

## Resultados esperados

A primeira avaliação de substituição, ao nível do ensaio, de relógios de envelhecimento, **num
desenho em que todos os desfechos possíveis são informativos e publicáveis**:

- Estimativa quantitativa, com incerteza e efeito-limiar, de quanto o efeito de uma intervenção no
  relógio prediz o seu efeito no tempo de vida, **corrigida do erro de medição** que atenua a
  correlação publicada.
- O resultado do teste de generalização entre intervenções, que determina se a capacidade aparente
  dos relógios de mortalidade resulta do **mecanismo biológico** ou da **construção do rótulo**.
- O resultado do teste de coerência com o dimorfismo sexual.
- Um **protocolo de pré-registo** e uma análise de potência por simulação que determina quantas
  intervenções seriam necessárias para estimar a substituição com precisão útil, aplicável ao
  desenho de estudos futuros na área.
- Código aberto e reprodutível, e a tabela de efeitos por intervenção como material suplementar,
  **independentemente do resultado**.
- Publicação científica submetida.

---

## Plano de trabalho

Ver `figuras/figura4_cronograma.png`.

| Semanas | Bloco |
|---|---|
| **1** | **Portão de viabilidade, sem código.** Três confirmações (ver abaixo). Se não passar, a pergunta é reformulada **nessa semana**, não no fim. |
| 2 a 4 | Reproduzir um valor publicado a partir do código e pesos, valida a cadeia de análise antes de lhe fazer perguntas novas. |
| 5 a 9 | **Teste de generalização entre intervenções. Resultado primário, deliberadamente cedo.** |
| 10 a 14 | Tabela de efeitos por intervenção, base de toda a análise seguinte. |
| 15 a 18 | Substituição com efeito-limiar, dimorfismo sexual, nulos. |

**A redação começa durante a fase primária e é contínua até à entrega.**

### As três confirmações da semana 1

1. Os dados públicos permitem **identificar a intervenção de origem de cada amostra**?
2. O número de intervenções com transcriptoma **e** curva de sobrevivência é **conhecido, e não
   apenas presumido**?
3. A análise de potência por simulação mostra que esse número **chega** para estimar a substituição
   com precisão útil?

**É desta análise que sai a margem de equivalência do resultado primário.**

---

## Referências

- **CAST Investigators** (1989). Preliminary report: effect of encainide and flecainide on mortality
  in a randomized trial of arrhythmia suppression after myocardial infarction.
  *New England Journal of Medicine*, **321**, 406-412.
- **Cummings, S. R.** (2022). Endpoints for geroscience clinical trials: health outcomes, biomarkers,
  and biologic age. *GeroScience*, **44**, 2925-2931.
- **Jiang, N., Xu, Z., Zhao, S., Gelfond, J., Strong, R., & Nelson, J. F.** (2025). Sex as a major
  determinant of pro-longevity drug efficacy: a review of two decades of the NIA Interventions
  Testing Program. *Journals of Gerontology Series A*, **80**, glaf138.
- **Mavrommatis, C., Belsky, D. W., Ying, K., Moqri, M., Campbell, A., Richmond, A., Gladyshev, V. N.,
  Chandra, T., McCartney, D. L., & Marioni, R. E.** (2025). An unbiased comparison of 14 epigenetic
  clocks in relation to 174 incident disease outcomes. *Nature Communications*, **16**, 11164.
- **Moqri, M., Herzog, C., Poganik, J. R., et al.**, Biomarkers of Aging Consortium (2024).
  Validation of biomarkers of aging. *Nature Medicine*, **30**, 360-372.
- **Prentice, R. L.** (1989). Surrogate endpoints in clinical trials: definitions and operational
  criteria. *Statistics in Medicine*, **8**, 431-440.
- **Tyshkovskiy, A., Kholdina, D., Davitadze, M., et al., & Gladyshev, V. N.** (2026). Universal
  transcriptomic hallmarks of mammalian ageing and mortality. *Nature*, **654**, 173-188.
