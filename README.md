# CyberTemp API Wrapper

A lightweight Python wrapper for the [cybertemp.xyz](https://cybertemp.xyz) API.

## Features

- Get available email domains
- Check public inboxes
- Access specific emails by ID
- Check account balance (requires API key)
- Access private inbox (requires API key)
- Delete specific emails or full inboxes (requires API key)

## Installation

- Python 3.10 or higher

```bash
pip install -r requirements.txt
```

## Usage

```python
from cybertemp import CyberTemp

client = CyberTemp(api_key="your_api_key")  # Optional if only using public endpoints

# Get available domains
domains = client.get_domains()

# Check a public inbox
inbox = client.check_mail("example@domain.com")

# Get an email by ID
email = client.check_mail_by_id("email_id")

# Check your balance (requires API key)
balance = client.check_balance()

# Access private mails (requires API key with Bearer auth)
private_emails = client.get_private_mails()

# Delete an email (requires API key with Bearer auth)
client.delete_mail("email_id")

# Delete entire inbox (requires API key with Bearer auth)
client.delete_inbox("example@domain.com")
```

## Note

- Some endpoints require an API key.
- Auth headers are handled automatically depending on the endpoint.

[Discord](https://discord.gg/undesync)