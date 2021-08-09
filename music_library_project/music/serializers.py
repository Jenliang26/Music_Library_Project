from rest_framework import serializers
from .models import song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = ['id', 'title', 'artist', 'album', 'release_date']