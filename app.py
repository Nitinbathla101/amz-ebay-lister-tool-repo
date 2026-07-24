from ebay.config import load_config

def main():
    config = load_config()

    print("Configuration loaded successfully!")
    print(f"Environment : {config.environment}")
    print(f"Runame      : {config.runame}")


if __name__ == "__main__":
    main()