
from flask import Flask, request, jsonify, Response
from ultralytics import YOLO
from datetime import datetime
from base64 import b64decode
import numpy as np
import cv2
import threading
import urllib.parse
import time

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

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    font-family: Arial, sans-serif;
    background: #07111f;
    color: white;
}

body {
    background:
    radial-gradient(
        circle at top,
        #174a7a 0%,
        #07111f 55%
    );
}

nav {
    width: 100%;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(7,17,31,0.92);
    border-bottom: 1px solid rgba(255,255,255,0.12);
    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    font-size: 22px;
    font-weight: bold;
}

.nav-links {
    display: flex;
    gap: 18px;
}

.nav-links a {
    color: #b8d9ff;
    text-decoration: none;
    font-size: 14px;
}

.nav-links a:hover {
    color: white;
}

.page {
    width: 100%;
    min-height: calc(100vh - 70px);
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
    padding: 70px 10px;
}

.logo-large {
    font-size: 75px;
}

h1 {
    font-size: clamp(42px, 10vw, 70px);
    margin: 10px 0;
}

.subtitle {
    color: #b8d9ff;
    font-size: 18px;
}

.card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 24px;
    padding: 25px;
    margin-top: 25px;
}

button {
    border: none;
    border-radius: 15px;
    padding: 16px 25px;
    font-size: 17px;
    font-weight: bold;
    cursor: pointer;
    background: white;
    color: #12365c;
    margin: 5px;
}

button:hover {
    transform: scale(1.02);
}

button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

h2 {
    font-size: 30px;
}

.info {
    color: #b8d9ff;
    line-height: 1.7;
}

#camera {
    width: 100%;
    max-height: 500px;
    object-fit: cover;
    display: none;
    margin-top: 20px;
    border-radius: 20px;
    background: black;
}

#preview {
    width: 100%;
    display: none;
    margin-top: 20px;
    border-radius: 20px;
}

.status {
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
}

.report {
    background: rgba(0,0,0,0.25);
    border-radius: 18px;
    padding: 20px;
    margin-top: 15px;
    line-height: 1.7;
}

.detection {
    background: rgba(255,255,255,0.07);
    border-radius: 15px;
    padding: 15px;
    margin-top: 12px;
}

.confidence {
    font-weight: bold;
    color: #8ab4f8;
}

.search {
    display: inline-block;
    margin-top: 10px;
    padding: 10px 15px;
    border-radius: 12px;
    background: #8ab4f8;
    color: #111;
    text-decoration: none;
    font-weight: bold;
}

@media (max-width: 650px) {

    nav {
        flex-direction: column;
        gap: 12px;
    }

    .nav-links {
        width: 100%;
        justify-content: space-between;
        gap: 8px;
    }

    .nav-links a {
        font-size: 12px;
    }

    .page {
        padding: 30px 15px;
    }

}

</style>

</head>

<body>

<nav>

<div class="logo">
Force X
</div>

<div class="nav-links">

<a href="#" onclick="showPage('home')">
HOME
</a>

<a href="#" onclick="showPage('detection')">
📷 DETECTION
</a>

<a href="#" onclick="showPage('reports')">
📊 REPORTS
</a>

<a href="#" onclick="showPage('about')">
ℹ️ ABOUT
</a>

</div>

</nav>

<section id="home" class="page active">

<div class="content">

<div class="hero">

<div class="logo-large">
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

<button id="startButton"
        onclick="startScan()">
📷 START SCAN
</button>

<button id="stopButton"
        onclick="stopScan()"
        disabled>
⛔ STOP
</button>

<video id="camera"
       autoplay
       playsinline>
</video>

<canvas id="canvas"
        style="display:none;">
</canvas>

<img id="preview">

<p id="scanStatus"
   class="status">
🟢 Ready to scan
</p>

</div>

</div>

</section>

<section id="reports" class="page">

<div class="content">

<h2>
📊 Reports
</h2>

<div class="card">

<div id="reportText"
     class="info">
No detection reports yet.
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
Force X is a computer-vision
website powered by Snow AI.

The system captures an image,
sends it to the Snow AI YOLO
detection model and returns
detected objects, confidence
levels and descriptions.
</p>

</div>

</div>

</section>

<script>

let stream = null;
let timer = null;
let scanning = false;
let startTime = 0;

function showPage(page) {

    document
    .querySelectorAll(".page")
    .forEach(function(section) {
        section.classList.remove("active");
    });

    document
    .getElementById(page)
    .classList.add("active");

    window.scrollTo(0,0);
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

                captureImage();
            }

        }, 1000);

    }

    catch(error) {

        status.innerText =
            "❌ Camera could not be started.";

        resetButtons();

        console.log(error);
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
        "🧠 Snow AI is analyzing...";

    fetch("/detect", {

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

    })

    .then(response => {

        if (!response.ok) {

            throw new Error(
                "Detection request failed"
            );
        }

        return response.json();

    })

    .then(data => {

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

        data.timestamp +

        "<br><br>" +

        "⏱️ <strong>Duration:</strong><br>" +

        data.duration +

        " seconds" +

        "<br><br>";

    if (data.objects.length === 0) {

        html +=
            "🔍 <strong>Detection:</strong><br>" +
            "No objects detected.";

    } else {

        html +=
            "🔍 <strong>Objects detected:</strong>";

        data.objects.forEach(function(object) {

            html +=

                "<div class='detection'>" +

                "🔹 <strong>" +
                object.name +
                "</strong><br>" +

                "🎯 Confidence: " +

                "<span class='confidence'>" +
                object.confidence +
                "</span><br>" +

                "📚 " +
                object.description +

                "<br>" +

                "<a class='search' " +
                "href='" +
                object.google_url +
                "' target='_blank'>" +

                "🔎 Search Google" +

                "</a>" +

                "</div>";
        });
    }

    html += "</div>";

    document.getElementById("reportText")
        .innerHTML = html;

    status.innerText =
        "🟢 Snow AI scan complete";

    showPage("reports");
}

function stopScan() {

    if (timer) {

        clearInterval(timer);

        timer = null;
    }

    stopCamera();

    resetButtons();

    document.getElementById("scanStatus")
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
    camera.style.display = "none";

    scanning = false;
}

function resetButtons() {

    document.getElementById("startButton")
        .disabled = false;

    document.getElementById("stopButton")
        .disabled = true;

    scanning = false;
}

</script>

</body>
</html>
"""

app = Flask(__name__)

@app.route("/detect", methods=["POST"])
def detect():

    try:

        data = request.get_json()

        image_data = data["image"]
        timestamp = data["timestamp"]
        duration = data["duration"]

        image_bytes = b64decode(
            image_data.split(",")[1]
        )

        frame = cv2.imdecode(
            np.frombuffer(
                image_bytes,
                np.uint8
            ),
            cv2.IMREAD_COLOR
        )

        results = model(frame)

        objects = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                confidence = float(
                    box.conf[0]
                )

                object_name = model.names[
                    class_id
                ].lower()

                description = object_info.get(
                    object_name,
                    "Snow AI detected this object, but a built-in description is not available yet."
                )

                google_url = (
                    "https://www.google.com/search?q="
                    + urllib.parse.quote(
                        object_name +
                        " information"
                    )
                )

                objects.append({

                    "name":
                        object_name.title(),

                    "confidence":
                        f"{confidence:.1%}",

                    "description":
                        description,

                    "google_url":
                        google_url
                })

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

        return jsonify({

            "success": False,

            "error":
                str(error)

        }), 500


@app.route("/")
def home():

    return Response(
        HTML,
        mimetype="text/html"
    )
if __name__ == "__main__":
    import os

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
