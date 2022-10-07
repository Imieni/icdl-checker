from django import forms 
from .models import BaseMode


class BaseModeForm(forms.ModelForm):
	#response = forms.CharField(required= True)

	class Meta:
		models = BaseMode
		fields = ["response"]