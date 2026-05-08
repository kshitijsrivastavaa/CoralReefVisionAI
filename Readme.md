<div align="center">

# 🌊 CoralSight — AI Coral Reef Health Assessment

**An AI-powered full-stack system for coral reef bleaching detection, damage quantification, and marine ecosystem monitoring using computer vision and deep learning.**

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Netlify-00C7B7?style=for-the-badge)](https://shiny-bunny-ba12ea.netlify.app/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Flask](https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)

</div>

---

## 📽️ Demo Video

> 🎬 **[https://github.com/user-attachments/assets/629f8b71-8537-4b70-a256-738d971ee59c]**

The demo showcases:
- Uploading real underwater coral reef photographs
- Live HSV segmentation overlay rendering over the original image
- Coral damage percentage calculated instantly
- Interactive pie chart showing healthy vs. affected area breakdown
- Multiple reef images tested — ranging from 7.25% to 40.39% affected area

---

## 📸 What It Looks Like

| Original Reef Image | AI Segmentation Overlay |
|---|---|
| Raw underwater coral photograph | Pink/red overlay highlighting bleached & damaged coral regions |

**Output includes:**
- Side-by-side original vs. segmented view
- `Affected Area: X.XX%` — precise damage percentage
- Interactive damage distribution pie chart with hover tooltips

---

## 🌍 Why This Exists

Coral reefs cover less than 1% of the ocean floor but support over 25% of all marine species. They are under severe threat from:

- 🌡️ Rising ocean temperatures causing mass bleaching events
- 🧪 Ocean acidification dissolving coral structures
- 🏭 Marine pollution and runoff
- 🦠 Coral disease outbreaks
- 🌿 Algae overgrowth smothering healthy reefs

Traditional monitoring relies on **manual diver surveys** — slow, expensive, and impossible to scale. CoralSight automates reef health assessment from a single photograph, making large-scale monitoring accessible to researchers, conservationists, and institutions worldwide.

---

## ✅ Working Features

### 🔬 Computer Vision Segmentation Pipeline (Live & Functional)
- Upload any underwater coral reef image via the web interface
- Image is sent to the Flask backend and processed through an **HSV color segmentation pipeline**
- Bleached/stressed coral regions (high brightness, low saturation) are detected automatically
- **Morphological filtering** cleans noise and sharpens the mask
- A **pink/red overlay** is rendered on the original image highlighting damaged zones
- Results returned to the frontend and displayed in real-time

### 📊 Coral Damage Quantification (Live & Functional)
- Calculates the **exact percentage of affected reef area** per image
- Results displayed as `Affected Area: X.XX%`
- Tested across multiple real coral images with varying damage levels (7–40% range seen in demo)

### 🥧 Interactive Damage Distribution Chart (Live & Functional)
- Pie chart rendering healthy vs. affected coral proportions
- **Hover tooltips** show exact values (e.g., `Healthy: 92.75`, `Affected: 7.25`)
- Built with a charting library for smooth interactive UX

### 🖼️ Side-by-Side Comparison View (Live & Functional)
- Original Image displayed on the left
- AI Segmentation Overlay displayed on the right
- Enables immediate visual verification of what the algorithm detected

### 🤖 U-Net Deep Learning Architecture (Implemented, Training-Ready)
- Full **encoder–decoder U-Net CNN** implemented in TensorFlow/Keras
- Designed for 4-class pixel-wise segmentation:
  - Healthy coral
  - Bleached coral
  - Diseased coral
  - Algae-covered coral
- Input: `224 × 224 × 3` RGB images
- Output: Pixel-wise segmentation map
- Architecture complete — awaiting labeled dataset for training run

---

## 🏗️ System Architecture

```
User uploads reef image via browser
            ↓
    React (Vite) Frontend
            ↓
    Flask REST API  (server.py)
            ↓
    Image Preprocessing (OpenCV)
     → RGB to HSV conversion
     → Low saturation + high brightness detection
     → Morphological filtering & noise removal
            ↓
    Segmentation Mask Generation
            ↓
    Damage Percentage Calculation
            ↓
    Overlay Visualization (OpenCV)
            ↓
    JSON response → Frontend
            ↓
    Side-by-side display + Pie chart render
```

---

## 🛠️ Tech Stack

### Frontend
| Tech | Purpose |
|---|---|
| React + Vite | UI framework and fast dev server |
| JavaScript ES6+ | Application logic |
| Tailwind CSS | Styling |
| Chart.js / Recharts | Interactive pie chart with hover tooltips |
| HTML5 / CSS3 | Structure and layout |

### Backend
| Tech | Purpose |
|---|---|
| Python 3.x | Core runtime |
| Flask | REST API server |
| Flask-CORS | Cross-origin request handling |

### Computer Vision
| Tech | Purpose |
|---|---|
| OpenCV | Image processing, color space conversion, overlay rendering |
| NumPy | Array operations, mask manipulation |

### Deep Learning
| Tech | Purpose |
|---|---|
| TensorFlow | Deep learning framework |
| Keras | U-Net model definition and training API |

---

## 🤖 Models In Detail

### Model 1 — HSV Baseline Segmentation (Active)

The currently deployed model uses classical computer vision. It's fast, offline, requires no GPU, and works immediately on any coral image.

**How it works:**
1. Convert uploaded image from **RGB → HSV** color space
2. Detect pixels with **low saturation + high brightness** — the optical signature of bleached coral
3. Apply **morphological operations** (dilation, erosion) to remove noise and fill gaps
4. Generate a **binary segmentation mask** over affected regions
5. Calculate the **percentage of masked pixels** relative to total image area
6. Render a **colored overlay** on the original image and return to frontend

**Output:** Binary mask + percentage damage + overlay image

---

### Model 2 — U-Net CNN Semantic Segmentation (Architecture Complete)

A full **U-Net convolutional neural network** is implemented and ready for training.

**Architecture:** Encoder–Decoder with skip connections

```
Input (224×224×3)
    → Encoder (contracting path): Conv → MaxPool × 4
    → Bottleneck
    → Decoder (expanding path): UpSample → Conv × 4  [+ skip connections]
    → Output: Pixel-wise segmentation map
```

**Target classes:**
- 🟢 Healthy coral
- 🔴 Bleached coral  
- 🟡 Diseased coral
- 🟤 Algae-covered coral

**Why U-Net:** Widely used in biomedical and environmental segmentation tasks requiring precise object boundaries. Skip connections preserve fine-grained spatial details lost during downsampling — critical for accurate reef boundary detection.

---

## 📂 Project Structure

```
CoralReefVisionAI/
│
├── coralsight-main/
│   └── backend/
│       └── ai/
│           └── segmentation/
│               ├── service.py       # Main segmentation service
│               ├── unet.py          # U-Net CNN architecture (TF/Keras)
│               └── segment.py       # HSV segmentation algorithm
│
├── src/
│   ├── App.jsx                      # Main React component
│   ├── main.jsx                     # React entry point
│   └── index.css                    # Global styles
│
├── models/                          # Model weights directory
├── scripts/                         # Utility scripts
│
├── server.py                        # Flask API server
├── index.html                       # Vite HTML entry
├── package.json                     # Node dependencies
├── vite.config.js                   # Vite build config
├── tailwind.config.js               # Tailwind CSS config
├── postcss.config.js                # PostCSS config
└── Readme.md
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- Python 3.8+
- pip

### 1. Clone the repository
```bash
git clone https://github.com/kshitijsrivastavaa/CoralReefVisionAI.git
cd CoralReefVisionAI
```

### 2. Install frontend dependencies
```bash
npm install
```

### 3. Install backend dependencies
```bash
pip install flask flask-cors opencv-python numpy tensorflow
```

### 4. Start the Flask backend
```bash
python server.py
```

### 5. Start the React frontend
```bash
npm run dev
```

### 6. Open in browser
```
http://localhost:5173
```

---

## 🌐 Deployment

**Frontend** is deployed on Netlify:
🔗 [https://shiny-bunny-ba12ea.netlify.app/](https://shiny-bunny-ba12ea.netlify.app/)

> ⚠️ The live Netlify link runs the frontend only. The Flask backend (image processing) must be run locally for full functionality.

**To build for production:**
```bash
npm run build
```
Output goes to the `dist/` directory.

---

## 📊 Sample Results

| Image | Affected Area | Interpretation |
|---|---|---|
| `coral 3img.jpeg` | **40.39%** | Significant bleaching — moderate-high stress |
| `coral2pic.jpeg` | **21.25%** | Early-stage bleaching detected |
| `coral img 4.jpeg` | **7.25%** | Mostly healthy reef, minor stress zones |

---

## 📚 Dataset Sources

Future U-Net training will use publicly available labeled coral datasets:

- [CoralNet](https://coralnet.ucsd.edu/) — Point annotation platform for benthic imagery
- [ReefBase](http://www.reefbase.org/) — Global coral reef monitoring database
- [NOAA Coral Reef Watch](https://coralreefwatch.noaa.gov/) — Satellite-derived reef monitoring data

---

## ⚠️ Current Limitations

- HSV segmentation may flag bright non-coral objects (e.g., light reflections, sandy patches) as bleached
- U-Net CNN training pipeline not yet connected — labeled dataset required
- Backend must be run locally; no cloud-hosted API currently

---

## 🔮 Roadmap

- [ ] Train U-Net on labeled coral datasets (CoralNet / NOAA)
- [ ] Replace HSV baseline with trained CNN inference
- [ ] Multi-class output: healthy / bleached / diseased / algae
- [ ] Temporal monitoring — compare reef health across dates
- [ ] Batch image processing for large-scale surveys
- [ ] Exportable PDF damage reports
- [ ] Cloud API deployment for remote access
- [ ] Mobile-responsive UI improvements

---

## 🤝 Contributing

Contributions are welcome — especially around model training and dataset integration.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📜 License

This project is built for **educational and academic research purposes**.

For questions or collaborations: [kshitij.srivastava16@gmail.com](mailto:kshitij.srivastava16@gmail.com)

---

<div align="center">

**Built to protect the reefs. 🪸**

</div>
