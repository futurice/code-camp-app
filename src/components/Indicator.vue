
<template>
  <div class="container">
    <div class="indicator">
      <img src="../assets/5 - Done.svg" />You are done
    </div>
  </div>
</template>

<script>
export default {
  name: "Indicator"
};
</script>

<style scoped>
.container {
  position: fixed;
  bottom: 0;
  width: 100vw;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.indicator {
  padding: 16px;
  border-radius: 32px;
  background: #000000ad;
  color: #fff;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
