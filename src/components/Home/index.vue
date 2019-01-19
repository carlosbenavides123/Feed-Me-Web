<template>
  <div>
    Home
    <span v-if="!show">
      <comp-content/>
    </span>
    <span v-else>
      <comp-results/>
    </span>
  </div>
</template>
<script>
import compContent from "./content";
import compResults from "./results";
export default {
  components: {
    compContent,
    compResults
  },
  computed: {
    show() {
      return this.$store.getters["foodsearch/getShowResult"];
    }
  }
};
</script>