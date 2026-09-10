# Links: coisas para ver, descarregar e correr

A lista de leitura (`reading-list.md`) tem os artigos. Este ficheiro é para o que se clica, descarrega
e corre. Verificar quando um link deixar de funcionar; se apodrecer, pesquisar pelo nome do recurso.

## Dados

| O que | Onde | Notas |
|---|---|---|
| Transcriptomas de fígado (170) + modelos tAge | Zenodo `10.5281/zenodo.18763485` | https://doi.org/10.5281/zenodo.18763485 · a matriz e os pesos publicados |
| RNA-seq cru | GEO `GSE292885` | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE292885 · só se for preciso reprocessar |
| Sobrevivência ITP | Mouse Phenome Database | https://phenome.jax.org/ · procurar o projeto **ITP1** |
| Página do ITP | NIA | https://www.nia.nih.gov/research/dab/interventions-testing-program-itp |

> Os dois primeiros e o terceiro **têm ratinhos diferentes**. Os sequenciados foram sacrificados aos
> 22 meses; os da sobrevivência morreram naturalmente. Só se ligam ao nível do fármaco. Esta é a
> restrição central do desenho, ver `docs/metodo.md`.

## Ferramentas

- **scikit-learn**: https://scikit-learn.org/stable/. O que interessa aqui:
  [`GroupKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GroupKFold.html)
  (a base do LOIO) e
  [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
  (para que o pré-processamento fique dentro do fold e não fuja).
- **lifelines**: https://lifelines.readthedocs.io/. Kaplan-Meier e Cox em Python, para os efeitos
  no tempo de vida a partir do ficheiro do ITP.
- **Pacote `Surrogate` do R**: https://cran.r-project.org/package=Surrogate. Implementa o
  enquadramento meta-analítico do Buyse-Molenberghs. É o que `analysis/R/surrogacy.R` vai usar.
- **statsmodels**: https://www.statsmodels.org/. Regressão e intervalos para a tabela de efeitos.

## Contexto

- **Aging Biomarker Consortium**: https://academic.oup.com/lifemedicine (procurar os consensos
  sobre biomarcadores de envelhecimento). Útil para a introdução da dissertação.
- **Open Genes**: https://open-genes.com/. Base de dados de genes associados a longevidade;
  serve para sanidade quando um gene aparecer com peso alto num relógio.

## Onde isto tudo vai dar

Fluxo do projeto, em uma linha: **Zenodo** (expressão) + **MPD/ITP1** (sobrevivência) →
`results/tabela_amostras.csv` → `results/intervencoes.csv` → LOIO (`src/clocks/loio.py`) →
`analysis/R/surrogacy.R` → tabela e figuras em `results/`.
