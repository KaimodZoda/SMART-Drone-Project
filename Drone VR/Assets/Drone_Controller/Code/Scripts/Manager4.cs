using UnityEngine;
using System.Collections;

public class GameManager4 : MonoBehaviour
{
    public TimeCounter timeCounter; // Reference to the TimeCounter script
    public int correctHoopsCount1 = 0;
    public int correctHoopsCount2 = 0;
    public int TotalCorrectHoop;
    public MistakeCounter mistakeCounter;
    public Material blackMaterial;
    public float delayDuration = 5f; // Adjust the delay duration as needed

    public Renderer[] targetRenderers; // Assign your 5 specific renderers in the Inspector

    private int lastHoopPassed1 = 0; // Keep track of the last hoop passed for CorrectHoopPassed1
    private int lastHoopPassed2 = 0; // Keep track of the last hoop passed for CorrectHoopPassed2

    // Called when a correct hoop is passed (Event 1)
    public void CorrectHoopPassed1(int hoopNumber)
    {
        if (hoopNumber != lastHoopPassed1) // Check if it's a new hoop
        {
            correctHoopsCount1++;

            // Check conditions and reset if needed with a delay
            StartCoroutine(CheckAndResetCounts());

            Sum();

            lastHoopPassed1 = hoopNumber; // Update the last hoop passed for CorrectHoopPassed1
        }
    }

    // Called when a correct hoop is passed (Event 2)
    public void CorrectHoopPassed2(int hoopNumber)
    {
        if (hoopNumber != lastHoopPassed2) // Check if it's a new hoop
        {
            correctHoopsCount2++;

            // Check conditions and reset if needed with a delay
            StartCoroutine(CheckAndResetCounts());

            Sum();

            lastHoopPassed2 = hoopNumber; // Update the last hoop passed for CorrectHoopPassed2
        }
    }

    private IEnumerator CheckAndResetCounts()
    {
        // If CorrectHoopPassed1 is triggered and correctHoopsCount2 is 1, reset correctHoopsCount1
        if (correctHoopsCount1 == 1 && correctHoopsCount2 == 1)
        {
            correctHoopsCount1 = 0;
            correctHoopsCount2 = 0;
            mistakeCounter.AddMistake();

            // Add a delay before changing the material for selected renderers
            yield return new WaitForSeconds(delayDuration);

            // Change the material of selected plane renderers after the delay
            ChangeMaterialForSelected(blackMaterial);
        }
        // If CorrectHoopPassed2 is triggered and correctHoopsCount1 is 1, reset correctHoopsCount2
        else if (correctHoopsCount2 == 1 && correctHoopsCount1 == 1)
        {
            correctHoopsCount1 = 0;
            correctHoopsCount2 = 0;
            mistakeCounter.AddMistake();

            // Add a delay before changing the material for selected renderers
            yield return new WaitForSeconds(delayDuration);

            // Change the material of selected plane renderers after the delay
            ChangeMaterialForSelected(blackMaterial);
        }
    }

    private void ChangeMaterialForSelected(Material newMaterial)
    {
        // Change the material for each selected renderer
        foreach (Renderer renderer in targetRenderers)
        {
            renderer.material = newMaterial;
        }
    }

    public void Sum()
    {
        // If the total is 4, trigger the StopTimer
        TotalCorrectHoop = correctHoopsCount1 + correctHoopsCount2;
        if (TotalCorrectHoop == 4)
        {
            StopTimer();
        }
    }

    private void StopTimer()
    {
        timeCounter.timerActive = false;
    }
}
