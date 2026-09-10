# Como se trabalha neste repositório

Escrito para o João. Lê uma vez de início ao fim, e volta cá quando o git te pregar uma partida.

O modelo é **fork + upstream + pull request**. O repositório dos orientadores é o `upstream`, e é a
versão de referência. O teu fork é o `origin`, onde tens liberdade total. Nada entra no `upstream`
sem passar por um pull request.

Isto não é burocracia: é o que faz com que, daqui a um ano, se consiga reconstruir *porque* é que
uma decisão foi tomada, a partir do histórico. Numa tese que se defende pelo método, o histórico
faz parte do resultado.

---

## 1. Montar, uma vez só

**Fork** de `jorgeMFS/msc-joao-alves` no GitHub. Depois, na tua máquina:

```bash
git clone git@github.com:joaoalvess2116/msc-joao-alves.git
cd msc-joao-alves

# ligar o repositório dos orientadores como upstream
git remote add upstream git@github.com:jorgeMFS/msc-joao-alves.git

# confirmar: deves ver origin (teu, fetch+push) e upstream (deles)
git remote -v
```

Ambiente:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

---

## 2. O ciclo, todas as semanas

### a) Sincronizar antes de começar

Faz isto **sempre** antes de abrir uma branch nova. Evita conflitos que depois custam uma tarde.

```bash
git checkout main
git fetch upstream
git merge upstream/main      # ou: git rebase upstream/main
git push origin main
```

### b) Uma branch por tarefa

```bash
git checkout -b portao/tabela-amostras
```

Nomes: `<área>/<o-quê>`, em minúsculas e com hífenes.

| Prefixo | Para quê | Exemplo |
|---|---|---|
| `portao/` | as três verificações da semana 1 | `portao/analise-potencia` |
| `loio/` | o resultado primário | `loio/rotulos-dentro-do-fold` |
| `analise/` | substituição, dimorfismo, nulos | `analise/surrogate-trial-level` |
| `docs/` | documentação, leituras, glossário | `docs/glossario-permutacao` |
| `semanal/` | o relatório da semana | `semanal/semana-03` |

### c) Commits que se leem daqui a um ano

Uma linha de assunto no imperativo, até ~70 caracteres. Se precisar de explicação, linha em branco
e depois o corpo, **o porquê**, não o quê (o quê está no diff).

```
Construir rótulos de mortalidade dentro do fold

Os rótulos publicados do tAge derivam das curvas de sobrevivência de
todas as intervenções, incluindo a que está a ser retida. Usá-los
reintroduz a fuga que a tese denuncia.

Refs #7
```

Commits pequenos e frequentes. Um commit que muda três coisas não se consegue reverter em paz.

### d) Pull request

```bash
git push -u origin portao/tabela-amostras
```

Depois, no GitHub, abre o PR **do teu fork para `upstream/main`**. No corpo:

- **O que faz** e **porquê**, em duas ou três linhas.
- **Closes #N** se fecha um issue.
- Se produz números, **põe os números no PR**. O orientador não devia ter de correr o código para
  saber o que aconteceu.
- Se ficou alguma coisa por resolver, diz qual.

PRs pequenos são revistos no próprio dia. PRs de 40 ficheiros ficam à espera uma semana.

---

## 3. Issues

**Cada verificação do portão da semana 1 é um issue.** O que não está em issue, não existe, não
porque seja regra, mas porque é assim que se sabe, na reunião, o que está aberto.

Um issue tem: o que é preciso fazer, como se sabe que está feito (o entregável), e o que bloqueia
se não estiver.

Etiquetas sugeridas:

| Etiqueta | Quando |
|---|---|
| `portao` | semana 1, bloqueia tudo o resto |
| `primario` | resultado primário, semanas 5 a 9 |
| `bloqueado` | à espera de decisão dos orientadores |
| `escrita` | dissertação |

---

## 4. Onde a semana entra nisto

Na sexta, o `relatorios_semanais/semana-NN.md` sai numa branch `semanal/semana-NN` e num PR próprio.

Isso tem uma vantagem prática: a secção **Escrito** do relatório é literalmente a lista de PRs da
semana, e a secção **Executado** aponta para os ficheiros em `results/`. Não há trabalho duplicado -
o relatório é a leitura dos PRs, não um exercício à parte.

---

## 5. O que nunca vai para o git

Está no `.gitignore`, mas convém saber porquê:

- **Dados.** Nem a matriz de expressão, nem o ficheiro do ITP, nem nada derivado que contenha dados
  ao nível do animal. Descarregam-se para `data/raw/` seguindo o `data/README.md`.
- **Figuras pesadas** geradas em `results/`. As **tabelas pequenas** em `results/` **vão**: são o
  material suplementar da tese e devem ter histórico.
- **`.venv/`**, `__pycache__/`, `.DS_Store`.

Se um ficheiro grande entrar por engano, avisa antes de fazer force-push: reescrever histórico
partilhado estraga o clone de toda a gente.

---

## 6. Quando o git corre mal

| Situação | O que fazer |
|---|---|
| Commit na `main` por engano | `git branch minha-branch && git reset --hard upstream/main && git checkout minha-branch` |
| Conflito ao sincronizar | Resolver ficheiro a ficheiro, `git add`, `git merge --continue`. Não `--force`. |
| Commit com a mensagem errada (ainda não empurrado) | `git commit --amend` |
| Ficheiro grande commitado por engano | **Pergunta antes de tentar corrigir.** |
| Perdido | `git status` e `git log --oneline --graph --all`. Quase nada se perde de verdade no git. |

---

## 7. Resumo, para colar no monitor

```bash
git checkout main && git fetch upstream && git merge upstream/main   # sincronizar
git checkout -b area/tarefa                                          # ramificar
# ... trabalhar, commits pequenos ...
git push -u origin area/tarefa                                       # empurrar
# abrir PR para upstream/main, com os números no corpo
```
