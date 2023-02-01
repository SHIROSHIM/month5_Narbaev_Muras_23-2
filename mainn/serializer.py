from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'all'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'all'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'all'