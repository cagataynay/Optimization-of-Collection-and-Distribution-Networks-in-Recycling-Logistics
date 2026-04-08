import pulp

# 1. Define the Problem (Minimize Total Cost)
prob = pulp.LpProblem("Reverse_Logistics_Optimization", pulp.LpMinimize)

# 2. Data Definition (Based on your recycling logistics analysis)
# Facilities (Potential Hubs) and Collection Points
facilities = ['Facility_1', 'Facility_2', 'Facility_3', 'Facility_4']
collection_points = ['Point_A', 'Point_B', 'Point_C', 'Point_D', 'Point_E']

# Fixed Costs for opening each facility
fixed_costs = {
    'Facility_1': 5000, 
    'Facility_2': 7000, 
    'Facility_3': 4500, 
    'Facility_4': 6000
}

# Capacity limits for each facility
capacities = {
    'Facility_1': 500, 
    'Facility_2': 700, 
    'Facility_3': 400, 
    'Facility_4': 600
}

# Demand (Amount of waste at each collection point)
demand = {
    'Point_A': 100, 
    'Point_B': 150, 
    'Point_C': 120, 
    'Point_D': 80, 
    'Point_E': 90
}

# Unit Transportation Costs (Distance/Cost Matrix)
transport_costs = {
    'Facility_1': {'Point_A': 4, 'Point_B': 6, 'Point_C': 3, 'Point_D': 5, 'Point_E': 7},
    'Facility_2': {'Point_A': 5, 'Point_B': 2, 'Point_C': 6, 'Point_D': 4, 'Point_E': 3},
    'Facility_3': {'Point_A': 2, 'Point_B': 8, 'Point_C': 5, 'Point_D': 2, 'Point_E': 6},
    'Facility_4': {'Point_A': 6, 'Point_B': 5, 'Point_C': 2, 'Point_D': 7, 'Point_E': 4}
}

# 3. Decision Variables
# Binary variable: Is the facility opened? (1 if yes, 0 if no)
use_facility = pulp.LpVariable.dicts("Open_Facility", facilities, cat='Binary')

# Continuous variable: Amount of waste transported from point to facility
flow = pulp.LpVariable.dicts("Waste_Flow", (facilities, collection_points), lowBound=0, cat='Continuous')

# 4. Objective Function (Min Z = Transport Cost + Fixed Cost)
prob += (
    pulp.lpSum([transport_costs[f][c] * flow[f][c] for f in facilities for c in collection_points]) +
    pulp.lpSum([fixed_costs[f] * use_facility[f] for f in facilities]),
    "Total_Network_Cost"
)

# 5. Constraints
# Every collection point's demand must be fully met
for c in collection_points:
    prob += pulp.lpSum([flow[f][c] for f in facilities]) == demand[c]

# Facility capacity must not be exceeded, and flow is 0 if facility is closed
for f in facilities:
    prob += pulp.lpSum([flow[f][c] for c in collection_points]) <= capacities[f] * use_facility[f]

# 6. Solve the Problem
prob.solve()

# Print Results
print(f"Optimization Status: {pulp.LpStatus[prob.status]}")
print(f"Minimized Total Cost: {pulp.value(prob.objective)}")

print("\n--- Optimal Facility Decisions ---")
for f in facilities:
    if pulp.value(use_facility[f]) > 0.5:
        print(f"Status: {f} is OPENED")
        for c in collection_points:
            if pulp.value(flow[f][c]) > 0:
                print(f"  -> {pulp.value(flow[f][c])} units transported from {c}")
