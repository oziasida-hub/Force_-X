<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Force X | Snow AI</title>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --bg: #030806;
    --panel: rgba(10, 25, 17, .82);
    --green: #35ff83;
    --green2: #18c968;
    --text: #f1fff5;
    --muted: #9bc8aa;
    --border: rgba(53,255,131,.18);
}

html {
    scroll-behavior: smooth;
}

body {
    min-height: 100vh;
    font-family: Arial, sans-serif;
    color: var(--text);
    background:
        radial-gradient(circle at 50% -10%, #174d30 0%, #07140d 35%, var(--bg) 75%);
}

/* NAVIGATION */

nav {
    position: sticky;
    top: 0;
    z-index: 100;

    min-height: 76px;
    padding: 10px 24px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background: rgba(2,8,5,.94);
    backdrop-filter: blur(14px);

    border-bottom: 1px solid var(--border);
}

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo {
    width: 48px;
    height: 48px;

    display: grid;
    place-items: center;

    border: 2px solid var(--green);
    border-radius: 14px;

    color: var(--green);
    font-size: 22px;
    font-weight: 900;

    box-shadow:
        0 0 20px rgba(53,255,131,.2);
}

.brand-name {
    font-weight: 900;
    letter-spacing: 3px;
    color: var(--green);
}

.brand-sub {
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1px;
}

.nav-links {
    display: flex;
    gap: 8px;
}

.nav-links button {
    background: transparent;
    color: var(--muted);
    border: 0;
    padding: 10px 12px;
    cursor: pointer;
    font-weight: bold;
}

.nav-links button:hover,
.nav-links button.active {
    color: var(--green);
}

/* PAGES */

.page {
    display: none;
    min-height: calc(100vh - 76px);
    padding: 45px 18px;
}

.page.active {
    display: block;
}

.container {
    width: min(1050px, 100%);
    margin: auto;
}

/* HOME */

.hero {
    min-height: 75vh;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;
}

.hero-inner {
    max-width: 800px;
}

.hero-logo {
    width: 95px;
    height: 95px;

    margin: 0 auto 25px;

    display: grid;
    place-items: center;

    border: 3px solid var(--green);
    border-radius: 28px;

    font-size: 45px;
    font-weight: 900;
    color: var(--green);

    box-shadow:
        0 0 45px rgba(53,255,131,.18);
}

h1 {
    font-size: clamp(50px, 11vw, 105px);
    letter-spacing: 6px;
    color: var(--green);
    margin-bottom: 10px;
}

.hero-subtitle {
    color: var(--muted);
    font-size: clamp(17px, 3vw, 23px);
    margin-bottom: 35px;
}

.hero-description {
    max-width: 650px;
    margin: auto;

    color: #c0ddc9;
    line-height: 1.8;
}

/* BUTTONS */

.primary {
    border: 0;
    border-radius: 15px;

    padding: 16px 26px;
    margin-top: 28px;

    background: var(--green);
    color: #031008;

    font-size: 16px;
    font-weight: 900;

    cursor: pointer;

    transition: .2s;
}

.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(53,255,131,.2);
}

.secondary {
    border: 1px solid var(--border);
    border-radius: 15px;

    padding: 15px 22px;
    margin: 6px;

    background: rgba(53,255,131,.05);
    color: var(--green);

    font-weight: bold;
    cursor: pointer;
}

.secondary:hover {
    background: rgba(53,255,131,.12);
}

/* CARDS */

.card {
    background: var(--panel);
    border: 1px solid var(--border);
    border-radius: 24px;

    padding: 25px;
    margin-top: 25px;

    box-shadow: 0 15px 45px rgba(0,0,0,.25);
}

h2 {
    color: var(--green);
    font-size: 32px;
    margin-bottom: 8px;
}

.section-description {
    color: var(--muted);
    line-height: 1.7;
}

/* DETECTION */

.scan-area {
    text-align: center;
}

#camera {
    width: 100%;
    max-height: 560px;

    display: none;

    margin-top: 22px;

    border-radius: 20px;
    border: 1px solid var(--border);

    background: #000;

    object-fit: cover;
}

#preview {
    width: 100%;

    display: none;

    margin-top: 22px;

    border-radius: 20px;
    border: 1px solid var(--border);
}

#canvas {
    display: none;
}

.status {
    margin-top: 22px;

    color: var(--green);
    font-weight: bold;

    min-height: 24px;
}

.progress {
    width: 100%;
    height: 6px;

    display: none;

    margin-top: 18px;

    overflow: hidden;

    border-radius: 20px;
    background: rgba(255,255,255,.08);
}

.progress-bar {
    width: 0%;
    height: 100%;

    background: var(--green);

    transition: width .1s linear;
}

/* REPORT */

.report {
    border: 1px solid var(--border);
    border-radius: 18px;

    padding: 20px;

    margin-top: 18px;

    background: rgba(0,0,0,.25);
}

.report-header {
    color: var(--green);
    font-size: 20px;
    font-weight: 900;
}

.detection {
    margin-top: 15px;

    padding: 17px;

    border-radius: 15px;

    background: rgba(53,255,131,.05);
    border: 1px solid rgba(53,255,131,.12);
}

.detection-name {
    color: var(--green);
    font-size: 20px;
    font-weight: 900;
}

.confidence {
    color: var(--green);
    font-weight: bold;
}

.search-link {
    display: inline-block;

    margin-top: 12px;
    padding: 9px 13px;

    border-radius: 10px;

    background: var(--green);
    color: #031008;

    text-decoration: none;
    font-weight: bold;
}

/* SPECIES */

.species-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;

    margin-top: 25px;
}

.species-card {
    padding: 22px;

    border: 1px solid var(--border);
    border-radius: 20px;

    background: rgba(10,30,19,.65);
}

.species-icon {
    font-size: 42px;
    margin-bottom: 12px;
}

.species-card h3 {
    color: var(--green);
    margin-bottom: 8px;
}

.species-card p {
    color: var(--muted);
    line-height: 1.6;
    font-size: 14px;
}

/* FOOTER */

footer {
    text-align: center;
    padding: 35px 20px;

    color: #648570;
    font-size: 13px;

    border-top: 1px solid var(--border);
}

/* MOBILE */

@media(max-width: 700px) {

    nav {
        flex-direction: column;
        gap: 8px;
        padding: 10px;
    }

    .nav-links {
        width: 100%;
        justify-content: space-between;
    }

    .nav-links button {
        font-size: 11px;
        padding: 8px 5px;
    }

    .page {
        padding: 30px 14px;
    }

    .hero {
        min-height: 70vh;
    }

    .species-grid {
        grid-template-columns: 1fr;
    }
}
</style>
</head>

<body>

<!-- NAVIGATION -->

<nav>

    <div class="brand">

        <div class="logo">X</div>

        <div>
            <div class="brand-name">FORCE X</div>
            <div class="brand-sub">POWERED BY SNOW AI</div>
        </div>

    </div>

    <div class="nav-links">

        <button class="active" onclick="showPage('home', this)">
            HOME
        </button>

        <button onclick="showPage('detection', this)">
            SCAN
        </button>

        <button onclick="showPage('reports', this)">
            REPORTS
        </button>

        <button onclick="showPage('about', this)">
            ABOUT
        </button>

    </div>

</nav>


<!-- HOME -->

<section id="home" class="page active">

    <div class="container hero">

        <div class="hero-inner">

            <div class="hero-logo">
                X
            </div>

            <h1>FORCE X</h1>

            <p class="hero-subtitle">
                Intelligent Species Detection
            </p>

            <p class="hero-description">
                Force X is an experimental computer-vision
                platform powered by Snow AI. Capture an image
                and send it to the Snow AI detection system for
                analysis.
            </p>

            <button
                class="primary"
                onclick="openDetection()">

                📷 START SCAN

            </button>

        </div>

    </div>

</section>


<!-- DETECTION -->

<section id="detection" class="page">

    <div class="container">

        <h2>📷 Snow AI Detection</h2>

        <p class="section-description">
            Start a five-second scan. Your camera image will
            be captured and sent to the Force X Snow AI backend.
        </p>

        <div class="card scan-area">

            <button
                id="startButton"
                class="primary"
                onclick="startScan()">

                📷 START SCAN

            </button>

            <button
                id="stopButton"
                class="secondary"
                onclick="stopScan()"
                disabled>

                ⛔ STOP

            </button>

            <video
                id="camera"
                autoplay
                playsinline>
            </video>

            <canvas id="canvas"></canvas>

            <img
                id="preview"
                alt="Captured scan">

            <div class="progress" id="progress">

                <div
                    class="progress-bar"
                    id="progressBar">
                </div>

            </div>

            <div
                id="scanStatus"
                class="status">

                🟢 Ready to scan

            </div>

        </div>

    </div>

</section>


<!-- REPORTS -->

<section id="reports" class="page">

    <div class="container">

        <h2>📊 Snow AI Reports</h2>

        <p class="section-description">
            Results returned by the Snow AI detection system.
        </p>

        <div class="card">

            <div id="reportText">

                <p class="section-description">
                    No detection reports yet.
                </p>

            </div>

        </div>

    </div>

</section>


<!-- ABOUT -->

<section id="about" class="page">

    <div class="container">

        <h2>ℹ️ About Force X</h2>

        <div class="card">

            <p class="section-description">

                Force X is a computer-vision project designed
                around Snow AI. The goal is to develop a system
                capable of recognising animals and other objects
                from images.

                <br><br>

                The project also focuses on species discovery,
                conservation and the possibility of identifying
                animals that may be difficult to distinguish
                using ordinary object-detection systems.

            </p>

        </div>


        <div class="species-grid">

            <div class="species-card">

                <div class="species-icon">🦍</div>

                <h3>Bonobo</h3>

                <p>
                    Pan paniscus — a great ape native to the
                    Democratic Republic of the Congo.
                </p>

            </div>


            <div class="species-card">

                <div class="species-icon">🦒</div>

                <h3>Okapi</h3>

                <p>
                    Okapia johnstoni — a forest-dwelling giraffid
                    native to the Democratic Republic of the Congo.
                </p>

            </div>


            <div class="species-card">

                <div class="species-icon">🐒</div>

                <h3>Likweli</h3>

                <p>
                    Colobus congoensis — a colobus monkey associated
                    with forests of the Democratic Republic of the Congo.
                </p>

            </div>

        </div>

    </div>

</section>


<footer>

    FORCE X • SNOW AI

</footer>


<script>

/*
==================================================
FORCE X FRONTEND
SNOW AI BACKEND CONNECTION
==================================================
*/

const SNOW_AI_API =
    "https://force-x-backend.onrender.com/detect";


let stream = null;
let timer = null;
let scanning = false;
let startTime = 0;


/* PAGE NAVIGATION */

function showPage(pageId, clickedButton = null) {

    document
        .querySelectorAll(".page")
        .forEach(page => {

            page.classList.remove("active");

        });


    const page =
        document.getElementById(pageId);

    if (page) {
        page.classList.add("active");
    }


    document
        .querySelectorAll(".nav-links button")
        .forEach(button => {

            button.classList.remove("active");

        });


    if (clickedButton) {
        clickedButton.classList.add("active");
    }


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}


function openDetection() {

    const scanButton =
        document.querySelector(
            ".nav-links button:nth-child(2)"
        );

    showPage(
        "detection",
        scanButton
    );

}


/* START SCAN */

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

    const progress =
        document.getElementById("progress");

    const progressBar =
        document.getElementById("progressBar");


    startButton.disabled = true;
    stopButton.disabled = false;


    status.innerText =
        "📷 Starting camera...";


    try {

        stream =
            await navigator.mediaDevices.getUserMedia({

                video: {
                    facingMode: {
                        ideal: "environment"
                    },

                    width: {
                        ideal: 1280
                    },

                    height: {
                        ideal: 720
                    }
                },

                audio: false

            });


        camera.srcObject = stream;

        camera.style.display = "block";

        scanning = true;

        startTime = Date.now();


        progress.style.display = "block";

        progressBar.style.width = "0%";


        let seconds = 5;


        status.innerText =
            "🟢 Scanning... 5 seconds";


        timer =
            setInterval(() => {

                seconds--;

                const percent =
                    ((5 - seconds) / 5) * 100;

                progressBar.style.width =
                    percent + "%";


                if (seconds > 0) {

                    status.innerText =
                        "🧠 Snow AI scanning... "
                        + seconds
                        + " seconds";

                }


                if (seconds === 0) {

                    clearInterval(timer);

                    timer = null;

                    captureImage();

                }

            }, 1000);


    } catch (error) {

        console.error(error);

        status.innerText =
            "❌ Camera permission was denied or the camera is unavailable.";

        resetButtons();

    }

}


/* CAPTURE IMAGE */

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


    const duration =
        (
            (Date.now() - startTime)
            / 1000
        ).toFixed(1);


    const timestamp =
        new Date().toLocaleString();


    status.innerText =
        "🔗 Connecting to Snow AI...";


    /*
    ==========================================
    THIS IS THE IMPORTANT CONNECTION
    ==========================================
    */

    fetch(
        SNOW_AI_API,
        {

            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                image: imageData,

                timestamp: timestamp,

                duration: duration

            })

        }
    )

    .then(response => {

        if (!response.ok) {

            throw new Error(
                "Backend returned HTTP "
                + response.status
            );

        }

        return response.json();

    })

    .then(data => {

        console.log(
            "Snow AI response:",
            data
        );


        if (!data.success) {

            throw new Error(
                data.error ||
                "Snow AI returned an error."
            );

        }


        displayResults(data);

        resetButtons();

    })

    .catch(error => {

        console.error(
            "Snow AI error:",
            error
        );


        status.innerText =
            "❌ Snow AI could not analyze the image.";

        resetButtons();

    });

}


/* DISPLAY RESULTS */

function displayResults(data) {

    const status =
        document.getElementById(
            "scanStatus"
        );

    const reportText =
        document.getElementById(
            "reportText"
        );


    let html = `

        <div class="report">

            <div class="report-header">
                ❄️ SNOW AI REPORT
            </div>

            <br>

            🕒 <strong>Timestamp</strong><br>
            ${escapeHTML(data.timestamp || "Unknown")}

            <br><br>

            ⏱️ <strong>Scan duration</strong><br>
            ${escapeHTML(data.duration || "Unknown")}
            seconds

    `;


    if (
        !data.objects ||
        data.objects.length === 0
    ) {

        html += `

            <div class="detection">

                🔍 <strong>No objects detected.</strong>

                <br><br>

                Snow AI did not find a recognised
                object in this scan.

            </div>

        `;

    } else {

        html += `

            <br><br>

            🔍 <strong>
            Objects detected:
            </strong>

        `;


        data.objects.forEach(object => {

            const name =
                object.name ||
                "Unknown object";


            const confidence =
                object.confidence ||
                "Unknown";


            const description =
                object.description ||
                "No description available.";


            const googleURL =
                object.google_url ||
                (
                    "https://www.google.com/search?q="
                    +
                    encodeURIComponent(name)
                );


            html += `

                <div class="detection">

                    <div class="detection-name">
                        🔹 ${escapeHTML(name)}
                    </div>

                    <br>

                    🎯 Confidence:

                    <span class="confidence">
                        ${escapeHTML(confidence)}
                    </span>

                    <br><br>

                    📚
                    ${escapeHTML(description)}

                    <br>

                    <a
                        class="search-link"
                        href="${escapeAttribute(googleURL)}"
                        target="_blank"
                        rel="noopener noreferrer">
