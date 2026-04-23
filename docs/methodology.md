# Research Methodology

## Dataset Purpose
This project benchmarks two RDP log filtering strategies (Keyword-based vs Event-ID-based)
against the LANL Unified Network Logs to identify the most efficient method
for detecting lateral movement.

## How Missing Values Were Handled
Missing values in the dataset were handled using a combination of:
- Mean imputation for small datasets with normally distributed values
- Median imputation for skewed distributions to reduce outlier influence

## Why That Strategy Was Chosen
Mean imputation preserves the overall average when data is symmetric.
Median imputation is more robust when outliers are present.
A combined strategy was used after resolving a conflict between both approaches.

## Visualisations Generated
- Score distribution histogram comparing both filtering strategies
- Bar chart showing false-positive rates of Keyword vs Event-ID filtering

## Limitations
- The benchmark is limited to Windows Event Viewer XML/EVTX log schema
- Results may vary with real-world noisy or incomplete log data
- Multi-threaded extraction methods have not yet been tested
