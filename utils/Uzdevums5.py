def calculate_days(total_cement=200, initial_consumption=5, increase_rate=0.20):
    days = 0
    remaining = total_cement
    consumption = initial_consumption
    while remaining > 0:
        days += 1
        print(f"Diena {days}: Patērē {consumption:.2f} tonnas, atlikums {remaining:.2f} tonnas")
        remaining -= consumption
        consumption *= (1 + increase_rate)
    return days


