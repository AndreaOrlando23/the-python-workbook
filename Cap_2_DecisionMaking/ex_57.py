# EXERCISE 57 : Cell phone bill

minutes = int(input("Enter the amount of minutes used: "))
text_message = int(input("Enter the amount of text messages sent: "))

base_charge = 15.00
additional_text_messages_charge = (text_message - 50) * 0.15
additional_minutes_charge = (minutes - 50) * 0.25
call_center_charge = 0.44

subtotal = base_charge + additional_text_messages_charge + additional_minutes_charge + call_center_charge

tax = subtotal / 100 * 5
total = subtotal + tax

print()
print(f"Base charge = ${round(base_charge, 2)}")

if additional_minutes_charge > 0:
    print(f"Additional minutes charge = ${round(additional_minutes_charge, 2)}")
elif additional_text_messages_charge > 0:
    print(f"Additional text message charge = ${round(additional_text_messages_charge, 2)}")

print(f"Call center charge = ${round(call_center_charge, 2)}")
print(f"Tax = ${round(tax, 2)}")
print()
print(f"Grand total = ${round(total, 2)}")
