# Basic Socket Communication Setup 🌐🍓🤖

Welcome to the Basic Socket Communication setup! This project provides a simplified codebase using the Python `socket` library to enable communication between Raspberry Pie over the same network. It also allows multiple Raspberry Pie to communicate seamlessly, making it an ideal setup for IoT applications.

## Getting Started 🚀

### Prerequisites
- Ensure you have Python 3 installed on your Raspberry Pi.

### Setting Up Devices for Communication 📡

Before running the code, follow these steps to ensure proper communication setup:

1. **Check System IPs:**
   - For Windows, use `ipconfig` in the command prompt.
   - For Linux, use `ifconfig` in the terminal.

2. **Ping Each Other:**
   - On each device, ping the IP of the other system where you want to connect. This ensures they are on the same network and the firewall is not interfering.
     ```bash
     ping <IP_of_another_system>
     ```

   Note: In a simple communication setup, it might not work if the firewall is on. Make sure to disable the firewall or configure it to allow communication.

### Running the Code 🏃‍♂️

1. Clone the repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/855princekumar/basic-socket-communication.git
   ```

2. Navigate to the project directory:
   ```bash
   cd basic-socket-communication
   ```

3. Run the server code on the designated server Raspberry Pi:
   ```bash
   python3 server.py
   ```

4. Run the client code on the other Raspberry Pi or device:
   ```bash
   python3 client.py
   ```

   Add the server IP manually in the client code after checking the system IPs. If you're on Windows, use `ipconfig`; if you're on Linux, use `ifconfig`.

## Server Port Handling ⚙️

It's crucial to note that when the server code runs on a Raspberry Pi and is stopped from the terminal, the port might remain open. To close the port and restart, use the following command on the server device:

```bash
sudo fuser -k 5000/tcp
```

Here, `5000` represents the open port. Ensure to modify and contribute to the codebase, keeping this in mind.

## Contribution 🤝

Feel free to modify and contribute to this repository. Your contributions are highly valued, and together we can enhance the functionality and usability of this simple yet useful communication setup. Share your improvements through pull requests, and let's build a robust solution for IoT communication.

I'll keep updating this repository with useful features and improvements. Happy coding! 🎉
