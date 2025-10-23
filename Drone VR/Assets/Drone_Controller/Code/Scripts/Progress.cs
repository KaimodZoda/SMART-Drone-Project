using UnityEngine;
using TMPro;

public class DisplayScore : MonoBehaviour
{
    public TextMeshProUGUI scoreText;
    public GameManager4 gameManager;

    void Start()
    {
        // Ensure that a TextMeshProUGUI component and GameManager4 are assigned in the Inspector
        if (scoreText == null)
        {
            Debug.LogError("TextMeshProUGUI component is not assigned!");
        }

        if (gameManager == null)
        {
            Debug.LogError("GameManager4 is not assigned!");
        }
    }

    void Update()
    {
        // Update the TMP Text with the TotalCorrectHoop value from GameManager4
        if (scoreText != null && gameManager != null)
        {
            scoreText.text = "Progress: " + gameManager.TotalCorrectHoop + "/4";

            //Score Counting Debug
            //scoreText.text = "Progress: " + gameManager.TotalCorrectHoop + "/4" + "Pair 1:" + gameManager.correctHoopsCount1 + "Pair 2:" + gameManager.correctHoopsCount2;
        }
    }
}
