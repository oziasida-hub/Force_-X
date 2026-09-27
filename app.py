<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0">

<title>FORCE X — Snow AI</title>

<style>

/* =========================================================
   FORCE X — SNOW AI INTERFACE
   Frontend only
   Backend connection:
   https://force-x-backend.onrender.com/detect
========================================================= */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --bg: #030706;
    --panel: #07120d;
    --panel2: #0b1c13;
    --green: #38ff88;
    --green2: #1bd66b;
    --text: #f3fff7;
    --muted: #8eaa9a;
    --border: rgba(56,255,136,0.16);
    --danger: #ff5d68;
}

html {
    scroll-behavior: smooth;
}

body {
    min-height: 100vh;
    background:
        radial-gradient(
            circle at 50% -10%,
            rgba(28,120,70,0.35),
            transparent 42%
        ),
        radial-gradient(
            circle at 100% 80%,
            rgba(20,90,55,0.15),
            transparent 35%
        ),
        var(--bg);

    color: var(--text);
    font-family:
        Inter,
        Arial,
        Helvetica,
        sans-serif;
}

/* =========================================================
   NAVIGATION
========================================================= */

.navbar {
    position: sticky;
    top: 0;
    z-index: 100;

    width: 100%;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 15px 5%;

    background:
        rgba(3,7,6,0.88);

    backdrop-filter: blur(18px);

    border-bottom:
        1px solid var(--border);
}

/* Custom Force X logo */

.brand {
    display: flex;
    align-items: center;
    gap: 12px;

    cursor: pointer;
}

.logo-mark {
    width: 42px;
    height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    border: 2px solid var(--green);

    border-radius: 12px;

    color: var(--green);

    font-size: 20px;
    font-weight: 900;

    box-shadow:
        0 0 18px rgba(56,255,136,0.18);

    transform: skew(-8deg);
}

.brand-text {
    font-size: 18px;
    font-weight: 900;
    letter-spacing: 3px;
}

.brand-text span {
    color: var(--green);
}

.nav-links {
    display: flex;
    gap: 25px;
}

.nav-links button {
    border: none;
    background: transparent;

    color: var(--muted);

    font-size: 13px;
    font-weight: 700;

    cursor: pointer;

    transition: 0.2s;
}

.nav-links button:hover,
.nav-links button.active {
    color: var(--green);
}

/* =========================================================
   PAGE SYSTEM
========================================================= */

.page {
    display: none;

    width: 100%;
    min-height: calc(100vh - 72px);

    padding: 60px 5%;
}

.page.active {
    display: block;
}

.container {
    width: 100%;
    max-width: 1100px;

    margin: auto;
}

/* =========================================================
   HERO
========================================================= */

.hero {
    min-height: 75vh;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    text-align: center;
}

.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;

    padding: 8px 14px;

    border: 1px solid var(--border);
    border-radius: 50px;

    background: rgba(56,255,136,0.05);

    color: var(--green);

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 1px;

    margin-bottom: 25px;
}

.status-dot {
    width: 7px;
    height: 7px;

    border-radius: 50%;

    background: var(--green);

    box-shadow:
        0 0 10px var(--green);
}

.hero h1 {
    font-size: clamp(55px, 12vw, 115px);

    line-height: 0.95;

    letter-spacing: -5px;

    margin-bottom: 20px;
}

.hero h1 span {
    color: var(--green);

    text-shadow:
        0 0 40px rgba(56,255,136,0.2);
}

.hero p {
    max-width: 650px;

    color: var(--muted);

    font-size: 17px;

    line-height: 1.7;

    margin-bottom: 35px;
}

.primary-btn {
    border: none;

    padding: 16px 28px;

    border-radius: 14px;

    background: var(--green);

    color: #021007;

    font-size: 15px;
    font-weight: 900;

    cursor: pointer;

    box-shadow:
        0 10px 35px rgba(56,255,136,0.15);

    transition: 0.2s;
}

.primary-btn:hover {
    transform: translateY(-2px);

    box-shadow:
        0 15px 40px rgba(56,255,136,0.25);
}

.secondary-btn {
    border: 1px solid var(--border);

    padding: 15px 25px;

    border-radius: 14px;

    background: rgba(255,255,255,0.02);

    color: var(--text);

    font-weight: 700;

    cursor: pointer;

    transition: 0.2s;
}

.secondary-btn:hover {
    border-color: rgba(56,255,136,0.4);
}

/* =========================================================
   SECTION HEADERS
========================================================= */

.section-header {
    margin-bottom: 30px;
}

.section-header h2 {
    font-size: 38px;

    margin-bottom: 8px;
}

.section-header p {
    color: var(--muted);
}

/* =========================================================
   DETECTION PANEL
========================================================= */

.scanner {
    display: grid;

    grid-template-columns:
        minmax(0, 1.4fr)
        minmax(280px, 0.6fr);

    gap: 20px;
}

.camera-panel,
.control-panel {
    background:
        linear-gradient(
            145deg,
            rgba(11,28,19,0.95),
            rgba(4,12,8,0.95)
        );

    border: 1px solid var(--border);

    border-radius: 24px;

    padding: 20px;
}

/* Camera */

.camera-container {
    position: relative;

    width: 100%;

    min-height: 450px;

    display: flex;
    align-items: center;
    justify-content: center;

    overflow: hidden;

    border-radius: 18px;

    background:
        radial-gradient(
            circle,
            #0d2116,
            #020504
        );

    border: 1px solid rgba(56,255,136,0.1);
}

#camera {
    width: 100%;
    height: 100%;

    min-height: 450px;

    object-fit: cover;

    display: none;
}

.camera-placeholder {
    text-align: center;

    color: var(--muted);
}

.camera-icon {
    font-size: 55px;

    margin-bottom: 15px;

    opacity: 0.7;
}

/* Scanner corners */

.scan-corners {
    position: absolute;

    inset: 25px;

    pointer-events: none;

    display: none;
}

.scan-corners::before,
.scan-corners::after {
    content: "";

    position: absolute;

    width: 45px;
    height: 45px;

    border-color: var(--green);
    border-style: solid;
}

.scan-corners::before {
    top: 0;
    left: 0;

    border-width: 3px 0 0 3px;
}

.scan-corners::after {
    bottom: 0;
    right: 0;

    border-width: 0 3px 3px 0;
}

/* scanning animation */

.scanning-line {
    position: absolute;

    left: 5%;
    right: 5%;

    top: 10%;

    height: 2px;

    background: var(--green);

    box-shadow:
        0 0 15px var(--green),
        0 0 30px var(--green);

    display: none;

    animation:
        scanLine 2s linear infinite;
}

@keyframes scanLine {

    0% {
        top: 10%;
    }

    50% {
        top: 90%;
    }

    100% {
        top: 10%;
    }

}

/* Controls */

.control-panel h3 {
    margin-bottom: 10px;
}

.control-panel p {
    color: var(--muted);

    line-height: 1.6;

    font-size: 14px;

    margin-bottom: 25px;
}

.control-buttons {
    display: flex;

    flex-direction: column;

    gap: 10px;
}

.control-buttons button {
    width: 100%;
}

#stopButton {
    background: rgba(255,93,104,0.08);

    border: 1px solid rgba(255,93,104,0.2);

    color: var(--danger);
}

#stopButton:hover {
    background: rgba(255,93,104,0.15);
}

.scan-status {
    margin-top: 25px;

    padding: 15px;

    border-radius: 14px;

    background: rgba(0,0,0,0.25);

    border: 1px solid var(--border);

    color: var(--green);

    font-size: 13px;

    line-height: 1.5;
}

/* =========================================================
   PREVIEW
========================================================= */

#preview {
    width: 100%;

    margin-top: 15px;

    display: none;

    border-radius: 18px;

    border: 1px solid var(--border);
}

/* =========================================================
   REPORTS
========================================================= */

.report-empty {
    padding: 70px 20px;

    text-align: center;

    border:
        1px dashed
        rgba(56,255,136,0.15);

    border-radius: 22px;

    color: var(--muted);
}

.report {
    background:
        linear-gradient(
            145deg,
            rgba(11,28,19,0.95),
            rgba(4,12,8,0.95)
        );

    border: 1px solid var(--border);

    border-radius: 24px;

    padding: 25px;
}

.report-header {
    display: flex;

    justify-content: space-between;

    gap: 20px;

    flex-wrap: wrap;

    padding-bottom: 20px;

    border-bottom: 1px solid var(--border);

    margin-bottom: 20px;
}

.report-title {
    color: var(--green);

    font-size: 20px;

    font-weight: 900;
}

.report-meta {
    color: var(--muted);

    font-size: 13px;
}

.detection {
    padding: 20px;

    margin-top: 12px;

    border-radius: 18px;

    background:
        rgba(56,255,136,0.035);

    border: 1px solid rgba(56,255,136,0.12);
}

.detection-name {
    font-size: 22px;

    font-weight: 900;

    margin-bottom: 8px;
}

.confidence {
    color: var(--green);

    font-weight: 900;
}

.detection-description {
    color: var(--muted);

    line-height: 1.6;

    margin-top: 10px;
}

.google-link {
    display: inline-block;

    margin-top: 15px;

    padding: 9px 13px;

    border-radius: 10px;

    background: rgba(56,255,136,0.08);

    border: 1px solid var(--border);

    color: var(--green);

    text-decoration: none;

    font-size: 12px;

    font-weight: 700;
}

/* =========================================================
   ABOUT
========================================================= */

.about-grid {
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 15px;
}

.species-card {
    padding: 25px;

    border-radius: 20px;

    background:
        rgba(8,22,15,0.8);

    border: 1px solid var(--border);

    transition: 0.2s;
}

.species-card:hover {
    transform: translateY(-4px);

    border-color:
        rgba(56,255,136,0.35);
}

.species-icon {
    font-size: 40px;

    margin-bottom: 15px;
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

.about-description {
    margin-top: 25px;

    padding: 25px;

    border-radius: 20px;

    background:
        rgba(8,22,15,0.8);

    border: 1px solid var(--border);

    color: var(--muted);

    line-height: 1.8;
}

/* =========================================================
   LOADING
========================================================= */

.loading {
    display: inline-block;

    width: 15px;
    height: 15px;

    border: 2px solid rgba(56,255,136,0.2);

    border-top-color: var(--green);

    border-radius: 50%;

    animation:
        spin 0.8s linear infinite;
}

@keyframes spin {

    to {
        transform: rotate(360deg);
    }

}

/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 800px) {

    .navbar {
        padding: 12px 18px;
    }

    .nav-links {
        gap: 10px;
    }

    .nav-links button {
        font-size: 11px;
    }

    .brand-text {
        display: none;
    }

    .scanner {
        grid-template-columns: 1fr;
    }

    .camera-container,
    #camera {
        min-height: 350px;
    }

    .about-grid {
        grid-template-columns: 1fr;
    }

    .page {
        padding: 40px 18px;
    }

}

@media (max-width: 500px) {

    .navbar {
        align-items: center;
    }

    .nav-links {
        gap: 5px;
    }

    .nav-links button {
        padding: 5px;
        font-size: 10px;
    }

    .hero h1 {
        letter-spacing: -3px;
    }

}

</style>

</head>

<body>

<!-- =======================================================
     NAVIGATION
======================================================= -->

<nav class="navbar">

    <div
        class="brand"
        onclick="showPage('home')">

        <div class="logo-mark">
            X
        </div>

        <div class="brand-text">
            FORCE <span>X</span>
        </div>

    </div>

    <div class="nav-links">

        <button
            id="nav-home"
            class="active"
            onclick="showPage('home')">
            HOME
        </button>

        <button
            id="nav-detection"
            onclick="showPage('detection')">
            SCAN
        </button>

        <button
            id="nav-reports"
            onclick="showPage('reports')">
            REPORTS
        </button>

        <button
            id="nav-about"
            onclick="showPage('about')">
            ABOUT
        </button>

    </div>

</nav>


<!-- =======================================================
     HOME
======================================================= -->

<section
    id="home"
    class="page active">

    <div class="container">

        <div class="hero">

            <div class="status-pill">

                <span class="status-dot"></span>

                SNOW AI ONLINE

            </div>

            <h1>
                FORCE <span>X</span>
            </h1>

            <p>

                Intelligent computer vision
                for discovering and identifying
                the world around you.

                Powered by Snow AI.

            </p>

            <button
                class="primary-btn"
                onclick="showPage('detection')">

                START DETECTION

            </button>

        </div>

    </div>

</section>


<!-- =======================================================
     DETECTION
======================================================= -->

<section
    id="detection"
    class="page">

    <div class="container">

        <div class="section-header">

            <h2>
                Snow AI Scanner
            </h2>

            <p>
                Point your camera at an object
                or animal and let Snow AI analyze it.
            </p>

        </div>


        <div class="scanner">


            <!-- CAMERA -->

            <div class="camera-panel">

                <div class="camera-container">

                    <div
                        id="cameraPlaceholder"
                        class="camera-placeholder">

                        <div class="camera-icon">
                            ◉
                        </div>

                        <p>
                            Camera ready
                        </p>

                    </div>

                    <video
                        id="camera"
                        autoplay
                        playsinline>
                    </video>

                    <div
                        id="scanCorners"
                        class="scan-corners">
                    </div>

                    <div
                        id="scanningLine"
                        class="scanning-line">
                    </div>

                </div>


                <canvas
                    id="canvas"
                    style="display:none;">
                </canvas>


                <img
                    id="preview"
                    alt="Captured image">

            </div>


            <!-- CONTROLS -->

            <div class="control-panel">

                <h3>
                    Detection Control
                </h3>

                <p>

                    Snow AI will activate your
                    camera, capture a frame and
                    send it to the Force X
                    detection system.

                </p>


                <div class="control-buttons">

                    <button
                        id="startButton"
                        class="primary-btn"
                        onclick="startScan()">

                        START SCAN

                    </button>


                    <button
                        id="stopButton"
                        class="secondary-btn"
                        onclick="stopScan()"
                        disabled>

                        STOP SCAN

                    </button>

                </div>


                <div
                    id="scanStatus"
                    class="scan-status">

                    ● Ready for detection

                </div>

            </div>

        </div>

    </div>

</section>


<!-- =======================================================
     REPORTS
======================================================= -->

<section
    id="reports"
    class="page">

    <div class="container">

        <div class="section-header">

            <h2>
                Detection Reports
            </h2>

            <p>
                Results generated by Snow AI.
            </p>

        </div>


        <div id="reportText">

            <div class="report-empty">

                No detection has been performed yet.

            </div>

        </div>

    </div>

</section>


<!-- =======================================================
     ABOUT
======================================================= -->

<section
    id="about"
    class="page">

    <div class="container">

        <div class="section-header">

            <h2>
                About Force X
            </h2>

            <p>
                Built to explore and protect
                the world's wildlife.
            </p>

        </div>


        <div class="about-grid">


            <div class="species-card">

                <div class="species-icon">
                    🦍
                </div>

                <h3>
                    Bonobo
                </h3>

                <p>

                    <strong>
                        Pan paniscus
                    </strong>

                    <br><br>

                    A great ape native to the
                    Democratic Republic of the Congo.

                    Snow AI can eventually be
                    trained to distinguish bonobos
                    from other primates.

                </p>

            </div>


            <div class="species-card">

                <div class="species-icon">
                    🦒
                </div>

                <h3>
                    Okapi
                </h3>

                <p>

                    <strong>
                        Okapia johnstoni
                    </strong>

                    <br><br>

                    A unique giraffid from the
                    forests of the Democratic
                    Republic of the Congo.

                    Its striped legs make it a
                    distinctive computer-vision target.

                </p>

            </div>


            <div class="species-card">

                <div class="species-icon">
                    🐒
                </div>

                <h3>
                    Likweli
                </h3>

                <p>

                    <strong>
                        Colobus congoensis
                    </strong>

                    <br><br>

                    A recently described African
                    colobus monkey associated with
                    forests of the Democratic
                    Republic of the Congo.

                </p>

            </div>

        </div>


        <div class="about-description">

            <strong
                style="color:var(--green);">

                THE FORCE X MISSION

            </strong>

            <br><br>

            Force X combines computer vision
  
