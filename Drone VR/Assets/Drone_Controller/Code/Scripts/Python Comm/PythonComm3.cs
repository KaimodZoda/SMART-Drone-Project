using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;
using System.Collections;


public class UnitySocketServer3 : MonoBehaviour
{
    public int port = 12345;
    public MoveObject3 moveObject; // Reference to the MoveObject script

    private TcpListener server;
    private TcpClient client;
    private NetworkStream stream;
    private byte[] buffer = new byte[1024];
    private StringBuilder receivedDataBuffer = new StringBuilder();
    private bool hasNewMessage = false;

    void Start()
    {
        server = new TcpListener(IPAddress.Any, port);
        server.Start();
        server.BeginAcceptTcpClient(new System.AsyncCallback(HandleConnection), null);
        StartCoroutine(CheckMessages());
    }

    void HandleConnection(System.IAsyncResult result)
    {
        client = server.EndAcceptTcpClient(result);
        stream = client.GetStream();
        stream.BeginRead(buffer, 0, buffer.Length, new System.AsyncCallback(ReadCallback), null);
    }

    void ReadCallback(System.IAsyncResult result)
    {
        int bytesRead = stream.EndRead(result);
        string receivedData = Encoding.UTF8.GetString(buffer, 0, bytesRead);

        // Append the received data to the buffer
        receivedDataBuffer.Append(receivedData);

        // Mark that a new message has been received
        hasNewMessage = true;

        // Process complete commands in the buffer
        ProcessCommands();

        // Continue listening for more data
        stream.BeginRead(buffer, 0, buffer.Length, new System.AsyncCallback(ReadCallback), null);
    }

    void ProcessCommands()
    {
        // Split the received data into lines
        string[] commands = receivedDataBuffer.ToString().Split('\n');

        // Process each command
        foreach (string command in commands)
        {
            if (!string.IsNullOrEmpty(command))
            {
                Debug.Log("Received data from Python: " + command);

                // Process received data and perform actions in Unity
                ProcessReceivedData(command);

                // Send a response back to Python if needed
                string response = "Command received";
                byte[] responseBytes = Encoding.UTF8.GetBytes(response);
                stream.Write(responseBytes, 0, responseBytes.Length);
            }
        }

        // Clear the buffer
        receivedDataBuffer.Clear();
    }

    void ProcessReceivedData(string data)
    {
        // Here, you can interpret the received data and perform actions in Unity.
        // For example, you can set the movement direction based on the received command.
        // Clear all movement flags before setting new ones
        

        // Set the movement direction based on the received command
        moveObject.MoveForward(data == "forward");
        moveObject.MoveBackward(data == "backward");
        moveObject.MoveLeft(data == "left");
        moveObject.MoveRight(data == "right");
        moveObject.MoveUpward(data == "up");
        moveObject.MoveDownward(data == "down");

        // Add more conditions based on your requirements
    }

    IEnumerator CheckMessages()
    {
        float slowdownDuration = 0.15f; // Duration for slowdown in seconds
        float elapsedTime = 0.0f;
        float initialSpeed = moveObject.speed;

        while (true)
        {
            yield return new WaitForSeconds(0.05f); // Check every 50 milliseconds

            // If there's no new message, slow down the object's movement
            if (!hasNewMessage)
            {
                elapsedTime += 0.05f; // Increase elapsed time
                float t = Mathf.Clamp01(elapsedTime / slowdownDuration); // Calculate the normalized time

                // Slow down the movement speed gradually
                moveObject.speed = Mathf.Lerp(initialSpeed, 0f, t);

                // If the slowdown duration has elapsed, stop the object
                if (t >= 1.0f)
                {
                    
                    elapsedTime = 0.0f; // Reset elapsed time
                    moveObject.speed = initialSpeed; // Reset speed to its initial value
                }
            }
            else
            {
                // If a new message is received, reset the elapsed time and speed
                elapsedTime = 0.0f;
                moveObject.speed = initialSpeed;
            }

            // Reset the flag for the next iteration
            hasNewMessage = false;
        }
    }


    void OnDestroy()
    {
        stream.Close();
        client.Close();
        server.Stop();
    }
}
