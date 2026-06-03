# Mining Telemetry Simulator

A Python-based Operational Technology (OT) simulator that generates and monitors real-time industrial telemetry data with automated safety threshold alerting. 

Built as a submission for the Stardance x NASA Hackathon.

## Overview
In industrial environments, monitoring equipment health is critical to preventing downtime and physical damage. This project simulates a live data feed from a heavy mining drill. It generates randomized, realistic values for core hardware metrics and outputs them to the console, mimicking a live Operational Technology (OT) telemetry stream. 

## Features
* **Live Data Generation:** Simulates Engine Temperature (C), Vibration levels (g), and Hydraulic Pressure (kPa).
* **Real-time Output:** Streams new data points every 2 seconds.
* **Automated Alerting:** Includes a logic trigger that instantly outputs a critical warning if the engine temperature exceeds safe operational thresholds (120C).

## Technologies Used
* Python 3 (Built-in `random` and `time` modules)

## How to Run
1. Clone this repository to your local machine.
2. Open a terminal in the project directory.
3. Run the script using the following command:
`python simulator.py`
