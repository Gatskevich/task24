from django.shortcuts import render, redirect
from .forms import StorageForm
from .models import Storage


def index(request):
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
        return redirect('/output/')
    else:
        form = StorageForm()
    return render(request, 'index.html', {'form': form})


def storage_list(request):
    data = Storage.objects.all().values('id', 'name', 'data')
    return render(request, 'output.html', {'json_list' : list(data)})