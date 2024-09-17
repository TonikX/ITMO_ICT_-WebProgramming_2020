import Vue from 'vue'
import Vuex from 'vuex'
import $ from 'jquery'

Vue.use(Vuex)

const mapFilterToQueryParam = (filter) => {
    switch (filter) {
        case 'withAvailableSeats':
            return 'number_of_seats_available_min';
        case 'withoutTransfer':
            return 'transit_landings';
        case 'airlineCompanies':
            return 'airline_companies';
    }
};

const store = new Vuex.Store({
    state: {
        backendUrl: "http://127.0.0.1:8000/api/v1",
        filters: {},
        flights: [],
        airline_companies: [],
        profile: {},
    },
    mutations: {
        setFilters(state, filters) {
            state.filters = {
                ...state.filters,
                ...filters,
            };
        },
        setFlights(state, flights) {
            state.flights = flights;
        },
        setAirlineCompanies(state, airline_companies) {
            state.airline_companies = airline_companies;
        },
        setProfile(state, profile) {
            state.profile = profile;
        }
    },
    actions: {
        async getAirlineCompanies({commit, state}) {
            const airline_companies = await fetch(`${state.backendUrl}/flight/airline_company`);
            commit('setAirlineCompanies', await airline_companies.json());
        },
        async getFlights({commit, state}, filters) {
            commit('setFilters', filters);

            const formData = new FormData();
            Object
                .keys(filters || {})
                .forEach(filter => formData.append(mapFilterToQueryParam(filter), filters[filter]));

            const queryString = new URLSearchParams(formData).toString();

            const flights = await fetch(`${state.backendUrl}/flight/?${queryString}`);
            commit('setFlights', await flights.json());
        },
        loadProfile({commit, state}, {token, id}) {
            return new Promise((resolve, reject) => {
                $.ajax({
                    url: `${state.backendUrl}/flight/profile/${id}/`,
                    type: "GET",
                    headers: {'Authorization': "Token " + token},
                    success: (response) => {
                        commit('setProfile', response);
                        resolve();
                    },
                    error: (error) => {
                        reject(error);
                    }
                })
            });
        },
    },
    modules: {},
    getters: {
        getServerUrl: state => {
            return state.backendUrl
        }
    }
})

export default store
