# Telegram Calculator Bot
## Before Running the Bot
Before running the bot, make sure to replace the placeholder value in the `BOT_TOKEN` variable with your own bot token obtained from Telegram BotFather. This token should be placed in the `bot.py` file.

To obtain a bot token from Telegram BotFather:
1. Start a conversation with [BotFather](https://telegram.me/BotFather) on Telegram.
2. Follow the instructions to create a new bot and obtain its token.
3. Copy the token provided by BotFather.
4. Open the `bot.py` file in your project directory.
5. Locate the `BOT_TOKEN` variable and replace the placeholder value with your bot token.
6. Save the changes to the `bot.py` file.

Now you can run the bot with your own bot token.

## Project Title
Telegram Calculator Bot

## Overview
This Telegram bot supports the commands `/add`, `/mult`, and `/calc` which respectively perform addition of two numbers, multiplication of two numbers, and evaluation of arithmetic expressions.

## Usage
To use the bot, first search for the bot on Telegram, then send one of the following commands along with the desired numbers:
- `/add <n> <m>`: Add two numbers `n` and `m`.
- `/mult <n> <m>`: Multiply two numbers `n` and `m`.
- `/calc <exp>`: Evaluate the arithmetic expression `exp`.

## Installation and Execution
To use the bot, follow these steps:
1. Install the required dependencies by running:
    ```
    pip install python-telegram-bot
    ```
2. Run the `bot.py` file in the initial project directory.
3. Add the bot to Telegram and start using it.

## Examples
- For addition: `/add 2 3` Output: `2 + 3 = 5`
- For multiplication: `/mult 2 3` Output: `2 * 3 = 6`
- For evaluating arithmetic expression: `/calc 1 + 3 * 2` Output: `1 + 3 * 2 = 7`

## Development Guide
If you wish to develop the bot further, you can edit the `bot.py` file and add new features to it.

## Open Issues
No open issues have been reported.

## Contribution
If you wish to contribute to the development of the bot, you can Fork it and submit your suggestions and Pull Requests.
