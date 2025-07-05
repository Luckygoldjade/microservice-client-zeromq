# Academic project completed in Winter 2024

## Project Title: microservice-client-zeromq

**WSJ Up/Down Volume Percentage Calculator (Client Microservice)**  
A command-line Python client that communicates via ZeroMQ to a microservice server. It retrieves stock volume data from the Wall Street Journal website and calculates the Up and Down Volume percentages for both NYSE and NASDAQ.

This repository contains my independent copy of a collaborative academic project completed as part of the
Computer Science program.

---

## Overview

This microservice client was designed to:

- Connect to a microservice server (written by a partner) via ZeroMQ.
- Send requests and receive JSON-formatted volume data.
- Display user-friendly calculations of volume percentages via an interactive CLI.
- Serve as a data visualization and analysis tool using scraped financial data.

This project demonstrates asynchronous communication, microservice principles, and modular CLI design using Python.

---

## Collaborators

This project was originally developed in collaboration with teammate Jacky K, and myself. This repo is
personalized, independently maintained version created for portfolio and resume.

---

## Technologies Used

- **Python 3**
- **ZeroMQ** (`pyzmq`)
- **CLI Interface** via `questionary` and `clint`

---

## Screenshots and Demo

- **Screenshots**:  



## Demo Videos – Project Progression

This section showcases the development of the microservice system through progressive demo stages:

- **Stage 1** – [Client Prompt and User Interaction (Video)](https://youtu.be/link-to-stage1)  
  Demonstrates the interactive command-line interface where users select volume percentage options (NYSE/NASDAQ Up/Down).

- **Stage 2** – [Server Scraping and JSON Response (Video)](https://youtu.be/link-to-stage2)  
  Shows the server microservice scraping live stock volume data from the *Wall Street Journal* and returning structured JSON responses.

- **Stage 3** – [Full Client-Server Integration with Live Data (Video)](https://youtu.be/7M-taMOrDU0)  
  Highlights the complete system running in two separate terminal windows, communicating in real time using ZeroMQ.

---

### Final Integrated Demo (Stage 3)

The Stage 3 video demonstrates a fully functional microservice system built with **Python** and **ZeroMQ** for asynchronous client-server messaging.

- **Client**  
  Interactive CLI that allows users to select from NYSE/NASDAQ Up or Down Volume options. Sends requests over ZeroMQ and displays results based on server response.

- **Server**  
  Retrieves live data from the *Wall Street Journal* using **Selenium**. Processes and returns stock volume data in JSON format.

#### What's Shown in the Video:
- Launching server and client in separate terminals  
- User interacting with the CLI prompt  
- Live financial data being scraped and returned as JSON  
- Real-time calculation and display of volume percentages

---

> **Watch the final integrated demo:** [Stage 3 – Full System Integration (Video)](https://youtu.be/7M-taMOrDU0)






---

## Features

- Interactive command-line interface to choose between:
  - NYSE Up Volume %
  - NYSE Down Volume %
  - NASDAQ Up Volume %
  - NASDAQ Down Volume %
- ZeroMQ-based client-server request/response model
- Real-time data parsing from received JSON
- Modular and readable Python structure

---

## How to Run the Client

### 1. Install Requirements
```
pip install -r requirements.txt
```

### 2. Start the Client in separate terminal

Make sure the server microservice is running and listening on port `5555`. This project assumes the server is on `tcp://localhost:5555`.

### 3. Run the Client
```
python client_zeromq_wsj_volume_query.py
```
### 4. Run the Server in separate terminal
```
python server_zeromq_wsj_volume_provider.py
```

You’ll be presented with a command-line menu. Choose any of the options to retrieve and analyze stock volume data.

---

## File Structure

- microservice-client-zeromq/
  - client_zeromq_wsj_volume_query.py    # Main client CLI application (renamed from prompt_030824_v03.py)
  - server_zeromq_wsj_volume_provider.py # server providing financial data
  - requirements.txt                     # Project dependencies
  - README.md                            # Project overview and instructions
  - docs/
    - *.png and *.pdf: Screenshots and report visuals

---

## Communication Protocol

- **Protocol**: ZeroMQ (REQ/REP)
- **Data Format**: JSON
- **Request Flow**:
  1. Client sends a static "Requesting Data" message.
  2. Server responds with JSON containing volume data.

Example JSON Response:
{
  "advancingNYSE": "1,234,567",
  "decliningNYSE": "2,345,678",
  "advancingNASDAQ": "3,456,789",
  "decliningNASDAQ": "4,567,890"
}

---

## Volume Percentage Calculation

Percentage = Advancing / (Advancing + Declining) * 100

Each calculation is shown clearly in the terminal with border highlights and color-coded values.

---

## Requirements

- **pyzmq**
- **questionary**
- **clint**

(Installed via `requirements.txt`)

---

## Notes

- The microservice server was provided externally and is not included in this repo.

## License

This project is for demonstration and educational purposes. No affiliation with TheMealDB.
