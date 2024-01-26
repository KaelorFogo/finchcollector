from django.shortcuts import render

finches = [
    {'name': 'Tweetie', 'species': 'zebra finch', 'color': 'orange and white', 'age': 1},
    {'name': 'Sunny', 'species': 'gouldian finch', 'color': 'rainbow', 'age': 2},
    {'name': 'Pip', 'species': 'budgerigar', 'color': 'green and yellow', 'age': 1},
    {'name': 'Feather', 'species': 'society finch', 'color': 'gray and white', 'age': 3},
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, "finches/index.html",{
  'finches': finches
  })
