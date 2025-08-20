# QuantumMeter Pro

<div align="center">
  <img src="../QuantumMeter_Pro.png" alt="QuantumMeter Pro Logo" width="400" height="300">
</div>

🔬 **Advanced Laboratory Software for Quantum Measurement Devices**

Welcome to QuantumMeter Pro, a comprehensive laboratory software solution designed to interface with and control quantum measurement devices. This software enables national laboratories and universities to standardize their electrical measurements without multiplying devices.

## 🌟 Key Features

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

## 🚀 Quick Start

### Desktop Application
```bash
git clone https://github.com/michaelgermini/quantum-meter-pro.git
cd quantum-meter-pro
pip install -r requirements.txt
python main.py
```

### Web Dashboard
```bash
python src/web/app.py
# Access at http://localhost:8080
```

### Streamlit Cloud (Recommended)
Deploy to [Streamlit Cloud](https://share.streamlit.io) using `streamlit_app_simple.py`

## 📊 Technical Specifications

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

## 📁 Project Structure

```
QuantumMeter Pro/
├── main.py                          # Desktop application entry point
├── streamlit_app_simple.py          # Cloud-ready Streamlit app
├── src/web/app.py                   # Flask web application
├── config/devices.yaml              # Device configuration
├── data/sample_quantum_data.csv     # Sample measurement data
├── requirements.txt                 # Python dependencies
├── requirements-streamlit-minimal.txt # Minimal Streamlit dependencies
└── docs/                           # Documentation
```

## 🔧 Configuration

The application supports multiple quantum measurement devices through the `config/devices.yaml` file:

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

## 🤝 Contributing

We welcome contributions to QuantumMeter Pro! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Add tests** (if applicable)
5. **Commit your changes**
6. **Push to your branch**
7. **Create a Pull Request**

For detailed contribution guidelines, see [CONTRIBUTING.md](https://github.com/michaelgermini/quantum-meter-pro/blob/main/CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/michaelgermini/quantum-meter-pro/blob/main/LICENSE) file for details.

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
- Streamlit cloud version
- Real-time data visualization
- AI analysis module
- Data import/export capabilities

For detailed version history, see [CHANGELOG.md](https://github.com/michaelgermini/quantum-meter-pro/blob/main/CHANGELOG.md).

---

**Made with ❤️ for the scientific community**

*QuantumMeter Pro - Advancing Quantum Measurement Technology*
