function add_log(text){
    const resultDiv = document.getElementById('message-box');
    resultDiv.innerHTML+=text
    return;
}

function set_video(vid_path){
    var video=document.getElementById("video2");
    video.setAttribute("src",vid_path);
    // xhr.send();
    video.play();
    return;
}

function run_stitch(callback) {
    const xhr = new XMLHttpRequest();
    add_log("Analysing Video....<br>Detecting Objects....<br>")
    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            add_log("Object Detection Completed....<br>")
            set_video('./static/video/object_detect.mp4');
        }
    };
    xhr.open('GET', '/run-stitch');
    
    xhr.onload = function() {
        // console.log('run-stitch completed');
        callback()
      };
      xhr.send();
}

function run_out() {
    const xhr = new XMLHttpRequest();
    add_log("Creating Timestamps....<br>")
    xhr.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            add_log("Timestamps Created....<br>Rendering Query Operations....<br>")
            set_video('./static/video/timestamp.mp4');
        }
    };
    xhr.open('GET', '/run-out');
    xhr.onload = function() {
        setTimeout(function() {
            // Code to run after 10 seconds
            const b1=document.getElementById("query1");
            const b2=document.getElementById("query2");
            const run=document.getElementById("run-btn");
            b1.style.cursor = "pointer";
            b2.style.cursor = "pointer"; 
            run.style.cursor = "pointer";
            b1.disabled = false;
            b2.disabled = false;
            run.disabled = false;
            add_log("Video Analysis Completed....<br>");
         }, 5000); // 10000 milliseconds = 10 seconds
    }

    xhr.send();
    return;
}


async function run_py(){
    const resultDiv = document.getElementById('message-box');
    resultDiv.innerHTML=null
    await new Promise((resolve, reject) => {
        run_stitch(() => {
          resolve();
        });
    });
    run_out();
}

window.onload = function() {
    var path;
    // const generateBtn = document.getElementById("generate-synopsis-btn");
    const runBtn = document.getElementById("run-btn");
    var video=document.getElementById("video2");
    var b1=document.getElementById("query1");
    var b2=document.getElementById("query2");
    runBtn.disabled = true;
    runBtn.style.cursor = "not-allowed";
    b1.style.cursor = "not-allowed";
    b2.style.cursor = "not-allowed";
    b1.disabled = true;
    b2.disabled = true;
    // generateBtn.addEventListener("click", () => {
    //     radioBtns.forEach(btn => {
    //         btn.disabled = false;
    //     });
    //     runBtn.disabled = false;
    //     runBtn.style.hover = "cursor: pointer";
        
    // });

    runBtn.addEventListener("click", () => {
        if (runBtn.style.backgroundColor=="green") {
            add_log("Running Query....<br>")
            setTimeout(function() {
                add_log("Query run successful <br> ")
                video.setAttribute("src",path);
            }, 5000); 
        };
    });

    b1.addEventListener("click",()=>{
        add_log("Query >> Fetch only car<br> ")
        runBtn.style.backgroundColor = "#333";
        setTimeout(function() {
            runBtn.style.backgroundColor = "green";
        }, 2000); 
        path=b1.getAttribute("value")
    });

    b2.addEventListener("click",()=>{
        add_log("Query >> Fetch only bikes<br> ")
        runBtn.style.backgroundColor = "#333";
        setTimeout(function() {
            runBtn.style.backgroundColor = "green";
         }, 2000); 
         path=b2.getAttribute("value")
    });
    
};



