/* eslint-disable */
import Vue from "vue";
import router from '../../router'
const foodsearch = {
    namespaced: true,
    state: {
        restaurantName: "",
        rating: 0,
        lat: "",
        long: "",
        showResult: false
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
            return state.rating;
        },
        getShowResult(state) {
            return state.showResult;
        }
    },
    mutations: {
        googleApiExtract(state, elgoog) {
            console.log(elgoog);
            state.restaurantName = elgoog.data.name;
            state.rating = elgoog.data.rating;
            state.lat = elgoog.data.geometry.location.lat;
            state.long = elgoog.data.geometry.location.lng;
            state.showResult = true;
        }
    },
    actions: {
        dispatchSearch({
            commit
        }, payload) {
            var q;
            if (!payload.radius) {
                payload.radius = "\'\'"
            }
            if (!payload.query) {
                q = "\'\'"
            } else {
                q = payload.query
            }
            if (!payload.price_range) {
                payload.price_range = "\'\'"
            }
            const api = `https://us-central1-feed-me-acf1c.cloudfunctions.net/testApi?radius=${payload.radius}&query=${q}&lat=${payload.lat}&long=${payload.long}`;
            console.log(api);
            Vue.axios
                .post(api)
                .then(response => {
                    commit("googleApiExtract", response)
                })
                .catch(err => {
                    console.log(err)
                });
        }
    }
}

export default foodsearch