using UnityEngine;

public class MoveObject3 : MonoBehaviour
{
    public float speed = 0.5f; // Adjust the speed in the Inspector
    private Rigidbody rb;

    private bool moveForward = false;
    private bool moveBackward = false;
    private bool moveLeft = false;
    private bool moveRight = false;
    private bool moveUpward = false;
    private bool moveDownward = false;

    private float delayTimer = 0f;
    private float delayDuration = 1f; // Adjust the delay duration as needed

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        // Move the object based on the input and speed
        Vector3 movement = Vector3.zero;

        // Move forward
        if (moveForward)
        {
            movement += Vector3.forward;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
        }

        // Move backward
        if (moveBackward)
        {
            movement += Vector3.back;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
        }

        // Move left
        if (moveLeft)
        {
            movement += Vector3.left;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
        }

        // Move right
        if (moveRight)
        {
            movement += Vector3.right;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
        }

        // Move upward
        if (moveUpward)
        {
            movement += Vector3.up;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
        }

        // Move downward
        if (moveDownward)
        {
            movement += Vector3.down;
            if (delayTimer >= delayDuration)
            {
                speed = 0f; // Slow down the speed after the delay
            }
            else
            {
                delayTimer += Time.fixedDeltaTime; // Increment the delay timer
            }
        }
        else
        {
            // Reset the delay timer if the movement input is released
            delayTimer = 0f;
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
}
