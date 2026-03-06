#!/usr/bin/env python3
"""
Script to check recent expenses against existing ratified expenses
and identify any new expenses that should be added to the resolution.
"""

from datetime import datetime
import re

# Existing ratified expenses from the resolution (totals by category)
EXISTING_RATIFIED = {
    "Engineering & Product": 49590.99,
    "Finance & Compliance": 599.32,
    "Marketing & Communications": 189.60,
    "People & Operations": 22523.33,
    "Travel": 8352.15,
    "Uncategorized": 0.02
}

# Recent expenses from bank statement
RECENT_EXPENSES = [
    # Format: (date, description, amount, category)
    ("2025-09-22", "UPWORK * -849030767 SAN FRANCISCO CA", -284.31, "Engineering & Product"),
    ("2025-09-22", "TWILIO INC SAN FRANCISCO CA", -10.01, "Engineering & Product"),
    ("2025-09-22", "UPWORK * -848892068 SAN FRANCISCO CA", -2621.11, "Engineering & Product"),
    ("2025-09-22", "TWILIO INC, SAN FRANCISCO, CA", -10.79, "Engineering & Product"),
    ("2025-09-22", "BILL.COM LLC, BILLING", -20.33, "People & Operations"),
    ("2025-09-21", "Google Play, Mountain View, CA", -25.00, "Engineering & Product"),
    ("2025-09-21", "CURSOR, AI POWERED IDE, NEW YORK, NY", -21.40, "Engineering & Product"),
    ("2025-09-21", "TWILIO INC, SAN FRANCISCO, CA", -10.03, "Engineering & Product"),
    ("2025-09-20", "TWINR INC., VAUDREUIL-DOR, QC", -2.00, "Engineering & Product"),
    ("2025-09-20", "TWINR INC., VAUDREUIL-DOR, QC", -68.50, "Engineering & Product"),
    ("2025-09-19", "TWILIO INC, SAN FRANCISCO, CA", -10.09, "Engineering & Product"),
    ("2025-09-19", "UBR* PENDING.UBER.COM, SAN FRANCISCO, CA", -87.40, "Travel"),
    ("2025-09-18", "BLOCKED AND REPORTED, BREMERTON, WA", -75.00, "Marketing & Communications"),
]

def analyze_expenses():
    """Analyze recent expenses and show what's new vs existing ratified amounts."""

    print("=== EXPENSE ANALYSIS ===\n")
    print("Existing ratified totals:")
    existing_total = 0
    for category, amount in EXISTING_RATIFIED.items():
        print(f"  {category}: ${amount:,.2f}")
        existing_total += amount
    print(f"  TOTAL EXISTING: ${existing_total:,.2f}")

    print("\n" + "="*50)
    print("RECENT EXPENSES (September 18-22, 2025):")
    print("="*50)

    # Group recent expenses by category
    new_by_category = {}
    for date, desc, amount, category in RECENT_EXPENSES:
        if category not in new_by_category:
            new_by_category[category] = []
        new_by_category[category].append((date, desc, abs(amount)))

    # Show recent expenses by category
    new_totals = {}
    for category in sorted(new_by_category.keys()):
        print(f"\n{category}:")
        category_total = 0
        for date, desc, amount in new_by_category[category]:
            print(f"  {date}: {desc} - ${amount:.2f}")
            category_total += amount
        new_totals[category] = category_total
        print(f"  >> Category total: ${category_total:.2f}")

    print("\n" + "="*50)
    print("UPDATED TOTALS:")
    print("="*50)

    # Calculate updated totals
    grand_total = 0
    for category in sorted(set(list(EXISTING_RATIFIED.keys()) + list(new_totals.keys()))):
        existing = EXISTING_RATIFIED.get(category, 0)
        new_amount = new_totals.get(category, 0)
        updated_total = existing + new_amount

        if new_amount > 0:
            print(f"{category}:")
            print(f"  Previous: ${existing:,.2f}")
            print(f"  New expenses: ${new_amount:,.2f}")
            print(f"  Updated total: ${updated_total:,.2f}")
            print()
        else:
            print(f"{category}: ${updated_total:,.2f} (no new expenses)")

        grand_total += updated_total

    print("-" * 40)
    print(f"UPDATED GRAND TOTAL: ${grand_total:,.2f}")
    print(f"Previous total: ${existing_total:,.2f}")
    print(f"New expenses: ${grand_total - existing_total:,.2f}")

    print("\n" + "="*50)
    print("RECOMMENDATION:")
    print("="*50)
    if grand_total > existing_total:
        print("✓ New expenses found that should be added to ratification list")
        print("✓ Update the resolution's Exhibit A with the new expenses")
        print(f"✓ Update total from ${existing_total:,.2f} to ${grand_total:,.2f}")
    else:
        print("✓ No new expenses - current ratification list is up to date")

def check_date_coverage():
    """Check if recent expenses fall outside the existing date range."""
    print("\n" + "="*50)
    print("DATE COVERAGE CHECK:")
    print("="*50)

    # The existing ratification list covers through 2025-09-16 based on the Upwork entry
    existing_end_date = datetime(2025, 9, 16)

    recent_dates = []
    for date_str, desc, amount, category in RECENT_EXPENSES:
        expense_date = datetime.strptime(date_str, "%Y-%m-%d")
        recent_dates.append(expense_date)

        if expense_date > existing_end_date:
            print(f"⚠️  NEW: {date_str} - {desc} (${abs(amount):.2f})")

    if recent_dates:
        earliest_new = min(recent_dates)
        latest_new = max(recent_dates)
        print(f"\nNew expense date range: {earliest_new.strftime('%Y-%m-%d')} to {latest_new.strftime('%Y-%m-%d')}")
        print(f"Existing ratification covers through: {existing_end_date.strftime('%Y-%m-%d')}")

        if latest_new > existing_end_date:
            print("✓ Resolution should be updated to include new expenses")

if __name__ == "__main__":
    analyze_expenses()
    check_date_coverage()

    print("\n" + "="*50)
    print("NEXT STEPS:")
    print("="*50)
    print("1. Review the new expenses above")
    print("2. Add them to Exhibit A in the resolution")
    print("3. Update category subtotals and grand total")
    print("4. Ensure all expenses align with the spending authority rules")