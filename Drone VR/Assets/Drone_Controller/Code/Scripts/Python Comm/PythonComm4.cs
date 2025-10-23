using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class UnitySocketServer4 : MonoBehaviour
{
    public int port = 12345;
    public MoveObject4 moveObject; // Reference to the MoveObject script

    private TcpListener server;
    private TcpClient client;
    private NetworkStream stream;
    private byte[] buffer = new byte[1024];
    private StringBuilder receivedDataBuffer = new StringBuilder();

    void Start()
    {
        server = new TcpListener(IPAddress.Any, port);
        server.Start();
        server.BeginAcceptTcpClient(new System.AsyncCallback(HandleConnection), null);
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
        moveObject.MoveForward(data == "forward");
        moveObject.MoveBackward(data == "backward");
        moveObject.MoveLeft(data == "left");
        moveObject.MoveRight(data == "right");
        moveObject.MoveUpward(data == "up");
        moveObject.MoveDownward(data == "down");

        // Add more conditions based on your requirements
    }

    void OnDestroy()
    {
        stream.Close();
        client.Close();
        server.Stop();
    }
}