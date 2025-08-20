#!/usr/bin/env python3
"""
QuantumMeter Pro - Main Application
Advanced Laboratory Software for Quantum Measurement Devices
"""

import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                             QWidget, QTabWidget, QLabel, QPushButton, QTextEdit, 
                             QGroupBox, QGridLayout, QComboBox, QSpinBox, 
                             QDoubleSpinBox, QCheckBox, QProgressBar, QTableWidget, 
                             QTableWidgetItem, QMessageBox, QSplitter)
from PyQt6.QtCore import QTimer, QThread, pyqtSignal, Qt
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import json
import datetime

class MeasurementThread(QThread):
    """Thread for collecting measurement data"""
    data_ready = pyqtSignal(dict)
    
    def __init__(self, sampling_rate):
        super().__init__()
        self.sampling_rate = sampling_rate
        self.running = False
        
    def run(self):
        """Main measurement loop"""
        self.running = True
        while self.running:
            # Simulate quantum measurement
            data = self.simulate_quantum_measurement()
            self.data_ready.emit(data)
            self.msleep(1000 // self.sampling_rate)
            
    def stop(self):
        """Stop measurement"""
        self.running = False
        
    def simulate_quantum_measurement(self):
        """Simulate quantum measurement data"""
        timestamp = datetime.datetime.now()
        
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

class QuantumMeterPro(QMainWindow):
    """Main application window"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuantumMeter Pro - Advanced Laboratory Software")
        self.setGeometry(100, 100, 1600, 1000)
        
        # Initialize data storage
        self.measurement_data = {
            'timestamp': [],
            'current': [],
            'voltage': [],
            'resistance': [],
            'temperature': []
        }
        
        # Setup UI
        self.setup_ui()
        self.setup_timers()
        self.setup_styles()
        
    def setup_ui(self):
        """Setup the main user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main splitter
        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        central_layout = QVBoxLayout(central_widget)
        central_layout.addWidget(main_splitter)
        
        # Left panel - Controls
        left_panel = self.create_control_panel()
        main_splitter.addWidget(left_panel)
        
        # Right panel - Visualization
        right_panel = self.create_visualization_panel()
        main_splitter.addWidget(right_panel)
        
        # Set splitter proportions
        main_splitter.setSizes([400, 1200])
        
    def create_control_panel(self):
        """Create the left control panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Device Connection
        connection_group = QGroupBox("🔌 Device Connection")
        connection_layout = QVBoxLayout(connection_group)
        
        self.device_combo = QComboBox()
        self.device_combo.addItems(["Quantum Device 001", "Quantum Device 002", "Simulation Mode"])
        connection_layout.addWidget(QLabel("Select Device:"))
        connection_layout.addWidget(self.device_combo)
        
        self.connect_btn = QPushButton("Connect")
        self.connect_btn.clicked.connect(self.toggle_connection)
        connection_layout.addWidget(self.connect_btn)
        
        layout.addWidget(connection_group)
        
        # Measurement Settings
        settings_group = QGroupBox("⚙️ Measurement Settings")
        settings_layout = QGridLayout(settings_group)
        
        settings_layout.addWidget(QLabel("Current Range (A):"), 0, 0)
        self.current_range = QComboBox()
        self.current_range.addItems(["1e-12", "1e-9", "1e-6", "1e-3", "1e-0"])
        settings_layout.addWidget(self.current_range, 0, 1)
        
        settings_layout.addWidget(QLabel("Voltage Range (V):"), 1, 0)
        self.voltage_range = QComboBox()
        self.voltage_range.addItems(["1e-3", "1e-0", "1e3", "1e6"])
        settings_layout.addWidget(self.voltage_range, 1, 1)
        
        settings_layout.addWidget(QLabel("Sampling Rate (Hz):"), 2, 0)
        self.sampling_rate = QSpinBox()
        self.sampling_rate.setRange(1, 1000)
        self.sampling_rate.setValue(10)
        settings_layout.addWidget(self.sampling_rate, 2, 1)
        
        settings_layout.addWidget(QLabel("Integration Time (s):"), 3, 0)
        self.integration_time = QDoubleSpinBox()
        self.integration_time.setRange(0.1, 10.0)
        self.integration_time.setValue(1.0)
        settings_layout.addWidget(self.integration_time, 3, 1)
        
        layout.addWidget(settings_group)
        
        # AI Settings
        ai_group = QGroupBox("🤖 AI Analysis")
        ai_layout = QVBoxLayout(ai_group)
        
        self.ai_enabled = QCheckBox("Enable AI Error Detection")
        self.ai_enabled.setChecked(True)
        ai_layout.addWidget(self.ai_enabled)
        
        self.ai_correction = QCheckBox("Enable AI Error Correction")
        self.ai_correction.setChecked(True)
        ai_layout.addWidget(self.ai_correction)
        
        layout.addWidget(ai_group)
        
        # Control Buttons
        control_group = QGroupBox("🎛️ Measurement Control")
        control_layout = QVBoxLayout(control_group)
        
        self.start_btn = QPushButton("▶ Start Measurement")
        self.start_btn.clicked.connect(self.start_measurement)
        self.start_btn.setEnabled(False)
        control_layout.addWidget(self.start_btn)
        
        self.stop_btn = QPushButton("⏹ Stop Measurement")
        self.stop_btn.clicked.connect(self.stop_measurement)
        self.stop_btn.setEnabled(False)
        control_layout.addWidget(self.stop_btn)
        
        self.export_btn = QPushButton("📊 Export Data")
        self.export_btn.clicked.connect(self.export_data)
        control_layout.addWidget(self.export_btn)
        
        layout.addWidget(control_group)
        
        # Status
        status_group = QGroupBox("📊 Status")
        status_layout = QVBoxLayout(status_group)
        
        self.status_label = QLabel("Ready")
        status_layout.addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        status_layout.addWidget(self.progress_bar)
        
        layout.addWidget(status_group)
        
        layout.addStretch()
        return panel
        
    def create_visualization_panel(self):
        """Create the right visualization panel"""
        panel = QWidget()
        layout = QVBoxLayout(panel)
        
        # Tab widget for different views
        self.tab_widget = QTabWidget()
        
        # Real-time plots tab
        plots_tab = QWidget()
        plots_layout = QVBoxLayout(plots_tab)
        
        # Create matplotlib figure
        self.figure = Figure(figsize=(12, 8))
        self.canvas = FigureCanvas(self.figure)
        plots_layout.addWidget(self.canvas)
        
        # Setup subplots
        self.ax1 = self.figure.add_subplot(311)  # Current
        self.ax2 = self.figure.add_subplot(312)  # Voltage
        self.ax3 = self.figure.add_subplot(313)  # Resistance
        
        self.figure.tight_layout()
        
        self.tab_widget.addTab(plots_tab, "📈 Real-time Plots")
        
        # Data table tab
        table_tab = QWidget()
        table_layout = QVBoxLayout(table_tab)
        
        self.data_table = QTableWidget()
        self.data_table.setColumnCount(5)
        self.data_table.setHorizontalHeaderLabels(["Timestamp", "Current (A)", "Voltage (V)", "Resistance (Ω)", "Temperature (°C)"])
        table_layout.addWidget(self.data_table)
        
        self.tab_widget.addTab(table_tab, "📋 Data Table")
        
        # AI Analysis tab
        ai_tab = QWidget()
        ai_layout = QVBoxLayout(ai_tab)
        
        self.ai_text = QTextEdit()
        self.ai_text.setReadOnly(True)
        ai_layout.addWidget(self.ai_text)
        
        self.tab_widget.addTab(ai_tab, "🤖 AI Analysis")
        
        layout.addWidget(self.tab_widget)
        return panel
        
    def setup_timers(self):
        """Setup timers for updates"""
        self.plot_timer = QTimer()
        self.plot_timer.timeout.connect(self.update_plots)
        self.plot_timer.start(1000)  # Update plots every second
        
    def setup_styles(self):
        """Setup application styling"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555555;
                border-radius: 5px;
                margin-top: 1ex;
                padding-top: 10px;
                background-color: #3b3b3b;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
                color: #4CAF50;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px 20px;
                text-align: center;
                font-size: 14px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:disabled {
                background-color: #cccccc;
                color: #666666;
            }
            QComboBox, QSpinBox, QDoubleSpinBox {
                padding: 8px;
                border: 1px solid #555555;
                border-radius: 4px;
                background-color: #3b3b3b;
                color: #ffffff;
                font-size: 12px;
            }
            QLabel {
                color: #ffffff;
                font-size: 12px;
            }
            QTabWidget::pane {
                border: 1px solid #555555;
                background-color: #2b2b2b;
            }
            QTabBar::tab {
                background-color: #3b3b3b;
                color: #ffffff;
                padding: 8px 16px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background-color: #4CAF50;
            }
        """)
        
    def toggle_connection(self):
        """Toggle device connection"""
        if self.connect_btn.text() == "Connect":
            self.connect_btn.setText("Disconnect")
            self.status_label.setText("Connected")
            self.start_btn.setEnabled(True)
        else:
            self.connect_btn.setText("Connect")
            self.status_label.setText("Disconnected")
            self.start_btn.setEnabled(False)
            self.stop_measurement()
            
    def start_measurement(self):
        """Start data collection"""
        # Create and start measurement thread
        self.measurement_thread = MeasurementThread(self.sampling_rate.value())
        self.measurement_thread.data_ready.connect(self.process_measurement)
        self.measurement_thread.start()
        
        self.start_btn.setEnabled(False)
        self.stop_btn.setEnabled(True)
        self.status_label.setText("Measuring...")
        
        # Clear previous data
        for key in self.measurement_data:
            self.measurement_data[key] = []
            
    def stop_measurement(self):
        """Stop data collection"""
        if hasattr(self, 'measurement_thread'):
            self.measurement_thread.stop()
            self.measurement_thread.wait()
            
        self.start_btn.setEnabled(True)
        self.stop_btn.setEnabled(False)
        self.status_label.setText("Measurement stopped")
        
    def process_measurement(self, data):
        """Process incoming measurement data"""
        # Store data
        self.measurement_data['timestamp'].append(data['timestamp'])
        self.measurement_data['current'].append(data['current'])
        self.measurement_data['voltage'].append(data['voltage'])
        self.measurement_data['resistance'].append(data['resistance'])
        self.measurement_data['temperature'].append(data['temperature'])
        
        # Update progress bar
        self.progress_bar.setValue((len(self.measurement_data['timestamp']) % 100))
        
        # AI analysis
        if self.ai_enabled.isChecked():
            self.perform_ai_analysis()
            
    def update_plots(self):
        """Update real-time plots"""
        if not self.measurement_data['timestamp']:
            return
            
        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        
        # Get recent data (last 100 points)
        recent_data = {key: values[-100:] for key, values in self.measurement_data.items()}
        
        # Plot current
        self.ax1.plot(recent_data['timestamp'], recent_data['current'], 'b-', linewidth=1.5)
        self.ax1.set_ylabel('Current (A)')
        self.ax1.set_title('QuantumMeter Pro - Real-time Measurements', fontsize=14, fontweight='bold')
        self.ax1.grid(True, alpha=0.3)
        self.ax1.tick_params(axis='x', rotation=45)
        
        # Plot voltage
        self.ax2.plot(recent_data['timestamp'], recent_data['voltage'], 'g-', linewidth=1.5)
        self.ax2.set_ylabel('Voltage (V)')
        self.ax2.grid(True, alpha=0.3)
        self.ax2.tick_params(axis='x', rotation=45)
        
        # Plot resistance
        self.ax3.plot(recent_data['timestamp'], recent_data['resistance'], 'r-', linewidth=1.5)
        self.ax3.set_ylabel('Resistance (Ω)')
        self.ax3.set_xlabel('Time')
        self.ax3.grid(True, alpha=0.3)
        self.ax3.tick_params(axis='x', rotation=45)
        
        self.figure.tight_layout()
        self.canvas.draw()
        
        # Update data table
        self.update_data_table()
        
    def update_data_table(self):
        """Update the data table"""
        if not self.measurement_data['timestamp']:
            return
            
        # Show last 50 measurements
        recent_data = {key: values[-50:] for key, values in self.measurement_data.items()}
        
        self.data_table.setRowCount(len(recent_data['timestamp']))
        
        for i, timestamp in enumerate(recent_data['timestamp']):
            self.data_table.setItem(i, 0, QTableWidgetItem(timestamp.strftime("%H:%M:%S")))
            self.data_table.setItem(i, 1, QTableWidgetItem(f"{recent_data['current'][i]:.2e}"))
            self.data_table.setItem(i, 2, QTableWidgetItem(f"{recent_data['voltage'][i]:.6f}"))
            self.data_table.setItem(i, 3, QTableWidgetItem(f"{recent_data['resistance'][i]:.2e}"))
            self.data_table.setItem(i, 4, QTableWidgetItem(f"{recent_data['temperature'][i]:.1f}"))
            
    def perform_ai_analysis(self):
        """Perform AI-based analysis on measurement data"""
        if len(self.measurement_data['current']) < 10:
            return
            
        # Simple anomaly detection
        current_values = np.array(self.measurement_data['current'])
        mean_current = np.mean(current_values)
        std_current = np.std(current_values)
        
        # Check for anomalies (3-sigma rule)
        anomalies = np.abs(current_values - mean_current) > 3 * std_current
        
        if np.any(anomalies):
            anomaly_count = np.sum(anomalies)
            self.ai_text.append(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] "
                              f"⚠️  Detected {anomaly_count} anomalous measurements\n")
            
        # Error correction (simple example)
        if self.ai_correction.isChecked():
            # Apply simple moving average filter
            window_size = 5
            if len(current_values) >= window_size:
                corrected_current = np.convolve(current_values, 
                                              np.ones(window_size)/window_size, 
                                              mode='valid')
                # Update the last corrected value
                if len(corrected_current) > 0:
                    self.measurement_data['current'][-1] = corrected_current[-1]
                    
    def export_data(self):
        """Export measurement data to various formats"""
        if not self.measurement_data['timestamp']:
            QMessageBox.warning(self, "No Data", "No measurement data to export.")
            return
            
        # Create DataFrame
        df = pd.DataFrame(self.measurement_data)
        
        # Export to CSV
        filename = f"quantum_measurements_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)
        
        QMessageBox.information(self, "Export Complete", 
                              f"Data exported to {filename}")

def main():
    """Main application entry point"""
    app = QApplication(sys.argv)
    app.setApplicationName("QuantumMeter Pro")
    app.setApplicationVersion("1.0.0")
    
    # Create and show main window
    window = QuantumMeterPro()
    window.show()
    
    # Start application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
