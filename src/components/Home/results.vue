<template>
  <v-layout>
    <v-flex xs12 sm6 offset-sm3>
      <v-card>
        <v-img
          class="white--text"
          height="200px"
          src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
        >
          <v-container fill-height fluid>
            <v-layout fill-height>
              <v-flex xs12 align-end flexbox>
                <span class="headline">{{formData.restuarant}}</span>
              </v-flex>
            </v-layout>
          </v-container>
        </v-img>
        <v-card-title>
          <div>
            <span class="grey--text">Number 10</span>
            <br>
            <span>Whitehaven Beach</span>
            <br>
            <span>Whitsunday Island, Whitsunday Islands</span>
          </div>
        </v-card-title>
        <v-card-actions>
          <v-btn flat color="orange">Share</v-btn>
          <v-btn flat color="orange">Explore</v-btn>
        </v-card-actions>
        <v-card-actions class="pa-3">
          <span class="grey--text test text--lighten-2 caption mr-2">{{formData.rating}}</span>
          <v-rating
            v-model="formData.rating"
            color="yellow darken-3"
            background-color="grey darken-1"
            empty-icon="$vuetify.icons.ratingFull"
            half-increments
          ></v-rating>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      formData: {
        image: null,
        restuarant: null,
        rating: 0
      }
    };
  },

  created() {
    this.formData.restuarant = this.$store.getters["foodsearch/getRestaurant"];
    this.formData.rating = this.$store.getters["foodsearch/getRating"];
    console.log(this.formData.rating);
  }
};
</script>

<style>
.test {
  padding: 1em;
}
</style>
