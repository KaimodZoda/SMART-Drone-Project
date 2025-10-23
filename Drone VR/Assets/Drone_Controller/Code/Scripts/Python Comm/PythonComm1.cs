using System.Net;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class UnitySocketServer : MonoBehaviour
{
    public int port = 12345;

    private TcpListener server;
    private TcpClient client;
    private NetworkStream stream;
    private byte[] buffer = new byte[1024];

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
        Debug.Log("Received data from Python: " + receivedData);

        // Process received data and perform actions in Unity
        ProcessReceivedData(receivedData);

        // Continue listening for more data
        stream.BeginRead(buffer, 0, buffer.Length, new System.AsyncCallback(ReadCallback), null);
    }

    void ProcessReceivedData(string data)
    {
        // Interpret the received data and perform actions in Unity
        switch (data.ToLower())
        {
            case "left":
                // Move the player to the left
                Debug.Log("Move player to the left");
                break;
            case "right":
                // Move the player to the right
                Debug.Log("Move player to the right");
                break;
            case "forward":
                // Move the player forward
                Debug.Log("Move player forward");
                break;
            case "backward":
                // Move the player backward
                Debug.Log("Move player backward");
                break;
            default:
                // Handle other commands as needed
                break;
        }

        // Send a response back to Python if needed
        string response = "Command received";
        byte[] responseBytes = Encoding.UTF8.GetBytes(response);
        stream.Write(responseBytes, 0, responseBytes.Length);
    }

    void OnDestroy()
    {
        stream.Close();
        client.Close();
        server.Stop();
    }
}
