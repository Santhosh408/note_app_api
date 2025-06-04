from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from .serializers import UserSerializer,NoteSerializer
from rest_framework.response import Response
from .models import Notes
from django.http import Http404
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

class RegisterApiView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User created successfully'},status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
class UserProfileApiView(APIView):
    def get(self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def put(self,request):
        serializer = UserSerializer(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def patch(self,request):
        serializer = UserSerializer(request.user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class NotesApiView(APIView):
    def get(self,request):
        user = request.user
        notes = Notes.objects.filter(user=user)
        serializer = NoteSerializer(notes,many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def post(self,request):
        data = request.data
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
class SingleNoteApiView(APIView):
    def get_object(self,pk):
        try:
            return Notes.objects.get(pk=pk,user=self.request.user)
        except Notes.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def put(self,request,pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        note = self.get_object(pk)
        serializer = NoteSerializer(note,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        note = self.get_object(pk)
        note.delete()
        return Response({"message":"note_deleted"},status=HTTP_200_OK)

