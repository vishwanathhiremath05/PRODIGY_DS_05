

📊 **PRODIGY\_DS\_05 – Road Accident Pattern Analysis and Visualization in India**

This project performs **exploratory data analysis and visualization** on an Indian accident dataset using Python. It extracts temporal and categorical patterns from road accident data and visualizes key insights related to severity, time, weather, and road conditions.

🔍 **Key Features:**

🧹 **Data Preprocessing**

* Loads real-world accident data from a CSV file (`accident_prediction_india.csv`)
* Parses and extracts useful datetime features:

  * `Hour` from the "Time of Day" field
  * Full `Date` from year, month, and day-of-week
  * Standardizes `DayOfWeek` for temporal analysis

📊 **Visualizations**

* **Severity Distribution**: Bar chart showing the frequency of accidents by severity level
* **Weekly Trend**: Bar plot of accident counts across days of the week
* **Hourly Distribution**: Histogram displaying accidents across different hours of the day
* **Top Weather Conditions**: Horizontal bar plot showing top 10 weather conditions during accidents
* **Road Condition Impact**: Bar chart categorizing accidents by road surface conditions

🎨 **Visualization Tools**
Utilizes **Seaborn** and **Matplotlib** for high-quality statistical plots and layout control. Uses `palette` styling for improved visual aesthetics.

📁 **Dataset File Used**:

* `accident_prediction_india.csv`
  📌 *Source: Real-world accident prediction dataset (user local directory)*

📸 **Visual Outputs**:

* Accidents by Severity – Categorical bar chart
* Accidents by Day of the Week – Weekly trend plot
* Accidents by Hour of the Day – Temporal histogram
* Top Weather Conditions – Horizontal frequency plot
* Accidents by Road Condition – Road surface analysis plot

🚀 **How to Run**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AmarHGit/PRODIGY_DS_05.git  
   cd PRODIGY_DS_05
   ```

2. **Install Required Libraries**

   ```bash
   pip install pandas matplotlib seaborn plotly
   ```

3. **Run the Script**

   ```bash
   python accident_analysis.py
   ```

The script will:

* Load and preprocess the accident dataset
* Generate insightful visualizations
* Display them interactively using `matplotlib`

