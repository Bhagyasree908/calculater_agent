def rule_based_agent(temp):
    if temp > 100:
        return "cool"
    else:
        return "idle"


# Example
temperature = 105
action = rule_based_agent(temperature)

print(f"Agent action: {action}")
