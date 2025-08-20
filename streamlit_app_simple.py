#!/usr/bin/env python3
"""
QuantumMeter Pro - Streamlit Version (Simplified)
Advanced Laboratory Software for Quantum Measurement Devices
Uses only default Streamlit libraries for maximum compatibility
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
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
        font-size: 2.5rem;
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
        margin: 0.5rem 0;
    }
    .status-connected {
        color: #28a745;
        font-weight: bold;
    }
    .status-disconnected {
        color: #dc3545;
        font-weight: bold;
    }
    .chart-container {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        margin: 1rem 0;
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
    try:
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
        else:
            # Generate sample data if file doesn't exist
            generate_sample_data()
            return True
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return False

def generate_sample_data():
    """Generate sample quantum measurement data"""
    base_time = datetime.now() - timedelta(seconds=50)
    data = {
        'timestamp': [],
        'current': [],
        'voltage': [],
        'resistance': [],
        'temperature': []
    }
    
    for i in range(50):
        timestamp = base_time + timedelta(seconds=i)
        base_current = 1e-9
        trend = 0.1 * np.sin(i * 0.2)
        noise = np.random.normal(0, base_current * 0.02)
        current = base_current * (1 + trend) + noise
        voltage = 1.0 + np.random.normal(0, 0.001) + (current - base_current) * 1e6
        resistance = voltage / current if current != 0 else 1e12
        temperature = 23.0 + 0.1 * np.sin(i * 0.1) + np.random.normal(0, 0.05)
        
        data['timestamp'].append(timestamp)
        data['current'].append(current)
        data['voltage'].append(voltage)
        data['resistance'].append(resistance)
        data['temperature'].append(temperature)
    
    st.session_state.measurement_data = data

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

def display_metric_card(title, value, subtitle=None, color="blue"):
    """Display a metric card with custom styling"""
    st.markdown(f"""
    <div class="metric-card">
        <h3 style="margin: 0; color: {color}; font-size: 1.2rem;">{title}</h3>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.5rem; font-weight: bold;">{value}</p>
        {f'<p style="margin: 0.2rem 0 0 0; font-size: 0.9rem; color: #666;">{subtitle}</p>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)

# Main application
def main():
    # Header
    st.markdown('<h1 class="main-header">🔬 QuantumMeter Pro</h1>', unsafe_allow_html=True)
    st.markdown("**Advanced Laboratory Software for Quantum Measurement Devices**")
    st.markdown("*Simplified version for maximum compatibility*")
    
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
            display_metric_card(
                "Current",
                f"{st.session_state.measurement_data['current'][latest_idx]:.2e} A",
                f"{(st.session_state.measurement_data['current'][latest_idx] * 1e9):.2f} nA",
                "#1f77b4"
            )
        
        with col2:
            display_metric_card(
                "Voltage",
                f"{st.session_state.measurement_data['voltage'][latest_idx]:.6f} V",
                f"{(st.session_state.measurement_data['voltage'][latest_idx] * 1e6):.2f} μV",
                "#ff7f0e"
            )
        
        with col3:
            display_metric_card(
                "Resistance",
                f"{st.session_state.measurement_data['resistance'][latest_idx]:.2e} Ω",
                f"{(st.session_state.measurement_data['resistance'][latest_idx] / 1e6):.2f} MΩ",
                "#2ca02c"
            )
        
        with col4:
            display_metric_card(
                "Temperature",
                f"{st.session_state.measurement_data['temperature'][latest_idx]:.1f} °C",
                color="#d62728"
            )
    
    # Real-time charts using Streamlit's built-in charting
    if st.session_state.measurement_data['timestamp']:
        st.header("📈 Real-time Measurements")
        
        # Create DataFrame for charts
        df = pd.DataFrame(st.session_state.measurement_data)
        
        # Current chart
        st.subheader("⚡ Current Measurement")
        st.line_chart(df.set_index('timestamp')['current'])
        
        # Voltage chart
        st.subheader("🔋 Voltage Measurement")
        st.line_chart(df.set_index('timestamp')['voltage'])
        
        # Resistance chart
        st.subheader("🔌 Resistance Calculation")
        st.line_chart(df.set_index('timestamp')['resistance'])
        
        # Temperature chart
        st.subheader("🌡️ Temperature Monitoring")
        st.line_chart(df.set_index('timestamp')['temperature'])
    
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
        
        # Summary statistics
        st.subheader("📊 Summary Statistics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Current Statistics:**")
            st.write(f"- Mean: {df['current'].mean():.2e} A")
            st.write(f"- Std Dev: {df['current'].std():.2e} A")
            st.write(f"- Min: {df['current'].min():.2e} A")
            st.write(f"- Max: {df['current'].max():.2e} A")
        
        with col2:
            st.write("**Voltage Statistics:**")
            st.write(f"- Mean: {df['voltage'].mean():.6f} V")
            st.write(f"- Std Dev: {df['voltage'].std():.6f} V")
            st.write(f"- Min: {df['voltage'].min():.6f} V")
            st.write(f"- Max: {df['voltage'].max():.6f} V")
    
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
