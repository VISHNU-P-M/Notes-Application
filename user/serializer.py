from django.db import models
from rest_framework import serializers
from .models import UserNotes

class UserNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotes
        fields = '__all__'