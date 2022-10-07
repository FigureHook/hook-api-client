from enum import Enum


class WebhookLang(str, Enum):
    ZH_TW = "zh-TW"
    EN = "en"
    JA = "ja"

    def __str__(self) -> str:
        return str(self.value)
