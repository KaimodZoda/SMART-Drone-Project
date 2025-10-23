#include "imu2.h"
// put the code you got in Step 3 into this file
#include "model.h"
#include "digipot.h"

// this class will be different if you used another type of classifier, just check the model.h file
Eloquent::ML::Port::RandomForest classifier;

#define NUM_IMUS 4  // Number of IMU sensors
#define NUM_SAMPLES 30
#define NUM_AXES 3
#define TRUNCATE_AT 20
#define ACCEL_THRESHOLD 5

double baseline[NUM_IMUS][NUM_AXES];
double features[NUM_IMUS][NUM_SAMPLES * NUM_AXES];
float flattenedFeatures[NUM_SAMPLES * NUM_AXES * NUM_IMUS]; // Adjusted size to accommodate all elements

void setup() {
    Serial.begin(9600);
    imu_setup();
    calibrate();
}

void loop() {
    float ax[NUM_IMUS], ay[NUM_IMUS], az[NUM_IMUS];

    for (int i = 0; i < NUM_IMUS; i++) {
        imu_read(i, &ax[i], &ay[i], &az[i]);
        ax[i] = constrain(ax[i] - baseline[i][0], -TRUNCATE_AT, TRUNCATE_AT);
        ay[i] = constrain(ay[i] - baseline[i][1], -TRUNCATE_AT, TRUNCATE_AT);
        az[i] = constrain(az[i] - baseline[i][2], -TRUNCATE_AT, TRUNCATE_AT);
    }

    if (!motionDetected(ax[0], ay[0], az[0]) && !motionDetected(ax[1], ay[1], az[1]) &&
        !motionDetected(ax[2], ay[2], az[2]) && !motionDetected(ax[3], ay[3], az[3])) {
        delay(10);
        return;
    }

    for (int i = 0; i < NUM_IMUS; i++) {
        recordIMU(i, ax[i], ay[i], az[i]);
    }

    // for (int i = 0; i < NUM_IMUS; i++) {
    //     printFeatures(i);
    // }
  
    classify();

    delay(2000);
}

void calibrate() {
    float ax[NUM_IMUS], ay[NUM_IMUS], az[NUM_IMUS];

    for (int i = 0; i < NUM_IMUS; i++) {
        for (int j = 0; j < 10; j++) {
            imu_read(i, &ax[i], &ay[i], &az[i]);
            delay(100);
        }

        baseline[i][0] = ax[i];
        baseline[i][1] = ay[i];
        baseline[i][2] = az[i];
    }
}

void recordIMU(int imuIndex, float ax, float ay, float az) {
    for (int i = 0; i < NUM_SAMPLES; i++) {
        ax = constrain(ax - baseline[imuIndex][0], -TRUNCATE_AT, TRUNCATE_AT);
        ay = constrain(ay - baseline[imuIndex][1], -TRUNCATE_AT, TRUNCATE_AT);
        az = constrain(az - baseline[imuIndex][2], -TRUNCATE_AT, TRUNCATE_AT);

        features[imuIndex][i * NUM_AXES + 0] = ax;
        features[imuIndex][i * NUM_AXES + 1] = ay;
        features[imuIndex][i * NUM_AXES + 2] = az;

        flatten();
        delay(100);
    }
}

void flatten() {
  // Flatten the features array
    int index = 0;

    for (int sampleIndex = 0; sampleIndex < NUM_SAMPLES; sampleIndex++) {
        for (int axisIndex = 0; axisIndex < NUM_AXES; axisIndex++) {
            for (int imuIndex = 0; imuIndex < NUM_IMUS; imuIndex++) {
                flattenedFeatures[index++] = features[imuIndex][sampleIndex * NUM_AXES + axisIndex];
            }
        }
    }
       // Print the flattenedFeatures array for testing
    for (int i = 0; i < NUM_SAMPLES * NUM_AXES * NUM_IMUS; i++) {
        Serial.print(flattenedFeatures[i]);
        Serial.print(" ");
    }

}

void classify() {
    const int chunkSize = 12;  // Define the chunk size

    Serial.println("Detected gestures:");

    // Iterate over flattenedFeatures in chunks of 12 values
    for (int i = 0; i < NUM_SAMPLES * NUM_AXES * NUM_IMUS; i += chunkSize) {
        // Extract a chunk of 12 values from flattenedFeatures
        float chunk[chunkSize];
        for (int j = 0; j < chunkSize; j++) {
            chunk[j] = flattenedFeatures[i + j];
        }

        // Perform classification on the chunk
        int gestureIdx = classifier.predict(chunk);
        String gestureLabel = classifier.idxToLabel(gestureIdx);

        // Print the result
        Serial.print("Gesture for values ");
        Serial.print(i);
        Serial.print(" to ");
        Serial.print(i + chunkSize - 1);
        Serial.print(": ");
        Serial.println(gestureLabel);
    }
}


// void printFeatures(int imuIndex) {
//     const uint16_t numFeatures = NUM_SAMPLES * NUM_AXES;

//     Serial.print("IMU ");
//     Serial.print(imuIndex);
//     Serial.print(": ");

//     for (int i = 0; i < numFeatures; i++) {
//         Serial.print(features[imuIndex][i]);
//         Serial.print(i == numFeatures - 1 ? '\n' : ',');
//     }
// }

bool motionDetected(float ax, float ay, float az) {
    return (abs(ax) + abs(ay) + abs(az)) > ACCEL_THRESHOLD;
}
