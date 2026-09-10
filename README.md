# msc-joao-alves

**Relógios de envelhecimento como endpoints substitutos**
Dissertação de mestrado (MBC 2026/27) do **João Alves**: [@joaoalvess2116](https://github.com/joaoalvess2116).
Orientadores: Jorge Miguel Silva (IEETA) e Gabriela Moura (DCM / iBiMED).

**Pergunta.** Os relógios transcriptómicos de envelhecimento servem como endpoint substituto para
intervenções geroprotetoras? Isto é: quando um fármaco **novo, nunca visto pelo modelo**, faz o
relógio descer, isso prediz que o fármaco prolonga o tempo de vida?

**Teste central.** *Leave one intervention out* (LOIO). Retirar um fármaco inteiro do treino,
retreinar os dois relógios (cronológico e de mortalidade) nos restantes, e medir se o relógio de
mortalidade mantém alguma vantagem quando vê o fármaco pela primeira vez.

**A previsão, pré-registada.** Os valores publicados são r² ≈ 0,13 (cronológico) e r² ≈ 0,28
(mortalidade). A tese prevê que o segundo **colapse para ≈ 0,13** sob LOIO, porque a vantagem viria
da construção do rótulo, não do mecanismo biológico. A hipótese primária é de **equivalência com
margem pré-registada**, não um teste de diferença.

---

## Por onde começar

1. Este ficheiro, até ao fim.
2. **`docs/proposta.md`**: a proposta submetida. O porquê, os cinco objetivos, a componente de ML.
3. **`docs/metodo.md`**: o método de uma assentada. Escrito para se ler de uma vez.
4. **`protocol/semana1_portao.md`**: as três perguntas que têm de passar antes de qualquer análise.
5. **`docs/reading-list.md`** §A1, §C1, §C0, as três leituras da semana 1.

Só depois se abre código.

## Mapa do repositório

| Caminho | O que é |
|---|---|
| `CONTRIBUTING.md` | Como se trabalha: fork, upstream, branches, PRs, issues. |
| `docs/metodo.md` | **Começa aqui.** A pergunta, os dados, o LOIO, os desfechos possíveis, a ordem de trabalho. |
| `docs/reading-list.md` | Artigos a ler, agrupados, cada um com DOI e o que retirar dele. |
| `docs/links.md` | O que se clica, descarrega e corre: portais de dados, pacotes, ferramentas. |
| `docs/glossary.md` | Termos técnicos num só sítio. Vai crescendo. |
| `docs/proposta.md` | **A proposta submetida ao MBC**, estruturada: problema, objetivos, componente de ML, plano. Fonte autoritativa. |
| `docs/figuras/` | As quatro figuras da proposta (desenho, CAST, esquemas de validação, cronograma). |
| `protocol/` | Pré-registo, portão da semana 1, análise de potência. **Fecha-se antes de analisar.** |
| `relatorios_semanais/` | Um ficheiro por semana. Copiar `TEMPLATE.md` todas as sextas. |
| `src/clocks/` | Código Python: carregar dados, construir rótulos dentro do fold, LOIO. |
| `analysis/R/` | Substituição ao nível do ensaio (pacote `Surrogate`). |
| `experiments/` | Uma pasta por experiência, com pergunta e resposta. Ver `experiments/README.md`. |
| `notebooks/` | Exploração descartável. O que valer a pena passa a `experiments/`. |
| `results/` | Tabelas e figuras geradas. As tabelas pequenas vão para o git; as figuras não. |
| `data/` | Dados brutos e processados. **Nada disto vai para o git**: ver `data/README.md`. |

## Relatórios semanais

**Todas as sextas**, copiar `relatorios_semanais/TEMPLATE.md` para `semana-NN.md` e preencher.
O `semana-01.md` já está começado como exemplo.

O formato separa de propósito três coisas:

- **Lido**: o que se leu, e o que se reteve *para esta tese*, não o resumo do artigo.
- **Escrito**: que ficheiros, para o orientador poder abrir.
- **Executado**: o que correu de facto, **com números**. "Nada" é uma resposta legítima.

Mais uma tabela de **números da semana**, que é o que permite ver progresso entre reuniões sem
reler o histórico, e uma secção de **decisões**, que é a que mais vale daqui a seis meses quando for
preciso justificar na dissertação porque é que uma intervenção conta como uma e não como três.

## Fontes de dados

| O que | Onde | Conteúdo |
|---|---|---|
| Transcriptomas de fígado (170 amostras) e modelos tAge | Zenodo `10.5281/zenodo.18763485` | linhas = ratinhos, colunas = genes, contagens de mRNA |
| RNA-seq cru | GEO `GSE292885` | ficheiros de sequenciação |
| Sobrevivência animal a animal | Mouse Phenome Database, projeto ITP1 | fármaco, sexo, idade de morte |

> **A restrição que define o projeto.** Os dois lados têm ratinhos diferentes. Os sequenciados foram
> sacrificados aos 22 meses; os da sobrevivência morreram naturalmente. Ligam-se só ao nível do
> fármaco. Consequência: a substituição **individual** não é estimável, só a de **nível de ensaio**.
> Isto vai no pré-registo e na introdução, não na discussão, como limitação descoberta no fim.

## Plano (18 semanas)

| Semanas | Bloco | Entregável |
|---|---|---|
| 1 | Portão de viabilidade, sem código de modelação | `protocol/potencia.md`, `protocol/pre_registo.md` fechado |
| 2 a 4 | Reproduzir um valor publicado com os pesos do tAge | `experiments/01-.../notes.md` |
| 5 a 9 | LOIO, resultado primário | `results/loio.csv` |
| 10 a 14 | Tabela de efeitos por intervenção | `results/intervencoes.csv` com os dois eixos |
| 15 a 18 | Substituição, dimorfismo sexual, nulos | `results/` + rascunho da discussão |

**A redação começa durante a fase primária e é contínua até à entrega**: não no fim.

## Os cinco objetivos

| # | Objetivo | Estatuto |
|---|---|---|
| 1 | Generalização para intervenções não observadas (LOIO), mortalidade vs cronológico | **primário** |
| 2 | Dimorfismo sexual, com a canagliflozina como caso de maior potência | convergente, exploratório |
| 3 | Substituição ao nível do ensaio (Buyse-Molenberghs) com efeito-limiar | secundário |
| 4 | Especificidade de módulo (relógios de via) | exploratório, condicional |
| 5 | Comparação contra nulo estocástico | controlo |

Detalhe em `docs/proposta.md`.

## Como se trabalha

**Fork + upstream + pull request.** O repositório dos orientadores é o `upstream` e é a versão de
referência; o teu fork é o `origin`. Nada entra no `upstream` sem PR.

- **Branches e pull requests.** Não se commita para `main`. Uma branch por tarefa.
- **Issues.** Cada verificação do portão da semana 1 é um issue.
- **Reunião semanal**, com o `semana-NN.md` escrito na sexta anterior, no seu próprio PR.
- **A escrita começa cedo**, em paralelo com o resultado primário, não no fim.

**Ver [`CONTRIBUTING.md`](CONTRIBUTING.md)** para os comandos, a convenção de nomes de branches, o
formato dos commits e o que fazer quando o git corre mal.

## Duas regras que não se negoceiam

1. **O pré-registo fecha antes de qualquer análise.** Hipótese, margem, esquema de folds e regra de
   decisão escritos antes de ver os dados. Se o resultado surpreender, o mérito é ter-se comprometido
   antes.
2. **Os rótulos do relógio de mortalidade são construídos dentro de cada fold.** Usar os rótulos
   publicados do tAge reintroduz exatamente a fuga que a tese denuncia, só que escondida.
   Ver `src/clocks/loio.py`.

## Ambiente

Python 3.11 · R 4.x

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

```r
install.packages("Surrogate")
```
