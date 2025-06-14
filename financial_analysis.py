import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load dataset ---
df = pd.read_csv(r"C:\Users\satya\OneDrive\Desktop\Self Project\Banking.csv")

# --- Dataset info ---
print("DATASET INFO:")
print(df.info())

# --- Sample data ---
print("\nSAMPLE DATA:")
print(df.head())

# --- Summary statistics ---
print("\nSUMMARY STATISTICS:")
print(df.describe())

# --- Scatter plot: Estimated Income vs Credit Card Balance ---
plt.figure(figsize=(8,5))
sns.scatterplot(x='Estimated Income', y='Credit Card Balance', data=df)
plt.title('Estimated Income vs Credit Card Balance')
plt.xlabel('Estimated Income')
plt.ylabel('Credit Card Balance')
plt.grid(True)
plt.savefig("estimated_income_vs_cc_balance.png", dpi=300, bbox_inches='tight')
plt.show()

# --- Bar plot: Average Bank Deposits by Risk Weighting ---
risk_deposits = df.groupby('Risk Weighting')['Bank Deposits'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(
    x='Risk Weighting',
    y='Bank Deposits',
    data=risk_deposits,
    hue='Risk Weighting',
    palette='viridis',
    legend=False
)
plt.title('Average Bank Deposits by Risk Weighting')
plt.xlabel('Risk Weighting')
plt.ylabel('Average Bank Deposits')
plt.grid(True)
plt.savefig("bank_deposits_by_risk.png", dpi=300, bbox_inches='tight')
plt.show()

# --- Bar plot: Average Bank Loans by Properties Owned ---
properties_loans = df.groupby('Properties Owned')['Bank Loans'].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(
    x='Properties Owned',
    y='Bank Loans',
    data=properties_loans,
    hue='Properties Owned',
    palette='coolwarm',
    legend=False
)
plt.title('Average Bank Loans by Properties Owned')
plt.xlabel('Properties Owned')
plt.ylabel('Average Bank Loans')
plt.grid(True)
plt.savefig("bank_loans_by_properties.png", dpi=300, bbox_inches='tight')
plt.show()

# --- Correlation heatmap (numeric columns only) ---
numeric_df = df.select_dtypes(include=['number'])

plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Heatmap of Numeric Features')
plt.savefig("correlation_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add your report content
pdf.cell(200, 10, txt="Financial Behavior Analysis Report", ln=True, align='C')
pdf.cell(200, 10, txt="Summary Statistics:", ln=True, align='L')

# Example: Add one line of data
pdf.multi_cell(0, 10, txt=str(df.describe()))

# Save the PDF
pdf.output("financial_report.pdf")

print("PDF report generated successfully!")
