import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize():
    df = pd.read_csv("data/clean_trends.csv")
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='category', palette='magma')
    plt.title("TrendPulse: Stories per Category")
    plt.savefig("data/trends_chart.png")
    print("Task 4: Visualization saved to data/trends_chart.png")
    plt.show()

if __name__ == "__main__": visualize()
