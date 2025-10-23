using System.Collections;
using System.Collections.Generic;
using System.Numerics;
using UnityEngine;
using UnityEngine.InputSystem;

namespace Click
{
    [RequireComponent(typeof(PlayerInput))]
    public class Drone_Inputs2 : MonoBehaviour
    {
        #region Variables

        private UnityEngine.Vector2 cyclic;
        private float pedals;
        private float throttle;

        public UnityEngine.Vector2 Cyclic2
        {
            get => cyclic;
            set => cyclic = value;
        }

        public float Pedals2
        {
            get => pedals;
            set => pedals = value;
        }

        public float Throttle2
        {
            get => throttle;
            set => throttle = value;
        }
        #endregion

        #region Main Methods
        void Update()
        {

        }
        #endregion

        #region Input Methods
        private void OnCyclic(InputValue value)
        {
            cyclic = value.Get<UnityEngine.Vector2>();
        }

        private void OnPedals(InputValue value)
        {
            pedals = value.Get<float>();
        }

        private void OnThrottle(InputValue value)
        {
            throttle = value.Get<float>();
        }
        #endregion
    }
}
