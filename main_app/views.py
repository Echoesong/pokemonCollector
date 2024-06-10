from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pokemon

# Views are equivalent to controllers in express?
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemons = Pokemon.objects.all() 
    return render(request, 'pokemon/index.html', { 'pokemons': pokemons})

def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemon/detail.html', {'pokemon': pokemon})

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

