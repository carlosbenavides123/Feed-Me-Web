<template>
  <v-app>
    <comp-header />
    <router-view></router-view>
    <comp-footer />
  </v-app>
</template>

<script>
import compHeader from "./components/Header-Footer/Header";
import compFooter from "./components/Header-Footer/Footer";

export default {
  components: {
    compHeader,
    compFooter
  }
  // To do refresh token stuff should be here
  // created() {
  //   this.$store.dispatch("admin/refreshToken");
  // }
};
</script>