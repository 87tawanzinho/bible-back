from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response 

from .serializers import UserSerializer,ProfileSerializer, UserWithoutChapter
from rest_framework import status 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import  User 
from django.shortcuts import get_object_or_404
from .models import Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes 
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']): 
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    profile_serializer = ProfileSerializer(instance=user.profile)
    return Response({"token": token.key, "user": profile_serializer.data })
    
       
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(): 
        serializer.save() 
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user) 
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response("Sucess{}".format(request.user.email))



#rota para pegar os dados do usuario
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def take_user_data(request):
    profile = get_object_or_404(Profile, user=request.user)
    serializer = UserWithoutChapter(profile)
    return Response(serializer.data)



#rota para mudar o aviso de devotional 
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_warn(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile.devotionalWarn = not profile.devotionalWarn 
    profile.save()
    return Response(f"Mudado com sucesso. {profile.devotionalWarn}")

#rota para pegar as tarefas
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def take_cards(request): 
    profile = get_object_or_404(Profile, user=request.user)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)



#rota para terminar uma tarefa 
@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def completed_this_card(request, chapter, card_id):
    profile = get_object_or_404(Profile, user=request.user)
    card_index = next((index for index, card in enumerate(profile.allChapters[chapter]) if card['id'] == int(card_id)), None)
    
    if card_index is not None: 
        profile.allChapters[chapter][card_index]['completed'] = not profile.allChapters[chapter][card_index]['completed']
        profile.myBibles += 1 
        profile.save()
        return Response({"profile": profile.allChapters[chapter], "bibles": profile.myBibles}, status=201)

    else:
        return Response("not found")





