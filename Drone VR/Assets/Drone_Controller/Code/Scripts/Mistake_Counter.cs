using UnityEngine;
using TMPro;

public class MistakeCounter : MonoBehaviour
{
    public TextMeshProUGUI mistakeText; // Reference to a TextMeshPro Text component to display the mistake count
    private int mistakeCount = 0;

    public void AddMistake()
    {
        mistakeCount++;
        UpdateMistakeText();
    }

    private void UpdateMistakeText()
    {
        if (mistakeText != null)
        {
            mistakeText.text = "Mistakes: " + mistakeCount;
        }
    }
}
