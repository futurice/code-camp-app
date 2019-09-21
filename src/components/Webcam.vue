<template>
  <video autoplay ref="video" />
</template>

<script>
export default {
  name: "Webcam",
  created: function() {
    const fs = require("fs");
    let i = 0;

    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then(stream => {
        this.$refs.video.srcObject = stream;
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
  }
};
</script>
