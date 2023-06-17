# Neko Anime Tracer

Neko Anime Tracer is a simple Discord bot implemented using the `discord.py` library. The bot provides various commands for interacting with users and performing tasks related to anime tracing within a Discord server.

## Features

- **Ping Command**: Responds with the bot's latency.
- **Trace Anime Command**: Allows users to trace anime from a screenshot by providing the attachment.
- **Help Command**: Displays a list of all available commands.

## Getting Started

To use Neko Anime Tracer, you need to have the following:

- Python 3.8 or higher installed on your machine.
- Discord bot token. You can obtain it by creating a new bot in the [Discord Developer Portal](https://discord.com/developers/applications).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/neko-anime-tracer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd neko-anime-tracer
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add the following line:

   ```plaintext
   DISCORD_TOKEN=<your-discord-bot-token>
   ```

   Replace `<your-discord-bot-token>` with the actual bot token you obtained.

### Usage

To run Neko Anime Tracer, execute the following command in the project directory:

```bash
python bot.py
```

The bot will connect to Discord and be ready to respond to commands.

### Command Examples

- Ping Command:

  ```
  /ping
  ```

  Output:
  ```
  Pong! <latency>ms
  ```

- Trace Anime Command:

  ```
  /traceanime <attach a screenshot image>
  ```

  Output:
  ```
  Results:
  - # Result 1
    - Filename: <filename>
    - Episode: <episode>
    - Similarity: <similarity>
    - Video URL: <video-url>
    - Image URL: <image-url>
  ```

- Help Command:

  ```
  /help
  ```

  Output:
  ```
  Bot Commands:

  - ping: Pings the bot and returns the latency.
  - traceanime: Trace anime from a screenshot.
  - help: Show all other commands.
  ```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please create an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
