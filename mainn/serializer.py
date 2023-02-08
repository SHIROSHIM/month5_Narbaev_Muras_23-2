from rest_framework import serializers
from .models import Director, Movie, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_name(self, value):
        if value == "":
            raise serializers.ValidationError("Name cannot be empty.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_title(self, value):
        if value == "":
            raise serializers.ValidationError("Title cannot be empty.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('id',)

    def validate_content(self, value):
        if value == "":
            raise serializers.ValidationError("Content cannot be empty.")
        return value
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Stars must be between 1 and 5.")
        return value
