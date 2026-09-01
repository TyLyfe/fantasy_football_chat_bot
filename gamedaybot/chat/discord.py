import requests


class DiscordException(Exception):
    pass


class Discord:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message):
        if str(self.webhook_url) != '1' and self.webhook_url is not None:
            # Formats all outgoing text inside a Discord ANSI green code block
            payload = {'content': f"```ansi\n\u001b[0;32m{message}\u001b[0m\n```"}
            r = requests.post(self.webhook_url, json=payload)
            if r.status_code not in (200, 204):
                raise DiscordException(r.content)
