# Research Methodology

## Dataset Purpose
This project benchmarks two filtering strategies against the LANL Unified Network Logs to identify the most efficient method for RDP lateral movement detection.

## Data Cleaning Strategy
* **Handling Missing Values**: Rows with null timestamps or missing Event IDs were excluded.
* **Strategy Choice**: This ensures the benchmark measures the accuracy of the logic rather than the quality of the data.

## Visualizations Generated
* Execution time comparison (Strategy A vs. B).
* Precision-Recall curve for login event detection.

## Limitations
* The current benchmark is limited to RDP-specific event codes (4624, 1149).
