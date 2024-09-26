from rest_framework import serializers
from django.contrib.auth.models import User
from hotel.models import Client, Room, Worker, Checkin, Floor, Cleaning


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'fio')


class ClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class AddClientSer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('full_name', 'passport', 'city')


class RoomSer(serializers.ModelSerializer):
    floor = serializers.SlugRelatedField(slug_field='floor_num', read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class WorkerSer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class AddWorkerSer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('full_name',)


class CheckinSer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    room = serializers.SlugRelatedField(slug_field='room_number', read_only=True)

    class Meta:
        model = Checkin
        fields = ('client', 'room', 'date_in', 'date_out')


class AddCheckinSer(serializers.ModelSerializer):

    class Meta:
        model = Checkin
        fields = ('client', 'room', 'date_in', 'date_out')


class FloorSer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class CleaningSer(serializers.ModelSerializer):
    floor = serializers.SlugRelatedField(slug_field='floor_num', read_only=True)

    class Meta:
        model = Cleaning
        fields = ('day_of_week', 'floor')


class CleaningAddSer(serializers.ModelSerializer):

    class Meta:
        model = Cleaning
        fields = ('worker', 'day_of_week', 'floor')


class CleaningListSer(serializers.ModelSerializer):
    worker = serializers.SlugRelatedField(slug_field='full_name', read_only=True)
    floor = serializers.SlugRelatedField(slug_field='floor_num', read_only=True)

    class Meta:
        model = Cleaning
        fields = ('day_of_week', 'worker', 'floor')


class FloorList(serializers.ModelSerializer):
    rooms = RoomSer(many=True)

    class Meta:
        model = Floor
        fields = ('floor_num', 'rooms')


class RoomDetailSer(serializers.ModelSerializer):
    floor = serializers.SlugRelatedField(slug_field='floor_num', read_only=True)
    checkins = CheckinSer(many=True)

    class Meta:
        model = Room
        fields = ('room_number', 'floor', 'phone', 'type', 'price', 'checkins')


class ClientDetailSer(serializers.ModelSerializer):
    checkins = CheckinSer(many=True)

    class Meta:
        model = Client
        fields = ('full_name', 'passport', 'city', 'checkins')
