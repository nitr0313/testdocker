from django import forms
from . import models


class FlatForm(forms.ModelForm):

    class Meta:
        model = models.Flat
        # fields = ('street', 'home_number', 'entrance',
        #           'number', 'person', 'active')
        fields = '__all__'
        street = forms.ModelChoiceField(
            queryset=models.Street.objects.all(),
            empty_label=None,
            to_field_name="street"),
        person = forms.ModelChoiceField(
            queryset=models.Person.objects.all(),
            empty_label=None,
            to_field_name="person"
        ),
        home_number = forms.IntegerField(),
        entrance = forms.IntegerField(),
        number = forms.IntegerField(),
        active = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super(FlatForm, self).__init__(*args, **kwargs)
        self.fields['person'].widget.attrs.update(
            {'id': 'person', 'onchange': 'edit_href(this)'}
        )


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person

        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput()
        }


# class Homepage_Form_Unique(forms.Form):
#     entrance = forms.ChoiceField(widget=forms.Select, label='Выбор этажа', choices=())
