<template>
    <div class="container">
        <div class="logo">
            <img src="../assets/Logo%20no%20eyes.svg" alt="">
            <img src="../assets/lefteye.svg" alt="">
            <img src="../assets/righteye.svg" alt="">
        </div>
        <div class="tag-line">
            <div class="app-name">Mug Factor</div>
            <div class="loading">Loading...</div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SplashScreen"
    }
</script>

<style scoped>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
</style>