from pathlib import Path

BASE = Path("src/python_essencial")

FILES = [
    "bloco_01_sintaxe.py",
    "bloco_02_funcoes.py",
    "bloco_03_estruturas.py",
    "bloco_04_classes.py",
    "bloco_05_excecoes.py",
    "bloco_06_generators.py",
    "bloco_07_datas_io.py",
    "bloco_08_organizacao.py",
    "bloco_09_qualidade.py",
]

def main() -> None:
    BASE.mkdir(parents=True, exist_ok=True)
    (BASE / "__init__.py").touch(exist_ok=True)

    for file in FILES:
        (BASE / file).touch(exist_ok=True)

    Path("tests").mkdir(exist_ok=True)
    (Path("tests") / "__init__.py").touch(exist_ok=True)

if __name__ == "__main__":
    main()
