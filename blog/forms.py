from django import forms
from crispy_forms.helper import FormHelper
from .models import Feedback
 
 
class FeedbackForm(forms.ModelForm):
    helper = FormHelper()

    class Meta:
        model = Feedback
        fields = "__all__"

    variable = 'Mysterious Science | Contact Us'