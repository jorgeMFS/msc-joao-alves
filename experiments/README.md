# Experiências

Uma pasta por experiência. Leve, mas reprodutível: qualquer pessoa, tu daqui a três meses, ou um
orientador, devia conseguir ler a pasta e perceber o que fizeste, o que aconteceu, e o que significou.

Isto é diferente de `notebooks/`. Um notebook é exploração descartável. Uma experiência tem uma
pergunta e uma resposta, e fica no registo mesmo quando falha.

## Convenção

Criar `experiments/NN-nome-curto/` (ex.: `01-reproduzir-tage-publicado/`) com um `notes.md`:

- **Questão.** O que se quer descobrir. Uma frase, com resposta verificável.
- **Montagem.** Dados, versões, divisão, modelo, parâmetros. O suficiente para repetir.
- **O que fiz.** Comandos ou passos, em curto.
- **Resultado.** Números. Incluindo os maus.
- **Conclusão.** O que significa para a tese, e que decisão sustenta.

Juntar código e configs pequenos ao lado do `notes.md`. **Não** juntar dados, matrizes de expressão,
nem nada com dados de animais (ver `.gitignore`).

## Índice

| # | Experiência | Questão | Estado |
|---|---|---|---|
| 01 | reproduzir-tage-publicado | Com os pesos publicados, obtenho o valor do artigo? | planeada |
| 02 | loio-piloto | O LOIO corre ponta a ponta com 3 intervenções? | planeada |
| 03 | baseline-aleatorio | Quanto do desempenho vem do procedimento e não dos genes? | planeada |

> A 01 é um portão. Se um valor publicado não se reproduz com os pesos publicados, para tudo e fala
> com os orientadores antes de avançar, o problema está nos dados ou no carregamento, e todos os
> números seguintes herdam-no.
