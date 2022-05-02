def get_number(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def get_integer(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    yearly_interest = (yearly_interest/100)
    months = years * 12

    # calculate future value
    future_value = 0.0
    x = 0
    tempval = 0.0
    for i in range(0, months):
      future_value += monthly_investment
      x += 1
      if (x % 12 == 0):
        tempval = future_value * yearly_interest
        future_value += tempval
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate %:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print("Future value:\t\t\t{:.2f}".format(future_value, 2))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
