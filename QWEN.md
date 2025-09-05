# Yemen-Jobs-RSS Project Context

## Project Overview

This is a Telegram bot that fetches jobs and tenders from https://yemenhr.com/ and delivers them to users via Telegram. The bot is based on the RSS-to-Telegram-Bot project (RSStT) which is a general-purpose RSS feed reader bot for Telegram.

The bot's username is @Yemenhrbot and there's a public channel at https://t.me/hr_yemen.

### Core Functionality

- Fetches RSS feeds from yemenhr.com
- Sends new job postings to subscribed Telegram users/channels
- Provides subscription management via Telegram commands
- Supports multi-user environment
- Handles media and content formatting for optimal reading experience

## Project Structure

```
.
├── src/                 # Main source code
│   ├── command/         # Telegram command handlers
│   ├── compat/          # Compatibility modules
│   ├── db/              # Database models and migrations
│   ├── helpers/         # Utility functions
│   ├── i18n/            # Internationalization support
│   ├── monitor/         # RSS feed monitoring logic
│   ├── parsing/         # Content parsing and formatting
│   ├── web/             # Web-related functionality
│   └── ...              # Core modules (env, log, etc.)
├── scripts/             # Utility scripts
├── docs/                # Documentation
├── telegramRSSbot.py    # Main entry point
├── main.py              # Simple test entry point
├── setup.py             # Package setup
├── pyproject.toml       # Project configuration
├── Procfile             # Deployment configuration
├── app.json             # Heroku deployment config
└── README.md            # Project description
```

## Technology Stack

- **Language**: Python 3.12+
- **Framework**: Telethon (Telegram client library)
- **Database**: SQLite/PostgreSQL (via Tortoise ORM)
- **Scheduling**: APScheduler
- **Networking**: aiohttp, python-socks
- **Logging**: colorlog
- **Environment**: python-dotenv

## Key Components

### Main Entry Point
- `telegramRSSbot.py` - Production entry point
- `src/entrypoint.py` - Core initialization and main loop

### Configuration
- `src/env.py` - Environment variable parsing and configuration
- `.env.sample` - Sample environment configuration
- Environment variables for API keys, database, proxies, etc.

### Core Services
- **Monitor**: RSS feed monitoring and fetching
- **Database**: Subscription and user data storage
- **Telegram Client**: Message sending and command handling
- **Scheduler**: Periodic feed checking

## Building and Running

### Prerequisites
1. Python 3.12+
2. Required API credentials (Telegram bot token, API ID/hash)
3. Database (SQLite by default, PostgreSQL supported)

### Installation
```bash
# Install dependencies (using pip or other package manager)
pip install -e .

# Or if using uv.lock
pip install --no-deps -e .
```

### Configuration
1. Copy `.env.sample` to `.env`
2. Set required environment variables:
   - `TOKEN` - Telegram bot token
   - `MANAGER` - Telegram user ID of bot manager
3. Optional configurations for API keys, database, proxies, etc.

### Running the Bot
```bash
# Standard run
python telegramRSSbot.py

# With custom config directory
python telegramRSSbot.py -c /path/to/config

# Test mode (no login)
TOKEN=test python telegramRSSbot.py
```

### Deployment
- **Heroku**: Configured via `app.json` and `Procfile`
- **Railway**: Automatic configuration support
- **Docker**: Health check support via `scripts/health_check.py`

## Development Guidelines

### Code Structure
- Modular design with clear separation of concerns
- Asynchronous programming with asyncio
- Type hints for better code documentation
- Internationalization support

### Testing
- Tests should be added in the `tests/` directory (not present in current structure)
- Integration tests for Telegram interactions
- Unit tests for parsing and utility functions

### Contributing
1. Follow existing code style and patterns
2. Add type hints to new functions
3. Write clear docstrings for public APIs
4. Test changes thoroughly before submitting

## Environment Variables

### Required
- `TOKEN` - Telegram bot token
- `MANAGER` - Telegram user ID(s) that can manage the bot

### Optional
- `API_ID`/`API_HASH` - Custom Telegram API credentials
- `DATABASE_URL` - Database connection string
- Proxy settings (`T_PROXY`, `R_PROXY`)
- Customization options (see `docs/advanced-settings.md`)

## Common Operations

### Adding New Features
1. Identify the appropriate module (command, monitor, parsing, etc.)
2. Follow existing patterns in the codebase
3. Add necessary database migrations if schema changes are needed
4. Update command handlers if new user interactions are added

### Debugging
- Enable debug logging with `DEBUG=1`
- Check logs for error messages
- Use test mode (`TOKEN=test`) for initial development
- Monitor database state for subscription issues

### Maintenance
- Regular database cleanup may be needed
- Monitor for API rate limits
- Update dependencies periodically
- Check for RSS feed format changes

## Important Notes

1. This is a fork/customization of the RSStT project specifically for Yemen job postings
2. The bot is designed for continuous operation with periodic feed checking
3. Database migrations are handled via aerich (see scripts directory)
4. Support for multiple users and channels via subscription management
5. Media handling optimized for Telegram delivery