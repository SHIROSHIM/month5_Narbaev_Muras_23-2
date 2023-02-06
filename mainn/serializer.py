from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = '__all__'

    def get_movies_count(self, obj):
        return obj.movie_set.count()

class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    reviews = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = '__all__'
