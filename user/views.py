
# rest_framework modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# importing model
from .models import UserNotes

# importing serializer
from .serializer import UserNoteSerializer


# class for read all notes
class Note(APIView):
    permission_classes = [IsAuthenticated]                                                   # authenticating
    
    def get(self, request):                                                                  # function for reading all notes   
        notes = UserNotes.objects.all()
        note_serializer = UserNoteSerializer(notes, many=True)
        return Response(note_serializer.data)
    
    def post(self, request):                                                                 # function for creating new note
        note_serializer = UserNoteSerializer(data=request.data)
        if note_serializer.is_valid():
            note_serializer.save()
            return Response(note_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
# class for reading details of note
class DetailNote(APIView):                                                                   
    permission_classes = [IsAuthenticated]
    
    def get(self, request,id):                                                              # function for reading the details of specific id
        if UserNotes.objects.filter(id=id).exists():                                        # checking for existence
            note = UserNotes.objects.get(id=id)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer_note = UserNoteSerializer(note)
        return Response(serializer_note.data)
    
    def put(self, request, id):                                                             # function for updating details of note
        note = UserNotes.objects.get(id=id)
        details_serialize = UserNoteSerializer(note,data=request.data)
        if details_serialize.is_valid():
            details_serialize.save()
            return Response(details_serialize.data, status=status.HTTP_200_OK)
        else:
            return Response(details_serialize.errors, status=status.HTTP_400_BAD_REQUEST)