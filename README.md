# RDP Log Extraction Benchmark: Keyword vs. Event-ID Filtering

## Project Structure
* **docs/**: Contains the research methodology and reproducibility guides.
* **scripts/**: Python scripts comparing extraction logic (Strategy A vs. Strategy B).
* **requirements.txt**: List of Python libraries needed for the benchmark.
* **CITATION.md**: Citation information for this benchmarking study.

## How to Run the Project
1. Install dependencies: `pip install -r requirements.txt`
2. Run the comparison script: `python scripts/benchmark_comparison.py`
3. **Expected Outputs**: Performance logs and a comparison chart showing accuracy/speed.

## Assumptions & Visualization
* **Assumptions**: We assume logs follow the standard Windows Event Viewer XML/EVTX schema.
* **Visualization**: A bar chart comparing the false-positive rates of each strategy.

## Future Scope
* Expanding the benchmark to include multi-threaded extraction methods.
