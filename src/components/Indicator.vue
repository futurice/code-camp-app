<template>
    <div v-if="status === 0" class="indicator">
        <img src="../assets/1 - Sober.svg"/>
        <p>You appear to be sober</p>
    </div>
    <div v-else-if="status === 1" class="indicator">
        <img src="../assets/2 - Tipsy.svg"/>
        <p>You appear to be tipsy</p>
    </div>
    <div v-else-if="status === 2" class="indicator">
        <img src="../assets/3 - Drunk.svg"/>
        <p>You are drunk!</p>
    </div>
    <div v-else-if="status === 3" class="indicator">
        <img src="../assets/4 - Wasted.svg"/>
        <p>You are wasted!</p>
    </div>
    <div v-else-if="status === 4" class="indicator">
        <img src="../assets/5 - Done.svg"/>
        <p>You are done!</p>
    </div>
    <p class="indicator" v-else>Unknown status</p>
</template>

<script>
    const { PythonShell } = require('python-shell');
    const chokidar = require('chokidar');
    const fs = require("fs");

    const pyShellOptions = {
        pythonPath: 'venv/bin/python3',
        pythonOptions: ['-u'], // get print results in real-time
    }

    export default {
        name: "Indicator",
        data() {
            return {status: 1};
        },
        created() {
            PythonShell.run('drowsiness_detect.py', pyShellOptions, function (err) {
                if (err) console.log(err);
                console.log('finished');
            });
            let  watcher = chokidar.watch('images/result.txt', {persistent: true});
            watcher.on('all', path => {
                fs.readFile('images/result.txt','utf-8', (err, data) => {
                    if (err) throw err;
                    console.log(data);
                    this.status = parseInt(data);
                });
            })
        }
    };
</script>

<style scoped>
    .indicator {
        padding: 8px 32px;
        border-radius: 100px;
        background: #000000ad;
        color: #fff;
        font-size: 20px;
        font-family: "Avenir", Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    img {
        margin-right: 8px;
    }
</style>
