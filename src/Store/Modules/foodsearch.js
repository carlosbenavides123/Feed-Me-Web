/* eslint-disable */
import Vue from "vue";
import router from '../../router'
const foodsearch = {
    namespaced: true,
    state: {
        googlePlacesAPI: "",
        yelpPlacesAPI: ""
    },
    getters: {},
    mutations: {},
    actions: {
        dispatchSearch({
            commit
        }, payload) {
            const api = `https://us-central1-feed-me-acf1c.cloudfunctions.net/testApi?radius=${payload.radius}&query=${payload.query}&lat=${payload.lat}&long=${payload.long}`
            Vue.axios
                .post(api)
                .then(response => {
                    console.log(response);
                });
        }
    }
}

export default foodsearch