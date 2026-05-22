# MOSS: Multi-Operator Spatial Sync & Asynchronous Sensor Player

MOSS is a next-generation, pure-software flight log analytics platform and live mission dashboard designed for advanced aerospace and autonomous system operators. 

Traditional analytics platforms are built entirely around standard frame-based data (like slow 30 FPS videos and 1Hz GPS logs). MOSS bridges the gap by providing an out-of-the-box data synchronization and playback dashboard optimized for high-speed, sub-millisecond data tracking and next-generation asynchronous sensors (such as Neuromorphic/Event-Based cameras).

---

## 🚀 Key Features

* **Asynchronous Multi-Stream Sync:** Instantly aligns traditional frame-based RGB video with high-frequency asynchronous telemetry vectors.
* **Neuromorphic Data Emulation:** Translates continuous change data into clean, microsecond-resolution visual tracking outputs.
* **Unified Mission Timeline:** Allows field operators to scrub through flights with frame-by-frame precision.
* **Deterministic Telemetry Tracking:** Dynamically locks sensor metrics (vibration signatures and lux illumination shifts) directly to the timeline.

---

## 🛠️ Tech Stack & Architecture

* **Frontend Dashboard:** Streamlit (Python-driven web application interface)
* **Computer Vision Backend:** OpenCV & NumPy (Asynchronous frame processing and change extraction)
* **Data Visualization:** Pandas & Streamlit Metrics (Synchronized microsecond telemetry data plotting)
* **Regulatory Compliance:** Designed entirely under **EAR99** classification (100% ITAR-Free / Zero Hardware Dependencies)

---

## 📦 Repository Structure

```text
├── app.py                  # Streamlit frontend UI application and state machine
├── data_processor.py       # Core backend vision and data synchronization engine
├── requirements.txt        # Production environment dependency declaration
├── test.mp4                # Baseline mission video payload file
└── README.md               # Project documentation and system architecture overview
```

---

## 💻 Local Installation & Deployment

If you want to run this application locally on your workstation instead of via the live cloud deployment, execute the following commands in your terminal:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd moss
   ```

2. **Establish and activate an isolated virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required system dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute the backend data processor:**
   ```bash
   python data_processor.py
   ```

5. **Launch the web dashboard:**
   ```bash
   streamlit run app.py
   ```

---

## 🛡️ Strategic Dual-Use Pivot Framework

* **Commercial Application:** Deployed by infrastructure, pipeline, and wind-turbine autonomous drone inspection companies to analyze high-vibration flights and eliminate data lag.
* **Future Defense Pivot:** Integrates directly with Counter-UAS (C-UAS) arrays and high-speed target acquisition hardware to handle real-time, low-latency tracking in GPS-denied environments without modifying the underlying software architecture.
