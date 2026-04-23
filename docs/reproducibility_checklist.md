# Reproducibility Checklist

## Input Files Required
- sample_data.csv (located in the data/ folder)
- Windows Event Log files in EVTX/XML format

## Scripts to Be Executed
1. scripts/data_cleaning.py
2. scripts/benchmark_comparison.py
3. scripts/visualisation.py

## Execution Order
1. Run data_cleaning.py first to preprocess the dataset
2. Run benchmark_comparison.py to generate results
3. Run visualisation.py to generate plots

## Expected Output Files
- benchmark_results.csv
- comparison_plot.png
- score_distribution_histogram.png

## Software Dependencies
- Python 3.8 or above
- pandas
- matplotlib
- numpy
- evtx

Install all dependencies using:
    pip install -r requirements.txt

## Assumptions
- Logs follow the standard Windows Event Viewer XML/EVTX schema
- Python environment is set up correctly before running scripts
- Input CSV file contains columns: timestamp, event_id, source_ip, dest_ip

## Limitations
- Only tested on LANL dataset format
- Does not handle encrypted or compressed log files
- Performance may vary on machines with less than 8GB RAM
