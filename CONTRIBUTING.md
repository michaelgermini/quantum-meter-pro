# Contributing to QuantumMeter Pro 🤝

Thank you for your interest in contributing to QuantumMeter Pro! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of Python, PyQt6, and Flask

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/quantum-meter-pro.git
   cd quantum-meter-pro
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

4. **Run tests**
   ```bash
   python -m pytest tests/
   ```

## 📝 How to Contribute

### 1. Reporting Issues

Before creating an issue, please:
- Check if the issue has already been reported
- Use the appropriate issue template
- Provide detailed information including:
  - Operating system and Python version
  - Steps to reproduce the issue
  - Expected vs actual behavior
  - Error messages or logs

### 2. Feature Requests

When requesting a feature:
- Describe the feature clearly
- Explain the use case and benefits
- Consider if it aligns with the project's goals
- Provide examples if possible

### 3. Code Contributions

#### Pull Request Process

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the coding standards below
   - Add tests for new functionality
   - Update documentation if needed

3. **Test your changes**
   ```bash
   python -m pytest tests/
   python main.py  # Test desktop app
   python src/web/app.py  # Test web dashboard
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

5. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

#### Commit Message Format

Use conventional commit messages:
- `Add:` for new features
- `Fix:` for bug fixes
- `Update:` for improvements
- `Remove:` for deletions
- `Docs:` for documentation changes

Examples:
```
Add: real-time temperature monitoring
Fix: chart rendering issue on mobile devices
Update: improve AI analysis accuracy
Docs: add installation guide for Windows
```

## 🎨 Coding Standards

### Python Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions small and focused
- Use meaningful variable names

### Example Code Structure

```python
#!/usr/bin/env python3
"""
Module description.
"""

from typing import Dict, List, Optional
import numpy as np


class MeasurementProcessor:
    """Process quantum measurement data."""
    
    def __init__(self, config: Dict[str, any]) -> None:
        """Initialize the processor.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.data = []
    
    def process_measurement(self, data: np.ndarray) -> Dict[str, float]:
        """Process a single measurement.
        
        Args:
            data: Raw measurement data
            
        Returns:
            Processed measurement results
        """
        # Implementation here
        pass
```

### Frontend Code (HTML/CSS/JavaScript)

- Use consistent indentation (2 spaces)
- Follow BEM naming convention for CSS
- Use semantic HTML elements
- Write self-documenting JavaScript code
- Add comments for complex logic

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage
python -m pytest --cov=src

# Run specific test file
python -m pytest tests/test_measurement.py

# Run with verbose output
python -m pytest -v
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Test both success and failure cases
- Mock external dependencies
- Use fixtures for common setup

Example test:
```python
import pytest
from src.core.measurement import MeasurementProcessor


class TestMeasurementProcessor:
    """Test the MeasurementProcessor class."""
    
    def test_process_measurement_valid_data(self):
        """Test processing valid measurement data."""
        processor = MeasurementProcessor({})
        data = np.array([1.0, 2.0, 3.0])
        result = processor.process_measurement(data)
        
        assert result is not None
        assert 'mean' in result
        assert result['mean'] == 2.0
```

## 📚 Documentation

### Code Documentation

- Write clear docstrings for all functions
- Include type hints
- Provide usage examples
- Document exceptions and edge cases

### User Documentation

- Update README.md for user-facing changes
- Add screenshots for UI changes
- Include step-by-step instructions
- Provide troubleshooting guides

## 🔧 Development Tools

### Recommended IDE Setup

- **VS Code**: Install Python and PyQt6 extensions
- **PyCharm**: Configure for PyQt6 development
- **Vim/Emacs**: Use appropriate Python plugins

### Pre-commit Hooks

Install pre-commit hooks for code quality:
```bash
pip install pre-commit
pre-commit install
```

### Linting and Formatting

```bash
# Format code with black
black src/ tests/

# Check code style with flake8
flake8 src/ tests/

# Sort imports with isort
isort src/ tests/
```

## 🏗️ Project Structure

```
QuantumMeter Pro/
├── src/
│   ├── core/           # Core measurement logic
│   ├── gui/            # Desktop application
│   ├── web/            # Web dashboard
│   ├── ai/             # AI analysis modules
│   └── utils/          # Utility functions
├── tests/              # Test suite
├── docs/               # Documentation
├── config/             # Configuration files
└── data/               # Sample data
```

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the project's coding standards

### Communication

- Use GitHub Issues for discussions
- Be clear and concise in communications
- Ask questions when unsure
- Share knowledge and experiences

## 🎯 Areas for Contribution

### High Priority
- Bug fixes and performance improvements
- Documentation improvements
- Test coverage expansion
- UI/UX enhancements

### Medium Priority
- New measurement device support
- Additional export formats
- Advanced AI analysis features
- Mobile app development

### Low Priority
- Cosmetic improvements
- Additional language support
- Plugin system development
- Cloud integration features

## 📞 Getting Help

- **Issues**: [GitHub Issues](https://github.com/yourusername/quantum-meter-pro/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/quantum-meter-pro/discussions)
- **Email**: dev@quantum-meter-pro.com

## 🙏 Recognition

Contributors will be recognized in:
- The project's README.md file
- Release notes
- Contributor hall of fame
- Project documentation

Thank you for contributing to QuantumMeter Pro! 🚀
