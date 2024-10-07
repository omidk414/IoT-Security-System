# Intelligent Door Knocking Security System Using IoT

An Arduino MEGA2560 and percussion sensor-based IoT security solution

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Components](#components)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)

## Introduction

This IoT project offers a cost-effective, DIY security solution using a knock sensor to detect high-pitched sounds and trigger notifications via email and SMS. Built with Arduino and Python, it serves as an affordable alternative to expensive commercial security systems.

## Features

- **Sound Detection**: Utilizes a knock sensor module to detect high-pitched sounds
- **Visual Indicator**: Triggers a micro LED light upon sound detection
- **Multi-channel Notifications**: 
  - Sends email alerts to multiple recipients
  - Delivers SMS notifications using Twilio
- **User Interface**: Provides a simple, intuitive web interface for system interaction
- **Security**: Implements secure user authentication and account management

![sensor](https://github.com/omidk414/IoT-Security-System/blob/main/images/knocksensor.jpg)

## Components

### Hardware Components

- Arduino MEGA2560 board
- Knock sensor module
- Micro LED light
- USB cable for Arduino connection

### Software Components

- Arduino IDE
- Python 3.x
- Flask (Python web framework)
- pySerial (Python library for serial communication)
- smtplib (Python library for sending emails)
- twilio (Python library for Twilio API integration)

## Getting Started

### Hardware Setup

1. Assemble the project components according to the schematic below:

![cirkit](https://github.com/omidk414/IoT-Security-System/blob/main/images/Cirkit_Design.png)

### Software Setup

1. Clone the repository:
```
git clone https://github.com/omidk414/IoT_Knock_Sensor.git
```

2. Install required Python packages:
```
pip install -r requirements.txt
```


3. Connect the Arduino board to your computer via USB.

4. Upload `knock_sensor.ino` to the Arduino using the Arduino IDE.

5. Configure the `config.ini` file with your email and Twilio account details.

6. Launch the Flask application:
```
flask run
```


7. Access the application at `http://localhost:5000` in your web browser.

## Usage

1. Create an account or log in with existing credentials.
2. Monitor the knock sensor status on the home page.
3. Receive notifications when a sound is detected.
4. Customize notification settings in the account settings page.

![Email](https://github.com/omidk414/IoT-Security-System/blob/main/images/email.png)

## Configuration

Detailed instructions for configuring email settings, Twilio integration, and other system parameters can be found in the `config.ini` file.

## Troubleshooting

Common issues and their solutions:

- **No sound detection**: Ensure the knock sensor is properly connected and configured.
- **Notification failures**: Verify email and Twilio settings in `config.ini`.
- **Web interface not loading**: Check Flask server logs for errors.

