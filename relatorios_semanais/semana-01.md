<!-- Primeira entrada, parcialmente preenchida como exemplo. Copiar o TEMPLATE.md
     para semana-02.md na próxima sexta. Apagar os comentários. -->

# Semana 01 (AAAA-MM-DD a AAAA-MM-DD)

**Horas dedicadas:** ~N h · **Bloco do plano:** 1, portão de viabilidade (sem código de modelação)

---

## 1. Lido

As três leituras da semana 1 (`docs/reading-list.md`: §A1, §C1, §C0).

- **Tyshkovskiy et al. (2026)**, *Nature*, o artigo posto à prova. Retido: o carimbo do relógio de mortalidade vem das curvas de sobrevivência dos fármacos do ITP, e a validação deixou de fora tecidos, conjuntos de dados e espécies, **nunca uma intervenção inteira**.
- **Prentice (1989)**: critérios operacionais para um marcador substituir um desfecho. Retido: são condições fortes, e "correlaciona" não é uma delas.
- **CAST (1989)**: dois antiarrítmicos suprimiram a arritmia e duplicaram a mortalidade. Retido: é o contra-exemplo que justifica a tese existir. Prever não é substituir.

## 2. Escrito

| Ficheiro | O que é | Estado |
|---|---|---|
| `protocol/semana1_portao.md` | as três perguntas do portão, respondidas | em curso |
| `results/tabela_amostras.csv` | uma linha por amostra: fármaco, sexo, idade de início, sítio | por fazer |

## 3. Executado

- **Nada de modelação**, por desenho. A semana 1 é portão de viabilidade e o código de modelação só abre depois de o pré-registo estar fechado.
- **Feito:** descarregados os ficheiros do Zenodo e os metadados do GEO; inspecionadas as colunas para ver se as amostras trazem identificação de fármaco.

## 4. Números da semana

| Quantidade | Valor | Semana anterior |
|---|---:|---:|
| Amostras de fígado no Zenodo | 170 | - |
| Amostras com fármaco identificado | ? | - |
| Intervenções com transcriptoma **e** sobrevivência | ? | - |
| N do LOIO (= linha acima) | ? | - |

> A terceira linha é o número que decide a tese. Se for baixo (< 8 a 10), a simulação de potência da pergunta 3 do portão vai dizer que o intervalo de confiança é largo de mais, e a pergunta tem de ser reformulada **nesta semana**.

## 5. Bloqueado

- [ ] Confirmar com os orientadores o que conta como "uma intervenção": composto, composto × dose, ou composto × idade de início. Fixa o N do LOIO e **não pode mudar depois** de escrito no pré-registo.

## 6. Decisões tomadas

- **Decidido:** nada ainda. **Porquê:** a definição de intervenção depende do que a tabela de amostras mostrar.

## 7. Plano para a próxima semana

- [ ] Fechar `results/tabela_amostras.csv` com as 170 linhas.
- [ ] Cruzar com o ITP1 e produzir `results/intervencoes.csv`.
- [ ] Correr a simulação de potência e escrever `protocol/potencia.md`.
- [ ] Se o portão passar, escrever `protocol/pre_registo.md` e só então abrir código.
