from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import TicketForm, TicketUpdateForm, AdminList

def home(request):
    form = AdminList(request.POST or None)
    return render(request, 'tickets/home.html', {'form':form})

@login_required
def user_tickets_view(request):
    all_tickets = Ticket.objects.all()
    return render(request, 'tickets/user_tickets.html', {'all_tickets': all_tickets})

@login_required
def user_my_tickets_view(request):
    all_tickets = Ticket.objects.filter(user_ticket_creator=request.user)
    return render(request, 'tickets/my_tickets.html', {'all_tickets': all_tickets})

@login_required
def assigned_tickets_view(request):
    all_tickets = Ticket.objects.filter(owner=request.user)
    return render(request, 'tickets/assigned_tickets.html', {'all_tickets': all_tickets})


def archive(request):
    return render(request, 'tickets/archive.html')

@login_required
def add_ticket(request):
    submitted = False
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.instance.user_ticket_creator = request.user.username
            print(form.instance.user_ticket_creator)
            form.save()
            return HttpResponseRedirect('/add_ticket?submitted=True')
    else:
        form = TicketForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'tickets/add_ticket.html', {'form':form, 'submitted':submitted})

@login_required
def update_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketUpdateForm(instance=ticket)

    if request.method == 'POST':
        form = TicketUpdateForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('/tickets')

    context = {'form':form}
    return render(request, 'tickets/add_ticket.html', context)

@login_required()
def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('/tickets')
    context= {'item': ticket}
    return render(request, 'tickets/delete.html', context)