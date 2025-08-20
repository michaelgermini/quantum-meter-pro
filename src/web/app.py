#!/usr/bin/env python3
"""
QuantumMeter Pro - Web Dashboard
Flask-based web interface for remote monitoring and control
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import json
import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import threading
import time

app = Flask(__name__)
CORS(app)

# Global data storage (in production, use a proper database)
measurement_data = {
    'timestamp': [],
    'current': [],
    'voltage': [],
    'resistance': [],
    'temperature': []
}

# Device status
device_status = {
    'connected': False,
    'measuring': False,
    'last_update': None
}

def generate_initial_data():
    """Generate initial sample data for demonstration"""
    print("🔬 Generating initial quantum measurement data...")
    
    # Try to load from sample CSV file first
    sample_file = Path('data/sample_quantum_data.csv')
    if sample_file.exists():
        try:
            load_data_from_csv(sample_file)
            print(f"✅ Loaded {len(measurement_data['timestamp'])} data points from sample file")
            return
        except Exception as e:
            print(f"⚠️ Could not load sample file: {e}")
    
    # Generate 50 sample data points if no file exists
    base_time = datetime.datetime.now() - datetime.timedelta(seconds=50)
    
    for i in range(50):
        timestamp = base_time + datetime.timedelta(seconds=i)
        
        # Generate realistic quantum measurement data with some variation
        base_current = 1e-9  # 1 nA base current
        # Add some realistic variations and trends
        trend = 0.1 * np.sin(i * 0.2)  # Slow sinusoidal trend
        noise = np.random.normal(0, base_current * 0.02)  # 2% noise
        current = base_current * (1 + trend) + noise
        
        # Voltage with slight correlation to current
        voltage = 1.0 + np.random.normal(0, 0.001) + (current - base_current) * 1e6
        
        # Resistance calculation
        resistance = voltage / current if current != 0 else 1e12
        
        # Temperature with slow drift
        temperature = 23.0 + 0.1 * np.sin(i * 0.1) + np.random.normal(0, 0.05)
        
        # Store data
        measurement_data['timestamp'].append(timestamp)
        measurement_data['current'].append(current)
        measurement_data['voltage'].append(voltage)
        measurement_data['resistance'].append(resistance)
        measurement_data['temperature'].append(temperature)
    
    print(f"✅ Generated {len(measurement_data['timestamp'])} initial data points")
    print(f"📊 Current range: {min(measurement_data['current']):.2e} - {max(measurement_data['current']):.2e} A")
    print(f"🔋 Voltage range: {min(measurement_data['voltage']):.6f} - {max(measurement_data['voltage']):.6f} V")
    print(f"🌡️ Temperature range: {min(measurement_data['temperature']):.1f} - {max(measurement_data['temperature']):.1f} °C")

def load_data_from_csv(filepath):
    """Load measurement data from CSV file"""
    df = pd.read_csv(filepath)
    
    # Clear existing data
    for key in measurement_data:
        measurement_data[key] = []
    
    # Convert timestamp strings to datetime objects
    timestamps = [datetime.datetime.fromisoformat(ts) for ts in df['timestamp']]
    
    # Load data
    measurement_data['timestamp'] = timestamps
    measurement_data['current'] = df['current'].tolist()
    measurement_data['voltage'] = df['voltage'].tolist()
    measurement_data['resistance'] = df['resistance'].tolist()
    measurement_data['temperature'] = df['temperature'].tolist()
    
    print(f"📁 Loaded {len(measurement_data['timestamp'])} data points from {filepath}")
    print(f"📊 Data range: {min(timestamps)} to {max(timestamps)}")

class DataSimulator:
    """Simulate quantum measurement data for web dashboard"""
    
    def __init__(self):
        self.running = False
        self.thread = None
        
    def start(self):
        """Start data simulation"""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._simulate_data)
            self.thread.daemon = True
            self.thread.start()
            
    def stop(self):
        """Stop data simulation"""
        self.running = False
        
    def _simulate_data(self):
        """Simulate quantum measurement data"""
        while self.running:
            # Generate realistic quantum measurement data
            timestamp = datetime.datetime.now()
            
            base_current = 1e-9  # 1 nA base current
            noise = np.random.normal(0, base_current * 0.01)
            current = base_current + noise
            
            voltage = 1.0 + np.random.normal(0, 0.001)
            resistance = voltage / current if current != 0 else 1e12
            temperature = 23.0 + np.random.normal(0, 0.1)
            
            # Store data (keep only last 1000 points)
            measurement_data['timestamp'].append(timestamp)
            measurement_data['current'].append(current)
            measurement_data['voltage'].append(voltage)
            measurement_data['resistance'].append(resistance)
            measurement_data['temperature'].append(temperature)
            
            # Limit data size
            if len(measurement_data['timestamp']) > 1000:
                for key in measurement_data:
                    measurement_data[key] = measurement_data[key][-1000:]
                    
            device_status['last_update'] = timestamp
            time.sleep(1)  # 1 Hz sampling

# Initialize data simulator
data_simulator = DataSimulator()

# Generate initial data on startup
generate_initial_data()

@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/status')
def get_status():
    """Get device and measurement status"""
    return jsonify({
        'device_connected': device_status['connected'],
        'measuring': device_status['measuring'],
        'last_update': device_status['last_update'].isoformat() if device_status['last_update'] else None,
        'data_points': len(measurement_data['timestamp'])
    })

@app.route('/api/measurements/current')
def get_current_measurements():
    """Get current measurement data"""
    if not measurement_data['timestamp']:
        return jsonify({'error': 'No data available'})
        
    # Return last 100 measurements
    recent_data = {key: values[-100:] for key, values in measurement_data.items()}
    
    # Convert timestamps to strings
    recent_data['timestamp'] = [ts.isoformat() for ts in recent_data['timestamp']]
    
    return jsonify(recent_data)

@app.route('/api/measurements/history')
def get_measurement_history():
    """Get historical measurement data"""
    if not measurement_data['timestamp']:
        return jsonify({'error': 'No data available'})
        
    # Convert timestamps to strings
    data = {key: values.copy() for key, values in measurement_data.items()}
    data['timestamp'] = [ts.isoformat() for ts in data['timestamp']]
    
    return jsonify(data)

@app.route('/api/device/connect', methods=['POST'])
def connect_device():
    """Connect to quantum measurement device"""
    device_status['connected'] = True
    device_status['last_update'] = datetime.datetime.now()
    return jsonify({'status': 'connected'})

@app.route('/api/device/disconnect', methods=['POST'])
def disconnect_device():
    """Disconnect from quantum measurement device"""
    device_status['connected'] = False
    device_status['measuring'] = False
    data_simulator.stop()
    return jsonify({'status': 'disconnected'})

@app.route('/api/measurement/start', methods=['POST'])
def start_measurement():
    """Start measurement collection"""
    if not device_status['connected']:
        return jsonify({'error': 'Device not connected'}), 400
        
    device_status['measuring'] = True
    data_simulator.start()
    return jsonify({'status': 'started'})

@app.route('/api/measurement/stop', methods=['POST'])
def stop_measurement():
    """Stop measurement collection"""
    device_status['measuring'] = False
    data_simulator.stop()
    return jsonify({'status': 'stopped'})

@app.route('/api/export/csv')
def export_csv():
    """Export data as CSV"""
    if not measurement_data['timestamp']:
        return jsonify({'error': 'No data to export'}), 400
        
    # Create DataFrame
    df = pd.DataFrame(measurement_data)
    
    # Save to file
    filename = f"quantum_measurements_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = Path('data') / filename
    filepath.parent.mkdir(exist_ok=True)
    df.to_csv(filepath, index=False)
    
    return jsonify({
        'filename': filename,
        'filepath': str(filepath),
        'data_points': len(df)
    })

@app.route('/api/load/sample', methods=['POST'])
def load_sample_data():
    """Load sample data from CSV file"""
    try:
        sample_file = Path('data/sample_quantum_data.csv')
        if not sample_file.exists():
            return jsonify({'error': 'Sample data file not found'}), 404
            
        load_data_from_csv(sample_file)
        
        return jsonify({
            'status': 'success',
            'message': f'Loaded {len(measurement_data["timestamp"])} data points from sample file',
            'data_points': len(measurement_data['timestamp'])
        })
        
    except Exception as e:
        return jsonify({'error': f'Failed to load sample data: {str(e)}'}), 500

@app.route('/api/load/csv', methods=['POST'])
def load_csv_data():
    """Load data from uploaded CSV file"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
            
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
            
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be a CSV'}), 400
        
        # Save uploaded file temporarily
        temp_file = Path('data/temp_upload.csv')
        temp_file.parent.mkdir(exist_ok=True)
        file.save(temp_file)
        
        # Load data from file
        load_data_from_csv(temp_file)
        
        # Clean up temp file
        temp_file.unlink()
        
        return jsonify({
            'status': 'success',
            'message': f'Loaded {len(measurement_data["timestamp"])} data points from {file.filename}',
            'data_points': len(measurement_data['timestamp'])
        })
        
    except Exception as e:
        return jsonify({'error': f'Failed to load CSV data: {str(e)}'}), 500

@app.route('/api/ai/analysis')
def get_ai_analysis():
    """Get AI analysis results"""
    if len(measurement_data['current']) < 10:
        return jsonify({'error': 'Insufficient data for analysis'}), 400
        
    # Simple AI analysis
    current_values = np.array(measurement_data['current'])
    voltage_values = np.array(measurement_data['voltage'])
    
    # Calculate statistics
    analysis = {
        'current': {
            'mean': float(np.mean(current_values)),
            'std': float(np.std(current_values)),
            'min': float(np.min(current_values)),
            'max': float(np.max(current_values))
        },
        'voltage': {
            'mean': float(np.mean(voltage_values)),
            'std': float(np.std(voltage_values)),
            'min': float(np.min(voltage_values)),
            'max': float(np.max(voltage_values))
        },
        'anomalies': {
            'current_anomalies': int(np.sum(np.abs(current_values - np.mean(current_values)) > 3 * np.std(current_values))),
            'voltage_anomalies': int(np.sum(np.abs(voltage_values - np.mean(voltage_values)) > 3 * np.std(voltage_values)))
        },
        'quality_score': float(1.0 - (np.std(current_values) / np.mean(current_values)))
    }
    
    return jsonify(analysis)

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Create data directory
    Path('data').mkdir(exist_ok=True)
    
    # Start the web server
    app.run(host='0.0.0.0', port=8080, debug=True)
