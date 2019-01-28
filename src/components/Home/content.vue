<template>
  <v-layout>
    <v-card>
      <form @submit.prevent="submitHandler">
        <v-container>
          <v-layout row wrap>
            <v-flex xs12>
              <div class="v-text_field">
                <v-text-field
                  v-model="formdata.query"
                  class="mx-2 v-text_field"
                  flat
                  label="Search"
                  prepend-inner-icon="search"
                  solo-inverted
                  placeholder="Search a certain food or leave empty."
                ></v-text-field>
              </div>
            </v-flex>

            <v-flex xs6>
              <div>
                <v-select
                  class="ratings_select"
                  v-model="formdata.radius"
                  :items="radius"
                  label="Radius"
                  centered
                  solo
                ></v-select>
              </div>
            </v-flex>

            <v-flex xs6>
              <div>
                <v-select v-model="formdata.ratings" :items="ratings" label="Ratings" centered solo></v-select>
              </div>
            </v-flex>

            <v-flex xs12 sm6 d-flex>
              <v-select
                :items="price_range"
                v-model="formdata.price_range"
                label="Price Range"
                outline
              ></v-select>
            </v-flex>

            <div>
              <v-btn type="submit" class="btnprimary" color="primary">Find me a restaurant!</v-btn>
            </div>

            <v-progress-circular
              class="loadMiddle"
              v-if="loading"
              :size="70"
              :width="7"
              color="purple"
              indeterminate
            ></v-progress-circular>
          </v-layout>
        </v-container>
      </form>
    </v-card>
  </v-layout>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      loading: false,
      radius: ["Walking Distance", "Drive", "Search around my city"],
      ratings: ["5 star", "4 star", "3 star", "2 star", "1 star"],
      price_range: [
        "$ - 0.00 to ~ 11.99",
        "$$ - 12.00 to ~23.99",
        "$$$ - 24.00 to ~35.99",
        "$$$$ - 36.00 and up"
      ],
      formdata: {
        query: "",
        radius: "",
        price_range: "",
        ratings: "",
        lat: "",
        long: ""
      }
    };
  },
  mounted() {
    this.retrieveLoc();
  },
  methods: {
    submitHandler() {
      if (!this.formdata.lat || !this.formdata.long) {
        this.retrieveLoc();
      }
      this.loading = true;
      this.$store.dispatch("foodsearch/dispatchSearch", this.formdata);

      // let api =
      //   "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?term=burger&location=sanfranscico";
      // let token =
      //   "Yua-MH2odW4jkldFX860GQ1EBNQG7X7EiWbkol4hOCCFT56D8ZxFPDeZT0DuM-mr29Iy3l-tjAeI6CoXGw1-Zu9coLnmiB2o4yPf4ychMPRM24BOD14kf4FjtigoXHYx";
      // axios
      //   .get(api, {
      //     headers: {
      //       Authorization: "Bearer " + token
      //     }
      //   })
      //   .then(response => {
      //     console.log(response);
      //   });
    },
    retrieveLoc() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          this.position = position.coords;
          this.formdata.lat = position.coords.latitude;
          this.formdata.long = position.coords.longitude;
        }),
          { timeout: 10000 };
      }
    }
  }
};
</script>

<style>
.v-text_field {
  text-align: justify;
  font-size: 4.3vw;
  display: block;
}
.v-text_field:after {
  width: 100%;
}
.btnprimary {
  text-align: justify;
  display: block;
  width: 100%;
}
.ratings_select {
  position: absolutes;
}

.loadMiddle {
  position: fixed;
  left: 50%;
  top: 35%;
  display: none;
  z-index: 1000;
  height: 31px;
  width: 31px;
}
</style>