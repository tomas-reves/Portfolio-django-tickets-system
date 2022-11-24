from django import forms
from .models import Ticket
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('numb', 'title', 'description', 'urgency',)

        labels = {
            'user_ticket_creator': 'Your Username',
            'numb': 'Ticket #',
            'title': 'Title',
            'description': 'Ticket Description',
            'date_created': 'Date Created',
            'status': 'Status',
            'urgency': 'Urgency',
            'status_date': 'Status Date',
            'owner': 'Owner'
        }

        widgets = {
            'user_ticket_creator': forms.Select(attrs={'class':'form-control',  'style': 'width:250px'}),
            'numb': forms.TextInput(attrs={'class':'form-control',  'style': 'width:100px', 'readonly':'readonly'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'style': 'width:500px'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'style': 'width:500px'}),
            'date_created': DateInput(attrs={'class':'form-control', 'style': 'width:200px'}),
            'status': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'}),
            'urgency': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'}),
            'status_date': DateInput(attrs={'class':'form-control', 'style': 'width:200px'}),
            'owner': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'})
        }

        user_ticket_creator = forms.ModelChoiceField(
            queryset=User.objects.all(),
            to_field_name='user_ticket_creator',
            required=True,
            widget=forms.Select(attrs={'class': 'form-control'})
        )

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('numb', 'title', 'description', 'date_created', 'status', 'urgency', 'status_date', 'user_ticket_creator', 'owner')

        labels = {
            'numb': 'Ticket #',
            'title': 'Title',
            'description': 'Ticket Description',
            'date_created': 'Date Created',
            'status': 'Status',
            'urgency': 'Urgency',
            'status_date': 'Status Date',
            'user_ticket_creator':'Created By',
            'owner': 'Owner'
        }

        widgets = {
            'numb': forms.TextInput(attrs={'class':'form-control',  'style': 'width:500px', 'readonly':'readonly'}),
            'title': forms.TextInput(attrs={'class':'form-control', 'style': 'width:500px'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'style': 'width:500px'}),
            'date_created': DateInput(attrs={'class':'form-control', 'style': 'width:200px'}),
            'status': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'}),
            'urgency': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'}),
            'status_date': DateInput(attrs={'class':'form-control', 'style': 'width:200px'}),
            'user_ticket_creator': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'}),
            'owner': forms.Select(attrs={'class':'form-control', 'style': 'width:500px'})
        }

    def __init__(self, *args, **kwargs):
        super(TicketUpdateForm, self).__init__(*args, **kwargs)

        all_users = User.objects.values()
        users_tuple = []
        admin_tuple = []
        for user in all_users:
            users_lists_items = []
            users_lists_items.append(user['username'])
            users_lists_items.append(user['username'])
            users_lists_items = tuple(users_lists_items)
            users_tuple.append(users_lists_items)
            if user['is_staff'] == True:
                admin_items = []
                admin_items.append(user['username'])
                admin_items.append(user['username'])
                admin_items = tuple(admin_items)
                admin_tuple.append(admin_items)
            admin_users_tuple = tuple(users_tuple)
        users_tuple = tuple(users_tuple)
        admin_tuple = tuple(admin_tuple)
        self.fields['user_ticket_creator'].choices = users_tuple
        self.fields['owner'].choices = admin_tuple


class AdminList(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('owner',)
        labels = {'owner': ''}
        widgets = {'owner': forms.Select(attrs={'class':'form-control', 'style': 'width:500px', 'required': 'False'})}
