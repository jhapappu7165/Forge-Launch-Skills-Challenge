# Forge Launch Skills Challenge

## Overview

The **"Spam Message Data Analysis"** project analyzes a public SMS dataset containing messages labeled as **ham (normal)** or **spam (promotional)**.

It was created for the **Forge Launch Skills Challenge**, following the required steps of **data cleaning**, **exploration**, and **visualization** using Python.

---

## How To Run
1. **Install dependencies**
   pip install -r requirements.txt

2. **Run the analysis**
    python analysis.py

3. **View results**
    Console output → basic dataset stats & insights
    figs/ folder → generated visualizations

## Key Steps in the Analysis

1. **Data Cleaning**

- Renamed columns (Category → label, Message → message)
- Lowercased and removed punctuation
- Removed missing values

2. **Feature Engineering**

- Calculated char_count and word_count for each message

3. **Visualization**
- Message category distribution
- Word count distribution by class
- Character count comparison (boxplot)

## Insights

- Dataset contains **5,572 messages (≈ 13% spam).**
- Spam messages are typically longer and include promotional phrases.
- Ham messages are shorter and conversational.

## Tools Used

- Python 3.12
- pandas, matplotlib, seaborn

Prepared by [**Pappu Jha**](https://jhapappu.com.np/) for the Forge Launch Skills Challenge.