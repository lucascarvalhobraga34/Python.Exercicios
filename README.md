# 🐍 Python Essencial – Lista de Exercícios (Nível Profissional)

Este repositório contém uma **lista estruturada de exercícios** para dominar o essencial de Python com foco **profissional**, voltado para quem já possui background sólido em desenvolvimento backend (ex: .NET, Java, etc).

O objetivo **não é aprender lógica**, mas **pensar em Python de forma idiomática**, preparando o terreno para aplicações em **dados, finanças e IA**.

---

## 🎯 Objetivos do Projeto

* Dominar a sintaxe essencial de Python
* Escrever código **limpo, legível e idiomático**
* Entender mutabilidade, tipagem e modelo de objetos do Python
* Criar base sólida para Pandas, NumPy e Machine Learning

---

## 📌 Regras Gerais

* Prefira **clareza a complexidade**
* Use **type hints** sempre que fizer sentido
* Evite efeitos colaterais desnecessários
* Pense em **imutabilidade por padrão**
* Código deve ser legível para outro desenvolvedor sênior

---

## 🔹 BLOCO 1 — Sintaxe e Tipos Fundamentais

### Exercício 1.1 — List Comprehension

Implemente uma função que:

* Receba uma lista de inteiros
* Retorne apenas os números pares
* Eleve cada número ao quadrado
* Ordene o resultado de forma decrescente

**Restrições:**

* Use `list comprehension`
* Não utilize `for` explícito

---

### Exercício 1.2 — Mutabilidade

Crie exemplos que demonstrem:

* Diferença entre `list` e `tuple`
* Diferença entre `dict` e `frozenset`
* Um bug clássico causado por objetos mutáveis

Explique em comentários **quando usar cada tipo**.

---

### Exercício 1.3 — Desempacotamento

Dado:

```python
data = ("PETR4", 32.45, "2026-01-10", 100)
```

Extraia os valores sem usar índices explícitos.

---

## 🔹 BLOCO 2 — Funções e Expressividade

### Exercício 2.1 — Função Pura

Crie a função:

```python
def calcular_retorno(preco_inicial: float, preco_final: float) -> float:
    ...
```

**Requisitos:**

* Sem efeitos colaterais
* Validação de entrada
* Retornar retorno percentual

---

### Exercício 2.2 — Funções como Objetos

Crie uma função que:

* Receba uma lista de preços
* Receba uma função de cálculo (ex: retorno simples, log-retorno)
* Aplique essa função a todos os preços

---

### Exercício 2.3 — Argumentos Nomeados e Defaults

Implemente uma função de **juros compostos** com:

* Valor inicial
* Taxa
* Tempo
* Aporte mensal (opcional)

Teste chamadas usando:

* Argumentos posicionais
* Argumentos nomeados
* Valores default

---

## 🔹 BLOCO 3 — Estruturas de Dados Pythonicas

### Exercício 3.1 — Dict Comprehension

Dada a lista:

```python
prices = [10, 12, 11, 13, 12]
```

Crie um dicionário no formato `{indice: valor}` **sem usar `enumerate`**.

---

### Exercício 3.2 — Agrupamento

Dada a lista:

```python
trades = [
    ("PETR4", 100),
    ("VALE3", 50),
    ("PETR4", 200),
]
```

Crie um dicionário com o total negociado por ticker.

---

### Exercício 3.3 — Sets e Ordem

Implemente uma função que:

* Receba uma lista de tickers
* Retorne apenas valores únicos
* Preserve a ordem original

---

## 🔹 BLOCO 4 — Classes e Dataclasses

### Exercício 4.1 — Classe Tradicional

Crie uma classe `Trade` com:

* Ticker
* Preço
* Quantidade

Inclua validações e `__repr__`.

---

### Exercício 4.2 — `@dataclass`

Reescreva a classe anterior usando `@dataclass`.
Inclua:

* Tipagem
* Propriedade calculada `valor_total`

---

### Exercício 4.3 — Imutabilidade

Transforme a `Trade` em imutável e explique:

* Vantagens
* Desvantagens

---

## 🔹 BLOCO 5 — Exceções

### Exercício 5.1 — Exceção Customizada

Crie a exceção:

```python
class PrecoInvalidoError(Exception):
    ...
```

Utilize-a nas validações do projeto.

---

### Exercício 5.2 — Controle de Fluxo

Simule:

* Leitura de arquivo
* Tratamento de erro
* Mensagem de sucesso
* Liberação de recursos

Utilize `try / except / else / finally`.

---

## 🔹 BLOCO 6 — Iteradores e Generators

### Exercício 6.1 — Generator

Crie um generator que produza retornos percentuais **sob demanda**, sem criar listas intermediárias.

---

### Exercício 6.2 — Lazy vs Eager

Implemente:

* Uma versão usando listas
* Uma versão usando generators

Explique a diferença de consumo de memória.

---

## 🔹 BLOCO 7 — Datas e IO

### Exercício 7.1 — Datas Financeiras

Converta a string:

```python
"2026-01-10"
```

Para `datetime`, some 30 dias e verifique se cai em fim de semana.

---

### Exercício 7.2 — Leitura de CSV

Leia um CSV de preços e:

* Ignore linhas inválidas
* Converta tipos corretamente
* Retorne uma estrutura tipada

---

## 🔹 BLOCO 8 — Organização de Código

### Exercício 8.1 — Módulos

Organize o projeto em:

* `models.py`
* `services.py`
* `utils.py`

Explique o critério da separação.

---

### Exercício 8.2 — Script Executável

Implemente um script com:

```python
if __name__ == "__main__":
```

Explique quando e por que usar.

---

## 🔹 BLOCO 9 — Qualidade Profissional

### Exercício 9.1 — Docstrings

Documente funções, classes e módulos usando **PEP 257**.

---

### Exercício 9.2 — Type Checking

Explique o uso de `mypy`:

* Onde ajuda
* Onde pode atrapalhar

---

## 🏁 Desafio Final — Mini Projeto

### 📊 Analisador de Retornos

Funcionalidades mínimas:

* Leitura de CSV de preços
* Cálculo de retornos
* Retorno acumulado
* Uso de classes, generators e exceções
* Código tipado e organizado

---

## ⏱️ Tempo Estimado

* 25 a 40 horas de prática real
* Ao final, você terá domínio sólido do **Python essencial**

---

🚀 **Próximos passos sugeridos:**

* Migrar exercícios para `pandas` e `numpy`
* Criar backtests simples
* Integrar com Machine Learning
* 

---

## 📁 Estrutura do Projeto

```
python-essencial/
├── pyproject.toml
├── poetry.lock
├── README.md
├── .gitignore
├── .venv/
├── src/
│   └── python_essencial/
│       ├── __init__.py
│       ├── bloco_01_sintaxe.py
│       ├── bloco_02_funcoes.py
│       ├── bloco_03_estruturas.py
│       ├── bloco_04_classes.py
│       ├── bloco_05_excecoes.py
│       ├── bloco_06_generators.py
│       ├── bloco_07_datas_io.py
│       ├── bloco_08_organizacao.py
│       └── bloco_09_qualidade.py
└── tests/
    ├── __init__.py
    └── test_bloco_01.py
```

---

## ⚙️ Configuração Inicial

### 1️⃣ Criar o projeto com Poetry

```bash
poetry init -n
poetry config virtualenvs.in-project true
poetry install
poetry run python scripts/bootstrap.py
```

---

## 📦 `pyproject.toml` (Base Recomendada)

```toml
[tool.poetry]
name = "python-essencial"
version = "0.1.0"
description = "Exercícios profissionais para dominar o essencial de Python"
authors = ["Seu Nome <seu@email.com>"]
readme = "README.md"
packages = [{ include = "python_essencial", from = "src" }]

[tool.poetry.dependencies]
python = "^3.11"

[tool.poetry.group.dev.dependencies]
black = "^24.1.0"
isort = "^5.13.2"
mypy = "^1.8.0"
pytest = "^8.0.0"

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.isort]
profile = "black"

[tool.mypy]
python_version = "3.11"
strict = true
warn_unused_configs = true

[tool.pytest.ini_options]
pythonpath = ["src"]
```

---

## 🧪 Testes

Os testes ficam em `tests/` e seguem o padrão `pytest`.

Exemplo:

```python
from python_essencial.bloco_01_sintaxe import filtrar_pares


def test_filtrar_pares():
    assert filtrar_pares([1, 2, 3, 4]) == [16, 4]
```

Rodar testes:

```bash
poetry run pytest
```

---

## 🎯 Convenções do Projeto

* Um arquivo por bloco de exercícios
* Funções pequenas e puras
* Tipagem explícita sempre que possível
* Sem lógica no escopo global (exceto exemplos simples)

---

## 🧼 Qualidade de Código

Formatar código:

```bash
poetry run black .
poetry run isort .
```

Verificar tipos:

```bash
poetry run mypy src
```

---

## ▶️ Execução Manual

Para executar exemplos pontuais:

```bash
poetry run python -m python_essencial.bloco_01_sintaxe
```

Use:

```python
if __name__ == "__main__":
```

Apenas quando o arquivo puder ser executado isoladamente.

---

## 🚀 Fluxo de Trabalho Recomendado

1. Criar branch ou commit para um bloco
2. Resolver exercícios
3. Rodar `black`, `mypy`, `pytest`
4. Commitar com mensagem clara

---

## 🧠 Mentalidade

> Este projeto não é sobre *terminar rápido*,
> é sobre **pensar corretamente em Python**.

---

## 🔜 Próximas Evoluções

* Adicionar Pandas e NumPy
* Criar mini backtests
* Introduzir notebooks Jupyter
* Integrar com Machine Learning

---

💡 **Dica:** este template pode ser reutilizado como base para qualquer projeto Python profissional.

