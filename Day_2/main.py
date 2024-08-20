def main():
    print('Welcome to the tip calculator!')
    total_bill = float(input('What was the total bill? $'))
    tip_percentage = int(input('How much tip would you like to give? 10, 12, or 15? '))
    tip_percentage = 1 + tip_percentage / 100
    total_bill_spit = int(input('How many people to split the bill? '))
    total_bill_spit_value = total_bill * tip_percentage / total_bill_spit
    # print(f'Each person should pay: ${round(total_bill_spit_value, 2)}')
    print(f'Each person should pay: ${total_bill_spit_value:.2f}')  # f-string rounding


if __name__ == '__main__':
    main()
