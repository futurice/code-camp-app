<template>
    <div id="app">
        <div v-show="loading" class="splash">
            <SplashScreen />
        </div>
        <div v-show="!loading" class="main">
            <Webcam/>
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
