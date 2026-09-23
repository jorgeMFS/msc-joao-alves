"""Carregamento e junção dos dois lados dos dados.

Os dois ficheiros têm ratinhos diferentes. A única chave que os liga é o fármaco.
Toda a junção acontece aqui, para que o resto do código não tenha de saber disso.
"""
from pathlib import Path

import pyreadr

import pandas as pd

RAW = Path(__file__).resolve().parents[2] / "data" / "raw"


def carregar_expressao(path=None):
    """Matriz de expressão do Zenodo. Linhas = amostras, colunas = genes."""
    if path is None:
        path=RAW/"Expression_data_absolute_rodents.rds"
    df=pyreadr.read_r(path)
    return df


def carregar_metadados_amostras(path=None):
    """Uma linha por amostra: id, fármaco, sexo, idade de início, sítio.

    Se o Zenodo não trouxer o fármaco, procurar no campo `characteristics` do
    GEO (GSE292885) e na tabela suplementar antes de dar por perdido.
    Entregável da semana 1: results/tabela_amostras.csv
    """
    raise NotImplementedError("semana 1")


def carregar_sobrevivencia(path=None):
    """Ficheiro do ITP1: fármaco, dose, sexo, idade de início, sítio, idade de morte."""
    raise NotImplementedError("semana 1")


def construir_tabela_intervencoes(amostras, sobrevivencia, definicao="composto"):
    """Uma linha por intervenção, com os dois lados.

    `definicao` fixa o N do LOIO e não pode mudar depois de escrita no pré-registo:
      "composto"            -> rapamicina conta uma vez
      "composto_dose"       -> rapamicina 14 ppm e 42 ppm contam duas
      "composto_idade"      -> separa também por idade de início

    Devolve: intervencao, n_figados_m, n_figados_f, efeito_vida_m, efeito_vida_f,
             hr_m, hr_f, e os respetivos erros padrão.
    Entregável da semana 1: results/intervencoes.csv
    """
    raise NotImplementedError("semana 1")