# Blockchain Fraud Detection System
A fraud detection system that analyzes Ethereum blockchain transactions to identify potentially fraudulent activity. It collects, stores, and analyzes 1 million+ transactions using blockchain data science, machine learning, and SQL-based rule detection.

📍 Frank Seely | Data Science @ Boston University   
Portfolio: https://seelyfrank.github.io/webportfolio/  
Email: seelyfrank@gmail.com  
LinkedIn: https://www.linkedin.com/in/frank-seely/  

## Technical Skills (to be) Used
- [x] Blockchain Data Engineering – Fetching transactions from Ethereum using ethers.js.  
- [x] Database Management (MySQL) – Storing blockchain transactions for structured analysis.  
- [x] Data Analysis (Python, Pandas, SQL) – Extracting insights from transaction data.  
- [x] Machine Learning (Unsupervised Anomaly Detection) – Detecting fraud without labeled data.  
- [x] Full-Stack Development (Node.js, JavaScript) – Backend integration with MySQL and blockchain.  
- [x] APIs (Alchemy, Ethers) – Fetching live blockchain data.  
- [ ] Data Visualization (Power BI, Matplotlib, Seaborn) – Presenting fraud detection insights.  

## Project Architecture
#### ✅ Step 1: Collect Transactions 🪙

The deploy.js script fetches, stores, and manages Ethereum blockchain transactions in a structured database for fraud detection analysis. It serves as the data pipeline that collects live transaction data, ensuring the system has a continuous  dataset for analysis.

#### 🔵 Step 2: Exploratory Data Analysis (EDA)

Analyze transaction volumes, wallet activity, and gas usage.
Identify high-value transactions and abnormal behavior.

#### 🔵 Step 3: Fraud Detection (Rules-Based & Machine Learning)

SQL-based heuristics to flag repetitive, high-value, or unusual transactions.
Unsupervised ML (Isolation Forest, DBSCAN) for anomaly detection.

#### 🔵 Step 4: Dashboard & Reporting

Visualizing fraud patterns in Power BI / Python Matplotlib.
Creating fraud detection reports for further investigation.


### Long-Term Goals
 Train an ML model for fraud classification (Unsupervised Learning) or use Anomaly Detection
 Deploy a real-time fraud detection API
 Build an interactive Power BI dashboard
 Integrate real-time alerts for suspicious transactions
