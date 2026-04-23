# Reproducibility Checklist

* **Input Files Required**: raw_event_logs.evtx or a parsed JSON equivalent.
* **Scripts to be Executed**: keyword_filter.py and eventid_filter.py.
* **Execution Order**: 1. Environment Setup -> 2. Data Load -> 3. Run Benchmark.
* **Expected Output Files**: benchmark_results.csv and comparison_plot.png.
* **Software Dependencies**: Python 3.9+ and dependencies listed in requirements.txt.
* **Assumptions**: Dataset is accessible in the /data directory.
* **Limitations**: Performance may vary based on CPU clock speed during file I/O.
