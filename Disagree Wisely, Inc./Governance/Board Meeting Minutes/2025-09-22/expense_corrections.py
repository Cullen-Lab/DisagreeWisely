#!/usr/bin/env python3
"""
Script to calculate expense corrections for the board resolution.
"""

# Current totals from the resolution
CURRENT_TOTALS = {
    "Engineering & Product": 52654.23,
    "Finance & Compliance": 599.32,
    "Marketing & Communications": 189.60,
    "People & Operations": 22543.66,
    "Travel": 8439.55,
    "Uncategorized": 0.02
}

# Individual line items that need corrections
CURRENT_LINKEDIN = 652.57  # Current amount shown
CURRENT_OFFICE_EXPENSES = 859.34  # Current amount shown
CURRENT_TRAVEL = 8439.55  # Current travel total

print("=== EXPENSE CORRECTIONS CALCULATOR ===\n")

# LinkedIn correction
print("1. LINKEDIN CORRECTION:")
print(f"   Current LinkedIn amount: ${CURRENT_LINKEDIN:.2f}")
linkedin_correction = -74.89
new_linkedin = CURRENT_LINKEDIN + linkedin_correction
print(f"   Correction: ${linkedin_correction:.2f}")
print(f"   New LinkedIn amount: ${new_linkedin:.2f}")

# Office expenses correction
print("\n2. OFFICE EXPENSES CORRECTION:")
print(f"   Current Office Expenses amount: ${CURRENT_OFFICE_EXPENSES:.2f}")
office_correction = -99.00
new_office_expenses = CURRENT_OFFICE_EXPENSES + office_correction
print(f"   Correction: ${office_correction:.2f}")
print(f"   New Office Expenses amount: ${new_office_expenses:.2f}")
print("   Transaction count: 11 → 10 (reduce by 1)")

# Travel corrections (AVDF reimbursements)
print("\n3. TRAVEL CORRECTIONS (AVDF Reimbursements):")
print(f"   Current Travel total: ${CURRENT_TRAVEL:.2f}")
travel_corrections = [-397.23, -610.96, -608.01, -2788.48]
total_travel_correction = sum(travel_corrections)
new_travel = CURRENT_TRAVEL + total_travel_correction

print("   Individual reimbursements to deduct:")
for i, correction in enumerate(travel_corrections, 1):
    print(f"     {i}. ${abs(correction):.2f}")
print(f"   Total correction: ${total_travel_correction:.2f}")
print(f"   New Travel total: ${new_travel:.2f}")
print("   Transaction count: 17 → 13 (reduce by 4)")

# Calculate new category totals
print("\n" + "="*50)
print("NEW CATEGORY TOTALS:")
print("="*50)

new_people_ops = CURRENT_TOTALS["People & Operations"] + linkedin_correction + office_correction
new_travel_total = CURRENT_TOTALS["Travel"] + total_travel_correction

new_totals = {
    "Engineering & Product": CURRENT_TOTALS["Engineering & Product"],
    "Finance & Compliance": CURRENT_TOTALS["Finance & Compliance"],
    "Marketing & Communications": CURRENT_TOTALS["Marketing & Communications"],
    "People & Operations": new_people_ops,
    "Travel": new_travel_total,
    "Uncategorized": CURRENT_TOTALS["Uncategorized"]
}

for category, amount in new_totals.items():
    current = CURRENT_TOTALS[category]
    change = amount - current
    if change != 0:
        print(f"{category}:")
        print(f"  Current: ${current:,.2f}")
        print(f"  Change: ${change:,.2f}")
        print(f"  New: ${amount:,.2f}")
        print()
    else:
        print(f"{category}: ${amount:,.2f} (no change)")

# Calculate new grand total
current_grand_total = sum(CURRENT_TOTALS.values())
new_grand_total = sum(new_totals.values())
total_change = new_grand_total - current_grand_total

print("-" * 40)
print(f"CURRENT GRAND TOTAL: ${current_grand_total:,.2f}")
print(f"TOTAL CORRECTIONS: ${total_change:,.2f}")
print(f"NEW GRAND TOTAL: ${new_grand_total:,.2f}")

print("\n" + "="*50)
print("SUMMARY FOR RESOLUTION UPDATES:")
print("="*50)
print(f"LinkedIn: ${CURRENT_LINKEDIN:.2f} → ${new_linkedin:.2f}")
print(f"Office Expenses: ${CURRENT_OFFICE_EXPENSES:.2f} → ${new_office_expenses:.2f} (11 → 10 transactions)")
print(f"Travel: ${CURRENT_TRAVEL:.2f} → ${new_travel_total:.2f} (17 → 13 transactions)")
print(f"People & Operations subtotal: ${CURRENT_TOTALS['People & Operations']:,.2f} → ${new_people_ops:,.2f}")
print(f"Travel subtotal: ${CURRENT_TOTALS['Travel']:,.2f} → ${new_travel_total:,.2f}")
print(f"GRAND TOTAL: ${current_grand_total:,.2f} → ${new_grand_total:,.2f}")

print(f"\nNote: Travel reduction of ${abs(total_travel_correction):,.2f} represents AVDF reimbursements")