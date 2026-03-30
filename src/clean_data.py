import pandas as pd
import os

def clean_data():
    # Define file paths
    input_path = 'data/sample_data.csv'
    output_path = 'data/cleaned_data.csv'
    
    # Step 7: Read the data
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Please ensure you created the sample data.")
        return

    df = pd.read_csv(input_path)
    
    print("--- Initial Data Summary ---")
    print(df.info())
    
    # Detect missing values
    missing_counts = df.isnull().sum()
    print("\n--- Missing Values Detected per Column ---")
    print(missing_counts)
    
    # Fill missing numeric values with the mean of the column
    # student_id is an identifier, so we focus on the experiment and environmental data
    numeric_cols = ['experiment_score', 'temperature', 'humidity']
    
    for col in numeric_cols:
        if col in df.columns:
            mean_value = df[col].mean()
            df[col] = df[col].fillna(mean_value)
            print(f"Filled missing values in '{col}' with mean: {mean_value:.2f}")

    # Save the cleaned file
    df.to_csv(output_path, index=False)
    print(f"\nSuccess: Cleaned data saved as {output_path}")

if __name__ == "__main__":
    clean_data()