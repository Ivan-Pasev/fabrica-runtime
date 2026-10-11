import fabrica as fab


def test_public_facade_exposes_interface():
    assert hasattr(fab, "Interface")


def test_upstream_runtime_marker():
    assert fab.UPSTREAM_RUNTIME == "gradio"


def test_upstream_version_is_string():
    assert isinstance(fab.upstream_version(), str)
