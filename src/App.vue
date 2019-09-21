<template>
  <div id="app">
    <Webcam class="webcam" />
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
  display: flex;
  height: 100vh;
  align-items: center;
}
.container {
  position: absolute;
  width: 100%;
  bottom: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
}
.webcam {
  width: 100%;
}
</style>
