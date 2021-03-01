from django.shortcuts import render, redirect
from .forms import StorageForm
from .models import Storage


def storage_create(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            data = dict()

            for count in range(1, len(request.POST) - 1):
                key = 'name' + str(count)
                value = request.POST[key]
                if value:
                    data[key] = value
        Storage.objects.create(data=data, name=name)
        return redirect('/storage_list/')
    else:
        form = StorageForm()
    return render(request, 'storage_create.html', {'form': form})


def storage_list(request):
    data = Storage.objects.all().values('name', 'data')
    return render(request, 'storage_list.html', {'storeges' : list(data)})