from Message import Message
from Logger import Logger
from Limit import Limit


def main():
    logger = Logger()

    limitH = Limit('H', 50.0, 45.0, 55.0, 2.0)
    limitT = Limit('T', 25.0, 20.0, 30.0, 2.0)

    while True:
        # Read input
        name = input("Enter the name (T or H): ")
        value = float(input("Enter the value of the sensor: "))
        
        # Check if the input is valid
        if name not in ['T', 'H']:
            print("Invalid name")
            continue

        # Check if the value is within the limits
        if name == 'T':
            message = limitT.produce_message(value)
        else:
            message = limitH.produce_message(value)

        # Log the message
        logger.log(message)
        
        # Print the message
        print(f"Message logged: {message.timestamp} {message.name} {message.value} {message.state} {message.difference}")

        # Ask if the user wants to continue
        if input("Stop? (y/n): ") == 'y':
            break

    # Print all messages
    print("All messages:")
    for message in logger.get_messages():
        print(f"{message.timestamp} {message.name} {message.value} {message.state} {message.difference}")

main()