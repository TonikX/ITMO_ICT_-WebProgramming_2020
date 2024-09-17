<template>
    <div class="container mt-4">
        <h2>Информация о рейсе № {{flight.flight_number}}</h2>
        <ul class="mt-4">
            <li>Пункт вылета: <b>{{ flight.departure_point }}</b></li>
            <li>Пункт назначения: <b>{{ flight.destination }}</b></li>
            <li>Дистанция: <b>{{ flight.distance }} км</b></li>
            <li v-if="flight.airplane">Авиакомпания: <b>{{ flight.airplane.airline_company }}</b></li>
            <li>Дата и время вылета: <b>{{ flight.departure_time }}</b></li>
            <li>Дата и время прибытия: <b>{{ flight.destination_time }}</b></li>
            <li>Общее количество мест: <b>{{flight.number_of_seats}}</b></li>
            <li>Количество проданных билетов: <b>{{flight.number_of_tickets_sold}}</b></li>
            <hr>
            <li v-if="flight.transit_landings">Прямой: <b>нет</b></li>
            <li v-if="flight.transit_landings">Время транзитных посадок: <b>{{ flight.transit_departure_time }}</b></li>
            <li v-if="flight.transit_landings">Время транзитных вылетов: <b>{{ flight.transit_destination_time }}</b>
            </li>

            <li v-if="flight.transit_landings === false">Прямой: <b>да</b></li>
            <hr>
            <li v-if="flight.airplane">Самолет: <b>{{flight.airplane.type}}</b></li>
            <li>Экипаж:</li>
            <p v-for="person in flight.served_flight" :key="person.id">
                Главный пилот: <b><i>{{person.head_pilot}}</i></b> <br>
                Второй пилот: <b><i>{{person.second_pilot}}</i></b> <br>
                Стюардессы: <b><i>{{person.stewardess1}}, {{person.stewardess2}}</i></b> <br>
                Стюард: <b><i>{{person.steward}}</i></b>
            </p>
        </ul>

        <div class="mt-5">
            <button class="btn btn-secondary ml-4" @click="goBackToFlights">Назад</button>
            <button class="btn btn-primary ml-4"
                    id="hintarea"
                    @click.once="checkIn()"
                    :class="buttonType"
            >
                Записаться на рейс
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Single",
        props: ['id'],
        data() {
            return {
                flight: {},
                indicator: false
            }
        },
        created() {
            // const user_id = localStorage.getItem('id');
            this.loadFlight()
        },
        computed: {
            auth() {
                const profile = this.$store.state.profile;
                return profile && profile.first_name;
            },
            buttonType() {
                return {
                    'disabled': !this.auth || (this.flight.number_of_seats - this.flight.number_of_tickets_sold <= 0) || (this.indicator)
                }
            },
            profile() {
                return this.$store.state.profile;
            }
        },
        methods: {
            async loadFlight() {
                this.flight = await fetch(
                    `${this.$store.getters.getServerUrl}/flight/${this.id}/`
                ).then(response => response.json())
                // console.log(this.flight)
                // console.log(this.id)
            },
            goBackToFlights() {
                this.$router.push('/')
            },
            async checkIn() {
                let data1 = {
                    flight: [this.id]
                }
                let data2 = {
                    number_of_tickets_sold: this.flight.number_of_tickets_sold + 1
                }
                const token = localStorage.getItem('token');
                await fetch(`${this.$store.getters.getServerUrl}/flight/profile/${this.profile.id}/`,
                    {
                        method: "PUT",
                        headers: {
                            'Authorization': 'Token ' + token,
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data1)
                    }
                )
                await fetch(`${this.$store.getters.getServerUrl}/flight/${this.id}/`,
                    {
                        method: "PUT",
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(data2)
                    }
                ).then(response => {
                    this.indicator = true
                    console.log(this.indicator);
                    alert('Вы успешно зарегистрированы на рейс!')
                }).catch(error => error)
            },
        }
    }
</script>

<style scoped>
    /*.btn:hover:disabled {*/
    /*    color: red;*/
    /*}*/
</style>