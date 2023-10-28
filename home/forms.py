from main.models import Quip
from django.forms import ModelForm, CharField, Textarea


class NewQuipForm(ModelForm):
    text = CharField(
        required=True,
        widget=Textarea(
            attrs={
                "cols": "80",
                "rows": "5",
                "placeholder": "What is going on?",
                "style": "font-size: 1.3em;",
                "autofocus": True,
            }
        ),
        label="",
        min_length=1,
        max_length=140,
    )

    class Meta:
        model = Quip
        fields = ("text",)
