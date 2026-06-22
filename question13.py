try:
    seat_no = int(input("Enter seat number (1-100): "))

    if 1 <= seat_no <= 100:
        print("Ticket booked successfully for seat", seat_no)
    else:
        print("Invalid seat number")

except ValueError:
    print("Please enter a valid seat number")