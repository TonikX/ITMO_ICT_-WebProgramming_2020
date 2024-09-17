<template>
    <div class="main-part">
        <div class="container mb-4 mt-4">
            <h2>Список рейсов</h2>
        </div>
        <div class="container">
            <div class="card mb-3" v-for="flight in flights" :key="flight.id">
                <h5 class="card-header">Рейс № {{flight.flight_number}} авиакомпании {{flight.airplane.airline_company}}</h5>
                <div class="card-body">
                    <h5 class="card-title">
                        {{flight.departure_point}} --> {{flight.destination}}
<!--                        <small><i>(расстояние: {{flight.distance}} км)</i></small>-->
                    </h5>
                    <p><b>Дата и время вылета:</b> {{flight.departure_time}}. <b>Дата и время прибытия:</b> {{flight.destination_time}}.
                        <b>Длительность полета:</b> {{flight.duration}} </p>
                    <p><b>Количество проданных билетов/общее количество мест:</b> {{flight.number_of_tickets_sold}}/{{flight.number_of_seats}}.</p>
                    <router-link :to="{ name: 'Single', params: {id: flight.id} }" class="btn btn-primary">Подробнее</router-link>
<!--                    <a href="#" @click="getAvailableFlight()" class="btn btn-primary">С билетами</a>-->
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .main-part {
        background: url(../assets/sky.jpg) no-repeat center;
        width: 1920px;
        height: 1080px;
        display: block;
        max-width: 100%;
        max-height: inherit;
        position: absolute;
    }
</style>

<script>

    export default {
        name: 'Home',
        data() {
            return {}
        },
        components: {},
        computed: {
            flights() {
                return this.$store.state.flights;
            },
        },
        created() {
            this.loadFlights()
        },
        methods: {
            loadFlights() {
                this.$store.dispatch('getFlights');
            }
        }
    }
</script>

