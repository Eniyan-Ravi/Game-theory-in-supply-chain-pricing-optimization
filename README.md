# Supply Chain Model Comparison

This project provides a Python-based simulation to compare the performance of two fundamental supply chain strategies: a **competitive model** and a **cooperative model**. By simulating a single-run scenario with a variety of potential supply chain disruptions, the script analyzes and visualizes key metrics like stakeholder profits, total revenue, and overall gross margin.

-----

## Core Concepts

The simulation models a simple supply chain with three main stakeholders:

  - **Suppliers**: The source of raw materials.
  - **Manufacturer**: Buys materials from suppliers and produces the final goods.
  - **Retailer**: Sells the final product to the market.

The core difference lies in the pricing and profit dynamics of the two models:

### Competitive Model

In this model, suppliers act independently to set their prices based on market conditions, such as demand and disruption events. The goal is to maximize individual profit, which can lead to price variations and potential instability for the manufacturer and the entire supply chain.

### Cooperative Model

This model assumes a more integrated approach. Supplier pricing is based on a fixed markup over their costs, promoting a shared-benefit structure. The retailer's discounting strategy is also more controlled, aiming to protect overall chain profitability and stakeholder satisfaction.

-----

## How It Works

The project consists of three Python scripts that work together:

1.  **`competitive.py`**: Contains the logic for the competitive supply chain model. It calculates individual supplier prices, stakeholder profits, and a satisfaction score based on aggressive, market-driven behavior.
2.  **`cooperative.py`**: Contains the logic for the cooperative supply chain model. It calculates profits based on a collaborative pricing approach and includes a satisfaction score that accounts for shared goals.
3.  **`model_comparision.py`**: This is the main script.
      - It prompts the user to input key parameters of the supply chain, such as costs, prices, and quantity.
      - It simulates a single random scenario by generating demand and introducing potential disruptions (e.g., "Delay," "Shortage," "Cost Surge").
      - It runs the simulation for both the competitive and cooperative models using the imported logic.
      - Finally, it prints a detailed summary of the results for both models and generates four comparative plots using `matplotlib`.

-----

## Getting Started

Follow these steps to run the simulation on your local machine.

### Prerequisites

You need Python installed, along with a few standard libraries. You can install them using `pip`:

```bash
pip install numpy matplotlib
```

### Usage

1.  Ensure all three files (`cooperative.py`, `competitive.py`, and `model_comparision.py`) are in the same directory.

2.  Open your terminal or command prompt.

3.  Run the main script using the Python interpreter:

    ```bash
    python model_comparision.py
    ```

4.  Follow the on-screen prompts to enter the required supply chain parameters.

### Example Scenario

You can use the following sample inputs to get a feel for the simulation:

  - **Enter market price of final product**: `100`
  - **Enter supplier's cost per unit**: `20`
  - **Enter manufacturer's cost per unit**: `30`
  - **Enter quantity of goods produced**: `50`
  - **Enter number of suppliers**: `3`
  - **Enter storage cost per unit**: `2`
  - **Enter negotiated price between manufacturer and retailer**: `75`

-----

## Output

After running the script, you will see a detailed analysis printed directly to your console, followed by four plots that visually summarize the results:

1.  **Competitive Model Performance**: A bar chart showing profits, revenue, and costs for the competitive scenario.
2.  **Cooperative Model Performance**: A bar chart for the cooperative scenario.
3.  **Direct Model Comparison**: A side-by-side bar chart that allows for a direct comparison of key metrics.
4.  **Profit Distribution by Stakeholder**: A stacked bar chart that clearly illustrates how profits are distributed among the supplier, manufacturer, and retailer in each model.
