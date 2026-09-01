import requests


class DiscordException(Exception):
    pass


class Discord:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_message(self, message):
        if str(self.webhook_url) != '1' and self.webhook_url is not None:
            payload = {'content': message}
            r = requests.post(self.webhook_url, json=payload)
            if r.status_code not in (200, 204):
                raise DiscordException(r.content)
