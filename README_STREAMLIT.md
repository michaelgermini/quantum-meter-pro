# QuantumMeter Pro - Streamlit Cloud Deployment

## 🚀 Quick Deploy to Streamlit Cloud

This version of QuantumMeter Pro is specifically designed to work on Streamlit Cloud and other cloud platforms.

### 📋 Prerequisites

- A GitHub account
- A Streamlit Cloud account (free at [share.streamlit.io](https://share.streamlit.io))

### 🛠️ Deployment Steps

1. **Fork this repository** to your GitHub account
2. **Go to Streamlit Cloud** and sign in with your GitHub account
3. **Click "New app"**
4. **Configure your app**:
   - **Repository**: Select your forked repository
   - **Branch**: `main`
   - **Main file path**: `streamlit_app.py`
   - **App URL**: Choose your preferred URL

5. **Click "Deploy"**

### 📁 Required Files

Make sure these files are in your repository:

```
quantum-meter-pro/
├── streamlit_app.py              # Main Streamlit application
├── requirements-streamlit.txt    # Python dependencies
├── .streamlit/
│   └── config.toml              # Streamlit configuration
└── data/
    └── sample_quantum_data.csv  # Sample data
```

### 🔧 Configuration

The `.streamlit/config.toml` file contains optimized settings for cloud deployment:

```toml
[global]
developmentMode = false

[server]
headless = true
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false

[theme]
primaryColor = "#1f77b4"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f0f2f6"
textColor = "#262730"
```

### 📊 Features Available in Streamlit Version

- ✅ **Real-time Measurement Display**
- ✅ **Interactive Charts** (Current, Voltage, Resistance, Temperature)
- ✅ **AI Analysis Module**
- ✅ **Data Import/Export**
- ✅ **Device Control Simulation**
- ✅ **Responsive Design**

### 🌐 Access Your App

Once deployed, your app will be available at:
```
https://your-app-name-your-username.streamlit.app
```

### 🔄 Updates

To update your deployed app:
1. Make changes to your local repository
2. Push changes to GitHub
3. Streamlit Cloud will automatically redeploy

### 🐛 Troubleshooting

#### Common Issues:

1. **Import Errors**: Make sure all dependencies are in `requirements-streamlit.txt`
2. **File Not Found**: Ensure `data/sample_quantum_data.csv` exists
3. **Memory Issues**: The app is optimized for cloud deployment with limited resources

#### Support:

- **GitHub Issues**: [Report bugs](https://github.com/michaelgermini/quantum-meter-pro/issues)
- **Email**: michael@germini.info
- **Documentation**: [Main README](README.md)

---

**Made with ❤️ for the scientific community**

*QuantumMeter Pro - Advancing Quantum Measurement Technology*
