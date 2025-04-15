import seaborn as sns
import matplotlib.pyplot as plt

def analyze_penguins():

    penguins = sns.load_dataset("penguins")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.scatterplot(data=penguins, 
                   x="flipper_length_mm", 
                   y="bill_length_mm",
                   hue="species",
                   style="species",
                   ax=ax1)
    
    ax1.set_title("Penguin Bill vs. Flipper Length")
    ax1.set_xlabel("Flipper Length (mm)")
    ax1.set_ylabel("Bill Length (mm)")
    
    sns.histplot(data=penguins,
                x="body_mass_g",
                hue="species",
                multiple="stack",
                ax=ax2)
    
    ax2.set_title("Penguin Body Mass Distribution")
    ax2.set_xlabel("Body Mass (g)")
    ax2.set_ylabel("Count")
    
    plt.tight_layout()
    
    plt.show()

if __name__ == "__main__":
    analyze_penguins()
