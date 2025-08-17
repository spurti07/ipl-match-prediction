{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # IPL Team Performance Prediction and Strategic Analytics\
\
## Project Overview\
\
This project presents a comprehensive data-driven framework to analyze and predict team performance in the Indian Premier League (IPL) using advanced machine learning techniques. The core focus lies in understanding how player retention policies, auction investment strategies, and team composition influence IPL franchises' long-term success, specifically playoff qualification and championship wins.\
\
Leveraging a rich IPL dataset spanning 2008-2025 with detailed match, player, auction, and team information, the project employs longitudinal predictive modeling, explainable AI techniques, and novel composite metrics to derive actionable insights for franchise management and strategic decision-making.\
\
## Research Questions\
\
This study addresses four vital research questions:\
- **RQ1:** How do IPL team retention and auction investment practices affect long-run team performance?\
- **RQ2:** What are the predictive elements that influence the most appropriate investments in players by IPL teams between 2008 and 2025?\
- **RQ3:** What is the impact of team makeup (age, nationality mix, role specialization) on qualifying to the playoffs and winning championships?\
- **RQ4:** Is it possible to establish an aggregate Retention Effectiveness Index to quantify team strategy effectiveness?\
\
## Key Features\
\
- **Longitudinal Predictive Modeling:** Uses Random Forest classifiers with temporal validation to prevent data leakage and accurately predict playoff qualification outcomes (81% accuracy, 0.85 ROC-AUC)\
- **Strategic Feature Engineering:** Crafts meaningful features encapsulating retention rates, core player stability, role specialization (spinners, all-rounders), and auction spend efficiency\
- **Explainability & Interpretability:** Applies SHAP analysis and feature importance rankings to identify key performance drivers and translate insights into actionable strategies  \
- **Team Composition Analysis:** Employs K-Means clustering and PCA to discover successful team archetypes based on demographics and player roles\
- **Novel Metrics:** Introduces the Retention Effectiveness Index (REI) as a composite measure for evaluating franchise strategy effectiveness\
\
## Dataset\
\
- **Source:** Official IPL records and verified Kaggle repositories\
- **Scope:** 17 IPL seasons (2008-2025) with 278,204+ records\
- **Content:** Ball-by-ball match data, player statistics, auction details, team composition, venue information\
- **Size:** 107.54 MB with 64 engineered features\
\
## Technologies Used\
\
- **Python 3.12** - Core programming language\
- **Jupyter Notebook** - Interactive development environment  \
- **Pandas, NumPy** - Data processing and manipulation\
- **Scikit-learn** - Machine learning modeling and evaluation\
- **SHAP** - Model explainability and feature interpretation\
- **Matplotlib, Seaborn** - Data visualization and reporting\
\
## Project Structure\
\
}