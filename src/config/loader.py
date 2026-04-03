from pathlib import Path

import yaml

from src.config.models import Config

DEFAULT_CONFIG_PATH = Path("lightspeed-config.yaml")


def load_config(path: Path = DEFAULT_CONFIG_PATH) -> Config:
    with open(path) as f:
        data = yaml.safe_load(f)
    return Config(**data)
