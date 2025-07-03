# Tony Chan
# 03/15/2024
# OSU CS361 Software Engineering I
# Assignment 12 Milestone 4 Microservce
# Description: This program contains the client that retrieves data
# from the wall street journal microservice.
# In this version, the User interface talks to my partner's
# microservice server and retrieves the data.
# The client uses the clint library to prompt the user to select an
# option and then sends a request to the server
# to retrieve the data. The data is then displayed in the console.
import json
import zmq
import questionary
from clint.textui import puts, colored

# ZeroMQ is the message broker
context = zmq.Context()


def select_prompt():
    """
    User command line prompt to select an option.
    """
    print("Welcome to the WSJ Up and Down Volume Percentage Calculator!")
    print("After selecting an option, press the Enter key to continue, " +
          "results will be displayed in the console.")
    while True:
        choices = ["NYSE Up Volume Percentage",
                   "NYSE Down Volume Percentage",
                   "Nasdaq Up Volume Percentage",
                   "Nasdaq Down Volume Percentage",
                   "Exit or Undo"]

        answer = questionary.select(
            "Select an option using your up and down arrow keys:",
            choices=choices,
        ).ask()

        if answer == "NYSE Up Volume Percentage":
            nyse_up_vol_percent()

        elif answer == "NYSE Down Volume Percentage":
            nyse_dn_vol_percent()

        elif answer == "Nasdaq Up Volume Percentage":
            nasdaq_up_vol_percent()

        elif answer == "Nasdaq Down Volume Percentage":
            nasdaq_dn_vol_percent()

        elif answer == "Exit or Undo":
            print("You selected Exit or Undo")
            break


def get_wsj_data():
    """
    This function is used to get the data from the microservice server.
    """
    print("Connecting to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    print("Sending request ...")
    socket.send(b"Requesting Data")

    message = socket.recv().decode()
    data = json.loads(message)

    return data


def display_output_border():
    """
    This function is used to create a border.
    """
    puts(colored.yellow("-" * 60))


def display_output_crlf():
    """
    This function is used to create a return line.
    """
    print("\n")


def percentage_volume(numerator, denominator):
    """
    This function is used to calculate the percentage volume increase
    or decrease.
    """
    return numerator / (numerator + denominator) * 100


def nyse_up_vol_percent():
    """
    This function is used to calculate the NYSE Up Volume Percentage.
    """
    print("You selected NYSE Up Volume Percentage")
    data = get_wsj_data()
    display_output_border()
    puts(colored.green("Advancing NYSE: " + str(data["advancingNYSE"])))
    puts(colored.red("Declining NYSE: " + str(data["decliningNYSE"])))
    advancing_nyse = int(data["advancingNYSE"].replace(',', ''))
    declining_nyse = int(data["decliningNYSE"].replace(',', ''))
    percentage_up = percentage_volume(advancing_nyse, declining_nyse)
    print(f"NYSE Up Volume percentage is {percentage_up:.2f} %")
    display_output_border()
    display_output_crlf()


def nyse_dn_vol_percent():
    """
    This function is used to calculate the NYSE Down Volume Percentage.
    """
    print("You selected NYSE Down Volume Percentage")
    data = get_wsj_data()
    display_output_border()
    puts(colored.green("Advancing NYSE: " + str(data["advancingNYSE"])))
    puts(colored.red("Declining NYSE: " + str(data["decliningNYSE"])))
    advancing_nyse = int(data["advancingNYSE"].replace(',', ''))
    declining_nyse = int(data["decliningNYSE"].replace(',', ''))
    percentage_dn = percentage_volume(declining_nyse, advancing_nyse)
    print(f"NYSE Down Volume percentage is {percentage_dn:.2f} %")
    display_output_border()
    display_output_crlf()


def nasdaq_up_vol_percent():
    """
    This function is used to calculate the Nasdaq Up Volume Percentage.
    """
    print("You selected Nasdaq Up Volume Percentage")
    data = get_wsj_data()
    display_output_border()
    puts(colored.green("Advancing Nasdaq: " + str(data["advancingNASDAQ"])))
    puts(colored.red("Declining Nasdaq: " + str(data["decliningNASDAQ"])))
    advancing_nasdaq = int(data["advancingNASDAQ"].replace(',', ''))
    declining_nasdaq = int(data["decliningNASDAQ"].replace(',', ''))
    percentage_up = percentage_volume(advancing_nasdaq, declining_nasdaq)
    print(f"Nasdaq Up Volume percentage is {percentage_up:.2f} %")
    display_output_border()
    display_output_crlf()


def nasdaq_dn_vol_percent():
    """
    This function is used to calculate the Nasdaq Down Volume Percentage.
    """
    print("You selected Nasdaq Down Volume Percentage")
    data = get_wsj_data()
    display_output_border()
    puts(colored.green("Advancing Nasdaq: " + str(data["advancingNASDAQ"])))
    puts(colored.red("Declining Nasdaq: " + str(data["decliningNASDAQ"])))
    advancing_nasdaq = int(data["advancingNASDAQ"].replace(',', ''))
    declining_nasdaq = int(data["decliningNASDAQ"].replace(',', ''))
    percentage_dn = percentage_volume(declining_nasdaq, advancing_nasdaq)
    print(f"Nasdaq Down Volume percentage is {percentage_dn:.2f} %")
    display_output_border()
    display_output_crlf()


if __name__ == '__main__':
    select_prompt()
