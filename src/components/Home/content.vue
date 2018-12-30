<template>
  <v-layout>
    <v-card>
      <form @submit.prevent="submitHandler">
        <v-container>
          <v-layout
            row
            wrap
          >
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

            <v-flex xs12>
              <div>
                <v-select
                  v-model="formdata.radius"
                  :items="radius"
                  label="Radius"
                  centered
                  solo
                ></v-select>
              </div>
            </v-flex>

            <div>
              <v-btn
                type="submit"
                class="btnprimary"
                :loading="loading"
                :disabled="loading"
                @click="loader = 'loading'"
                color="primary"
              >Find me a restaurant!</v-btn>
            </div>

          </v-layout>
        </v-container>
      </form>
    </v-card>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      loader: null,
      loading: false,
      radius: ["Walking Distance", "Drive", "Search around my city"],
      formdata: {
        query: "",
        radius: ""
      }
    };
  },
  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 3000);

      this.loader = null;
    }
  },
  methods: {
    submitHandler() {
      this.$store.dispatch("foodsearch/dispatchSearch", this.formdata);
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
</style>