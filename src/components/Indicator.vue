
<template>
  <div>
    <div class="indicator">
      <p v-if="status === 1" class="bounce">
        <img src="../assets/1 - Sober.svg" />You appear to be sober
      </p>
      <p v-else-if="status === 2">
        <img src="../assets/2 - Tipsy.svg" />You appear to be tipsy
      </p>
      <p v-else-if="status === 3">
        <img src="../assets/3 - Drunk.svg" />You are drunk!
      </p>
      <p v-else-if="status === 4">
        <img src="../assets/4 - Wasted.svg" />You are wasted!
      </p>
      <p v-else-if="status === 5">
        <img src="../assets/5 - Done.svg" />You are done!
      </p>
      <p v-else>Unknown status</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Indicator",
  data: function() {
    return { status: 3 };
  },
  created: function() {
    let that = this;
    setInterval(function() {
      that.status = Math.floor((Math.random() * 10) / 2);
    }, 1000);
  }
};
</script>

<style scoped>
.indicator {
  padding: 8px 16px;
  border-radius: 99999px;
  background: #000000ad;
  color: #fff;
  font-size: 24px;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>
