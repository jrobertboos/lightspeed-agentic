from src.config import load_config
from src.runners.uvicorn import run


def main():
    config = load_config()
    run(config)


if __name__ == "__main__":
    main()
