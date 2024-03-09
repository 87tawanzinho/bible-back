from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from .serializer import TextSerializer
from .models import TextsDevotional
from bibleAuth.models import Profile
from datetime import date 
from django.apps import apps
from django.shortcuts import get_object_or_404
modelProfile = apps.get_model('bibleAuth', 'Profile')
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

    concluded_by_users = text_to_return.concluded_by.all()

    concluded_by_usernames = [user.username for user in concluded_by_users]


    response = {
        'id': text_to_return.id, 
        'title': text_to_return.title,
        'content': text_to_return.content,
        'version': text_to_return.version,
        'summary': text_to_return.summary,
        'chapter': text_to_return.chapter,
        'concluded_by': concluded_by_usernames
    }

    return Response(response)


# concluir devocional 
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def conclude_devotional(request, devotionalPk):
    user = request.user
    try:
        devotional = TextsDevotional.objects.get(pk=devotionalPk)
    except TextsDevotional.DoesNotExist:
        return Response ("Devocional não existe.")  

    devotional.concluded_by.add(user) 
    devotional.save()

    profile = get_object_or_404(Profile, user=user)
    profile.myPrays += 1 
    profile.save()

    return Response({"prays": profile.myPrays, "concluido": "Parabéns"}, status=201)