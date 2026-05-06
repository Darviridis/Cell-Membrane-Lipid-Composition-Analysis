import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv(r"C:\Users\Darya\Documents\Biology\membrane_data.csv")

# Pie chart — erythrocyte membrane composition
erythrocyte = df[df["cell_type"] == "Erythrocyte"].iloc[0]
lipids = ["PC", "PE", "SM", "Cholesterol", "Other"]
values = [erythrocyte[lip] for lip in lipids]

plt.figure(figsize=(7, 7))
plt.pie(values, labels=lipids, autopct="%1.1f%%")
plt.title("Erythrocyte Membrane Lipid Composition")
plt.savefig("erythrocyte_membrane.png")
plt.show()

# Bar chart — comparison of three cell types
df.set_index("cell_type")[lipids].plot(kind="bar", figsize=(10, 6))
plt.title("Lipid Composition of Cell Membranes")
plt.xlabel("Cell Type")
plt.ylabel("Percentage of Total Lipids")
plt.xticks(rotation=0)
plt.legend(loc="upper right")
plt.tight_layout()
plt.savefig("membrane_comparison.png")
plt.show()