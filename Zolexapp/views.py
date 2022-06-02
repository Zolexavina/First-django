from django.shortcuts import render

# Create your views here.
def index(request):
"""The home page for Zolexapp.""”

return render(request, 'zicodxapp/index.html’)