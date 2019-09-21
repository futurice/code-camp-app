<template>
  <div id="app">
    <Webcam />
    <Indicator />
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
