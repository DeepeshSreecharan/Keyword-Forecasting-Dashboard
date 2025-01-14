# 📊 Keyword Trend Analysis Dashboard

A powerful, user-friendly web application that helps you track and visualize technology trends across different countries using Google Trends data. Perfect for market researchers, tech enthusiasts, and anyone interested in understanding global technology adoption patterns.We can search for any keyword by changing them in the python file.

## 🌟 What Can This Dashboard Do?

This tool helps you:
- Track popularity trends of different technologies and job roles
- Compare trends across multiple countries
- Visualize data through interactive graphs
- Download trend data for further analysis

## 🎯 Currently Tracking

We're currently monitoring these technology trends:
- 💼 Data Analyst (Career trend)
- ☕ Java (Programming language)
- 🤖 AI (Artificial Intelligence)

## 🗺️ Available Regions

Track trends in these countries:
- 🇺🇸 United States (US)
- 🇬🇧 United Kingdom (GB)
- 🇮🇳 India (IN)
- 🇧🇷 Brazil (BR)

## 🛠️ Setup Guide

### Step 1: System Requirements

Make sure you have:
- Python 3.7 or higher
- Stable internet connection
- 500MB free disk space

### Step 2: Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd keyword-trend-analysis
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Step 3: Configuration

No additional configuration needed! The application works out of the box with default settings.

## 🚀 How to Use

### Starting the Application

1. Open your terminal/command prompt
2. Navigate to the project directory
3. Run:
```bash
python app.py
```
4. Open your web browser and go to:
```
http://127.0.0.1:8050/
```

### Using the Dashboard

1. **Select Region**: 
   - Use the dropdown menu at the top to choose a country
   - The graph updates automatically when you change regions

2. **View Trends**:
   - Each keyword has its own color-coded line
   - Hover over lines to see exact values
   - Use the timeline slider to zoom in/out

3. **Interactive Features**:
   - Click legend items to show/hide specific keywords
   - Double-click to reset the view
   - Use the toolbar to download graphs as PNG files

## 📊 Data Details

### Data Collection
- Updates every time you run the application
- Collects last 12 months of trend data
- 5-second delay between API calls (prevents rate limiting)
- Automatically handles missing data

### Data Quality
- Real-time data from Google Trends
- Normalized values (0-100 scale)
- Handles timezone differences automatically
- Built-in error checking for data consistency

## 🔧 Technical Features

### Built With
- **Dash**: For web interface
- **Plotly**: For interactive graphs
- **Pandas**: For data handling
- **PyTrends**: For Google Trends API access
- **Prophet**: For trend analysis

### Error Handling
The application handles:
- 🌐 Network connection issues
- 📊 Missing or incomplete data
- ⏱️ API rate limits
- 🔄 Data type mismatches

## 💡 Tips for Best Results

1. **Optimal Performance**:
   - Run during off-peak hours for faster data collection
   - Close other browser tabs for smoother graph interactions

2. **Data Analysis**:
   - Compare related keywords for better insights
   - Consider seasonal trends in your analysis
   - Look for correlation between different regions

## 🤝 Contributing

Want to improve this dashboard? Here's how:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 👨‍💻 Author

Created with  by Deepesh Sreecharan M

## 🆘 Troubleshooting

Common issues and solutions:

1. **Graph not updating?**
   - Refresh the browser page
   - Check your internet connection

2. **Installation errors?**
   - Make sure Python version is compatible
   - Try creating a new virtual environment

3. **Slow performance?**
   - Check your internet speed
   - Reduce the number of browser tabs open

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting guide above
2. Search existing GitHub issues
3. Create a new issue with:
   - Detailed description of the problem
   - Steps to reproduce
   - Error messages
   - Your system information
