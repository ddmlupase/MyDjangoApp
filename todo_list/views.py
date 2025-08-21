from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm()

    all_items = List.objects.all().order_by('-id')
    context = {'all_items': all_items, 'form': form}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'myname': 'Daniel David'})

def delete(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.delete()
    return redirect('home')

def strike(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def unstrike(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')
