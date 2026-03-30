import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_visualizations():
    input_file = 'data/cleaned_data.csv'
    output_folder = 'results'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(df['student_id'].astype(str), df['experiment_score'], color='teal')
    plt.title('Student Performance: Experiment Scores')
    plt.savefig(f'{output_folder}/scores_bar_chart.png')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['temperature'], df['humidity'], color='darkorange')
    plt.title('Environmental Conditions: Temp vs Humidity')
    plt.savefig(f'{output_folder}/temp_humidity_scatter.png')
    print("Visualisation complete. Check results/ folder.")

if __name__ == "__main__":
    generate_visualizations()