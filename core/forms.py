from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Request, Donation

class RequestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Request
        fields = ['name','email','tickets']

class DonateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(DonateForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Donation
        fields = ['name','email','tickets']