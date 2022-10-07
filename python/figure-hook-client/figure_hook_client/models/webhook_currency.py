from enum import Enum


class WebhookCurrency(str, Enum):
    JPY = "JPY"
    USD = "USD"
    EUR = "EUR"

    def __str__(self) -> str:
        return str(self.value)
