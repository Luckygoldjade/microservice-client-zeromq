# Project Title: microservice-client-zeromq

## Academic project completed in Winter 2024

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

## Screenshots

- **Screenshots**:  
This section showcases the visual components and validation results from the microservice project.

- **User Interface Menu (Client Side)**  
  ![User Interface](docs/screenshots/assign_12_User_interface_menu_(from_client_side)_070725_v01.png)

- **Wall Street Journal Data (Server Side)**  
  ![WSJ Data](docs/screenshots/assign_12_Wall_Street_Journal_data_(from_server_side)_070725_v02.png)

- **Terminal Output – NYSE Results**  
  [View Screenshot](docs/screenshots/assign_12_Terminal_output_showing_results_NYSE_070725_v03.png)

- **Terminal Output – Nasdaq Results**  
  [View Screenshot](docs/screenshots/assign_12_Terminal_output_showing_results_Nasdaq_070725_v04.png)

- **Comparison Against Walter Deemer Metrics**  
  [View Screenshot](docs/screenshots/assign_12_Output_comparison_against_Walter_Deemer_metrics_070725_v05.png)

## Demo Videos – Project Progression

This section showcases the development of the microservice system through progressive demo stages:

- **Stage 1** – [Client Prompt and User Interaction (Video)](https://youtu.be/yz9epsfDPJQ)  
  Demonstrates the interactive command-line interface where users select volume percentage options (NYSE/NASDAQ Up/Down).

- **Stage 2** – [Server Scraping and JSON Response (Video)](https://youtu.be/Yt8J8iD2Uoo)  
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
Demonstrates real-time interaction between a Python client and server using ZeroMQ. The client queries financial data, while the server scrapes the Wall Street Journal and responds with JSON. Features include CLI prompts, live data scraping, and percentage calculations.
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

## How to Run

### 1. Install Dependencies

Run the following command in your terminal to install all required Python packages:

```bash
pip install -r requirements.txt
```

---

### 2. Start the Server (in a separate terminal)

The server uses Selenium to scrape stock volume data from the Wall Street Journal and sends the data via ZeroMQ:

```bash
python server_zeromq_wsj_volume_provider.py
```

> The server listens on `tcp://localhost:5555` by default.

---

### 3. Start the Client (in another terminal)

The client is a CLI app that connects to the server via ZeroMQ and displays real-time NYSE/NASDAQ volume percentage data:

```bash
python client_zeromq_wsj_volume_query.py
```

You’ll be prompted with an interactive menu to select from Up/Down Volume options for NYSE and NASDAQ.

---

## File Structure

```markdown
microservice-client-zeromq/
- client_zeromq_wsj_volume_query.py     # Main CLI client (formerly prompt_030824_v03.py)
- server_zeromq_wsj_volume_provider.py  # WSJ scraping server using Selenium
- requirements.txt                      # Python dependencies for both client and server
- README.md                             # Project documentation and instructions
- docs/
  - screenshots/                        # Interface and result screenshots (for README and report)
  - *.pdf                               # Report or design documents
```

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
