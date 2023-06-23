# IoT Knock Detection System
Using an Arduino MEGA2560 and percussion sensor

This is an IoT project that utilizes a knock sensor to detect high-pitched sounds and triggers notifications through email and SMS. The project provides a low-cost, DIY security solution, serving as an alternative to expensive commercial security products. The system is built using Arduino and Python programming.
Features

    Detects high-pitched sounds using a knock sensor module.
    Triggers a micro LED light when a sound is detected.
    Sends email notifications to multiple recipients.
    Sends SMS notifications using Twilio.
    Simple and intuitive web interface for user interaction.
    Secure user authentication and account management.

## Hardware Components

    Arduino board
    Knock sensor module
    Micro LED light
    USB cable for Arduino connection

## Software Components

    Arduino IDE
    Python
    Flask (Python web framework)
    pySerial (Python library for serial communication)
    smtplib (Python library for sending emails)
    twilio (Python library for sending SMS using Twilio API)

## Getting Started
1. Construct the project using the schematics shown below.
![Image](https://github.com/omidk414/IoT_Knock_Sensor/blob/main/Cirkit_Designer_JRrqDBtxGl.png)

2. Clone the repository:

    ```git clone https://github.com/omidk414/IoT_Knock_Sensor.git```

3. Install the necessary Python packages:

    ```pip install -r requirements.txt```

4. Connect the Arduino board to your computer via USB.

5. Upload the knock_sensor.ino file to the Arduino using the Arduino IDE.

6. Update the necessary configurations in the config.ini file, including email and Twilio account details.

7. Run the Flask application:

    ```flask run```

8. Open your web browser and navigate to http://localhost:5000 to access the application.

9. Test the knock and view email to verify if the message is sent. 
![Email](https://github.com/omidk414/IoT_Knock_Sensor/blob/main/8TLFob1FZ6.png)

## Usage

    Create an account or log in with your existing credentials.

    On the home page, you will see the status of the knock sensor and receive notifications when a sound is detected.

    Customize the notification settings by adding email addresses and phone numbers in the account settings.

      
          
      

  
