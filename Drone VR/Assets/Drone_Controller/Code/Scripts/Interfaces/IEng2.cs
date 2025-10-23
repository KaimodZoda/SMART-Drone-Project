using System;
using System.Collections;
using System.Collections.Generic;
using System.Xml.Serialization;
using UnityEngine;

namespace Click
{
    public interface IEngine2
    {
        void InitEngine();
        void UpdateEngine(Rigidbody rb, Drone_Inputs2 input);
    }

}