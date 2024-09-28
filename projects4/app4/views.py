from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
import requests
from .models import Item
from .serializers import ItemSerializer
from .forms import ItemForm

@api_view(['GET'])
def api_get_items(request):
    """
    API endpoint that returns a list of items in JSON format.
    """
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

def item_create_view(request):
    """
    View to render and process the item creation form.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    
    return render(request, 'item_form.html', {'form': form})

def item_list_view(request):
    """
    View to display items fetched from the API in an HTML template.
    """
    response = requests.get('http://localhost:8000/api/items/')
    items = response.json()
    return render(request, 'item_list.html', {'items': items})
