class bus:
    def __init__(self):
        bus_1 = "bus_one will go from gaza to khanyonis"
        bus_2 = "bus_two will go from gaza to Jerusalem"
        bus_3 = "bus_three will go from Jerusalem to Yafa"
        print(bus_1)
        print(bus_2)
        print(bus_3)
        reservation = int(
            input("Do you want to book or not?(put 1 if you want book and put 0 if you dont want book)  : "))
        if reservation == 1:
            number_bus = int(input("What bus number do you want to take? : "))
            bus.available_bus(number_bus)
        else:
            print("I hope you come back again")

    def available_bus(self):
        if self == 1:
            print("bus_one will go from gaza to khanyonis and the available seats is 2 and a free seats is 4")
            bus.seats(1)
        elif self == 2:
            print("bus_two will go from gaza to Jerusalem and the available seats is 4 and a Free seats are reserved")
            bus.seats(2)
        elif self == 3:
            print("bus_three will go from Jerusalem to Yafa and the available seats is 5 and a free seats is 2")
            bus.seats(3)

    def seats(self):
        number_bus = int(input("What bus number do you want to take? : "))
        if self == 1:
            print("in bus_one you have 2 seats and 4 free seats")
            seat_1 = "The first seat is on the fourth line on the left, next to the window And the seat number is (20) "
            seat_2 = "The second seat is on the penultimate line on the right And the seat number is (49)"
            seat_3 = "The first seat is free and a seat is in the last of bus and the number is (57)"
            seat_4 = "The second seat is free and a seat is in the last of bus and the number is (58)"
            seat_5 = "The fourth seat is free and a seat is in the last of bus and the number is (59)"
            seat_6 = "The last seat is free and a seat is in the last of bus and the number is (60)"
            free_seats = (seat_3,"////////////" , seat_4,"////////////" , seat_5, "////////////" ,seat_6)
            Paid_Seats = (seat_1 , "////////////" , seat_2)
            paid_or_free = int(input(
                "do you need paid_seats or free_seats(if you need free seat put 1 and if you need paid seat put 2) : "))
            if paid_or_free == 1:
                print(free_seats)
                num = int(input("what the seat do you need please enter the seat number :"))
                n = int(input(f"do you need seat {num} ?(if you need seat {num} put 1 if you dont need seat {num} put 0) :"))
                if n == 1:
                    print(f"you are in seat {num}")
                else:
                    print("Thank you for dealing with us")
            elif paid_or_free == 2:
                print(Paid_Seats)
                num_2 = int(input("what the seat do you need please enter the seat number : "))
                n = int(
                    input(f"do you need seat {num_2} ?(if you need seat {num_2} put 1 if you dont need seat {num_2} put 0) :  "))
                if n == 1:
                    print(f"you are in seat {num_2}")

                else:
                    print("Thank you for dealing with us")
            else:
                print("you are put a wrong number")

        elif self == 2:
            print("In bus_two we have 4 seats and there are no free seats ")
            seat_1 = "The first seat is on the second line on the right, next to the window And the seat number is (13) "
            seat_2 = "The second seat is located in the fifth row on the right And the seat number is (32)"
            seat_3 = "The  third seat is located in the seventh line in the middle And the seat number is (44)"
            seat_4 = "The fourth seat is located in the first line at the side of the window And the seat number is (1)"
            seats = (seat_1 , "////////////" ,seat_2, "////////////" ,seat_3, "////////////" ,seat_4)
            print(seats)
            num_2 = int(input("what the seat do you need Please enter the bus number : "))
            n = int(
                input(
                    f"do you need seat {num_2} ?(if you need seat {num_2} put 1 if you dont need seat {num_2} put 0) : "))

            if n == 1:
                print(f"you are in seat {num_2}")
                del (num_2)
            else:
                print("Thank you for dealing with us")


        elif number_bus == 3:
            print("in bus three the available seats is 5 and a free seats is 2")
            seat_1 = "The first seat is on the line 5 on the right, next to the window And the seat number is (16) \n"
            seat_2 = "The second seat is located in the fifth row on the right And the seat number is (19)\n"
            seat_3 = "The  third seat is located in the seventh line in the middle And the seat number is (42)\n"
            seat_4 = "The fourth seat is located in the first line at the side of the window And the seat number is (3)\n"
            seat_5 = "The fifth seat is free and a seat is in the last of bus and the number is (10)\n"
            seat_6 = "The last seat is free and a seat is in the last of bus and the number is (44)\n"
            free_seats = (seat_5, "////////////", seat_6)
            Paid_Seats = (seat_1, "////////////", seat_2 ,  "////////////", seat_3, "////////////", seat_4)
            paid_or_free = int(input(
                "do you need paid_seats or free_seats(if you need free seat put 1 and if you need paid seat put 2) : "))
            if paid_or_free == 1:
                print(free_seats)
                num = int(input("what the seat do you need please enter the seat number :"))
                n = int(input(
                    f"do you need seat {num} ?(if you need seat {num} put 1 if you dont need seat {num} put 0) :"))
                if n == 1:
                    print(f"you are in seat {num}")
                elif n == 0:
                    print("Thank you for dealing with us")
                else:
                    print("you are put a wrong number")
            elif paid_or_free == 2:
                print(Paid_Seats)
                num_2 = int(input("what the seat do you need please enter the seat number : "))
                n = int(
                    input(
                        f"do you need seat {num_2} ?(if you need seat {num_2} put 1 if you dont need seat {num_2} put 0) :  "))
                if n == 1:
                    print(f"you are in seat {num_2}")

                elif n== 0:
                    print("Thank you for dealing with us")
                else:
                    print("you are put a wrong number")
            else:
                print("you are put a wrong number")
bus()