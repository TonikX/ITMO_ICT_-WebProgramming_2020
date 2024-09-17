<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">SkySurface</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse"
                    data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                        <router-link :to="{ name: 'Home'}" class="nav-link">Главная<span class="sr-only">(current)</span></router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Фильтры
                        </a>
                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#" @click="getFlightsWithAvailableSeats()">Рейсы только со
                                свободными местами</a>
                            <a class="dropdown-item" href="#" @click="getFlightsWithoutTransfer()">Рейсы без
                                пересадок</a>
                            <div class="dropdown-divider"></div>

                            <p class="ml-4">Авиакомпании:</p>
                            <div id="checkboxes" class="ml-4" v-for="airline_company in airline_companies">
                                <input class="ml-2 mr-2" type="checkbox" :value="airline_company.name"
                                       v-model="airlineCategories" @change="getFlightsAccordingToCompany()"/>
                                <label>{{ airline_company.name }}</label><br>
                            </div>
                        </div>
                    </li>
<!--                    <li class="nav-item active">-->
<!--                        <router-link :to="{ name: 'Home'}" class="nav-link">Справка о самолетах<span class="sr-only">(current)</span></router-link>-->
<!--                    </li>-->
                </ul>
                <span class="button mr-5" v-if="!auth">
                    <button class="btn btn-primary" @click="goLogin()">Войти</button>
                    <button class="btn btn-light ml-2" @click="goToRegistration()">Зарегистрироваться</button>
                </span>

                <span class="button mr-5" v-else>
                    <a href="#" style="color: black; font-size: 15px" @click="goToProfile()">
                        <img class="mr-1" src="../assets/account.png" alt="Личный кабинет"
                             width="35" height="35"
                        > Личный кабинет
                    </a>
                    <button class="btn btn-danger ml-3" @click="logout()">Выход</button>
                </span>
                <!--                <form class="form-inline my-2 my-lg-0">-->
                <!--                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">-->
                <!--                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>-->
                <!--                </form>-->
            </div>
        </nav>
    </div>
</template>

<script>

    export default {
        name: "NavBar",
        data() {
            return {
                airlineCategories: ['Utair', 'S7'],
            }
        },
        computed: {
            auth() {
                const profile = this.$store.state.profile;
                return profile && profile.first_name;
            },
            airline_companies() {
                return this.$store.state.airline_companies;
            },
        },
        created() {
            this.loadAirlineCompanies()
        },
        methods: {
            // getAvailableFlight() {
            //     this.$store.dispatch('asyncChangeAvailableStatus')
            // },
            getFlightsWithAvailableSeats() {
                this.$store.dispatch('getFlights', {
                    withAvailableSeats: 1,
                });
            },
            getFlightsWithoutTransfer() {
                this.$store.dispatch('getFlights', {
                    withoutTransfer: false,
                });
            },
            getFlightsAccordingToCompany() {
                this.$store.dispatch('getFlights', {
                    airlineCompanies: this.airlineCategories.length != 0 ? this.airlineCategories : null,
                });
            },
            goLogin() {
                this.$router.push({name: 'Login'})
            },
            goToProfile() {
                this.$router.push({name: "Profile"})
            },
            goToRegistration() {
                this.$router.push({name: 'Registration'})
            },
            logout() {
                localStorage.removeItem("token")
                this.$store.commit('setProfile', {});
                this.$router.push({name: 'Home'})
            },
            loadAirlineCompanies() {
                this.$store.dispatch('getAirlineCompanies');
            },
        }
    }
</script>

<style scoped>
    /*#checkboxes input{*/
    /*    display: inline-block;*/
    /*    margin-right: 10px;*/
    /*}*/
    /*#checkboxes label{*/
    /*    display: inline-block;*/
    /*}*/
</style>