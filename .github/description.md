# QuantumMeter Pro - Advanced Laboratory Software

🔬 **Advanced Laboratory Software for Quantum Measurement Devices**

QuantumMeter Pro is a comprehensive laboratory software solution designed to interface with and control quantum measurement devices. It enables national laboratories and universities to standardize their electrical measurements without multiplying devices.

## 🌟 Key Features

- **Real-time Measurement**: Nanoampere precision (1 nA base) with microvolt accuracy
- **4 Interactive Charts**: Current, Voltage, Resistance, and Temperature monitoring
- **AI Analysis Module**: Statistical analysis, anomaly detection, and quality assessment
- **Multi-Platform**: Desktop (PyQt6), Web Dashboard (Flask), and Cloud (Streamlit)
- **Data Management**: CSV/Excel/SQL export, import capabilities, and sample data
- **Device Control**: Connect/disconnect devices, start/stop measurements remotely

## 🚀 Quick Start

### Desktop Application
```bash
python main.py
```

### Web Dashboard
```bash
python src/web/app.py
```

### Streamlit Cloud (Recommended)
Deploy to [Streamlit Cloud](https://share.streamlit.io) using `streamlit_app_simple.py`

## 📊 Technical Specifications

- **Current**: 1 nA base with 0.01% precision
- **Voltage**: 1 V base with 1 μV precision  
- **Resistance**: Calculated from V/I ratio in megohms
- **Temperature**: 23°C ± 0.1°C controlled environment
- **Quantum Precision**: 0.01 ppm accuracy

## 🔧 Supported Devices

- Quantum Resistance Bridges
- Nanoampere Meters
- Voltage Standards
- Temperature Controllers

## 📁 Project Structure

```
├── main.py                          # Desktop application
├── streamlit_app_simple.py          # Cloud-ready Streamlit app
├── src/web/app.py                   # Flask web dashboard
├── config/devices.yaml              # Device configuration
├── data/sample_quantum_data.csv     # Sample measurement data
└── requirements-*.txt               # Dependencies
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/michaelgermini/quantum-meter-pro/issues)
- **Email**: michael@germini.info
- **Author**: Michael Germini

---

**Made with ❤️ for the scientific community**

*Advancing Quantum Measurement Technology*
