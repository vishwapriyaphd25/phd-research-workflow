# RDP Log Extraction Benchmark: Keyword vs. Event-ID Filtering

## Project Structure
- **docs/** — Research methodology, reproducibility checklist, and final reflection
- **scripts/** — Python scripts comparing extraction strategies (Strategy A vs B)
- **data/** — Sample dataset with missing values (sample_data.csv)
- **requirements.txt** — Python libraries needed to run the project
- **CITATION.md** — Citation information for this benchmarking study

## How to Run the Project
1. Install dependencies:
   pip install -r requirements.txt
2. Run data cleaning:
   python scripts/data_cleaning.py
3. Run the benchmark comparison:
   python scripts/benchmark_comparison.py
4. Generate visualisations:
   python scripts/visualisation.py

## Expected Outputs
- benchmark_results.csv — Performance comparison of both strategies
- comparison_plot.png — Bar chart of false-positive rates
- score_distribution_histogram.png — Score distribution across strategies

## Assumptions
- Logs follow the standard Windows Event Viewer XML/EVTX schema
- Missing values were handled using mean and median imputation strategies

## Future Scope
- Expand the benchmark to include multi-threaded extraction methods
- Test against additional log formats beyond EVTX
- Integrate automated anomaly detection pipelines
