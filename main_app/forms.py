from django.forms import ModelForm
from .models import PriorFlame

class PriorFlameForm(ModelForm):
    class Meta:
        model = PriorFlame
        fields = ['name', 'age', 'relationship_duration', 'breakup_date']