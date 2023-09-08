# Echo-with-Thingsboard

## Objective

The Echo-with-Thingsboard project is implemented to demonstrate how to echo data read from Thingsboard shared attributes to telemetry by using Python. The project sets up a connection to Thingsboard, continuously monitors a shared attribute with the key 'data' from a specific device, and sends this data to telemetry as 'echo_data' whenever it changes.

## Prerequisites 

Before running this project, make sure you have the following:

  1. An account on Thingsboard: You can use the demo Thingsboard.

  2. A device created in Thingsboard: You will need a device on Thingsboard to monitor the 'data' shared attribute.

  3. Python installed: Ensure that you have Python installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/RohitAayushmaan/Echo-with-Thingsboard.git
   
   cd Echo-with-Thingsboard

2. Install the required Python libraries:

   ```bash
   pip install requirements.txt

3. Update the main.py file:
   
   Replace YOUR_THINGSBOARD_HOST with the URL of your demo Thingsboard instance.
   
   Replace YOUR_DEVICE_ACCESS_TOKEN with the access token of your device.
   
5. Run the Python script:
   ```bash
   python main.py
   
The script will connect to your Thingsboard instance, monitor the 'data' shared attribute, and echo changes to telemetry.


## Additional Resources

For more information about the Thingsboard API, you can visit the [official documentation](https://thingsboard.io/docs/reference/http-api/#telemetry-upload-api) .

