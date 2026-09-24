<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Force X</title>

<link
    rel="icon"
    type="image/png"
    href="./file_0000000074d482118627681d3d6c1bfd.png">

<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    font-family: Arial, sans-serif;
    background: #050807;
    color: #ffffff;
}

body {
    background:
        radial-gradient(
            circle at top,
            #123b28 0%,
            #07130d 35%,
            #050807 75%
        );
}

nav {
    width: 100%;
    min-height: 78px;
    padding: 10px 22px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background: rgba(3,8,5,0.97);

    border-bottom:
        1px solid rgba(53,255,131,0.25);

    box-shadow:
        0 4px 25px rgba(0,0,0,0.35);

    position: sticky;
    top: 0;
    z-index: 10;
}

.brand {
    display: flex;
    align-items: center;
}

.brand-name {
    font-size: 20px;
    font-weight: bold;
    color: #35ff83;
    letter-spacing: 3px;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 22px;
}

.nav-links a {
    color: #9ee8b8;
    text-decoration: none;
    font-size: 14px;
    font-weight: bold;
    transition: 0.2s;
}

.nav-links a:hover {
    color: #35ff83;
}

.page {
    width: 100%;
    min-height: calc(100vh - 78px);
    display: none;
    padding: 50px 20px;
}

.page.active {
    display: block;
}

.content {
    width: 100%;
    max-width: 900px;
    margin: auto;
}

.hero {
    text-align: center;
    padding: 75px 10px;
}

.hero-symbol {
    font-size: 55px;
    margin-bottom: 15px;
}

h1 {
    font-size: clamp(48px, 11vw, 80px);
    margin: 10px 0;

    color: #35ff83;

    letter-spacing: 3px;

    text-shadow:
        0 0 25px rgba(53,255,131,0.25);
}

.subtitle {
    color: #a8d9b8;
    font-size: 18px;
    margin-bottom: 35px;
}

.card {
    background: rgba(10,30,19,0.80);

    border:
        1px solid rgba(53,255,131,0.20);

    border-radius: 24px;

    padding: 25px;

    margin-top: 25px;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.25);
}

.info {
    color: #a8d9b8;
    line-height: 1.7;
}

button {
    border:
        1px solid rgba(53,255,131,0.35);

    border-radius: 15px;

    padding: 16px 25px;

    font-size: 17px;

    font-weight: bold;

    cursor: pointer;

    background: #35ff83;

    color: #041008;

    margin: 5px;

    transition: 0.2s;
}

button:hover {
    transform: scale(1.02);
    background: #68ff9e;
}

button:disabled {
    opacity: 0.45;
    cursor: not-allowed;
}

.secondary-button {
    background: transparent;
    color: #35ff83;
}

.secondary-button:hover {
    background: rgba(53,255,131,0.10);
}

h2 {
    font-size: 30px;
    color: #35ff83;
}

#camera {
    width: 100%;
    max-height: 500px;

    object-fit: cover;

    display: none;

    margin-top: 20px;

    border-radius: 20px;

    background: #000000;

    border:
        1px solid rgba(53,255,131,0.25);
}

#preview {
    width: 100%;

    display: none;

    margin-top: 20px;

    border-radius: 20px;

    border:
        1px solid rgba(53,255,131,0.25);
}

.status {
    font-size: 18px;
    font-weight: bold;

    margin-top: 20px;

    color: #35ff83;
}

.report {
    background: rgba(0,0,0,0.35);

    border:
        1px solid rgba(53,255,131,0.18);

    border-radius: 18px;

    padding: 20px;

    margin-top: 15px;

    line-height: 1.7;
}

.warning {
    color: #a8d9b8;

    background:
        rgba(53,255,131,0.05);

    border:
        1px solid rgba(53,255,131,0.12);

    border-radius: 15px;

    padding: 18px;

    margin-top: 15px;
}

.footer {
    text-align: center;

    padding: 30px 15px;

    color: #5d8d6d;

    font-size: 13px;
}

@media (max-width: 650px) {

    nav {
        flex-direction: column;

        gap: 12px;

        padding: 14px 15px;
    }

    .brand {
        width: 100%;
        justify-content: flex-start;
    }

    .nav-links {
        width: 100%;

        justify-content: space-between;

        gap: 7px;
    }

    .nav-links a {
        font-size: 11px;
    }

    .page {
        padding: 30px 15px;
    }

    .hero {
        padding: 55px 5px;
    }

    h1 {
        font-size: 50px;
    }

}

</style>

</head>

<body>

<nav>

<div class="brand">

<span class="brand-name">
FORCE X
</span>

</div>

<div class="nav-links">

<a
    href="#"
    onclick="showPage('home'); return false;">
HOME
</a>

<a
    href="#"
    onclick="showPage('detection'); return false;">
📷 DETECTION
</a>

<a
    href="#"
    onclick="showPage('reports'); return false;">
📊 REPORTS
</a>

<a
    href="#"
    onclick="showPage('about'); return false;">
ℹ️ ABOUT
</a>

</div>

</nav>

<section
    id="home"
    class="page active">

<div class="content">

<div class="hero">

<div class="hero-symbol">
❄️
</div>

<h1>
Force X
</h1>

<p class="subtitle">
Intelligent Detection System
</p>

<div class="card">

<p class="info">
Welcome to Force X — an intelligent
computer-vision system powered by
Snow AI.
</p>

<p class="info">
The system is designed to identify
objects and animals using artificial
intelligence.
</p>

<button
    onclick="showPage('detection')">
📷 START SCAN
</button>

</div>

</div>

</div>

</section>

<section
    id="detection"
    class="page">

<div class="content">

<h2>
📷 Detection
</h2>

<div class="card">

<p class="info">
Start a five-second camera scan.
</p>

<button
    id="startButton"
    onclick="startScan()">
📷 START SCAN
</button>

<button
    id="stopButton"
    class="secondary-button"
    onclick="stopScan()"
    disabled>
⛔ STOP
</button>

<video
    id="camera"
    autoplay
    playsinline>
</video>

<canvas
    id="canvas"
    style="display:none;">
</canvas>

<img
    id="preview"
    alt="Captured image">

<p
    id="scanStatus"
    class="status">
🟢 Ready to scan
</p>

<div class="warning">

Snow AI is currently running in
frontend-only mode.

The camera can capture an image,
but AI analysis will be connected
later.

</div>

</div>

</div>

</section>

<section
    id="reports"
    class="page">

<div class="content">

<h2>
📊 Reports
</h2>

<div class="card">

<div
    id="reportText"
    class="info">

No detection reports yet.

</div>

</div>

</div>

</section>

<section
    id="about"
    class="page">

<div class="content">

<h2>
ℹ️ About Force X
</h2>

<div class="card">

<p class="info">
Force X is a computer-vision
interface powered by Snow AI.
</p>

<p class="info">
Its purpose is to capture visual
information and eventually use
artificial intelligence to identify
objects and animals.
</p>

<p class="info">
The frontend is being developed
separately so the interface can be
tested before reconnecting the
Snow AI detection backend.
</p>

</div>

</div>

</section>

<div class="footer">

Force X • Powered by Snow AI

</div>

<script>

let stream = null;
let timer = null;
let scanning = false;

function showPage(page) {

    document
        .querySelectorAll(".page")
        .forEach(function(section) {

            section.classList.remove("active");

        });

    document
        .getElementById(page)
        .classList.add("active");

    window.scrollTo(0, 0);
}

async function startScan() {

    if (scanning) {
        return;
    }

    const camera =
        document.getElementById("camera");

    const status =
        document.getElementById("scanStatus");

    const startButton =
        document.getElementById("startButton");

    const stopButton =
        document.getElementById("stopButton");

    startButton.disabled = true;
    stopButton.disabled = false;

    status.innerText =
        "📷 Starting camera...";

    try {

        stream =
            await navigator.mediaDevices
                .getUserMedia({

                    video: {
                        facingMode: {
                            ideal: "environment"
                        }
                    },

                    audio: false

                });

        camera.srcObject = stream;

        camera.style.display =
            "block";

        scanning = true;

        let seconds = 5;

        status.innerText =
            "🟢 Scanning... 5 seconds";

        timer =
            setInterval(function() {

                seconds--;

                if (seconds > 0) {

                    status.innerText =
                        "🧠 Snow AI scan... "
                        + seconds
                        + " seconds";

                }

                if (seconds === 0) {

                    clearInterval(timer);

                    timer = null;

                    captureImage();

                }

            }, 1000);

    } catch(error) {

        console.log(error);

        status.innerText =
            "❌ Camera could not be started.";

        resetButtons();

    }

}

function captureImage() {

    const camera =
        document.getElementById("camera");

    const canvas =
        document.getElementById("canvas");

    const preview =
        document.getElementById("preview");

    const status =
        document.getElementById("scanStatus");

    if (!camera.videoWidth) {

        status.innerText =
            "❌ Camera image unavailable.";

        stopCamera();

        resetButtons();

        return;

    }

    canvas.width =
        camera.videoWidth;

    canvas.height =
        camera.videoHeight;

    const context =
        canvas.getContext("2d");

    context.drawImage(
        camera,
        0,
        0,
        canvas.width,
        canvas.height
    );

    const imageData =
        canvas.toDataURL(
            "image/jpeg",
            0.9
        );

    preview.src =
        imageData;

    preview.style.display =
        "block";

    stopCamera();

    status.innerText =
        "📸 Image captured.";

    document
        .getElementById("reportText")
        .innerHTML =
        "<div class='report'>" +
        "<strong>📸 IMAGE CAPTURED</strong>" +
        "<br><br>" +
        "The image was successfully " +
        "captured by Force X." +
        "<br><br>" +
        "🧠 Snow AI analysis is not " +
        "connected yet." +
        "</div>";

    resetButtons();

}

function stopScan() {

    if (timer) {

        clearInterval(timer);

        timer = null;

    }

    stopCamera();

    resetButtons();

    document
        .getElementById("scanStatus")
        .innerText =
        "🟢 Ready to scan";

}

function stopCamera() {

    if (stream) {

        stream
            .getTracks()
            .forEach(function(track) {

                track.stop();

            });

        stream = null;

    }

    const camera =
        document.getElementById("camera");

    camera.srcObject = null;

    camera.style.display =
        "none";

    scanning = false;

}

function resetButtons() {

    document
        .getElementById("startButton")
        .disabled = false;

    document
        .getElementById("stopButton")
        .disabled = true;

    scanning = false;

}

</script>

</body>

</html>
