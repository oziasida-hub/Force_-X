from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS
from ultralytics import YOLO
from datetime import datetime
from base64 import b64decode
import numpy as np
import cv2
import urllib.parse
import os

model = YOLO("yolo11n.pt")

object_info = {
    "person": "A human being.",
    "dog": "A domesticated mammal commonly kept as a companion animal.",
    "cat": "A domesticated mammal commonly kept as a companion animal.",
    "bird": "A warm-blooded animal with feathers, wings and a beak.",
    "horse": "A large domesticated mammal commonly used for riding and work.",
    "cow": "A domesticated mammal commonly raised for milk and meat.",
    "sheep": "A domesticated mammal commonly raised for wool and meat.",
    "elephant": "A very large land mammal known for its trunk and tusks.",
    "bear": "A large mammal belonging to the bear family.",
    "zebra": "A wild African mammal known for its black-and-white stripes.",
    "giraffe": "A tall African mammal known for its long neck and legs.",
    "car": "A motor vehicle mainly designed to transport people.",
    "bicycle": "A human-powered vehicle with two wheels.",
    "motorcycle": "A two-wheeled motor vehicle.",
    "bus": "A large road vehicle designed to transport passengers.",
    "truck": "A motor vehicle designed mainly for transporting goods.",
    "laptop": "A portable personal computer.",
    "cell phone": "A portable electronic device used for communication and digital tasks.",
    "bottle": "A container commonly used to hold liquids.",
    "chair": "A piece of furniture designed for one person to sit on.",
    "backpack": "A bag designed to be carried on a person's back."
}

app = Flask(__name__)

CORS(
    app,
    origins=[
        "https://force-x.onrender.com",
        "https://force-x-frontend.onrender.com"
    ]
)

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Force X</title>

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
    background: rgba(3,8,5,0.96);
    border-bottom: 1px solid rgba(48,255,125,0.25);
    box-shadow: 0 4px 25px rgba(0,0,0,0.35);
    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-mark {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 15px;
    background: linear-gradient(135deg, #35ff83, #0b5d31);
    color: #041008;
    font-size: 25px;
    font-weight: 900;
    box-shadow: 0 0 20px rgba(53,255,131,0.25);
}

.logo-name {
    font-size: 19px;
    font-weight: bold;
    color: #35ff83;
    letter-spacing: 2px;
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
    padding: 65px 10px;
}

h1 {
    font-size: clamp(44px, 10vw, 76px);
    margin: 10px 0;
    color: #35ff83;
    letter-spacing: 2px;
}

.subtitle {
    color: #a8d9b8;
    font-size: 18px;
}

.card {
    background: rgba(10,30,19,0.78);
    border: 1px solid rgba(53,255,131,0.20);
    border-radius: 24px;
    padding: 25px;
    margin-top: 25px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.25);
}

button {
    border: 1px solid rgba(53,255,131,0.35);
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

h2 {
    font-size: 30px;
    color: #35ff83;
}

.info {
    color: #a8d9b8;
    line-height: 1.7;
}

#camera {
    width: 100%;
    max-height: 500px;
    object-fit: cover;
    display: none;
    margin-top: 20px;
    border-radius: 20px;
    background: #000000;
    border: 1px solid rgba(53,255,131,0.25);
}

#preview {
    width: 100%;
    display: none;
    margin-top: 20px;
    border-radius: 20px;
    border: 1px solid rgba(53,255,131,0.25);
}

.status {
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
    color: #35ff83;
}

.report {
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(53,255,131,0.18);
    border-radius: 18px;
    padding: 20px;
    margin-top: 15px;
    line-height: 1.7;
}

.detection {
    background: rgba(53,255,131,0.06);
    border: 1px solid rgba(53,255,131,0.12);
    border-radius: 15px;
    padding: 15px;
    margin-top: 12px;
}

.confidence {
    font-weight: bold;
    color: #35ff83;
}

.search {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 15px;
    border-radius: 12px;
    background: #35ff83;
    color: #041008;
    text-decoration: none;
    font-weight: bold;
}

.empty {
    text-align: center;
    padding: 30px;
    color: #82ad91;
}

.connection {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    margin-top: 15px;
    padding: 8px 14px;
    border-radius: 20px;
    background: rgba(53,255,131,0.08);
    border: 1px solid rgba(53,255,131,0.15);
    color: #9ee8b8;
    font-size: 13px;
}

.dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #35ff83;
    box-shadow: 0 0 10px #35ff83;
}

.gps-status {
    margin-top: 15px;
    padding: 12px 15px;
    border-radius: 14px;
    background: rgba(53,255,131,0.06);
    border: 1px solid rgba(53,255,131,0.15);
    color: #9ee8b8;
    font-size: 14px;
}

.scan-notification {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translate(-50%, -150%);
    width: min(92%, 420px);
    background: rgba(3,12,7,0.98);
    border: 1px solid rgba(53,255,131,0.35);
    border-radius: 20px;
    padding: 16px;
    display: flex;
    align-items: center;
    gap: 14px;
    z-index: 9999;
    box-shadow: 0 12px 40px rgba(0,0,0,0.5);
    cursor: pointer;
    opacity: 0;
    transition: 0.35s ease;
}

.scan-notification.show {
    transform: translate(-50%, 0);
    opacity: 1;
}

.notification-logo {
    width: 50px;
    height: 50px;
    min-width: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 14px;
    background: linear-gradient(135deg, #35ff83, #0b5d31);
    color: #041008;
    font-size: 20px;
    font-weight: 900;
    box-shadow: 0 0 20px rgba(53,255,131,0.25);
}

.notification-text {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.notification-title {
    color: #35ff83;
    font-size: 16px;
    font-weight: bold;
}

.notification-message {
    color: #a8d9b8;
    font-size: 13px;
}

.notification-close {
    margin-left: auto;
    color: #82ad91;
    font-size: 20px;
    padding: 5px;
}

@media (max-width: 650px) {

    nav {
        height: auto;
        min-height: 78px;
        flex-direction: column;
        gap: 10px;
        padding: 10px 15px;
    }

    .logo {
        width: 100%;
        justify-content: flex-start;
    }

    .nav-links {
        width: 100%;
        justify-content: space-between;
        gap: 8px;
    }

    .nav-links a {
        font-size: 11px;
    }

    .page {
        padding: 30px 15px;
    }

    .hero {
        padding: 45px 5px;
    }
}

</style>

</head>

<body>

<div
    id="scanNotification"
    class="scan-notification"
    onclick="openScanResults()">

    <div class="notification-logo">
        FX
    </div>

    <div class="notification-text">

        <div class="notification-title">
            Snow AI is done scanning
        </div>

        <div class="notification-message">
            Tap to view results
        </div>

    </div>

    <div class="notification-close">
        ×
    </div>

</div>

<nav>

<div class="logo">

<div class="logo-mark">
FX
</div>

<span class="logo-name">
FORCE X
</span>

</div>

<div class="nav-links">

<a href="#" onclick="showPage('home'); return false;">
HOME
</a>

<a href="#" onclick="showPage('detection'); return false;">
📷 DETECTION
</a>

<a href="#" onclick="showPage('reports'); return false;">
📊 REPORTS
</a>

<a href="#" onclick="showPage('about'); return false;">
ℹ️ ABOUT
</a>

</div>

</nav>

<section id="home" class="page active">

<div class="content">

<div class="hero">

<h1>
Force X
</h1>

<p class="subtitle">
Intelligent Detection System
</p>

<div class="connection">
<span class="dot"></span>
Snow AI connection ready
</div>

<div class="card">

<p class="info">
Welcome to Force X — a detection
system powered by Snow AI,
designed to identify objects and
animals using artificial intelligence.
</p>

<button onclick="showPage('detection')">
📷 START SCAN
</button>

</div>

</div>

</div>

</section>

<section id="detection" class="page">

<div class="content">

<h2>
📷 Detection
</h2>

<div class="card">

<p class="info">
Start a five-second Snow AI scan.
</p>

<button
id="startButton"
onclick="startScan()">
📷 START SCAN
</button>

<button
id="stopButton"
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

<img id="preview">

<p
id="scanStatus"
class="status">
🟢 Ready to scan
</p>

<div
id="gpsStatus"
class="gps-status">
📍 GPS: Waiting for location permission
</div>

</div>

</div>

</section>

<section id="reports" class="page">

<div class="content">

<h2>
📊 Reports
</h2>

<div class="card">

<div
id="reportText"
class="info">

<div class="empty">
No detection reports yet.
</div>

</div>

</div>

</div>

</section>

<section id="about" class="page">

<div class="content">

<h2>
ℹ️ About Force X
</h2>

<div class="card">

<p class="info">

<strong>Force X</strong> is a
computer-vision platform powered
by Snow AI.

The system captures an image,
sends it to Snow AI for analysis,
and displays the resulting
detection report.

<br><br>

The project focuses on
identifying animals and objects
while supporting future
conservation and species
recognition research.

<br><br>

<strong>Current target species:</strong>

<br><br>

🦍 <strong>Bonobo — Pan paniscus</strong>

<br><br>

<strong>Classification:</strong>
Great ape, family Hominidae.

<br>

<strong>Range:</strong>
Democratic Republic of the Congo (DRC).

<br>

<strong>Habitat:</strong>
Tropical forests, including primary
and secondary forest.

<br>

<strong>Scientific recognition:</strong>
Bonobos were formally recognised as
a separate species in 1929. Before
this, specimens were sometimes
mistaken for unusually small
chimpanzees.

<br>

<strong>Conservation status:</strong>
Endangered.

<br>

<strong>Main threats:</strong>
Hunting, habitat loss and human
encroachment.

<br><br>

<strong>Why Force X is interested:</strong>

Bonobos are closely related to
chimpanzees and have distinctive
physical and behavioural
characteristics. Snow AI could
eventually learn to distinguish
bonobos from other primates instead
of simply identifying them as
"monkeys."

<br><br>

🦒 <strong>Okapi — Okapia johnstoni</strong>

<br><br>

<strong>Classification:</strong>
Giraffid — family Giraffidae.

<br>

<strong>Closest living relative:</strong>
Giraffe.

<br>

<strong>Range:</strong>
Democratic Republic of the Congo.

<br>

<strong>Habitat:</strong>
Dense tropical rainforest.

<br>

<strong>Scientific recognition:</strong>
The okapi was scientifically
recognised in the early 1900s.
Specimens obtained in 1901 helped
scientists establish it as a
previously undescribed giraffid.

<br>

<strong>Conservation status:</strong>
Endangered.

<br>

<strong>Main threats:</strong>
Hunting, habitat destruction and
human disturbance.

<br>

<strong>Interesting fact:</strong>
Although its body can look similar
to a forest antelope and its legs
have zebra-like stripes, the okapi
is actually the closest living
relative of the giraffe.

<br><br>

<strong>Why Force X is interested:</strong>

The okapi has several distinctive
visual characteristics, including
its body shape, dark coat, striped
legs and giraffid head and neck.
These features could help Snow AI
learn to recognise the species.

<br><br>

🐒 <strong>Likweli — Colobus congoensis</strong>

<br><br>

<strong>Common name:</strong>
Likweli.

<br>

<strong>Scientific name:</strong>
Colobus congoensis.

<br>

<strong>Range:</strong>
Lomami National Park and surrounding
forest areas in the Democratic
Republic of the Congo.

<br>

<strong>Habitat:</strong>
High, closed forest canopy,
particularly terra-firme forest.

<br>

<strong>Scientific recognition:</strong>
Researchers first photographed an
unfamiliar monkey in 2008.
Additional observations and
photographs were collected over the
following years.

<br>

<strong>Formal description:</strong>
The species was formally described
in a scientific publication in 2026.

<br>

<strong>Appearance:</strong>
The animal is predominantly black,
with distinctive orange-cream
colouration around the mouth and
nose and a white area beneath the
tail.

<br>

<strong>Conservation:</strong>
Researchers have recommended an
initial Endangered classification
because of its limited known range,
population concerns, hunting pressure
and habitat conversion.

<br>

<strong>Why Force X is interested:</strong>

Likweli is especially interesting
for Snow AI because it demonstrates
the challenge of recognising species
that may be unfamiliar to a general
object-detection model.

Instead of incorrectly identifying
an unfamiliar animal as another
species, a future version of Snow AI
could recognise uncertainty and
respond with something such as:

<br><br>

<strong>
"Possible unidentified or
insufficiently trained species.
Further analysis required."
</strong>

<br><br>

Snow AI can be expanded with
additional training data as the
Force X project develops.

</p>

</div>

</div>

</section>

<script>

let stream = null;
let timer = null;
let scanning = false;
let startTime = 0;
let gpsLocation = null;

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

function getGPSLocation() {

    const gpsStatus =
        document.getElementById("gpsStatus");

    return new Promise(function(resolve) {

        if (!navigator.geolocation) {

            gpsStatus.innerText =
                "❌ GPS: Geolocation is not available.";

            resolve(null);

            return;
        }

        gpsStatus.innerText =
            "📍 GPS: Requesting location...";

        navigator.geolocation.getCurrentPosition(

            function(position) {

                gpsLocation = {

                    latitude:
                        position.coords.latitude,

                    longitude:
                        position.coords.longitude,

                    accuracy:
                        position.coords.accuracy

                };

                gpsStatus.innerText =
                    "🟢 GPS: Location acquired";

                resolve(gpsLocation);
            },

            function(error) {

                gpsLocation = null;

                if (error.code === 1) {

                    gpsStatus.innerText =
                        "⚠️ GPS: Location permission denied.";

                } else if (error.code === 2) {

                    gpsStatus.innerText =
                        "⚠️ GPS: Location unavailable.";

                } else if (error.code === 3) {

                    gpsStatus.innerText =
                        "⚠️ GPS: Location request timed out.";

                } else {

                    gpsStatus.innerText =
                        "⚠️ GPS: Could not get location.";

                }

                resolve(null);
            },

            {
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 0
            }

        );

    });
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

    const locationPromise =
        getGPSLocation();

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
        camera.style.display = "block";

        scanning = true;
        startTime = Date.now();

        let seconds = 5;

        status.innerText =
            "🟢 Scanning... 5 seconds";

        timer = setInterval(function() {

            seconds--;

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

        await locationPromise;

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

    preview.src = imageData;
    preview.style.display = "block";

    stopCamera();

    const duration =
        ((Date.now() - startTime) / 1000)
        .toFixed(1);

    const timestamp =
        new Date().toLocaleString();

    status.innerText =
        "🔗 Connecting to Snow AI...";

    fetch(
        "https://force-x-backend.onrender.com/detect",
        {
            method: "POST",

            headers: {
                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({

                image: imageData,

                timestamp: timestamp,

                duration: duration,
                latitude:
                    gpsLocation
                        ? gpsLocation.latitude
                        : null,

                longitude:
                    gpsLocation
                        ? gpsLocation.longitude
                        : null,

                gps_accuracy:
                    gpsLocation
                        ? gpsLocation.accuracy
                        : null

            })
        }
    )
    .then(response => {

        if (!response.ok) {

            throw new Error(
                "Detection request failed"
            );

        }

        return response.json();

    })
    .then(data => {

        if (!data.success) {

            throw new Error(
                data.error ||
                "Snow AI returned an error."
            );

        }

        data.latitude =
            gpsLocation
                ? gpsLocation.latitude
                : null;

        data.longitude =
            gpsLocation
                ? gpsLocation.longitude
                : null;

        data.gps_accuracy =
            gpsLocation
                ? gpsLocation.accuracy
                : null;

        displayResults(data);

        resetButtons();

    })
    .catch(error => {

        console.log(error);

        status.innerText =
            "❌ Snow AI could not analyze the image.";

        resetButtons();

    });
}

function displayResults(data) {

    const status =
        document.getElementById("scanStatus");

    let html =
        "<div class='report'>" +

        "<strong>❄️ SNOW AI REPORT</strong>" +

        "<br><br>" +

        "🕒 <strong>Timestamp:</strong><br>" +

        (data.timestamp || "Unknown") +

        "<br><br>" +

        "⏱️ <strong>Duration:</strong><br>" +

        (data.duration || "Unknown") +

        " seconds" +

        "<br><br>";

    if (
        data.latitude !== null &&
        data.longitude !== null
    ) {

        html +=

            "📍 <strong>GPS Location:</strong><br>" +

            "Latitude: " +
            data.latitude +

            "<br>" +

            "Longitude: " +
            data.longitude +

            "<br>" +

            "Accuracy: " +
            (data.gps_accuracy
                ? Math.round(data.gps_accuracy)
                : "Unknown") +

            " metres" +

            "<br><br>";

    } else {

        html +=
            "📍 <strong>GPS Location:</strong><br>" +
            "Location unavailable." +
            "<br><br>";

    }

    if (
        !data.objects ||
        data.objects.length === 0
    ) {

        html +=
            "🔍 <strong>Detection:</strong><br>" +
            "No objects detected.";

    } else {

        html +=
            "🔍 <strong>Objects detected:</strong>";

        data.objects.forEach(function(object) {

            const name =
                object.name || "Unknown";

            const confidence =
                object.confidence || "Unknown";

            const description =
                object.description ||
                "No description available.";

            const googleUrl =
                object.google_url ||
                "https://www.google.com/search?q="
                + encodeURIComponent(name);

            html +=

                "<div class='detection'>" +

                "🔹 <strong>" +
                name +
                "</strong><br>" +

                "🎯 Confidence: " +

                "<span class='confidence'>" +
                confidence +
                "</span><br>" +

                "📚 " +
                description +

                "<br>" +

                "<a class='search' " +
                "href='" +
                googleUrl +
                "' " +
                "target='_blank'>" +

                "🔎 Search Google" +

                "</a>" +

                "</div>";

        });

    }

    /*
        Add storage controls to the report.
    */

    html +=

        "<div class='storage-buttons'>" +

        "<button onclick='saveScanImage()'>" +
        "🖼️ SAVE IMAGE" +
        "</button>" +

        "<button onclick='saveScanReport()'>" +
        "📁 SAVE REPORT" +
        "</button>" +

        "<button onclick='saveScanEverything()'>" +
        "💾 SAVE EVERYTHING" +
        "</button>" +

        "<div id='storageMessage' class='storage-message'>" +
        "Reports can be saved to your device." +
        "</div>" +

        "</div>";

    html += "</div>";

    document
        .getElementById("reportText")
        .innerHTML = html;

    /*
        Create a clean text version of the report
        for saving.
    */

    lastScanReport =
        buildReportText(data);

    status.innerText =
        "🟢 Snow AI scan complete";

    showScanCompleteNotification();
}

function buildReportText(data) {

    let report = "";

    report += "FORCE X - SNOW AI REPORT\n";
    report += "================================\n\n";

    report +=
        "Timestamp: " +
        (data.timestamp || "Unknown") +
        "\n\n";

    report +=
        "Duration: " +
        (data.duration || "Unknown") +
        " seconds\n\n";

    if (
        data.latitude !== null &&
        data.longitude !== null
    ) {

        report += "GPS LOCATION\n";
        report += "Latitude: " +
            data.latitude + "\n";

        report += "Longitude: " +
            data.longitude + "\n";

        report += "Accuracy: " +
            (data.gps_accuracy
                ? Math.round(data.gps_accuracy)
                : "Unknown") +
            " metres\n\n";

    } else {

        report +=
            "GPS Location: Unavailable\n\n";
    }

    report += "DETECTION RESULTS\n";
    report += "================================\n\n";

    if (
        !data.objects ||
        data.objects.length === 0
    ) {

        report +=
            "No objects detected.\n";

    } else {

        data.objects.forEach(function(object, index) {

            report +=
                "Detection " +
                (index + 1) +
                "\n";

            report +=
                "Name: " +
                (object.name || "Unknown") +
                "\n";

            report +=
                "Confidence: " +
                (object.confidence || "Unknown") +
                "\n";

            report +=
                "Description: " +
                (object.description ||
                    "No description available.") +
                "\n\n";

        });
    }

    report +=
        "================================\n";

    report +=
        "Generated by Force X / Snow AI\n";

    return report;
}

function downloadFile(content, filename, type) {

    const blob =
        new Blob(
            [content],
            { type: type }
        );

    const url =
        URL.createObjectURL(blob);

    const link =
        document.createElement("a");

    link.href = url;
    link.download = filename;

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    URL.revokeObjectURL(url);
}

function saveScanImage() {

    if (!lastScanImage) {

        alert(
            "No scan image is available to save."
        );

        return;
    }

    const link =
        document.createElement("a");

    link.href = lastScanImage;

    link.download =
        "ForceX_Scan_" +
        Date.now() +
        ".jpg";

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    showStorageMessage(
        "🟢 Scan image saved to your device."
    );
}

function saveScanReport() {

    if (!lastScanReport) {

        alert(
            "No scan report is available to save."
        );

        return;
    }

    downloadFile(
        lastScanReport,
        "ForceX_SnowAI_Report_" +
        Date.now() +
        ".txt",
        "text/plain"
    );

    showStorageMessage(
        "🟢 Snow AI report saved to your device."
    );
}

function saveScanEverything() {

    if (!lastScanImage || !lastScanReport) {

        alert(
            "There is no completed scan to save."
        );

        return;
    }

    saveScanImage();

    setTimeout(function() {

        saveScanReport();

    }, 300);

    showStorageMessage(
        "🟢 Scan image and report saved."
    );
}

function showStorageMessage(message) {

    const element =
        document.getElementById(
            "storageMessage"
        );

    if (element) {

        element.innerText = message;
    }
}

function showScanCompleteNotification() {

    const notification =
        document.getElementById(
            "scanNotification"
        );

    notification.classList.add("show");
}

function openScanResults() {

    const notification =
        document.getElementById(
            "scanNotification"
        );

    notification.classList.remove("show");

    showPage("reports");
}

function stopScan() {

    if (timer) {

        clearInterval(timer);
        timer = null;

    }

    stopCamera();

    scanning = false;

    resetButtons();

    document
        .getElementById("scanStatus")
        .innerText =
        "🟡 Scan stopped";
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
    camera.style.display = "none";
}

function resetButtons() {

    scanning = false;

    const startButton =
        document.getElementById(
            "startButton"
        );

    const stopButton =
        document.getElementById(
            "stopButton"
        );

    startButton.disabled = false;
    stopButton.disabled = true;
}

window.addEventListener(
    "beforeunload",
    function() {

        if (timer) {

            clearInterval(timer);

        }

        stopCamera();

    }
);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return Response(HTML, mimetype="text/html")


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "service": "Force X",
        "snow_ai": "connected"
    })


@app.route("/detect", methods=["POST"])
def detect():

    try:

        data = request.get_json()

        if not data or "image" not in data:

            return jsonify({
                "success": False,
                "error": "No image received."
            }), 400

        image_data = data["image"]

        if "," in image_data:

            image_data = image_data.split(",", 1)[1]

        image_bytes = b64decode(image_data)

        array = np.frombuffer(
            image_bytes,
            dtype=np.uint8
        )

        image = cv2.imdecode(
            array,
            cv2.IMREAD_COLOR
        )

        if image is None:

            return jsonify({
                "success": False,
                "error": "Invalid image."
            }), 400

        results = model(image)

        objects = []

        for result in results:

            for box in result.boxes:

                confidence = float(
                    box.conf[0]
                )

                class_id = int(
                    box.cls[0]
                )

                name = model.names[class_id]

                description = object_info.get(
                    name,
                    "Snow AI detected this object."
                )

                google_url = (
                    "https://www.google.com/search?q="
                    + urllib.parse.quote(name)
                )

                objects.append({

                    "name": name,

                    "confidence":
                        f"{confidence * 100:.1f}%",

                    "description":
                        description,

                    "google_url":
                        google_url
                })

        timestamp = data.get(
            "timestamp",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )

        duration = data.get(
            "duration",
            "Unknown"
        )

        return jsonify({

            "success": True,

            "timestamp":
                timestamp,

            "duration":
                duration,

            "objects":
                objects

        })

    except Exception as error:

        print("Detection error:", error)

        return jsonify({

            "success": False,

            "error":
                "Snow AI could not process the image."

        }), 500


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
)
            
