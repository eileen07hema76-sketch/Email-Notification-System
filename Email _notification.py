
with open("Customers.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line or line.lower() == "customers":
            continue

        name, email = line.split(",")

        print("--------------------------------")
        print("To      :", email)
        print("Subject :", "Confirmation Email")
        print()
        print(f"Hello {name},")
        print("Your registration has been confirmed.")
        print("Thank you!")
        print("✅ Email sent successfully!")
        print("--------------------------------\n")
