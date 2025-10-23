using UnityEngine;

public class GameManager : MonoBehaviour
{
    public TimeCounter timeCounter; // Reference to the TimeCounter script
    public int correctHoopsCount = 0;

    // Called when a correct hoop is passed
    public void CorrectHoopPassed()
    {
        correctHoopsCount++;

        // Check if the required number of correct hoops have been passed
        if (correctHoopsCount >= 2)
        {
            StopTimer();
        }
    }

    // Stop the timer and permanently display the original image
    private void StopTimer()
    {
        timeCounter.timerActive = false;
    }
}
