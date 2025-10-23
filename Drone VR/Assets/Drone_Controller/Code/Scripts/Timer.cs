using UnityEngine;
using TMPro;

public class TimeCounter : MonoBehaviour
{
    private float countdownStartTime;
    private float startTime;
    private TextMeshProUGUI elapsedTimeText;
    public bool timerActive = true;

    // Add a variable to control the countdown
    private bool countdownActive = true;
    private float countdownDuration = 15f;

    public Material finishMaterial; // Material for when countdown finishes 

    public Renderer planeRenderer1; // Reference to the first plane's renderer
    public Material countdownMaterial1; // Material for the countdown phase for the first plane
    
    public Renderer planeRenderer2; // Reference to the second plane's renderer
    public Material countdownMaterial2; // Material for the countdown phase for the second plane
 
    public Renderer planeRenderer3; // Reference to the third plane's renderer
    public Material countdownMaterial3; // Material for the countdown phase for the third plane
    
    public Renderer planeRenderer4; // Reference to the Fourth plane's renderer
    public Material countdownMaterial4; // Material for the countdown phase for the Fourth plane
  
    public Renderer planeRenderer5; // Reference to the Fifth plane's renderer
    public Material countdownMaterial5; // Material for the countdown phase for the Fifth plane
 
    public TextMeshProUGUI objectiveText; // Reference to the UI Text element for the objective
    public TextMeshProUGUI gameoverText; // Reference to the UI Text element for the game over
    void Start()
    {
        // Record the time when the game starts
        startTime = Time.time;

        // Find the TextMeshProUGUI component
        elapsedTimeText = GetComponent<TextMeshProUGUI>();

        // Record the time when the countdown starts
        countdownStartTime = Time.time;

        // Initialize the planes with the countdown materials
        planeRenderer1.material = countdownMaterial1;
        planeRenderer2.material = countdownMaterial2;
        planeRenderer3.material = countdownMaterial3;
        planeRenderer4.material = countdownMaterial4;
        planeRenderer5.material = countdownMaterial5;

        // Set the objective text as inactive at the start
        objectiveText.gameObject.SetActive(false);
        // Set the gameover text as inactive at the start
        gameoverText.gameObject.SetActive(false);
    }

    void Update()
    {
        if (countdownActive)
        {
            // Calculate the remaining time in the countdown
            float remainingTime = countdownDuration - (Time.time - countdownStartTime);

            // Check if the countdown has ended
            if (remainingTime <= 0)
            {
                // Countdown has ended; start the timer
                countdownActive = false;
                startTime = Time.time; // Reset the start time

                // Apply the finish materials to the planes
                planeRenderer1.material = finishMaterial;
                planeRenderer2.material = finishMaterial;
                planeRenderer3.material = finishMaterial;
                planeRenderer4.material = finishMaterial;
                planeRenderer5.material = finishMaterial;

                objectiveText.gameObject.SetActive(true);
            }
            else
            {
                // Display the remaining time in the countdown
                string formattedTime = remainingTime.ToString("F1") + " seconds";
                elapsedTimeText.text = "Countdown: " + formattedTime;
            }
        }
        else if (timerActive)
        {
            // Calculate the elapsed time
            float elapsedTime = Time.time - startTime;
            string formattedTime = elapsedTime.ToString("F2") + " seconds";

            // Update the TextMeshProUGUI text with the elapsed time
            elapsedTimeText.text = "Time Elapsed: " + formattedTime;
        }
        else if (timerActive == false)
        {
            gameoverText.gameObject.SetActive(true);
        }
    }
}
