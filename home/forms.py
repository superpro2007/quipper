from main.models import Quip
from django.forms import ModelForm, CharField, Textarea


class NewQuipForm(ModelForm):
    text = CharField(
        required=True,
        widget=Textarea(
            attrs={"cols": "80", "rows": "10", "placeholder": "What is going on?"}
        ),
        label="",
        min_length=1,
        max_length=140,
    )

    class Meta:
        model = Quip
        fields = ("text",)
