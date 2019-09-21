<template>
    <div id="app">
        <div v-show="loading" class="splash">
            <SplashScreen />
        </div>
        <div v-show="!loading" class="main bounce">
            <Webcam class="webcam"/>
            <div class="container">
                <Indicator class="bounce"/>
            </div>
        </div>
    </div>
</template>

<script>
    import Webcam from "./components/Webcam.vue";
    import Indicator from "./components/Indicator.vue";
    import SplashScreen from  "./components/SplashScreen"

    export default {
        name: "app",
        data() {
            return {
                loading: true,
            }
        },
        beforeCreate() {
            setTimeout( () => {
                this.loading = false
            }, 3000)
        },
        components: {
            Webcam,
            Indicator,
            SplashScreen
        }
    };
</script>

<style scoped>
.main {
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
