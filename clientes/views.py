from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClientForm

@login_required
def client_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente.html', {'clientes' : clientes, 'action': 'client_new'})

@login_required
def client_new(request):
    form = ClientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'form.html', {'form': form})

@login_required
def client_update(request, id):
    client = get_object_or_404(Cliente, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('client_list')

    return render(request, 'form.html', {'form': form, 'action': 'client_update'})

@login_required
def client_delete(request, id):
    client = get_object_or_404(Cliente, pk=id)

    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    
    return render(request, 'delete.html',{'client': client.first_name})