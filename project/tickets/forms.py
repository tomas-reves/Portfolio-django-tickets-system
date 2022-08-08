from django import forms
from django.forms import ModelForm
from .models import Ticket

class DateInput(forms.DateInput):
    input_type = 'date'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('numb', 'title', 'description', 'urgency', 'user_ticket_creator')

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

class TicketUpdateForm(ModelForm):
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

class AdminList(ModelForm):
    class Meta:
        model = Ticket
        fields = ('owner',)
        labels = {'owner': ''}
        widgets = {'owner': forms.Select(attrs={'class':'form-control', 'style': 'width:500px', 'required': 'False'})}
