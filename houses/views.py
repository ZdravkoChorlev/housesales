from django.shortcuts import render

# Create your views here.
from houses.models import House


def index(request):
    return render(request, 'shared/base.html')


def create_house(request):
    house = House()
    return persist_house(request, house, 'post_house.html')

def persist_house(request, pet, template_name):
    if request.method == 'GET':
        form = HouseForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = pet.image
        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet
        )
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            Like.objects.filter(pet_id=pet.id) \
                .delete()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)

