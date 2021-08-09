from django.db.models.query import InstanceCheckMeta
from rest_framework import serializers
from .models import song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields = ['id', 'title', 'artist', 'album', 'release_date']
    
    def create(self, validated_data):
    return song.objects.create(**validated_data)

    def udpate(self, instance, validated_data):
        instance.title = validated_data.get('title, instance.title')
        instance.artist = validated_data.get('artist, instance.artist')
        instance.album = validated_data.get('album, instance.album')
        instance.release_date = validated_data('release_date, instance.release_date')
        instance.save()
        return Instance
        