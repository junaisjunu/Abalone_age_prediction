from src.utils.common import read_yaml
from pathlib import Path


def test_read_yaml():
    test_content = read_yaml(Path('config/config.yaml'))
    assert test_content.artifacts_root == "artifacts"
