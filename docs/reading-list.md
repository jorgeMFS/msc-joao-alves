# Lista de leitura

Agrupada por tema. Para as coisas que se *clicam para ver e correr* (repositórios, portais de dados,
pacotes), ver `links.md`; este ficheiro são os artigos. Cada entrada dá a referência, um DOI ou link
estável, e uma nota sobre **o que retirar dela para esta tese**.

**Semana 1, por esta ordem:** A1 (Tyshkovskiy 2026, saber de cor, é o artigo posto à prova),
C1 (Prentice 1989) e C0 (CAST 1989). Os dois últimos são curtos e dão o argumento.
Depois C2 (Buyse-Molenberghs) e B1 (desenho do ITP), que chegam para escrever o pré-registo.

## A. Relógios de envelhecimento e intervenções

- **A1. Tyshkovskiy, Kholdina, Davitadze, et al., & Gladyshev (2026),** "Universal transcriptomic
  hallmarks of mammalian ageing and mortality", *Nature* **654**:173-188.
  Dados: Zenodo 10.5281/zenodo.18763485 · GEO GSE292885.
  **É o artigo posto à prova por esta tese, tem de se saber de cor.** Ler com atenção *como o
  rótulo do relógio de mortalidade é construído*: vem das curvas de sobrevivência dos fármacos do
  ITP, e é aí que mora a questão da fuga.
- **A1b. Tyshkovskiy, Bozaykut, Borodinova, et al. (2019),** "Identification and Application of Gene
  Expression Signatures Associated with Lifespan Extension", *Cell Metabolism* 30(3):573-593.
  DOI: 10.1016/j.cmet.2019.06.018. O trabalho anterior do mesmo grupo, que estabelece a abordagem
  de assinaturas de expressão a partir de intervenções.
- **A2. Horvath (2013),** "DNA methylation age of human tissues and cell types", *Genome Biology*
  14:R115. DOI: 10.1186/gb-2013-14-10-r115.
  O relógio cronológico canónico. Importa perceber que prevê **idade**, não mortalidade, a distinção
  que separa os dois relógios desta tese.
- **A3. Levine, Lu, Quach, et al. (2018),** "An epigenetic biomarker of aging for lifespan and
  healthspan", *Aging* 10(4):573-591. DOI: 10.18632/aging.101414.
  PhenoAge: o passo de relógio cronológico para relógio treinado em desfechos de saúde. É o análogo
  metilómico do relógio de mortalidade.
- **A4. Lu, Quach, Wang, et al. (2019),** "DNA methylation GrimAge strongly predicts lifespan and
  healthspan", *Aging* 11(2):303-327. DOI: 10.18632/aging.101684.
  Vai mais longe: treina diretamente contra tempo até à morte. Ver como constroem os rótulos, porque
  o `src/clocks/loio.py` tem de reconstruir rótulos equivalentes **dentro de cada fold**.
- **A4b. Mavrommatis, Belsky, Ying, Moqri, Campbell, Richmond, Gladyshev, Chandra, McCartney,
  Marioni (2025),** "An unbiased comparison of 14 epigenetic clocks in relation to 174 incident
  disease outcomes", *Nature Communications* **16**:11164.
  A capacidade **preditiva** dos relógios, estabelecida sem viés em 18.859 adultos da Generation
  Scotland. É o ponto de partida da introdução: predizer está provado, substituir não.
- **A5. Peters, Joehanes, Pilling, et al. (2015),** "The transcriptional landscape of age in human
  peripheral blood", *Nature Communications* 6:8570. DOI: 10.1038/ncomms9570.
  Relógio transcriptómico (não metilómico), que é a modalidade desta tese. Escala de efeito esperada.

## B. O Interventions Testing Program (a fonte da sobrevivência)

- **B1. Nadon, Strong, Miller, et al. (2008),** "Design of aging intervention studies: the NIA
  Interventions Testing Program", *Age* 30(4):187-199. DOI: 10.1007/s11357-008-9048-1.
  **Ler antes de tocar nos dados do ITP.** Explica o desenho de três sítios, a heterogeneidade
  genética dos ratinhos, e porque é que os efeitos são reportados por sexo. Isso condiciona o que
  significa "efeito no tempo de vida" na tabela de intervenções.
- **B2. Harrison, Strong, Sharp, et al. (2009),** "Rapamycin fed late in life extends lifespan in
  genetically heterogeneous mice", *Nature* 460:392-395. DOI: 10.1038/nature08221.
  O resultado mais citado do ITP. Serve de caso de teste: o pipeline tem de reproduzir este efeito
  a partir do ficheiro de sobrevivência antes de se confiar nele.
- **B0. Jiang, Xu, Zhao, Gelfond, Strong, Nelson (2025),** "Sex as a major determinant of
  pro-longevity drug efficacy: a review of two decades of the NIA Interventions Testing Program",
  *Journals of Gerontology Series A* **80**:glaf138.
  **A base do objetivo 2.** A extensão da longevidade depende fortemente do sexo e com direção
  variável entre compostos, enquanto os autores do tAge reportam assinaturas concordantes entre
  sexos. Essa tensão é o teste convergente.
- **B3. Miller, Harrison, Astle, et al. (2011),** "Rapamycin, but not resveratrol or simvastatin,
  extends life span of genetically heterogeneous mice", *The Journals of Gerontology: Series A*
  66A(2):191-201. DOI: 10.1093/gerona/glq178.
  Exemplo de intervenções com efeito nulo. São tão importantes como as positivas: sem nulos, a
  correlação entre efeito no relógio e efeito na vida não tem amplitude.

## C. Endpoints substitutos (o enquadramento estatístico)

- **C0. CAST Investigators (1989),** "Preliminary report: effect of encainide and flecainide on
  mortality in a randomized trial of arrhythmia suppression after myocardial infarction",
  *New England Journal of Medicine* **321**:406-412. DOI: 10.1056/NEJM198908103210629.
  Resultado final: Echt, Liebson, Mitchell, et al. (1991), *NEJM* **324**(12):781-788.
  DOI: 10.1056/NEJM199103213241201.
  **O precedente que dá o argumento inteiro.** A encainida e a flecainida suprimiram a arritmia -
  melhoria inequívoca do marcador, e elevaram a mortalidade total de **3,0 para 7,7 %** (RR 2,5), e
  a morte arrítmica ou paragem não fatal de **1,2 para 4,5 %** (RR 3,6). O marcador respondia ao
  tratamento **sem mediar** o seu efeito no desfecho. Ler na semana 1.
- **C0b. Moqri, Herzog, Poganik, et al.,** Biomarkers of Aging Consortium (2024), "Validation of
  biomarkers of aging", *Nature Medicine* **30**:360-372.
  O quadro de validação de referência do campo, e **é todo epidemiologia observacional**. Nenhum
  dos cinco tipos de validação corresponde a substituição; nenhuma das doze recomendações menciona
  aleatorização; o próprio documento admite que o caminho para endpoints substitutos ainda não
  existe. É a lacuna que esta tese ocupa.
- **C0c. Cummings (2022),** "Endpoints for geroscience clinical trials: health outcomes, biomarkers,
  and biologic age", *GeroScience* **44**:2925-2931.
  Coautor do quadro acima, argumenta que um relógio que integra vários mecanismos dificilmente será
  substituto válido para tratamentos de via única. Propõe o remédio, agrupar ensaios com desfecho
  comum e testar se o efeito generaliza para além de um tratamento, e declara o obstáculo: não há
  desfechos comuns entre ensaios humanos. **O ITP é exatamente o que falta.**

- **C1. Prentice (1989),** "Surrogate endpoints in clinical trials: definition and operational
  criteria", *Statistics in Medicine* 8(4):431-440. DOI: 10.1002/sim.4780080407.
  A definição clássica e os critérios operacionais. Curto. **Ler primeiro de toda esta secção.**
- **C2. Buyse & Molenberghs (1998),** "Criteria for the validation of surrogate endpoints in
  randomized experiments", *Biometrics* 54(3):1014-1029. DOI: 10.2307/2533853.
  Introduz a separação entre substituição **individual** e **de ensaio**. Crítico aqui: como nenhum
  ratinho tem transcriptoma e tempo de vida, só existe o nível de ensaio. Esta limitação vai para o
  pré-registo, não para a discussão.
- **C3. Burzykowski, Molenberghs, Buyse (2005),** *The Evaluation of Surrogate Endpoints*, Springer.
  DOI: 10.1007/b138566. Livro. Consultar o capítulo do meta-analytic framework, que é o que o pacote
  `Surrogate` do R implementa (`analysis/R/surrogacy.R`).
- **C4. Baker & Kramer (2003),** "A perfect correlate does not a surrogate make", *BMC Medical
  Research Methodology* 3:16. DOI: 10.1186/1471-2288-3-16.
  Quatro páginas, e é o contra-argumento que a discussão da tese tem de responder: correlação alta
  entre marcador e desfecho **não** implica que o marcador sirva de substituto.

## D. Validação, fuga e sobreajuste (o método)

- **D1. Varma & Simon (2006),** "Bias in error estimation when using cross-validation for model
  selection", *BMC Bioinformatics* 7:91. DOI: 10.1186/1471-2105-7-91.
  Porque é que afinar hiperparâmetros fora do fold inflaciona o desempenho. É a razão de o
  `loio.py` insistir em afinar **dentro** de cada fold.
- **D2. Cawley & Talbot (2010),** "On over-fitting in model selection and subsequent selection bias
  in performance evaluation", *JMLR* 11:2079-2107.
  Link: https://jmlr.org/papers/v11/cawley10a.html. O mesmo problema, tratado a fundo.
- **D3. Kaufman, Rosset, Perlich (2011),** "Leakage in Data Mining: Formulation, Detection, and
  Avoidance", *ACM KDD 2011*, pp. 556-563. DOI: 10.1145/2020408.2020496.
  Taxonomia de fugas. Útil para nomear com precisão, na dissertação, **que tipo** de fuga o LOIO
  elimina e qual é que não elimina.

## E. Fontes de dados desta tese

- **E1. Tyshkovskiy et al. (2026).** Conjunto de dados de fígado do ITP e modelos tAge.
  Zenodo: 10.5281/zenodo.18763485 · GEO: GSE292885.
  **Confirmar a citação exata do artigo associado** e acrescentar aqui o DOI assim que estiver
  disponível. Ver `data/README.md` para o que descarregar.
- **E2. Mouse Phenome Database, projeto ITP1** (NIH U24 AG066346).
  https://phenome.jax.org/. Sobrevivência animal a animal.

---

## Como acrescentar uma entrada

Autor(es), ano, título entre aspas, revista, volume, páginas, DOI. Depois **uma frase** com o que
retiraste, não o resumo do artigo, a consequência para esta tese. Se não consegues escrever essa
frase, ainda não leste o artigo.
