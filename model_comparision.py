import competitive
import cooperative
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_scenario(q, n):
    demand = random.randint(int(0.8 * q), int(1.2 * q))
    disruptions = random.choices(
        ["None", "Delay", "Shortage", "Cost Surge"],
        weights=[0.7, 0.1, 0.1, 0.1],
        k=n
    )
    return demand, disruptions

def compare_models():
    # Input collection
    p = float(input("Enter market price of final product: "))
    c_s = float(input("Enter supplier's cost per unit: "))
    c_m = float(input("Enter manufacturer's cost per unit: "))
    q = int(input("Enter quantity of goods produced: "))
    n = int(input("Enter number of suppliers: "))
    storage_cost_per_unit = float(input("Enter storage cost per unit: "))
    p_m = float(input("Enter negotiated price between manufacturer and retailer: "))

    demand, disruptions = generate_scenario(q, n)
    
    competitive_results = competitive.run_competitive_model(
        p, c_s, c_m, q, disruptions, storage_cost_per_unit, p_m, demand
    )
    # Recalculate p_s_list to extract best supplier info
    demand_ratio = demand / q
    disruption_multipliers = {
        "None": 1.0,
        "Delay": 1.05,
        "Shortage": 1.1,
        "Cost Surge": 1.2
    }

    p_s_list = [
        competitive.competitive_supplier_pricing(c_s, demand_ratio, disruption_multipliers[event])
        for event in disruptions
    ]

    best_price = min(p_s_list)
    best_supplier_index = p_s_list.index(best_price) + 1  # 1-based index for readability

    print(f"\n--- Best Supplier Info ---")
    print(f"Supplier #{best_supplier_index} offered the lowest price: ${best_price:.2f} in competitive scenario")

    cooperative_results = cooperative.run_cooperative_model(
        p, c_s, c_m, q, disruptions, storage_cost_per_unit, p_m, demand
    )
    # Print results for debugging
    #print("Competitive Results:", competitive_results)
    #print("Cooperative Results:", cooperative_results)
    labels = ["Supplier Profit", "Manufacturer Profit", "Retailer Profit", 
          "Revenue", "Total Cost", "Gross Margin", "Satisfaction"]

    print("\n--- Competitive Results ---")
    for label, value in zip(labels, competitive_results):
      print(f"{label}: {value:.2f}")

    print("\n--- Cooperative Results ---")
    for label, value in zip(labels, cooperative_results):
        print(f"{label}: {value:.2f}")

    
    labels = ["Supplier Profit", "Manufacturer Profit", "Retailer Profit", 
              "Revenue", "Total Cost", "Gross Margin", "Satisfaction"]
    
    # Create figure with 4 subplots
    fig = plt.figure(figsize=(18, 10))
    fig.suptitle("Supply Chain Model Performance Analysis", fontsize=16, y=1.02)
    
    # Subplot 1: Competitive only (bar)
    ax1 = plt.subplot(2, 2, 1)
    bars = ax1.bar(labels, competitive_results, color='royalblue')
    ax1.set_title("Competitive Model Performance", pad=20)
    ax1.set_ylabel("Value ($)")
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,.0f}', ha='center', va='bottom')
    
    # Subplot 2: Cooperative only (bar)
    ax2 = plt.subplot(2, 2, 2)
    bars = ax2.bar(labels, cooperative_results, color='forestgreen')
    ax2.set_title("Cooperative Model Performance", pad=20)
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:,.0f}', ha='center', va='bottom')
    
    # Subplot 3: Side-by-side comparison (bar)
    ax3 = plt.subplot(2, 2, 3)
    x = np.arange(len(labels))
    width = 0.35
    bars1 = ax3.bar(x - width/2, competitive_results, width, label='Competitive', color='royalblue')
    bars2 = ax3.bar(x + width/2, cooperative_results, width, label='Cooperative', color='forestgreen')
    ax3.set_xticks(x)
    ax3.set_xticklabels(labels, rotation=45)
    ax3.set_ylabel("Value ($)")
    ax3.set_title("Direct Model Comparison")
    ax3.legend()
    ax3.grid(axis='y', linestyle='--', alpha=0.7)
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:,.0f}', ha='center', va='bottom', fontsize=8)
    
    # Subplot 4: Profit distribution comparison (stacked bar)
    ax4 = plt.subplot(2, 2, 4)
    profit_labels = ['Supplier', 'Manufacturer', 'Retailer']
    comp_profits = competitive_results[:3]
    coop_profits = cooperative_results[:3]
    
    ax4.bar(['Competitive'], comp_profits[0], label=profit_labels[0])
    ax4.bar(['Competitive'], comp_profits[1], bottom=comp_profits[0], label=profit_labels[1])
    ax4.bar(['Competitive'], comp_profits[2], bottom=comp_profits[0]+comp_profits[1], label=profit_labels[2])
    
    ax4.bar(['Cooperative'], coop_profits[0])
    ax4.bar(['Cooperative'], coop_profits[1], bottom=coop_profits[0])
    ax4.bar(['Cooperative'], coop_profits[2], bottom=coop_profits[0]+coop_profits[1])
    
    ax4.set_ylabel("Profit ($)")
    ax4.set_title("Profit Distribution by Stakeholder")
    ax4.legend()
    ax4.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    compare_models()

#sample input
#Enter market price of final product: 100
#Enter supplier's cost per unit: 20
#Enter manufacturer's cost per unit: 30
#Enter quantity of goods produced: 50
#Enter number of suppliers: 3
#Enter storage cost per unit: 2
#Enter negotiated price between manufacturer and retailer: 75