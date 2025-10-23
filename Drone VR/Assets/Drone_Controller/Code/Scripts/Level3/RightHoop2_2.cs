using UnityEngine;

public class HoopCollisionHandler3_4 : MonoBehaviour
{
    public TimeCounter timeCounter; // Reference to the TimeCounter script
    public MistakeCounter mistakeCounter; // Reference to the MistakeCounter script
    public Renderer planeRenderer; // Reference to the plane's renderer
    public Material originalMaterial; // Original material with the image
    public Material blackMaterial; // Material for the black image
    public float displayOriginalImageDuration = 5f; // Duration to display the original image
    public GameManager4 gameManager4;

    private bool isDisplayingOriginalImage = false;
    private float originalImageDisplayEndTime;

    // Hoop number for RightHoop4
    public int hoopNumber = 4;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("RightHoop4"))
        {
            planeRenderer.material = originalMaterial;
            gameManager4.CorrectHoopPassed2(hoopNumber); // Pass the hoop number to the GameManager4
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
