using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

namespace Click
{
    [RequireComponent(typeof(Drone_Inputs))]
    public class Drone_Controller : Base_Rigidbody
    {
        #region Variables
        [Header("Control Properties")]
        [SerializeField] private float minMaxPitch = 30f;
        [SerializeField] private float minMaxRoll = 30f;
        [SerializeField] private float yawPower = 4f;
        [SerializeField] private float lerpSpeed = 2f;

        private Drone_Inputs input;
        private List<IEngine> engines = new List<IEngine>();

        private float finalPitch;
        private float finalRoll;
        private float yaw;
        private float finalYaw;
        private bool canMove = false;
        private float elapsedTime = 0f;
        #endregion

        #region Main Methods

        void Start()
        {
            input = GetComponent<Drone_Inputs>();
            engines = GetComponentsInChildren<IEngine>().ToList<IEngine>();
        }
        #endregion

        #region Custom Methods
        protected override void HandlePhysics()
        {
            if (elapsedTime < 15f)
            {
                elapsedTime += Time.deltaTime;
            }
            else
            {
                canMove = true;
            }

            if (canMove)
            {
                HandleEngines();
                HandleControls();
            }
        }

        protected virtual void HandleEngines()
        {
            foreach (IEngine engine in engines)
            {
                engine.UpdateEngine(rb, input);
            }
        }

        protected virtual void HandleControls()
        {
            float pitch = input.Cyclic.y * minMaxPitch;
            float roll = input.Cyclic.x * minMaxRoll;
            yaw += input.Pedals * yawPower;

            finalPitch = Mathf.Lerp(finalPitch, pitch, Time.deltaTime * lerpSpeed);
            finalRoll = Mathf.Lerp(finalRoll, roll, Time.deltaTime * lerpSpeed);
            finalYaw = Mathf.Lerp(finalYaw, yaw, Time.deltaTime * lerpSpeed);

            Quaternion rot = Quaternion.Euler(finalPitch, finalYaw, finalRoll);
            rb.MoveRotation(rot);
        }
        #endregion
    }
}
