from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class EbayConfig:
    client_id: str
    client_secret: str
    dev_id: str
    runame: str
    environment: str
    callback_host: str
    callback_port: int


def load_config() -> EbayConfig:
    required = [
        "EBAY_CLIENT_ID",
        "EBAY_CLIENT_SECRET",
        "EBAY_DEV_ID",
        "EBAY_RUNAME",
    ]

    missing = [key for key in required if not os.getenv(key)]

    if missing:
        raise ValueError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    return EbayConfig(
        client_id=os.getenv("EBAY_CLIENT_ID"),
        client_secret=os.getenv("EBAY_CLIENT_SECRET"),
        dev_id=os.getenv("EBAY_DEV_ID"),
        runame=os.getenv("EBAY_RUNAME"),
        environment=os.getenv("EBAY_ENVIRONMENT", "PRODUCTION").upper(),
        callback_host=os.getenv("LOCAL_CALLBACK_HOST", "127.0.0.1"),
        callback_port=int(os.getenv("LOCAL_CALLBACK_PORT", "8080")),
    )