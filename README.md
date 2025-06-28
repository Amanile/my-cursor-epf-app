# 💰 EPF Calculator Web Application

<div align="center">

![EPF Calculator](https://img.shields.io/badge/EPF-Calculator-orange)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.3+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**A modern, responsive Employees' Provident Fund (EPF) Calculator built with Python Flask and Tailwind CSS**

*Calculate your EPF maturity amount with interactive sliders, real-time updates, and detailed year-wise breakdown*

[🚀 Live Demo](#) | [📖 Documentation](#features) | [🐛 Report Bug](../../issues) | [💡 Request Feature](../../issues)

</div>

---

## 📸 Screenshots

<div align="center">
<img src="https://via.placeholder.com/800x400/f97316/ffffff?text=EPF+Calculator+Screenshot" alt="EPF Calculator Interface" width="80%">
</div>

---

A responsive Employees' Provident Fund (EPF) Calculator built with Python Flask and Tailwind CSS, inspired by the design style of emicalculator.net.

## ✨ Features

### 🎯 Core Functionality
- 🧮 **Accurate EPF Calculations**: Calculate your EPF maturity amount using compound interest
- 📊 **Interactive Charts**: Visual representation of EPF growth with pie charts
- 📈 **Year-wise Breakdown**: Detailed table showing annual contributions, interest, and balance
- 💰 **Indian Currency Format**: All amounts displayed with Indian Rupee (₹) symbol and Lakh/Crore notation

### 🎨 Modern Design
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- 🎚️ **Interactive Sliders**: Orange-themed range sliders with real-time value updates
- 🌐 **Cross-Browser Compatible**: Tested and working on Chrome, Firefox, Opera, Safari
- ✨ **Smooth Animations**: Professional transitions and hover effects
- 🎪 **Modern UI**: Clean interface inspired by emicalculator.net design

### 🚀 User Experience
- ⚡ **Real-time Calculations**: Instant updates as you adjust sliders
- 🔄 **Dynamic Sync**: Sliders and input fields automatically sync
- 📋 **Tab Navigation**: Easy navigation between Home, EPF Calculator, and About pages
- 📊 **Visual Feedback**: Color-coded charts and progress indicators

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: Tailwind CSS
- **Charts**: Chart.js
- **Icons**: Heroicons (via Tailwind CSS)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd calculator
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv epf_calculator_env
   source epf_calculator_env/bin/activate  # On Windows: epf_calculator_env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to `http://localhost:5000`

## Usage

### EPF Calculator Inputs

- **Monthly Salary (Basic + DA)**: Your monthly basic salary plus dearness allowance
- **Current Age**: Your current age in years
- **Contribution to EPF (%)**: Total EPF contribution percentage (default: 24% - 12% employee + 12% employer)
- **Annual Salary Increase (%)**: Expected annual increment in salary
- **Rate of Interest (%)**: Current EPF interest rate (default: 8.25% for FY 2023-24)
- **Retirement Age**: Age at which you plan to retire

### Results

The calculator provides:

1. **Summary Cards**:
   - Final EPF maturity amount
   - Total contributions made
   - Total interest earned

2. **Interactive Charts**:
   - Line chart showing EPF growth over time
   - Bar chart for year-wise comparison
   - Toggle between chart types

3. **Detailed Table**:
   - Year-wise breakdown of contributions
   - Annual interest earned
   - Running EPF balance

## EPF Calculation Logic

The calculator uses the following formula for EPF calculation:

1. **Annual Contribution** = Monthly Salary × 12 × (EPF Contribution Rate / 100)
2. **Interest Earned** = Previous Year Balance × (Interest Rate / 100)
3. **New Balance** = Previous Balance + Annual Contribution + Interest Earned
4. **Salary Growth** = Previous Salary × (1 + Annual Increase Rate / 100)

## File Structure

```
calculator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    ├── base.html         # Base template with common layout
    ├── index.html        # Home page
    ├── epf_calculator.html # EPF calculator page
    └── about.html        # About page
```

## API Endpoints

- `GET /` - Home page
- `GET /epf-calculator` - EPF calculator page
- `GET /about` - About page
- `POST /calculate-epf` - API endpoint for EPF calculations (JSON)

## Browser Support

- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 **Fork the repository**
2. 🌱 **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. 💡 **Make your changes**
4. ✅ **Add tests if applicable**
5. 📝 **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
6. 🚀 **Push to the branch** (`git push origin feature/AmazingFeature`)
7. 🎯 **Open a Pull Request**

### Development Setup
```bash
git clone https://github.com/yourusername/epf-calculator.git
cd epf-calculator
pip install -r requirements.txt
python app.py
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🚀 Deployment

Ready to share your EPF Calculator with the world? This project is configured for easy deployment to popular platforms.

### 🎯 Recommended: Vercel (FREE & INSTANT)
- ⚡ **Instant Deployment**: 1-click deploy from GitHub
- 🌍 **Global CDN**: Lightning-fast worldwide
- 🔒 **Automatic HTTPS**: Secure by default
- 📊 **Real-time Analytics**: Built-in monitoring

**👉 [Deploy to Vercel](https://vercel.com/new)** - See [VERCEL_DEPLOYMENT_GUIDE.md](VERCEL_DEPLOYMENT_GUIDE.md) for detailed instructions.

### Other Deployment Options:
- **GitHub Pages**: For static hosting  
- **Herokuapp**: For full-stack hosting
- **Netlify**: For JAMstack deployment
- **AWS**: For scalable cloud hosting

For GitHub setup, see [GITHUB_UPLOAD_GUIDE.md](GITHUB_UPLOAD_GUIDE.md)

## ⚠️ Disclaimer

This calculator provides estimated calculations based on the inputs provided and current EPF rules. Actual EPF returns may vary due to changes in interest rates, government policies, and individual circumstances. Please consult with financial advisors or EPFO officials for personalized advice and accurate information about your EPF account.

## 🆘 Support

If you encounter any issues or have questions:

- 🐛 **Bug Reports**: [Create an issue](../../issues/new?template=bug_report.md)
- 💡 **Feature Requests**: [Request a feature](../../issues/new?template=feature_request.md)
- 💬 **Questions**: [Start a discussion](../../discussions)
- 📧 **Email**: [your-email@example.com](mailto:your-email@example.com)

## ⭐ Star History

If this project helped you, please consider giving it a ⭐ star on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/epf-calculator&type=Date)](https://star-history.com/#yourusername/epf-calculator&Date)

---

<div align="center">

**🎯 Happy Calculating! 🎯**

Made with ❤️ in India 🇮🇳

</div> 