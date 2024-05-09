from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class enregistrementForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(enregistrementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'last_name',
            'first_name',
            'password1',
            'password2',
            Submit('submit', 'Envoyer', css_class='btn btn-primary')
        )
