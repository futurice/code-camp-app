<template>
  <video autoplay />
</template>

<script>
export default {
  name: "Webcam"
};

const fs = require("fs");
const debug = false;
let i = 0;

navigator.mediaDevices
  .getUserMedia({ video: true })
  .then(function(stream) {
    document.querySelector("video").srcObject = stream;
    const canvas = document.querySelector("canvas");

    const track = stream.getVideoTracks()[0];
    setInterval(() => {
      const imageCapture = new ImageCapture(track);
      imageCapture
        .takePhoto()
        .then(blob => {
          blob
            .arrayBuffer()
            .then(arrayBuffer =>
                fs
                    .createWriteStream(`images/image_${i}.jpg`)
                    .write(Buffer.from(arrayBuffer))
            )
            .finally(() => i++);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error("grabFrame() error: ", error);
        });
    }, 1000);
  })
  .catch(function(err) {
    // eslint-disable-next-line
    console.error(err);
    alert("could not connect stream");
  });
</script>
