import yaml
import dotenv
import os
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load .env config and envs
envs = {
    **dotenv.dotenv_values(config_dir / "config.example.env"),
    **os.environ,
}

# config parameters
telegram_token = envs["TELEGRAM_TOKEN"]
openai_api_key = envs["OPENAI_API_KEY"]
use_chatgpt_api = bool(int(envs.get("USE_CHATGPT_API", 1)))
allowed_telegram_usernames = envs["ALLOWED_TELEGRAM_USERNAMES"].split(",")
new_dialog_timeout = float(envs["NEW_DIALOG_TIMEOUT"])
enable_message_streaming = bool(int(envs.get("ENABLE_MESSAGE_STREAMING", 1)))
mongodb_uri = f"mongodb://mongo:{envs['MONGODB_PORT']}"

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# prices
chatgpt_price_per_1000_tokens = float(envs.get("CHATGPT_PRICE_PER_1000_TOKENS", 0.002))
gpt_price_per_1000_tokens = float(envs.get("GPT_PRICE_PER_1000_TOKENS", 0.02))
whisper_price_per_1_min = float(envs.get("WHISPER_PRICE_PER_1_MIN", 0.006))
