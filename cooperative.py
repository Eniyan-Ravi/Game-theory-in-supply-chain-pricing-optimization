import random

def retailer_discounting(p, demand, q):
    if demand < q:
        discount = min(0.05, (q - demand) / q)
        p *= (1 - discount)
    return p

def cooperative_supplier_pricing(base_c_s, disruption_multiplier=1.0):
    markup = random.uniform(5, 12)
    return base_c_s * (1 + markup / 100) * disruption_multiplier

def calculate_cooperative_profits(p, avg_c_s, c_m, q, p_m, demand, storage_cost_per_unit):
    q_sold = min(q, demand)
    unsold = max(0, q - demand)
    
    pi_s = (p_m - avg_c_s) * q_sold
    pi_m = (p_m - avg_c_s - c_m) * q_sold - unsold * (c_m + storage_cost_per_unit)
    pi_r = (p - p_m) * q_sold
    
    revenue = p * q_sold
    total_cost = avg_c_s * q_sold + c_m * q_sold + unsold * storage_cost_per_unit
    
    return [pi_s, pi_m, pi_r, revenue, total_cost, revenue - total_cost]

def run_cooperative_model(p, base_c_s, c_m, q, disruptions, storage_cost_per_unit, p_m, demand):
    disruption_multipliers = {
        "None": 1.0,
        "Delay": 1.05,
        "Shortage": 1.1,
        "Cost Surge": 1.2
    }
    
    c_s_list = [
        base_c_s * random.uniform(0.95, 1.05) * disruption_multipliers[event]
        for event in disruptions
    ]
    
    avg_c_s = sum(c_s_list) / len(c_s_list)
    p = retailer_discounting(p, demand, q)
    results = calculate_cooperative_profits(p, avg_c_s, c_m, q, p_m, demand, storage_cost_per_unit)
    
    reliability_penalty = (
        disruptions.count("Shortage") * 10 + 
        disruptions.count("Delay") * 7
    )
    satisfaction = max(0, min(100, (100 - (p - p_m) * 1.5 + (demand / q) * 100 + (90 - reliability_penalty)) / 3))
    
    return results + [satisfaction]