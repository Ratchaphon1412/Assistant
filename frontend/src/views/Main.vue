<template>
  <div class="container-fluid main">
    <div class="row">
      <div class="col-3"></div>
      <div class="col-6"></div>
      <div class="col-3">
        <weatherModule />
      </div>
    </div>
  </div>
</template>

<script>
import weatherModule from "@/components/weatherModule.vue";
export default {
  data() {
    return {};
  },
  components: {
    weatherModule,
  },
};
</script>

<style lang="scss" scoped>
.main {
  width: 100%;
  height: 100vh;
  padding: 0;
  margin: 0;
  -webkit-app-region: drag;
}
.red {
  background-color: red;
}
</style>
