from rest_framework import serializers

from .models import Employee, AirlineCompany, Crew, Airplane, Flight


class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Employee
        fields = ['username', 'password', 'first_name', 'last_name', 'age', 'passport_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Employee(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            age=self.validated_data['age'],
            passport_number=self.validated_data['passport_number'],

        )
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']

        # if password != password2:
        #     raise serializers.ValidationError({'password': 'Пароли должны совпадать'})
        account.set_password(password)
        account.save()
        return account


class CrewSerializer(serializers.ModelSerializer):
    head_pilot = serializers.CharField(source="head_pilot.get_username", read_only=True)
    second_pilot = serializers.CharField(source="second_pilot.get_username", read_only=True)
    stewardess1 = serializers.CharField(source="stewardess1.get_username", read_only=True)
    stewardess2 = serializers.CharField(source="stewardess2.get_username", read_only=True)
    steward = serializers.CharField(source="steward.get_username", read_only=True)
    airline_company = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Crew
        fields = '__all__'


class AirPlaneGeneralSerializer(serializers.ModelSerializer):
    airline_company = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Airplane
        fields = ('type', 'airline_company')


class FlightListSerializer(serializers.ModelSerializer):
    """Список рейсов"""
    airplane = AirPlaneGeneralSerializer(read_only=True)
    number_of_seats_available = serializers.IntegerField()
    duration = serializers.StringRelatedField()

    class Meta:
        model = Flight
        fields = ('id', 'flight_number', 'distance', 'departure_point', 'destination', \
                  'departure_time', 'destination_time', 'number_of_seats', 'transit_landings', \
                  'number_of_tickets_sold', 'airplane', 'duration', 'number_of_seats_available')

    # def get_duration(self, obj):
    #     duration = obj.destination_time - obj.departure_time
    #     seconds = duration.total_seconds()
    #     hours = seconds // 3600
    #     minutes = (seconds % 3600) // 60
    #     seconds = seconds % 60
    #     return f'{int(hours)} час {int(minutes)} минут'

    '''def get_neat_date(self, obj):
        departure_time = datetime.datetime.strptime(str(obj.departure_time), "%Y-%m-%d %H:%M:%S±%H:%M") #2020-05-21T12:00:00Z
        new_format = "%Y-%m-%d"
        return departure_time.strftime(new_format)'''


class AirlineCompanySerializer(serializers.ModelSerializer):
    airline_company = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = AirlineCompany
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    # flight = serializers.SlugRelatedField(slug_field="flight_number", queryset=Employee.objects.all(), many=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name',)


class FlightDetailSerializer(serializers.ModelSerializer):
    """Полная информация о рейсе"""
    airplane = AirPlaneGeneralSerializer(read_only=True)
    served_flight = CrewSerializer(many=True)
    passengers = PassengerSerializer(many=True)

    class Meta:
        model = Flight
        fields = '__all__'


class FlightInfoSerializer(serializers.ModelSerializer):
    """Полная информация о рейсе"""
    airplane = AirPlaneGeneralSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = (
        'id', 'flight_number', 'departure_point', 'destination', 'departure_time', 'destination_time', 'airplane')


class EmployeeSerializer(serializers.ModelSerializer):
    """Информация о пользователе"""

    # flight = serializers.SlugRelatedField(slug_field="flight_number", queryset=Employee.objects.all(), many=True)
    #flight = FlightInfoSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'
