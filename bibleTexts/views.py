from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TextSerializer
from .models import TextsDevotional
from datetime import date 
# criar texto
@api_view(['POST'])
def create_text(request):
    serializer = TextSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# pegar texto
@api_view(['GET'])
def take_text(request): 
    texts = TextsDevotional.objects.count()

    if texts == 0:
        return Response({"Nenhum texto."})
    
    indice_text = date.today().toordinal() % texts

    text_to_return = TextsDevotional.objects.all()[indice_text]

    response = {
        'title': text_to_return.title,
        'content': text_to_return.content,
        'version': text_to_return.version,
        'concluded': text_to_return.concluded
    }

    return Response(response)