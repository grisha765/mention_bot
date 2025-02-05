# mention_bot
This Telegram bot can mention all chat members or only administrators.

### Initial Setup

1. **Clone the repository**: Clone this repository using `git clone`.
2. **Create Virtual Env**: Create a Python Virtual Env `venv` to download the required dependencies and libraries.
3. **Download Dependencies**: Download the required dependencies into the Virtual Env `venv` using `pip`.

```shell
git clone https://github.com/grisha765/mention_bot.git
cd mention_bot
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt 
```

### Deploy

- Run the bot:
    ```bash
    TG_TOKEN="your_telegram_bot_token" .venv/bin/python main.py
    ```

- Other working env's:
    ```env
    LOG_LEVEL="INFO"
    TG_ID="your_telegram_api_id"
    TG_HASH="your_telegram_api_hash"
    TG_TOKEN="your_telegram_bot_token"
    ```

#### Container

- Pull container:
    ```bash
    podman pull ghcr.io/grisha765/mention_bot:latest
    ```

- Run bot:
    ```bash
    podman run -d \
    --name mention_bot \
    -e TG_TOKEN="your_telegram_bot_token" \
    ghcr.io/grisha765/mention_bot:latest
    ```

## Usage

- `@all` - Mention all from chat.

- `@admins` - Mention only administrators from chat.
