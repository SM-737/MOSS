import streamlit as st
import os
import pandas as pd
import numpy as np
from data_processor import generate_sync_data

# 1. Page Configuration
st.set_page_config(page_title="MOSS Control Console", layout="wide")

st.title("🎛️ Asynchronous Sensor Sync & Diagnostic Player")
st.caption("MOSS Protocol | EAR99 Commercial Data Processing Framework")

DATA_DIR = "data"
VIDEO_FILE = "test.mp4"

# 2. Automatically check and generate data if it doesn't exist on the server yet
if not os.path.exists(DATA_DIR) or len(os.listdir(DATA_DIR)) == 0:
    if os.path.exists(VIDEO_FILE):
        with st.spinner("Processing asynchronous telemetry layers... Please wait."):
            generate_sync_data(VIDEO_FILE, DATA_DIR)
    else:
        st.error(f"Error: Please upload a short video named '{VIDEO_FILE}' to your GitHub repository.")
        st.stop()

# 3. Master Mission Timeline Control
st.subheader("🎞️ Master Mission Timeline")
current_frame = st.slider("Scrub through asynchronous flight slices", min_value=0, max_value=49, value=0, step=1)

# 4. Multi-Stream Screen Viewports
col1, col2 = st.columns(2)

with col1:
    st.subheader("📺 Standard Frame-Based Feed (RGB)")
    st.caption("Traditional 30 FPS Camera Stream - Blurs under rapid movement")
    rgb_path = os.path.join(DATA_DIR, f"rgb_{current_frame}.jpg")
    if os.path.exists(rgb_path):
        st.image(rgb_path, use_container_width=True)

with col2:
    st.subheader("⚡ Neuromorphic Event-Stream Vector")
    st.caption("Asynchronous Change Accumulator - Sub-millisecond polarity tracking")
    event_path = os.path.join(DATA_DIR, f"event_{current_frame}.jpg")
    if os.path.exists(event_path):
        st.image(event_path, use_container_width=True)

# 5. Synchronized Telemetry Array
st.subheader("📊 Microsecond Diagnostic Telemetry Matrix")
np.random.seed(current_frame) # Locks chart animation to the timeline slider position
chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Structural Vibration (Hz)', 'Lux Illumination Shifting']
)
st.line_chart(chart_data)
