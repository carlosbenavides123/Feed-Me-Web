/* eslint-disable */
import Vue from "vue";
import router from '../../router'

const foodsearch = {
    namespaced: true,
    state: {
        query: "",
        radius: ""
    },
    getters: {},
    mutations: {},
    actions: {
        dispatchSearch({
            commit
        }, payload) {

        }
    }
}

export default foodsearch