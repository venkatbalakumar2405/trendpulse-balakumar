import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations():
    # Load the cleaned data
    df = pd.read_csv("data/cleaned_trends.csv")

    # Set the visual style
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # 1. Top 10 Authors by Story Count
    top_authors = df['author'].value_counts().head(10)
    sns.barplot(x=top_authors.values, y=top_authors.index, ax=axes[0], palette="viridis")
    axes[0].set_title('Top 10 Authors by Number of Stories', fontsize=14)
    axes[0].set_xlabel('Count')
    axes[0].set_ylabel('Author')

    # 2. Distribution of Scores (Engagement)
    sns.histplot(df['score'], bins=20, kde=True, ax=axes[1], color="salmon")
    axes[1].set_title('Distribution of Story Scores', fontsize=14)
    axes[1].set_xlabel('Score (Upvotes)')
    axes[1].set_ylabel('Frequency')

    plt.tight_layout()
    
    # Save the visualization
    plt.savefig("data/trend_analysis.png")
    print("Visualizations saved to data/trend_analysis.png")
    plt.show()

if __name__ == "__main__":
    generate_visualizations()
