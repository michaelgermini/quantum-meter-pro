# QuantumMeter Pro 🚀

**Advanced Laboratory Software for Quantum Measurement Devices**

QuantumMeter Pro is a comprehensive laboratory software solution designed to interface with and control quantum measurement devices. It enables national laboratories and universities to standardize their electrical measurements without multiplying devices.

## 🌟 Features

### 🔬 Real-time Measurement
- **Current Measurement**: Nanoampere precision (1 nA base)
- **Voltage Measurement**: Microvolt precision (μV)
- **Resistance Calculation**: Automatic calculation in megohms (MΩ)
- **Temperature Monitoring**: Controlled environment tracking
- **Quantum Precision**: 0.01 ppm accuracy

### 📊 Data Visualization
- **4 Real-time Charts**: Current, Voltage, Resistance, Temperature
- **Interactive Dashboard**: Web-based interface with Chart.js
- **Desktop Application**: PyQt6-based GUI with Matplotlib
- **Responsive Design**: Works on desktop, tablet, and mobile

### 🤖 AI Analysis Module
- **Statistical Analysis**: Mean, standard deviation, min/max values
- **Anomaly Detection**: 3-sigma rule for outlier identification
- **Quality Assessment**: Overall measurement quality score
- **Error Correction**: Automatic experimental error detection

### 📁 Data Management
- **Export Formats**: CSV, Excel, SQL
- **Import Capabilities**: Load existing measurement data
- **Sample Data**: Pre-loaded demonstration datasets
- **Data Retention**: Configurable storage policies

### 🌐 Web Dashboard
- **Real-time Updates**: Live data streaming
- **Device Control**: Connect/disconnect devices
- **Measurement Control**: Start/stop measurements
- **API Endpoints**: RESTful API for integration

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/michaelgermini/quantum-meter-pro.git
   cd quantum-meter-pro
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the desktop application**
   ```bash
   python main.py
   ```

4. **Run the web dashboard**
   ```bash
   python src/web/app.py
   ```

5. **Access the web interface**
   - Open `http://localhost:8080` in your web browser

## 📁 Project Structure

```
QuantumMeter Pro/
├── main.py                          # Desktop application entry point
├── requirements.txt                 # Python dependencies
├── README.md                       # This file
├── .gitignore                      # Git ignore rules
├── config/
│   └── devices.yaml               # Device configuration
├── data/
│   └── sample_quantum_data.csv    # Sample measurement data
└── src/
    └── web/
        ├── app.py                 # Flask web application
        └── templates/
            └── dashboard.html     # Web dashboard template
```

## 🔧 Configuration

### Device Configuration (`config/devices.yaml`)

The application supports multiple quantum measurement devices:

```yaml
devices:
  quantum_device_001:
    name: "Primary Quantum Meter"
    type: "quantum_resistance_bridge"
    connection:
      type: "serial"
      port: "COM3"
      baudrate: 115200
    measurement_ranges:
      current: [1e-12, 1e-9, 1e-6, 1e-3]
      voltage: [1e-3, 1e-0, 1e3]
    sampling_rates: [1, 10, 100, 1000]
```

### Global Settings

- **Data Retention**: Configure how long to keep measurement data
- **Auto Backup**: Automatic data backup settings
- **Export Formats**: Supported export file types
- **AI Analysis**: Enable/disable AI features

## 🎯 Usage

### Desktop Application

1. **Launch the application**
   ```bash
   python main.py
   ```

2. **Start measurements**
   - Click "Start Measurement" to begin data collection
   - Real-time charts will update automatically
   - View AI analysis in the dedicated tab

3. **Export data**
   - Click "Export Data" to save measurements
   - Choose format: CSV, Excel, or SQL
   - Data includes timestamps and all measurement values

### Web Dashboard

1. **Access the dashboard**
   - Open `http://localhost:8080`
   - View real-time measurement charts
   - Monitor device status

2. **Control devices**
   - Connect/disconnect measurement devices
   - Start/stop measurements remotely
   - Configure sampling rates

3. **Data management**
   - Load sample data for demonstration
   - Import CSV files with existing measurements
   - Export current dataset

4. **AI Analysis**
   - View statistical analysis of measurements
   - Check for anomalies and quality scores
   - Monitor measurement stability

## 🔬 Technical Specifications

### Measurement Precision
- **Current**: 1 nA base with 0.01% precision
- **Voltage**: 1 V base with 1 μV precision
- **Resistance**: Calculated from V/I ratio
- **Temperature**: 23°C ± 0.1°C controlled

### Supported Devices
- **Quantum Resistance Bridges**: High-precision resistance measurement
- **Nanoampere Meters**: Ultra-low current measurement
- **Voltage Standards**: Calibrated voltage sources
- **Temperature Controllers**: Environmental monitoring

### Data Formats
- **CSV**: Comma-separated values with timestamps
- **Excel**: Multi-sheet format with charts
- **SQL**: Database export for analysis
- **JSON**: API data exchange format

## 🤝 Contributing

We welcome contributions to QuantumMeter Pro! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Add tests** (if applicable)
5. **Commit your changes**
   ```bash
   git commit -m "Add: your feature description"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Development Setup

For development, install additional dependencies:

```bash
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **National Laboratories**: For feedback and testing
- **Universities**: For academic collaboration
- **Quantum Physics Community**: For technical guidance
- **Open Source Community**: For the amazing tools and libraries

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/michaelgermini/quantum-meter-pro/issues)
- **Documentation**: [Wiki](https://github.com/michaelgermini/quantum-meter-pro/wiki)
- **Email**: michael@germini.info
- **GitHub**: [michaelgermini](https://github.com/michaelgermini)
- **Author**: Michael Germini

## 🔄 Version History

### v1.0.0 (Current)
- Initial release
- Desktop application with PyQt6
- Web dashboard with Flask
- Real-time data visualization
- AI analysis module
- Data import/export capabilities

---

**Made with ❤️ for the scientific community**

*QuantumMeter Pro - Advancing Quantum Measurement Technology*
