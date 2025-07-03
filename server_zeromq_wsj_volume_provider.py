# Name: Jacky Kuang
# OSU Email: kuangja@oregonstate.edu
# Course: CS361 - SOFTWARE ENGINEERING I
# Homework: Microservice
# Due Date: 2/26/24
# Description: This program contains the microservice that retrieve scraped
# data from the wall street journal.

from selenium import webdriver
from selenium.webdriver.common.by import By
import zmq
import time
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("please wait...")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.wsj.com/market-data/stocks?mod=nav_top_subsection")
driver.implicitly_wait(3)


while True:
    message = socket.recv()
    print(f"Received request: {message}")

    time.sleep(1)

    # Get all tables with the following class name
    tables = driver.find_elements(
        By.CLASS_NAME, "WSJTables--table__body--3Y0p0d6H")

    # Fourth table contains share volume data
    table = tables[3]

    # Extract rows
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Extract advancing data from the rows
    advancing = rows[1]
    advancingTD = advancing.find_elements(By.TAG_NAME, "td")
    advancingNYSE = advancingTD[1]
    advancingNASDAQ = advancingTD[2]

    # Extract declining data from the rows
    declining = rows[2]
    decliningTD = declining.find_elements(By.TAG_NAME, "td")
    decliningNYSE = decliningTD[1]
    decliningNASDAQ = decliningTD[2]

    data = {
        "advancingNYSE": advancingNYSE.text,
        "decliningNYSE": decliningNYSE.text,
        "advancingNASDAQ": advancingNASDAQ.text,
        "decliningNASDAQ": decliningNASDAQ.text
    }

    socket.send_string(json.dumps(data))
