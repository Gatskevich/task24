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
                key = f'name{count}'
                value = request.POST.get(key)
                if value:
                    data[key] = value
        Storage.objects.create(data=data, name=name)
        return redirect('/storage_list/')
    else:
        form = StorageForm()
    return render(request, 'storage_create.html', {'form': form})


def storage_list(request):
    lines = list(Storage.objects.all().values('name', 'data'))
    storages = []
    for line in lines:
        storage = {'name': line['name']}
        for key in line['data']:
            storage[key] = line['data'][key]
        storages.append(storage)

    return render(request, 'storage_list.html', {'storages': storages})
