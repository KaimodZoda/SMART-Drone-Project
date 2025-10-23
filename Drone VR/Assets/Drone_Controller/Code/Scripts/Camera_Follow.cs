using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform target;  // Reference to the drone's transform
    public Vector3 offset;    // Offset of the camera from the drone

    public float rotationSpeed = 5f;  // Speed of the camera rotation

    // Adjust these parameters to control camera movement smoothness
    public float smoothPosition = 0.125f;
    public float smoothRotation = 5f;

    void LateUpdate()
    {
        if (target == null)
        {
            Debug.LogWarning("Camera target not set!");
            return;
        }

        // Calculate the desired position of the camera
        Vector3 desiredPosition = target.position + offset;

        // Smoothly move the camera towards the desired position
        transform.position = Vector3.Lerp(transform.position, desiredPosition, Time.deltaTime * smoothPosition);

        // Make the camera look at the target (drone) with smooth rotation
        Quaternion lookRotation = Quaternion.LookRotation(target.position - transform.position);
        transform.rotation = Quaternion.Slerp(transform.rotation, lookRotation, Time.deltaTime * smoothRotation);

        // Handle mouse input for rotation
        float horizontalInput = Input.GetAxis("Mouse X") * rotationSpeed;
        float verticalInput = Input.GetAxis("Mouse Y") * rotationSpeed;

        // Rotate the camera based on mouse input
        transform.RotateAround(target.position, Vector3.up, horizontalInput);
        transform.RotateAround(target.position, transform.right, -verticalInput);
    }
}
