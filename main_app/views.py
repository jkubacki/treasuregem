from django.shortcuts import render

# Create your views here.
def index(request):
  name = 'Gold Nugget'
  value = 1000.00
  context = { 'treasures': treasures }
  return render(request, 'index.html', context)


class Treasure:
  def __init__(self, name, value, material, location):
    self.name = name
    self.value = value
    self.material = material
    self.location = location

treasures = [
  Treasure('Gold Nugget', 5000, 'gold', 'somewhere'),
  Treasure('Silver Nugget', 2000, 'silver', 'poznan')
]
