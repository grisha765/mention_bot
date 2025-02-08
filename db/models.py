from tortoise import fields
from tortoise.models import Model

class Settings(Model):
    id = fields.IntField(pk=True)
    chat_id = fields.BigIntField()
    option = fields.CharField(max_length=255)
    parametr = fields.BooleanField(default=False)

    class Meta:  # type: ignore
        table = "settings"
        unique_together = ("chat_id", "option")

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
