# 🧠 Data Science Repository  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/) 
[![Tableau](https://img.shields.io/badge/Tableau-2022.1-orange?logo=tableau&logoColor=white)](https://www.tableau.com/) 
[![Data Visualization](https://img.shields.io/badge/Domain-Data_Visualization-lightgrey?logo=bar-chart&logoColor=white)](#) 
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

<br>

**A curated portfolio of original, high-quality data visualizations and analytical dashboards built in Python and Tableau.**  

These projects combine design integrity, interactivity, and reproducible analysis — ranging from NASA’s Near-Earth Objects to quantum-state visualizations.

<img src="https://github.com/sabneet95/Data-Science/blob/master/images/bains_project03_dashboard.jpg" alt="NEO Tableau Dashboard" width="800">

> *Note: These visualizations are primarily educational and research-oriented, intended to demonstrate analytical storytelling, interactivity, and design best practices.*


## 🧭 Table of Contents  

- [Overview](#overview)  
- [Projects](#projects)  
- [Architecture](#architecture)  
- [Requirements](#requirements)  
- [Usage](#usage)  
- [Testing](#testing)  
- [Contributing](#contributing)  
- [Author](#author)  
- [License](#license)  


## 🧩 Overview  

This repository showcases data-driven visualizations created during graduate-level studies in **Data Visualization**.  

Each project demonstrates the process of **data exploration → statistical analysis → visual encoding → interactive storytelling**, using both proprietary (Tableau) and open-source (Python) tools.


## 📊 Projects  

### **🪐 Project #1 — Visualization Critique**  
Redesign of a flawed *Kitchn* grocery-spending chart to illustrate perceptual balance and data integrity.  
Replaced a hybrid square chart with a functional pie chart labeled directly on slices.  

<img src="https://github.com/sabneet95/Data-Science/blob/master/images/Pie_Chart.png" width="280">


### **🌍 Project #2 — Data Exploration and Design**  
Exploration of NASA JPL Near-Earth Object (NEO) datasets.  

Proposed multiple visual designs — radar, bubble, histogram, and area plots — to assess asteroid proximity, rarity, and hazard size.  
Focus: *Analytical questioning → visual form evaluation → design justification.*


### **🛰 Project #3 — Interactive Visualization using Tableau**  
Interactive dashboard analyzing NEOs (1900 – 2200 CE) by approach distance, rarity, and diameter.  
Global filters interlink bubble, histogram, and area charts for cross-filtering.  

🔗 [View on Tableau Public](https://public.tableau.com/app/profile/sabneet.bains/viz/bains_project03/NEODashboard)  

<img src="https://github.com/sabneet95/Data-Science/blob/master/images/bains_project03_dashboard.jpg" width="600">


### **🐍 Project #4 — Interactive Visualization using Python**  
Three open-source dashboards built with **Matplotlib + Pandas** to replicate Tableau-style interactivity:  
1. **Electric Vehicle Range Analysis** — dual filters by manufacturer × category.  
   <img src="https://github.com/sabneet95/Data-Science/blob/master/images/Screenshot_sample01.jpeg" width="220">  
2. **YouTube Subscribers Analysis** — pie charts by category or country with adaptive labels.  
   <img src="https://github.com/sabneet95/Data-Science/blob/master/images/Screenshot_sample02.jpeg" width="220">  
3. **Job Recruitment vs Skills** — histograms comparing hired vs non-hired students across Python, SQL, ML, Tableau, and Excel.  
   <img src="https://github.com/sabneet95/Data-Science/blob/master/images/Screenshot_sample03.jpeg" width="220">

Each script uses `matplotlib.widgets.RadioButtons` for live filtering and descriptive statistics overlays.


### **⚛ Quantum Computing Visualization**  
Tableau-based **Bloch sphere simulator** illustrating single-qubit gate transformations (Pauli-X/Y/Z, Hadamard).  

Applies spherical trigonometry and rotation matrices to simulate quantum-state evolution.  

<img src="https://github.com/sabneet95/Data-Science/blob/master/images/bloch_anim.gif" width="280">


## 🧱 Architecture  

````text
Data-Science/
├── Tableau/
│   ├── Interactive_Visualization_using_Tableau.twbx
│   ├── Quantum_Computing_Visualization.twbx
│   └── Visualization_Critique/
├── Python/
│   ├── Sample1.py
│   ├── Sample2.py
│   ├── Sample3.py
│   └── datasets/
│       ├── Data1.csv
│       ├── Data2.csv
│       └── Data3.csv
├── R/
│   ├── Developer_Statistics.r
│   └── Stack_Overflow_2018_Developer_Public_Survey.csv
├── images/
│   ├── Pie_Chart.png
│   ├── bains_project03_dashboard.jpg
│   ├── Screenshot_sample01.jpeg
│   ├── Screenshot_sample02.jpeg
│   ├── Screenshot_sample03.jpeg
│   └── bloch_anim.gif
├── LICENSE
└── README.md
````


## ⚙️ Requirements  

- **Python 3.9 or later (64-bit)**  
  [Download Python](https://www.python.org/downloads/)  

- **Tableau 2022.1 or later**  
  [Download Tableau](https://www.tableau.com/)  

- **Python packages:**  
  ````bash
  pip install pandas numpy matplotlib
  ````


## 🚀 Usage  

1. Clone the repository:  
   ````bash
   git clone https://github.com/sabneet95/Data-Science.git
   cd Data-Science
   ````

2. Run any Python sample:  
   ````bash
   python Python/Sample1.py
   ````

3. Open Tableau workbooks in Tableau Public or Desktop.  

4. Interact with filters and explore the linked dashboards.


## 🧪 Testing  

<details>
<summary>Testing Status</summary>
  
Automated testing is not yet implemented.  
Future plans include integrating **pytest** for Python scripts and scripted validation dashboards in Tableau.  

</details>


## 🤝 Contributing  

1. Open an issue to discuss major changes.  
2. Follow existing documentation and style conventions.  
3. Submit pull requests with clear descriptions and, if possible, demo screenshots.  

> 💡 Contributors interested in **data storytelling**, **interactive visualization**, or **quantum simulation** are especially welcome.


## 🧠 Author  

**Sabneet Bains** — *Quantum × AI × Scientific Computing*  
[LinkedIn](https://www.linkedin.com/in/sabneet-bains/) • [GitHub](https://github.com/sabneet-bains)


## 📄 License  

This repository is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

