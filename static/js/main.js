window.onload = function() {
    const fileUpload = document.getElementById("file-upload");
    const nextButton = document.querySelector(".next-button");
    const func_page = document.querySelector(".function");
    flag=1;
    window.addEventListener("load", () => {
    nextButton.disabled = true;
    func_page.style.display = "none";
    });

    fileUpload.addEventListener("change", () => {
        if (fileUpload.value) {
            nextButton.disabled = false;
            nextButton.style.backgroundColor = "#4CAF50";
        }
        else {
            nextButton.disabled = true;
            nextButton.style.backgroundColor = "#ccc";
        }
    });
    nextButton.addEventListener("click", () => {
        if (fileUpload.value) {
            // check if the file is a .mp4 or .mkv file
            if (fileUpload.value.endsWith(".mp4") || fileUpload.value.endsWith(".mkv")) {
                
                // file_name = fileUpload.value.split("\\").pop();
                // // Get the selected video file
                // var videoFile = document.getElementById('file-upload').files[0];
                
                // // Create a video element and load the video file
                // var videoElement = document.createElement('video');
                // videoElement.src = URL.createObjectURL(videoFile);
                
                // // Wait for the video to load
                // videoElement.addEventListener('loadedmetadata', function() {
                //     // Create a canvas element and set its dimensions to match the video
                //     var canvasElement = document.createElement('canvas');
                //     canvasElement.width = this.videoWidth;
                //     canvasElement.height = this.videoHeight;
                    
                //     // Draw the first frame of the video onto the canvas
                //     var context = canvasElement.getContext('2d');
                //     context.drawImage(this, 0, 0, canvasElement.width, canvasElement.height);
                    
                //     // Convert the canvas to a PNG image
                //     var pngImage = canvasElement.toDataURL('image/png');
                    

                    // alert(pngImage);
                // });
                flag=0;
                
                
            } else {
                nextButton.disabled = true;
                nextButton.style.backgroundColor = "#e91a1a";
                fileUpload.value = "";
                alert("Wrong input file type. Please upload a .mp4 or .mkv file.");
                return;
            }
        } else {
            nextButton.style.backgroundColor = "#e91a1a";
        }
    // Perform your desired action here
    });
}
