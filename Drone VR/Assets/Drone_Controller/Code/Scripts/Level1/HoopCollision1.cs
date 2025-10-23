using UnityEngine;

public class HoopCollisionHandler1 : MonoBehaviour
{
    public TimeCounter timeCounter; // Reference to the TimeCounter script
    public MistakeCounter mistakeCounter; // Reference to the MistakeCounter script
    public Renderer planeRenderer; // Reference to the plane's renderer
    public Material originalMaterial; // Original material with the image
    public Material blackMaterial; // Material for the black image
    public float displayOriginalImageDuration = 5f; // Duration to display the original image

    private bool isDisplayingOriginalImage = false;
    private float originalImageDisplayEndTime;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("WrongHoop1"))
        {
            // This is the hoop where you want to count mistakes
            mistakeCounter.AddMistake();

            // Display the original image for the specified duration
            planeRenderer.material = originalMaterial;
            isDisplayingOriginalImage = true;
            originalImageDisplayEndTime = Time.time + displayOriginalImageDuration;
        }
        else if (other.CompareTag("RightHoop1"))
        {
            // This is the hoop where you want to stop the timer
            timeCounter.timerActive = false;
            planeRenderer.material = originalMaterial;

        }
    }

    void Update()
    {
        if (isDisplayingOriginalImage && Time.time >= originalImageDisplayEndTime)
        {
            // The original image display time is over; turn it black
            planeRenderer.material = blackMaterial;
            isDisplayingOriginalImage = false;
        }
    }
}
