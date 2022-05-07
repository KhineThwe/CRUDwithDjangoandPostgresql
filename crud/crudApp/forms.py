from django import forms
from .models import Details
class detailsForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = "__all__"