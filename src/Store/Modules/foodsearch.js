/* eslint-disable */
import Vue from "vue";
import router from '../../router'
const foodsearch = {
    namespaced: true,
    state: {
        restaurantName: "",
        lat: "",
        long: "",
        ratings: "",
        yelpPlacesAPI: ""
    },
    getters: {
        getRestaurant(state) {
            return state.restaurantName
        },
        getLat(state) {
            return state.lat
        },
        getLong(state) {
            return state.long;
        },
        getRating(state) {
            return state.ratings;
        }
    },
    mutations: {
        googleApiExtract(state, elgoog) {
            console.log(elgoog)
            state.restaurantName = elgoog.data.name;
            state.ratings = elgoog.data.ratings;
            state.lat = elgoog.data.geometry.location.lat;
            state.long = elgoog.data.geometry.location.lng;
        }
    },
    actions: {
        dispatchSearch({
            commit
        }, payload) {
            if (payload.query === '') payload.query = "random"
            if (payload.radius === '') payload.radius = "random"

            const api = `https://us-central1-feed-me-acf1c.cloudfunctions.net/testApi?radius=''&query=''&lat=${payload.lat}&long=${payload.long}`
            Vue.axios
                .post(api)
                .then(response => {
                    console.log(response)
                    commit("googleApiExtract", response)
                });
        }
    }
}

export default foodsearch