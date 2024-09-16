from rest_framework import serializers
from newspapersapp.models import *


class PostOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOffice
        fields = '__all__'


class PrintingHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintingHouse
        fields = '__all__'


class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newspaper
        fields = '__all__'


class InStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = InStock
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintingHouse
        fields = '__all__'


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = '__all__'
