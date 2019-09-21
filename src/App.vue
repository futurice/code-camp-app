<template>
  <div id="app">
    <Webcam />
    <div class="container">
      <Indicator class="bounce" />
    </div>
  </div>
</template>

<script>
import Webcam from "./components/Webcam.vue";
import Indicator from "./components/Indicator.vue";

export default {
  name: "app",
  components: {
    Webcam,
    Indicator
  }
};
</script>

<style scoped>
#app {
  position: relative;
}
.container {
  position: absolute;
  height: 100%;
  width: 100%;
  bottom: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}
</style>
