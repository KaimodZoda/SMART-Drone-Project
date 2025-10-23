using UnityEngine;

public class HoopCollisionHandler3_5 : MonoBehaviour
{
    public TimeCounter timeCounter; // Reference to the TimeCounter script
    public MistakeCounter mistakeCounter; // Reference to the MistakeCounter script
    public Renderer planeRenderer; // Reference to the plane's renderer
    public Material originalMaterial; // Original material with the image
    public Material blackMaterial; // Material for the black image
    public float displayOriginalImageDuration = 5f; // Duration to display the original image
    public Renderer[] targetRenderers;
    public GameManager4 gameManager4;

    private bool isDisplayingOriginalImage = false;
    private float originalImageDisplayEndTime;

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("WrongHoop5"))
        {
            // This is the hoop where you want to count mistakes
            mistakeCounter.AddMistake();

            gameManager4.correctHoopsCount1 = 0;
            gameManager4.correctHoopsCount2 = 0;

            gameManager4.Sum();

            // Display the original image for the specified duration
            planeRenderer.material = originalMaterial;
            isDisplayingOriginalImage = true;
            originalImageDisplayEndTime = Time.time + displayOriginalImageDuration;
        }
    }

    void Update()
    {
        if (isDisplayingOriginalImage && Time.time >= originalImageDisplayEndTime)
        {
            // The original image display time is over; turn all selected renderers to black
            SetMaterialForAll(blackMaterial);
            isDisplayingOriginalImage = false;
        }
    }

    private void SetMaterialForAll(Material newMaterial)
    {
        // Change the material for each selected renderer
        foreach (Renderer renderer in targetRenderers)
        {
            renderer.material = newMaterial;
        }
    }
}
