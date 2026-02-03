
# Player Segmentation & Behavioral Persona Analytics

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

## 🎮 Executive Summary

A comprehensive player segmentation system analyzing **50,000+ players** to create actionable behavioral personas for game design, marketing, and LiveOps optimization. This project demonstrates advanced SQL analytics, machine learning clustering, and interactive dashboard development.

### Key Findings

| Metric | Value |
|--------|-------|
| **Total Players Analyzed** | 50,000 |
| **Distinct Personas Identified** | 7 |
| **ML Clusters Discovered** | 6 |
| **Total Revenue Tracked** | $2.09M |

> **🐋 Critical Insight:** The "Whale Walter" persona represents only **3.6% of players** but contributes **86.6% of total revenue** - highlighting the importance of VIP retention strategies.

---

## 📊 Personas Discovered

| Persona | Population | Avg LTV | Avg Playtime | Key Characteristic |
|---------|------------|---------|--------------|-------------------|
| 🐋 **Whale Walter** | 3.6% | $997.82 | 172.8h | High spender, premium content buyer |
| ⚔️ **Competitive Carl** | 25.8% | $9.43 | 123.2h | Hardcore PvP, skill-focused |
| 🗺️ **Explorer Emma** | 37.9% | $3.25 | 29.7h | Story-driven, thorough explorer |
| 📱 **Casual Casey** | 31.1% | $2.48 | 14.5h | Mobile player, short sessions |
| 🏆 **Collector Chris** | 1.0% | $84.19 | 93.2h | Achievement hunter, cosmetic lover |
| 👥 **Social Sara** | 0.3% | $105.77 | 122.0h | Community-driven, plays with friends |
| ⏰ **Weekend Warrior Will** | 0.2% | $3.17 | 55.5h | Limited time, intense weekend sessions |

---

## 🔍 Technical Approach

### Data Pipeline
```
Synthetic Generation → SQLite Database → SQL Segmentation → ML Clustering → Interactive Dashboards
      (50K players)         (7 tables)      (12 RFM segments)   (6 clusters)     (3 dashboards)
```

### Segmentation Methods

1. **Behavioral Segmentation (SQL)**
   - Engagement levels: Trial → Light → Casual → Regular → Hardcore
   - Monetization tiers: Free → Minnow → Dolphin → Whale
   - Play styles: Competitive, Social Player, Solo Explorer, Team Player

2. **RFM Analysis**
   - Recency: Days since last login
   - Frequency: Sessions per week
   - Monetary: Lifetime value
   - 12 strategic segments (Champions, At Risk, Lost Whales, etc.)

3. **ML Clustering (K-Means)**
   - 11 behavioral features
   - Optimal k=6 (silhouette score: 0.33)
   - PCA visualization (65.2% variance explained)

---

## 📁 Project Structure

```
player-segmentation-project/
├── data/
│   ├── generate_data.py          # Synthetic data generator
│   ├── player_analytics.db       # SQLite database (50K players)
│   └── segments/                 # ML cluster outputs
├── sql/
│   ├── schema/schema.sql         # 7-table database schema
│   ├── segmentation/
│   │   ├── behavioral_segments.sql
│   │   ├── rfm_analysis.sql
│   │   └── persona_profiles.sql
│   └── analysis/
│       ├── retention_by_segment.sql
│       ├── ltv_analysis.sql
│       └── feature_engagement.sql
├── notebooks/
│   └── ml_clustering.py          # K-Means clustering analysis
├── dashboards/
│   ├── segment_overview.html     # Executive overview
│   ├── persona_deepdive.html     # Individual persona analysis
│   ├── performance_comparison.html # Cross-persona comparison
│   └── assets/                   # JSON data files
└── reports/
    └── persona_playbooks/        # Strategy documents
```

---

## 🛠️ Technologies Used

- **Database:** SQLite with 7 interconnected tables
- **SQL:** Advanced CTEs, window functions (NTILE, ROW_NUMBER), aggregations
- **Python:** pandas, scikit-learn (KMeans, PCA, StandardScaler), matplotlib, seaborn
- **Visualization:** Chart.js interactive dashboards with modern dark theme
- **Statistical Analysis:** Silhouette scoring, elbow method optimization

---

## 💡 Business Insights & Recommendations

### Revenue Optimization
- **Top 1% of payers** generate **60%+ of revenue** - implement VIP loyalty programs
- **Whale Walter** segment has **$997.82 average LTV** - prioritize retention over acquisition

### Engagement Optimization
- **Competitive Carl** has highest PvP ratio (52%) - focus on ranked features and esports content
- **Explorer Emma** (largest segment) responds well to story content and achievements

### Churn Prevention
- **"At Risk"** RFM segment contains **1,361 players** - immediate re-engagement needed
- **"Lost Whales"** segment represents **$0 current revenue** from previously high-value players

---

## 🚀 Quick Start

### View Dashboards
```bash
cd dashboards
python3 -m http.server 8000
# Open http://localhost:8000/segment_overview.html
```

### Run SQL Analysis
```bash
sqlite3 data/player_analytics.db < sql/segmentation/persona_profiles.sql
```

### Run ML Clustering
```bash
python3 notebooks/ml_clustering.py
```

---

## 📈 Skills Demonstrated

- ✅ **Advanced SQL** - CTEs, window functions, complex aggregations, multi-table joins
- ✅ **Data Modeling** - 7-table relational schema with proper constraints
- ✅ **Statistical Segmentation** - RFM analysis, behavioral clustering
- ✅ **Machine Learning** - K-Means clustering with validation
- ✅ **Data Visualization** - Interactive Chart.js dashboards
- ✅ **Business Analytics** - Actionable insights and recommendations

---

## 📄 Resume Bullet Points

> "Developed a player segmentation model analyzing 50K+ users, identifying 7 distinct personas where top 3.6% of players drove 86.6% of revenue"

> "Built SQL-based RFM segmentation system classifying players into 12 actionable segments using advanced window functions and CTEs"

> "Created interactive Chart.js dashboards visualizing player persona characteristics with strategy matrix and radar chart comparisons"

> "Performed K-Means clustering on 11 behavioral features, achieving 0.33 silhouette score with PCA visualization explaining 65% of variance"

---

## 📞 Contact

Built by **[Your Name]** for gaming industry analytics portfolio demonstration.

*This project uses synthetic data generated to match realistic gaming industry patterns.*
