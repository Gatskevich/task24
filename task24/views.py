from django.shortcuts import render, redirect
from .forms import StorageForm
from .models import Storage


def index(request):
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            for count in range(0, len(request.POST) - 1):
                start_value = 'name' + str(count)
                value = request.POST[start_value]
                if value:
                    name = start_value
                    data = value
                    Storage.objects.create(data=data, name=name)
                count += 1
        return redirect('/output/')
    else:
        form = StorageForm()
    return render(request, 'index.html', {'form': form})


def done(request):
    data = Storage.objects.all().values('id', 'name', 'data')
    return render(request, 'output.html', {'json_list' : list(data)})