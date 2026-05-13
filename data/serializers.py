import requests
from rest_framework import serializers
from .models import Project, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'external_id', 'notes', 'is_visited']

    def validate_external_id(self, value):
        response = requests.get(f"https://api.artic.edu/api/v1/artworks/{value}")
        if response.status_code != 200:
            raise serializers.ValidationError("Place does not exist in Art Institute of Chicago API.")
        return value


class ProjectSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, required=False)
    is_completed = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'places', 'is_completed']

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])

        if len(places_data) > 10:
            raise serializers.ValidationError("A project cannot have more than 10 places.")

        project = Project.objects.create(**validated_data)
        for place_data in places_data:
            Place.objects.create(project=project, **place_data)
        return project