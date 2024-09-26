from rest_framework import serializers
from kursovik.models import *


class ClientSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields= '__all__'

class WorkerSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Worker
        fields= '__all__'

class RoomSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields= '__all__'

class WorktableSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Worktable
        fields= '__all__'

class JournalSerialiser(serializers.ModelSerializer):
    class Meta:
        model=Journal
        fields= '__all__'