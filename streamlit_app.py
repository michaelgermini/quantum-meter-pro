#!/usr/bin/env python3
"""
QuantumMeter Pro - Streamlit Version
Advanced Laboratory Software for Quantum Measurement Devices
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="QuantumMeter Pro",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .status-connected {
        color: #28a745;
        font-weight: bold;
    }
    .status-disconnected {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'measurement_data' not in st.session_state:
    st.session_state.measurement_data = {
        'timestamp': [],
        'current': [],
        'voltage': [],
        'resistance': [],
        'temperature': []
    }
if 'measuring' not in st.session_state:
    st.session_state.measuring = False
if 'device_connected' not in st.session_state:
    st.session_state.device_connected = False

def load_sample_data():
    """Load sample quantum measurement data"""
    sample_file = Path('data/sample_quantum_data.csv')
    if sample_file.exists():
        df = pd.read_csv(sample_file)
        st.session_state.measurement_data = {
            'timestamp': [datetime.fromisoformat(ts) for ts in df['timestamp']],
            'current': df['current'].tolist(),
            'voltage': df['voltage'].tolist(),
            'resistance': df['resistance'].tolist(),
            'temperature': df['temperature'].tolist()
        }
        return True
    return False

def simulate_quantum_measurement():
    """Simulate quantum measurement data"""
    timestamp = datetime.now()
    
    # Generate realistic quantum measurement data
    base_current = 1e-9  # 1 nA base current
    noise = np.random.normal(0, base_current * 0.01)
    current = base_current + noise
    
    voltage = 1.0 + np.random.normal(0, 0.001)
    resistance = voltage / current if current != 0 else 1e12
    temperature = 23.0 + np.random.normal(0, 0.1)
    
    return {
        'timestamp': timestamp,
        'current': current,
        'voltage': voltage,
        'resistance': resistance,
        'temperature': temperature
    }

def perform_ai_analysis(data):
    """Perform AI analysis on measurement data"""
    if not data['current']:
        return None
    
    current_array = np.array(data['current'])
    voltage_array = np.array(data['voltage'])
    
    # Statistical analysis
    current_stats = {
        'mean': np.mean(current_array),
        'std': np.std(current_array),
        'min': np.min(current_array),
        'max': np.max(current_array)
    }
    
    voltage_stats = {
        'mean': np.mean(voltage_array),
        'std': np.std(voltage_array),
        'min': np.min(voltage_array),
        'max': np.max(voltage_array)
    }
    
    # Anomaly detection (3-sigma rule)
    current_anomalies = np.sum(np.abs(current_array - current_stats['mean']) > 3 * current_stats['std'])
    voltage_anomalies = np.sum(np.abs(voltage_array - voltage_stats['mean']) > 3 * voltage_stats['std'])
    
    # Quality score calculation
    current_stability = 1 - (current_stats['std'] / current_stats['mean']) if current_stats['mean'] != 0 else 0
    voltage_stability = 1 - (voltage_stats['std'] / voltage_stats['mean']) if voltage_stats['mean'] != 0 else 0
    quality_score = (current_stability + voltage_stability) / 2
    
    return {
        'current': current_stats,
        'voltage': voltage_stats,
        'anomalies': {
            'current_anomalies': int(current_anomalies),
            'voltage_anomalies': int(voltage_anomalies)
        },
        'quality_score': quality_score
    }

# Main application
def main():
    # Header
    st.markdown('<h1 class="main-header">🔬 QuantumMeter Pro</h1>', unsafe_allow_html=True)
    st.markdown("**Advanced Laboratory Software for Quantum Measurement Devices**")
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Device Control")
        
        # Device connection
        if st.button("🔌 Connect Device" if not st.session_state.device_connected else "🔌 Disconnect Device"):
            st.session_state.device_connected = not st.session_state.device_connected
            if st.session_state.device_connected:
                st.success("Device connected successfully!")
            else:
                st.warning("Device disconnected")
        
        # Measurement control
        if st.session_state.device_connected:
            if st.button("▶️ Start Measurement" if not st.session_state.measuring else "⏹️ Stop Measurement"):
                st.session_state.measuring = not st.session_state.measuring
        
        # Data management
        st.header("📁 Data Management")
        if st.button("📊 Load Sample Data"):
            if load_sample_data():
                st.success("Sample data loaded successfully!")
            else:
                st.error("Sample data file not found")
        
        if st.button("💾 Export Data"):
            if st.session_state.measurement_data['timestamp']:
                df = pd.DataFrame(st.session_state.measurement_data)
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📥 Download CSV",
                    data=csv,
                    file_name=f"quantum_measurements_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
        
        # Device status
        st.header("📊 Device Status")
        status_color = "status-connected" if st.session_state.device_connected else "status-disconnected"
        status_text = "Connected" if st.session_state.device_connected else "Disconnected"
        st.markdown(f'<p class="{status_color}">🔌 {status_text}</p>', unsafe_allow_html=True)
        
        if st.session_state.measuring:
            st.markdown('<p class="status-connected">📊 Measuring</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="status-disconnected">⏸️ Stopped</p>', unsafe_allow_html=True)
    
    # Main content area
    col1, col2, col3, col4 = st.columns(4)
    
    # Real-time metrics
    if st.session_state.measurement_data['timestamp']:
        latest_idx = -1
        with col1:
            st.metric(
                "Current",
                f"{st.session_state.measurement_data['current'][latest_idx]:.2e} A",
                f"{(st.session_state.measurement_data['current'][latest_idx] * 1e9):.2f} nA"
            )
        
        with col2:
            st.metric(
                "Voltage",
                f"{st.session_state.measurement_data['voltage'][latest_idx]:.6f} V",
                f"{(st.session_state.measurement_data['voltage'][latest_idx] * 1e6):.2f} μV"
            )
        
        with col3:
            st.metric(
                "Resistance",
                f"{st.session_state.measurement_data['resistance'][latest_idx]:.2e} Ω",
                f"{(st.session_state.measurement_data['resistance'][latest_idx] / 1e6):.2f} MΩ"
            )
        
        with col4:
            st.metric(
                "Temperature",
                f"{st.session_state.measurement_data['temperature'][latest_idx]:.1f} °C"
            )
    
    # Real-time charts
    if st.session_state.measurement_data['timestamp']:
        st.header("📈 Real-time Measurements")
        
        # Create charts
        fig_current = go.Figure()
        fig_current.add_trace(go.Scatter(
            x=st.session_state.measurement_data['timestamp'],
            y=st.session_state.measurement_data['current'],
            mode='lines+markers',
            name='Current (A)',
            line=dict(color='#1f77b4', width=2)
        ))
        fig_current.update_layout(
            title="Current Measurement",
            xaxis_title="Time",
            yaxis_title="Current (A)",
            height=300
        )
        
        fig_voltage = go.Figure()
        fig_voltage.add_trace(go.Scatter(
            x=st.session_state.measurement_data['timestamp'],
            y=st.session_state.measurement_data['voltage'],
            mode='lines+markers',
            name='Voltage (V)',
            line=dict(color='#ff7f0e', width=2)
        ))
        fig_voltage.update_layout(
            title="Voltage Measurement",
            xaxis_title="Time",
            yaxis_title="Voltage (V)",
            height=300
        )
        
        fig_resistance = go.Figure()
        fig_resistance.add_trace(go.Scatter(
            x=st.session_state.measurement_data['timestamp'],
            y=st.session_state.measurement_data['resistance'],
            mode='lines+markers',
            name='Resistance (Ω)',
            line=dict(color='#2ca02c', width=2)
        ))
        fig_resistance.update_layout(
            title="Resistance Calculation",
            xaxis_title="Time",
            yaxis_title="Resistance (Ω)",
            height=300
        )
        
        fig_temperature = go.Figure()
        fig_temperature.add_trace(go.Scatter(
            x=st.session_state.measurement_data['timestamp'],
            y=st.session_state.measurement_data['temperature'],
            mode='lines+markers',
            name='Temperature (°C)',
            line=dict(color='#d62728', width=2)
        ))
        fig_temperature.update_layout(
            title="Temperature Monitoring",
            xaxis_title="Time",
            yaxis_title="Temperature (°C)",
            height=300
        )
        
        # Display charts in columns
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            st.plotly_chart(fig_current, use_container_width=True)
            st.plotly_chart(fig_resistance, use_container_width=True)
        
        with chart_col2:
            st.plotly_chart(fig_voltage, use_container_width=True)
            st.plotly_chart(fig_temperature, use_container_width=True)
    
    # AI Analysis
    if st.session_state.measurement_data['timestamp']:
        st.header("🤖 AI Analysis")
        
        analysis = perform_ai_analysis(st.session_state.measurement_data)
        if analysis:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("📊 Current Analysis")
                st.metric("Mean", f"{analysis['current']['mean']:.2e} A")
                st.metric("Std Dev", f"{analysis['current']['std']:.2e} A")
                st.metric("Stability", f"{(1 - analysis['current']['std']/analysis['current']['mean']) * 100:.2f}%" if analysis['current']['mean'] != 0 else "N/A")
            
            with col2:
                st.subheader("🔋 Voltage Analysis")
                st.metric("Mean", f"{analysis['voltage']['mean']:.6f} V")
                st.metric("Std Dev", f"{analysis['voltage']['std']:.6f} V")
                st.metric("Stability", f"{(1 - analysis['voltage']['std']/analysis['voltage']['mean']) * 100:.2f}%" if analysis['voltage']['mean'] != 0 else "N/A")
            
            with col3:
                st.subheader("⚠️ Anomaly Detection")
                st.metric("Current Anomalies", analysis['anomalies']['current_anomalies'])
                st.metric("Voltage Anomalies", analysis['anomalies']['voltage_anomalies'])
                st.metric("Quality Score", f"{analysis['quality_score'] * 100:.1f}%")
                
                if analysis['quality_score'] > 0.95:
                    st.success("✅ Excellent Quality")
                elif analysis['quality_score'] > 0.9:
                    st.warning("🟡 Good Quality")
                else:
                    st.error("🔴 Needs Improvement")
    
    # Data table
    if st.session_state.measurement_data['timestamp']:
        st.header("📋 Measurement Data")
        df = pd.DataFrame(st.session_state.measurement_data)
        st.dataframe(df, use_container_width=True)
    
    # Auto-refresh for real-time updates
    if st.session_state.measuring and st.session_state.device_connected:
        time.sleep(1)
        new_data = simulate_quantum_measurement()
        st.session_state.measurement_data['timestamp'].append(new_data['timestamp'])
        st.session_state.measurement_data['current'].append(new_data['current'])
        st.session_state.measurement_data['voltage'].append(new_data['voltage'])
        st.session_state.measurement_data['resistance'].append(new_data['resistance'])
        st.session_state.measurement_data['temperature'].append(new_data['temperature'])
        
        # Keep only last 100 data points
        if len(st.session_state.measurement_data['timestamp']) > 100:
            for key in st.session_state.measurement_data:
                st.session_state.measurement_data[key] = st.session_state.measurement_data[key][-100:]
        
        st.rerun()

if __name__ == "__main__":
    main()
