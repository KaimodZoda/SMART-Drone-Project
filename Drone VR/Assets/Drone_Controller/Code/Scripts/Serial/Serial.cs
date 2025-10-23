using UnityEngine;
using System.IO.Ports;

public class SerialCommunication : MonoBehaviour
{
    SerialPort serialPort;

    // Set your serial port name and baud rate
    string portName = "COM15"; // Change this to match your port
    int baudRate = 38400; // Change this to match your baud rate

    void Awake()
    {
        InitializeSerialPort();
    }

    void InitializeSerialPort()
    {
        // Initialize the serial port
        serialPort = new SerialPort(portName, baudRate);

        try
        {
            // Open the serial port
            serialPort.Open();
            Debug.Log("Serial port opened.");
        }
        catch (System.Exception ex)
        {
            Debug.LogError("Error: " + ex.Message);
        }
    }

    void Update()
    {
        if (serialPort != null && serialPort.IsOpen)
        {
            try
            {
                // Read all available bytes from the serial port
                string data = serialPort.ReadLine();

                // Print received data to the Unity console
                Debug.Log("Received data: " + data);
            }
            catch (System.Exception ex)
            {
                Debug.LogError("Error reading serial data: " + ex.Message);
            }
        }
    }

    void OnApplicationQuit()
    {
        // Close the serial port when the application quits
        if (serialPort != null && serialPort.IsOpen)
        {
            serialPort.Close();
            Debug.Log("Serial port closed.");
        }
    }
}
