# Academic project completed in Winter 2024

## Project Title: microservice-client-zeromq

**WSJ Up/Down Volume Percentage Calculator (Client Microservice)**  
A command-line Python client that communicates via ZeroMQ to a microservice server. It retrieves stock volume data from the Wall Street Journal website and calculates the Up and Down Volume percentages for both NYSE and NASDAQ.

This repository contains my independent copy of a collaborative academic project completed as part of the
Computer Science program.

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

## Demo

_Fix***_

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

pip install -r requirements.txt
```

### 2. Start the Client in separate terminal

Make sure the server microservice is running and listening on port `5555`. This project assumes the server is on `tcp://localhost:5555`.

### 3. Run the Client

python microservice-client-zeromq.py

### 4. Run the Server in separate terminal

python server_zeromq_wsj_volume_provider

```

You’ll be presented with a command-line menu. Choose any of the options to retrieve and analyze stock volume data.

---

## File Structure

- microservice-client-zeromq/
  - microservice-client-zeromq.py       # Main client CLI application (renamed from prompt_030824_v03.py)
  - requirements.txt                    # Project dependencies
  - README.md                           # Project overview and instructions
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
```

## Volume Percentage Calculation

```
Percentage = Advancing / (Advancing + Declining) * 100
```

Each calculation is shown clearly in the terminal with border highlights and color-coded values.

---

## Requirements

```
pyzmq
questionary
clint
```

(Installed via `requirements.txt`)

---

## Notes

- The microservice server was provided externally and is not included in this repo.
- This project was part of a larger collaboration where each team member wrote a client and a separate server for the other.
