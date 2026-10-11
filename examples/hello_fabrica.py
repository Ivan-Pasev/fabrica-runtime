import fabrica as fab


def greet(name: str) -> str:
    return f"Hello, {name}. This is Fabrica Runtime."


demo = fab.Interface(fn=greet, inputs="text", outputs="text", title="Fabrica Runtime")


if __name__ == "__main__":
    demo.launch()
