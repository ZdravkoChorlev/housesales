from django.shortcuts import render

# Create your views here.
from houses.forms.house_form import HouseForm
from houses.models import House


def index(request):
    return render(request, 'shared/base.html')


def create_house(request):
    house = House()
    return persist_house(request, house, 'post_house')


def persist_house(request, pet, template_name):
    form = HouseForm(instance=pet)

    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, f'{template_name}.html', context)


def list_houses(request):
    context = {
        'Houses': House.objects.all(),
    }
    return render(request, 'list_houses.html', context)
