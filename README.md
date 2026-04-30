Predictive Maintenance for Industrial Equipment
Project Overview
This project focuses on Predictive Maintenance using machine learning to predict machine failures before they occur. By analyzing sensor data (Temperature, Torque, Speed), we aim to minimize downtime and prevent catastrophic mechanical failures.
Key Engineering Features (Feature Engineering)
Unlike basic models, this project utilizes physical engineering principles to enhance prediction accuracy:
Temperature Difference (temp_diff): Calculated as the delta between Process and Ambient temperature to monitor cooling efficiency.
Mechanical Power (power): Derived from the relationship Power=Torque×Speed, serving as a core indicator of engine load.
Tool Wear Monitoring: Tracking the cumulative usage time of equipment to predict failure points.
Model Performance & Strategy
Algorithm: Random Forest Classifier (100 Trees) with balanced class weights to handle data imbalance.
Recall Optimization: The decision threshold was tuned to 0.2 to prioritize Recall (0.68). In industrial maintenance, catching a potential failure (Recall) is more critical than occasional false alarms (Precision).