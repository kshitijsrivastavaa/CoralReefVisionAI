# 🌊 CoralSight — AI Coral Reef Health Assessment

CoralSight is an **AI-assisted coral reef health assessment system** that analyzes underwater reef images to estimate bleaching or stress levels using computer vision segmentation techniques and a planned deep learning segmentation architecture.

The system combines **OpenCV-based image processing with a planned U-Net CNN deep learning model** to identify damaged coral regions and compute the **percentage of affected coral area**.

The project integrates:

- React frontend
- Flask backend API
- Computer vision processing pipeline
- Deep learning architecture for semantic segmentation

---

# 🚀 Live Demo

Frontend deployed using Netlify:

🔗 https://shiny-bunny-ba12ea.netlify.app/

---

# 📌 Project Overview

Coral reefs are among the most biologically diverse ecosystems on Earth, but they are increasingly threatened by environmental stressors such as rising sea temperatures, pollution, and ocean acidification.

One of the most visible impacts is **coral bleaching**, where corals lose their symbiotic algae and turn white.

Manual reef monitoring is **time-consuming, costly, and difficult to scale**.

CoralSight aims to support marine researchers by providing an **automated AI-assisted coral health analysis system** capable of detecting damaged reef regions from underwater imagery.

---

# 🎯 Core Problem Addressed

Coral reefs face several environmental threats including:

- Rising ocean temperatures  
- Marine pollution  
- Ocean acidification  
- Coral disease outbreaks  
- Algae overgrowth  

Traditional reef monitoring requires **manual inspection by divers or marine researchers**, which limits the scale and frequency of monitoring.

CoralSight automates part of this process by performing **image-based coral health assessment using computer vision and deep learning techniques**.

---

# 🏗 System Architecture

```
User Upload Image
        ↓
React Frontend Interface
        ↓
Flask Backend API
        ↓
Image Preprocessing (OpenCV)
        ↓
Segmentation Algorithm
        ↓
Mask Generation
        ↓
Damage Percentage Calculation
        ↓
Overlay Visualization
        ↓
Results Displayed on Frontend
```

---

# 🛠 Technologies Used

## Frontend

- React (Vite)
- JavaScript (ES6+)
- HTML5
- CSS3
- Tailwind CSS

Purpose:

- User interface
- Image upload
- Visualization of segmentation overlay
- Display of coral damage statistics

---

## Backend

- Python 3.x
- Flask
- Flask-CORS

Purpose:

- API for image processing
- Execution of segmentation algorithms
- Returning analysis results to frontend

---

## Computer Vision Libraries

- OpenCV  
- NumPy  

Purpose:

- Image preprocessing  
- Color space transformation  
- Segmentation mask generation  
- Coral damage area estimation  
- Overlay visualization  

---

## Deep Learning Framework (Architecture Included)

- TensorFlow  
- Keras  

Purpose:

Implementation of **U-Net Convolutional Neural Network architecture** for future semantic segmentation training.

---

# 🤖 Models and Algorithms

## 1️⃣ Current Working Model — Baseline Segmentation

The current system uses **HSV color segmentation combined with morphological filtering**.

### Method

The algorithm detects high brightness and low saturation regions that may correspond to coral bleaching.

### Process

1. Convert RGB image to HSV color space  
2. Detect low saturation and high brightness pixels  
3. Apply morphological filtering to remove noise  
4. Generate segmentation mask  
5. Calculate percentage of affected coral area  

### Libraries Used

- OpenCV  
- NumPy  

### Output

- Binary segmentation mask  
- Coral damage overlay visualization  
- Estimated bleaching percentage  

---

## 2️⃣ Deep Learning Model — U-Net Architecture

Future versions of CoralSight will integrate a **U-Net Convolutional Neural Network** for semantic segmentation.

### Framework

TensorFlow / Keras

### Architecture Type

Encoder–Decoder CNN with skip connections.

### Input

224 × 224 × 3 RGB image

### Output

Pixel-wise segmentation map.

### Target Classes

- Healthy coral  
- Bleached coral  
- Diseased coral  
- Algae-covered coral  

### Why U-Net

U-Net is widely used for segmentation tasks requiring precise object boundaries such as:

- medical imaging  
- satellite imagery  
- environmental monitoring  

---

# 🔄 Image Processing Pipeline

```
Image Upload
     ↓
Image Preprocessing
     ↓
Color Segmentation
     ↓
Noise Removal
     ↓
Mask Generation
     ↓
Affected Area Calculation
     ↓
Overlay Visualization
     ↓
Result Display
```

---

# ⭐ Key Features

- Automated coral reef image analysis  
- Coral bleaching region detection  
- Coral damage percentage estimation  
- Overlay visualization of affected areas  
- Offline image processing capability  
- Interactive web interface  
- Extendable deep learning segmentation architecture  

---

# 📂 Project Folder Structure

```
coralsight/
│
├── backend/
│   ├── ai/
│   │   └── segmentation/
│   │       ├── service.py
│   │       ├── unet.py
│   │       └── segment.py
│   │
│   ├── uploads/
│   └── results/
│
├── src/
│   ├── App.jsx
│   ├── main.jsx
│   └── index.css
│
├── public/
├── server.py
├── package.json
├── vite.config.js
└── README.md
```

---

# 📊 Dataset Sources

Future model training will use publicly available coral reef datasets such as:

- CoralNet dataset  
- ReefBase coral image repository  
- NOAA coral reef monitoring datasets  

These datasets contain labeled coral reef images used in marine ecosystem research.

---

# ⚠ Limitations

Current limitations include:

- HSV segmentation may detect bright objects unrelated to coral bleaching  
- CNN training pipeline not yet integrated  
- Dataset labeling required for accurate model training  

---

# 🔮 Future Improvements

Planned improvements include:

- Training U-Net on coral reef datasets  
- Multi-class coral health classification  
- Temporal coral monitoring  
- Historical reef health analysis  
- Exportable coral damage reports  
- Batch reef image processing  
- Cloud deployment for large-scale reef monitoring  

---

# 💻 Installation

Clone repository

```bash
git clone https://github.com/yourusername/coralsight.git
cd coralsight
```

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

Open browser

```
http://localhost:5173
```

---

# 🚀 Build for Production

```
npm run build
```

Production files will be generated inside the **dist** directory.

---

# 🌐 Deployment

Frontend deployed using **Netlify**

Live demo:

https://shiny-bunny-ba12ea.netlify.app/

Backend API runs locally using **Flask**.

---

# 🎓 Intended Use

This project is designed for:

- educational purposes  
- research demonstrations  
- coral reef monitoring experiments  

It is **not a certified scientific diagnostic tool**.

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve CoralSight:

1. Fork the repository  
2. Create a feature branch  
3. Submit a pull request  

---

# 📜 License

This project is intended for **educational and academic research purposes**. 
kshitij.srivastava16@gmail.com
