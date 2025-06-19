def split_bill():
    total_amount = float(input("Enter total bill amount: ₹"))
    num_people = int(input("Enter number of people: "))

    names = []
    paid = []

    for i in range(num_people):
        name = input(f"Name of person {i+1}: ")
        amount = float(input(f"Amount paid by {name}: ₹"))
        names.append(name)
        paid.append(amount)

    share = total_amount / num_people
    print("\n📊 Final Summary:\n")

    for i in range(num_people):
        balance = paid[i] - share
        if balance > 0:
            print(f"{names[i]} should get ₹{balance:.2f}")
        elif balance < 0:
            print(f"{names[i]} should pay ₹{-balance:.2f}")
        else:
            print(f"{names[i]} is settled up.")

split_bill()
