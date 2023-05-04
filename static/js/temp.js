function add_log(text){
    const resultDiv = document.getElementById('message-box');
    resultDiv.innerHTML+=text
}

function set_video(vid_path){
    var video=document.getElementById("video2");
    video.setAttribute("src",vid_path);
}

function run_stitch() {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        const resultDiv = document.getElementById('message-box');
        resultDiv.innerHTML+="Analysing Video...<br>"
      }
    };
    xhr.open('GET', '/run-out');
    xhr.send();
    add_log("Video analysis Completed....<br>");
    set_video('./static/videos/output.avi');
}

function run_out() {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        const resultDiv = document.getElementById('message-box');
        resultDiv.innerHTML += "Stitching Video....<br>";
      }
    };
    xhr.open('GET', '/run-stitch');
    text= "Video Stitching Completed....<br>";
    xhr.send();
    add_log(text);
}


function run_py(){
    run_stitch();
    run_out();
}

window.onload = function() {

    const generateBtn = document.getElementById("generate-synopsis-btn");
    const radioBtns = document.querySelectorAll("input[name='query']");
    const runBtn = document.getElementById("run-btn");

    radioBtns.forEach(btn => {
        btn.disabled = true;
    });
    runBtn.disabled = true;
    runBtn.style.hover = "cursor: not-allowed";
    generateBtn.addEventListener("click", () => {
        radioBtns.forEach(btn => {
            btn.disabled = false;
        });
        runBtn.disabled = false;
        runBtn.style.hover = "cursor: pointer";
        
    });

    const b1=document.getElementById("query1");
    const b2=document.getElementById("query2");
    var video=document.getElementById("video2");
    const run=document.getElementById("run-btn");
    b1.addEventListener("click",()=>{
        // setTimeout(delayedFunction, 2000);
        video.setAttribute("src",b1.getAttribute("value"));
    });
    b2.addEventListener("click",()=>{
        // setTimeout(delayedFunction, 5000);
        video.setAttribute("src",b2.getAttribute("value"));
    });
    
};



