using UnityEngine;

public class MoveObject4 : MonoBehaviour
{
    public float speed = 0.05f; // Adjust the speed in the Inspector
    private Rigidbody rb;

    private bool moveForward = false;
    private bool moveBackward = false;
    private bool moveLeft = false;
    private bool moveRight = false;
    private bool moveUpward = false;
    private bool moveDownward = false;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        // Move the object based on the input and speed
        Vector3 movement = Vector3.zero;

        if (moveForward)
        {
            movement += Vector3.forward;
        }
        if (moveBackward)
        {
            movement += Vector3.back;
        }
        if (moveLeft)
        {
            movement += Vector3.left;
        }
        if (moveRight)
        {
            movement += Vector3.right;
        }
        if (moveUpward)
        {
            movement += Vector3.up;
        }
        if (moveDownward)
        {
            movement += Vector3.down;
        }

        rb.velocity = movement * speed;
    }

    // Methods to set movement direction
    public void MoveForward(bool value)
    {
        moveForward = value;
    }

    public void MoveBackward(bool value)
    {
        moveBackward = value;
    }

    public void MoveLeft(bool value)
    {
        moveLeft = value;
    }

    public void MoveRight(bool value)
    {
        moveRight = value;
    }

    public void MoveUpward(bool value)
    {
        moveUpward = value;
    }

    public void MoveDownward(bool value)
    {
        moveDownward = value;
    }

    public void SetSpeed(float newSpeed)
    {
        speed = newSpeed;
    }

}
