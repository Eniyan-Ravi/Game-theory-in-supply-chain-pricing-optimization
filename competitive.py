def retailer_discounting(p, demand, q):
    if demand < q:
        discount = min(0.1, (q - demand) / q)
        p *= (1 - discount)
    return p

def competitive_supplier_pricing(c_s, demand_ratio, disruption_multiplier=1.0):
    greed_factor = 0.105
    price = c_s * (1 + ((demand_ratio - 1) * 0.2 + greed_factor)) * disruption_multiplier
    return max(price, c_s * 1.03)

def calculate_competitive_profits(p, c_s, c_m, q, p_s_list, p_m, demand, storage_cost_per_unit):
    q_sold = min(q, demand)
    unsold = max(0, q - demand)
    
    pi_s = sum((p_s - c_s) * q_sold for p_s in p_s_list)
    avg_p_s = sum(p_s_list) / len(p_s_list)
    pi_m = (p_m - avg_p_s - c_m) * q_sold - unsold * (c_m + storage_cost_per_unit)
    pi_r = (p - p_m) * q_sold
    
    revenue = p * q_sold
    total_cost = avg_p_s * q_sold + c_m * q_sold + unsold * storage_cost_per_unit
    
    return [pi_s, pi_m, pi_r, revenue, total_cost, revenue - total_cost]

def run_competitive_model(p, c_s, c_m, q, disruptions, storage_cost_per_unit, p_m, demand):
    demand_ratio = demand / q
    disruption_multipliers = {
        "None": 1.0,
        "Delay": 1.05,
        "Shortage": 1.1,
        "Cost Surge": 1.2
    }
    
    p_s_list = [
        competitive_supplier_pricing(c_s, demand_ratio, disruption_multipliers[event])
        for event in disruptions
    ]
    
    reliability_penalty = (
        disruptions.count("Shortage") * 15 + 
        disruptions.count("Delay") * 10
    )
    
    p = retailer_discounting(p, demand, q)
    results = calculate_competitive_profits(p, c_s, c_m, q, p_s_list, p_m, demand, storage_cost_per_unit)
    satisfaction = max(0, min(100, 100 - (p - p_m) * 2 - reliability_penalty))
    
    return results + [satisfaction]