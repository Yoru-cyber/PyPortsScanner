# PyPortsScanner
This project is a simple port scanner implemented in Python using the `socket` library and the `rich` library for enhanced output. It allows you to check if specific ports are open on a given host.

## Features

* **Port Scanning:** Scans a specified range of ports on a target host.
* **Colored Output:** Uses the `rich` library to display results with color-coded information. **Indeterminate Progress Bar:** Provides visual feedback during the scanning process using an indeterminate progress bar.
* **Clear Output:** Displays open and closed ports in a readable format.
* **Local Server Testing:** Includes instructions for testing the scanner against a local Python server.

## Prerequisites

* Python 3.11 or higher
* Poetry for dependency management (recommended)

## Installation
1.  **Clone the repository (or download the script):**

    ```bash
    git clone git@github.com:Yoru-cyber/PyPortsScanner.git
    cd PyPortsScanner
    ```

2.  **Install dependencies using Poetry or pip:**

    ```bash
    poetry install
    ```

    ```bash
    pip install
    ```
3.  **Activate the Poetry virtual environment or Pip:**

    ```bash
    poetry env activate
    ```
    
    ```bash
    python3 -m venv venv
    ```
    * **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

    * **On Windows:**

        ```bash
        venv\Scripts\activate
        ```
## Usage

1.  **Run the script:**

    ```bash
    python pyportsscanner.py <host> <start_port> <end_port>
    ```

    * `<host>`: The target host (e.g., `localhost`, `192.168.1.1`, `example.com`).
    * `<start_port>`: The starting port number.
    * `<end_port>`: The ending port number.

    **Example:**

    ```bash
    python pyportsscanner.py localhost 1 1024
    ```

## Testing with a Local Server

To test the port scanner in a controlled environment, you can launch a local Python server:

1. **Simple HTTP Server:**
    
    ```bash
    python -m http.server 8000
    ```
    Or, for ports below 1024:

    ```bash
    sudo python -m http.server 80
    ```

    ```bash
    python pyportsscanner.py localhost 8000 8001
    ```

## Example Output

<p style="color: magenta;">Running...</p>
<p style="color: green;">Port 80 is open</p>
<p style="color: red;">Port 81 is closed</p>
