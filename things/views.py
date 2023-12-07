from django.shortcuts import render
from things.forms import ThingForm

def home(request):
     form = ThingForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('home')
    return render(request, 'home.html', {'form': form})
