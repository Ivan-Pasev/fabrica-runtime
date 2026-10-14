import fabrica as fab


@fab.capability(id="math.add", version="1.0.0")
def add(a: int, b: int = 1) -> int:
    """Add two integers."""
    return a + b


def test_capability_remains_callable():
    assert add(2, 3) == 5


def test_capability_metadata_is_exposed():
    spec = fab.get_capability_spec(add)
    assert spec.id == "math.add"
    assert spec.name == "add"
    assert spec.version == "1.0.0"
    assert spec.output == "int"
    assert spec.effects == ("PURE",)
    assert spec.description == "Add two integers."


def test_ports_are_reflected():
    spec = fab.get_capability_spec(add)
    assert [p.name for p in spec.inputs] == ["a", "b"]
    assert [p.annotation for p in spec.inputs] == ["int", "int"]
    assert [p.required for p in spec.inputs] == [True, False]


def test_capability_detection():
    assert fab.is_capability(add)
    assert not fab.is_capability(lambda: None)


def test_spec_is_machine_readable():
    data = fab.get_capability_spec(add).to_dict()
    assert data["id"] == "math.add"
    assert data["inputs"][0]["name"] == "a"
