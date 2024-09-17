<template>
    <div class="container">
        <h2 class="mt-4">Профиль пользователя</h2>
        <div>
            <ul class="mt-4">
                <li>Имя: <b>{{ profile.first_name }} {{ profile.last_name }}</b></li>
                <li>Возраст: <b>{{ profile.age }}</b></li>
                <li v-if="profile.status!='Пользователь сайта'">Образование: <b>{{ profile.education }}</b></li>
                <li>Паспортные данные: <b>{{ profile.passport_number }}</b></li>
                <li v-if="profile.status!='Пользователь сайта'">Должность: <b>{{ profile.position }}</b></li>
                <li>Текущий статус: <b>{{ profile.status }}</b></li>
            </ul>
            <p class="mt-4 ml-3">
                <button class="btn btn-light mr-4" type="button"
                        @click="(isFlight = !isFlight) && (isVisible = false)">
                    Мои рейсы
                </button>
                <button class="btn btn-info" v-if="profile.status === 'Пользователь сайта'" type="button"
                        @click="(isVisible = !isVisible) && (isFlight = false)">
                    Хочу работать у вас!
                </button>
            </p>
        </div>

        <hr v-show="isVisible">
        <JobApplication v-show="isVisible"/>
        <div v-if="profile.is_superuser">
            <hr>
            <h3 class="mt-4">Список поданных заявок:</h3>
            <ApplicationList/>
        </div>

        <hr v-show="isFlight">
        <div v-show="isFlight" v-for="flight in flights" v-if="profile.flight[0] === flight.id">
            <div class="card w-75">
                <div class="card-body">
                    <h6 class="card-title">Рейс № {{flight.flight_number}} авиакомпании
                        {{flight.airplane.airline_company}}</h6>
                    <p class="card-text">
                        <b>{{flight.departure_point}}</b> --> <b>{{flight.destination}}</b>
                    </p>
                    <div>
                        <small>
                            <b><i>Дата и время вылета:</i></b> {{flight.departure_time}}.
                            <b><i>Дата и время прибытия:</i></b> {{flight.destination_time}}.
                        </small>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import JobApplication from "../components/JobApplication"
    import ApplicationList from "../components/ApplicationList"

    export default {
        name: "Profile",
        components: {JobApplication, ApplicationList},
        data() {
            return {
                isVisible: false,
                isFlight: false
            }
        },
        computed: {
            profile() {
                return this.$store.state.profile;
            },
            flights() {
                return this.$store.state.flights;
            },
        },
        created() {
            const token = localStorage.getItem('token');
            const id = localStorage.getItem('id');
            if (!!token && !(this.profile && this.profile.first_name)) {
                this.$store.dispatch('loadProfile', {token, id});
            }
            this.loadFlights()
        },
        methods: {
            loadFlights() {
                this.$store.dispatch('getFlights');
            }
        }
    }
</script>

<style scoped>

</style>