from django.shortcuts import render, redirect
from .forms import StorageForm
from .models import Storage


def index(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            name_stat = form.cleaned_data['name']
            list_obj = dict()
            for count in range(1, len(request.POST) - 1):
                start_value = 'name' + str(count)
                value = request.POST[start_value]
                if value:
                    list_obj[start_value] = value
                count += 1
        Storage.objects.create(data=list_obj, name=name_stat)
        return redirect('/output/')
    else:
        form = StorageForm()
    return render(request, 'index.html', {'form': form})


def storage_list(request):
    data = Storage.objects.all().values('id', 'name', 'data')
    return render(request, 'output.html', {'json_list' : list(data)})