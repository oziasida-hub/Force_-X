from flask import Flask, request, jsonify, Response,send_file
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

<link
    rel="icon"
    type="image/png"
    href="/static/file_0000000074d482118627681d3d6c1bfd.png">

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

    border-bottom:
        1px solid rgba(48,255,125,0.25);

    box-shadow:
        0 4px 25px rgba(0,0,0,0.35);

    position: sticky;
    top: 0;
    z-index: 10;
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.force-x-logo {
    width: 75px;
    height: 58px;
    object-fit: contain;
    object-position: center;
    display: block;
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

    border:
        1px solid rgba(53,255,131,0.20);

    border-radius: 24px;

    padding: 25px;

    margin-top: 25px;

    box-shadow:
        0 10px 35px rgba(0,0,0,0.25);
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

    .force-x-logo {
        width: 70px;
        height: 52px;
    }

    .logo-name {
        font-size: 17px;
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

<nav>

<div class="logo">

<img
    src="/static/b7077110b14418925995ebc6e641fc8c.png"
    alt="Force X Logo"
    class="force-x-logo">

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
sends it to the Snow AI and
get's a detailed report of the
scan.Our system mainly focuses
on discovering new species and
conserving rare ones.Our main species 
include:


🦍 1. Bonobo — Pan paniscus
Classification: Great ape, family Hominidae
Range: Democratic Republic of the Congo (DRC)
Habitat: Primarily tropical forests, including primary/old secondary forest, with some use of swamp and more open/secondary habitats. Research at Wamba found that bonobos strongly preferred forested areas and used primary/old secondary forest for most ranging and sleeping. �

What makes it interesting?
Bonobos are extremely social great apes. Their communities have a fission–fusion structure: a larger community can split into smaller groups while foraging and come together again. Their diet is dominated by plant foods, especially fruit, but includes leaves, stems, roots, flowers, mushrooms and some invertebrates. �
Animal Diversity Web +1
They're also particularly important to evolutionary research because bonobos and chimpanzees are our closest living relatives.

Scientific discovery
Bonobos were formally recognised as a separate species, Pan paniscus, in 1929. Earlier specimens had been mistaken for unusually small chimpanzees. �
Smithsonian Magazine

Conservation
Endangered. Major threats include hunting, habitat degradation and human encroachment. Their population is difficult to estimate accurately because much of their range is remote and heavily forested; conservation organisations currently describe the wild population as roughly 10,000–20,000, while emphasising that it is fragmented and declining. �
BONOBO
For Force X: Bonobo detection could be particularly useful because distinguishing bonobos from other primates requires more than simply detecting "monkey." A future Snow AI model could learn characteristics such as body shape, facial appearance and behaviour.


🦒 2. Okapi — Okapia johnstoni
Classification: Giraffid
Closest living relative: Giraffe
Range: Democratic Republic of the Congo
Habitat: Tropical rainforest, particularly the forests of central and northeastern DRC. �


The okapi is one of the coolest targets for Force X because it can look almost like a combination of different animals: its body resembles a forest antelope, while its legs have striking zebra-like striping. Despite its appearance, it is actually a member of the giraffe family. �


Diet
Okapis are primarily browsers. They feed on vegetation, including leaves and other forest plants. Their long tongue helps them pull foliage from branches. �
Smith College Science

Scientific discovery
This one has an interesting history.
Local peoples already knew the animal, but European scientists initially had difficulty determining what it was. Sir Harry Johnston obtained pieces of skin in the late 1890s, and further specimens—including a complete skin and skulls—were obtained in 1901. Scientists then recognised it as a previously undescribed giraffid and established the genus Okapia. �


So for your website, I'd phrase this as:
Scientifically recognised: 1901
rather than saying simply "discovered in 1901," because people living in its range already knew the animal.
Conservation
The okapi is Endangered. It is endemic to the DRC and depends heavily on forest habitat. Conservation efforts therefore focus strongly on protecting its forest environment and reducing pressures such as hunting and habitat disturbance. �

For Force X: Okapi would be an excellent target species because its unusual appearance gives a computer-vision system several potentially useful features to learn—body proportions, brown coat, distinctive striped legs and giraffid head/neck structure.

🐒 3. Likweli — Colobus congoensis
This is the newest and most interesting one for your project.
Scientific name
Colobus congoensis
Common name: Likweli
It is a newly described African colobus monkey from the Democratic Republic of the Congo. �

Where does it live?
Researchers have found it in Lomami National Park and surrounding areas in the DRC.
It appears to be strongly associated with high, closed forest canopy, including terra-firme forest. The published study estimated its known range at approximately 1,700 km². �

Appearance
This is where Likweli becomes particularly useful for Snow AI.
It is predominantly black, with distinctive orange-cream coloration around the mouth and nose. It also has a white patch beneath the tail. �


Researchers used several types of evidence to distinguish it from related colobus monkeys:
physical characteristics
skull and dental characteristics
genetics
vocalisations
geographical distribution
The researchers concluded that it is a distinct species. �


How recently was it discovered?
This needs a little nuance.
Researchers photographed an unfamiliar monkey in 2008. Additional observations and much better photographs followed, particularly from 2018 onward. Researchers eventually accumulated enough evidence to formally establish it as a new species.
The scientific description was published on 15 July 2026. �


So the Force X website could say:
Formally described as a new species: 15 July 2026
That's much more accurate than simply saying "discovered in 2026."
Population observations
Between 2018 and 2022, researchers recorded 114 observations over approximately 1,700 km². The monkeys were usually observed in small groups averaging about 6 individuals. �

Conservation status
This is another important distinction.
The scientists recommend a preliminary classification of Endangered (EN) because of the species' small known range and population, combined with hunting pressure and habitat conversion. �
PubMed Central (PMC)

        Why Likweli matters to Snow AI
This is actually a great example of why your "unrecognised species" idea makes sense.
A camera system could encounter an animal that doesn't match the species it has been trained on. Instead of confidently calling it something else, Snow AI could eventually respond:

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

    } catch(error) {

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

                duration: duration

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
                "' " +
                "target='_blank'>" +

                "🔎 Search Google" +

                "</a>" +

                "</div>";

        });

    }

    html += "</div>";

    document
        .getElementById("reportText")
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
    camera.style.display = "none";

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
"""

@app.route("/")
def home():

    return Response(
        HTML,
        mimetype="text/html"
    )

@app.route("/detect", methods=["POST"])
def detect():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "No data received"
            }), 400

        image_data = data["image"]

        timestamp = data.get(
            "timestamp",
            datetime.now().isoformat()
        )

        duration = data.get(
            "duration",
            "0"
        )

        image_bytes = b64decode(
            image_data.split(",", 1)[1]
        )

        frame = cv2.imdecode(
            np.frombuffer(
                image_bytes,
                np.uint8
            ),
            cv2.IMREAD_COLOR
        )

        if frame is None:

            return jsonify({
                "success": False,
                "error": "Invalid image"
            }), 400

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
                        object_name + " information"
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
    
    @app.route("/logo")
def logo():
    return send_file("b7077110b14418925995ebc6e641fc8c.png")

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=int(
            os.environ.get(
                "PORT",
                5000
            )
        )

)
