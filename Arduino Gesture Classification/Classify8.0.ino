#include "imu.h"
#include "modelSVMfold13.h"

Eloquent::ML::Port::SVM classifier;

#define NUM_SAMPLES 50
#define NUM_AXES 3
#define NUM_IMUS 4
#define ACCEL_THRESHOLD 5 
#define INTERVAL 1 //in millisecond, INTERVAL = NUM_SAMPLES / (sampling rate/axis) 
// sometimes you may get "spikes" in the readings
// set a sensible value to truncate too large values
#define TRUNCATE_AT 20

double baseline1[NUM_AXES], baseline2[NUM_AXES], baseline3[NUM_AXES], baseline4[NUM_AXES];
double features1[NUM_SAMPLES * NUM_AXES], features2[NUM_SAMPLES * NUM_AXES], features3[NUM_SAMPLES * NUM_AXES], features4[NUM_SAMPLES * NUM_AXES];
float features[NUM_SAMPLES * NUM_AXES * NUM_IMUS];

void setup() {
    Serial.begin(38400);
    imu_setup();
    calibrate();
}

void loop() {
    float ax1, ay1, az1, ax2, ay2, az2, ax3, ay3, az3, ax4, ay4, az4;

    imu_read(&ax1, &ay1, &az1, &ax2, &ay2, &az2, &ax3, &ay3, &az3, &ax4, &ay4, &az4);

    ax1 = constrain(ax1 - baseline1[0], -TRUNCATE_AT, TRUNCATE_AT);
    ay1 = constrain(ay1 - baseline1[1], -TRUNCATE_AT, TRUNCATE_AT);
    az1 = constrain(az1 - baseline1[2], -TRUNCATE_AT, TRUNCATE_AT);

    ax2 = constrain(ax2 - baseline2[0], -TRUNCATE_AT, TRUNCATE_AT);
    ay2 = constrain(ay2 - baseline2[1], -TRUNCATE_AT, TRUNCATE_AT);
    az2 = constrain(az2 - baseline2[2], -TRUNCATE_AT, TRUNCATE_AT);

    ax3 = constrain(ax3 - baseline3[0], -TRUNCATE_AT, TRUNCATE_AT);
    ay3 = constrain(ay3 - baseline3[1], -TRUNCATE_AT, TRUNCATE_AT);
    az3 = constrain(az3 - baseline3[2], -TRUNCATE_AT, TRUNCATE_AT);

    ax4 = constrain(ax4 - baseline4[0], -TRUNCATE_AT, TRUNCATE_AT);
    ay4 = constrain(ay4 - baseline4[1], -TRUNCATE_AT, TRUNCATE_AT);
    az4 = constrain(az4 - baseline4[2], -TRUNCATE_AT, TRUNCATE_AT);

    //No trunicate
    // ax1 = ax1 - baseline1[0];
    // ay1 = ay1 - baseline1[2];
    // az1 = az1 - baseline1[3];

    // ax2 = ax2 - baseline2[0];
    // ay2 = ay2 - baseline2[2];
    // az2 = az2 - baseline2[3];

    // ax3 = ax3 - baseline3[0];
    // ay3 = ay3 - baseline3[2];
    // az3 = az3 - baseline3[3];

    // ax4 = ax4 - baseline4[0];
    // ay4 = ay4 - baseline4[2];
    // az4 = az4 - baseline4[3];

    // Serial.print("imu1:");
    // Serial.print(imu1.accel_x_mps2());
    // Serial.print("\t");
    // Serial.print(imu1.accel_y_mps2());
    // Serial.print("\t");
    // Serial.print(imu1.accel_z_mps2());
    // Serial.print("\n");

    // Serial.print("imu2");
    // Serial.print(imu2.accel_x_mps2());
    // Serial.print("\t");
    // Serial.print(imu2.accel_y_mps2());
    // Serial.print("\t");
    // Serial.print(imu2.accel_z_mps2());
    // Serial.print("\n");

    // Serial.print("imu3");
    // Serial.print(imu3.accel_x_mps2());
    // Serial.print("\t");
    // Serial.print(imu3.accel_y_mps2());
    // Serial.print("\t");
    // Serial.print(imu3.accel_z_mps2());
    // Serial.print("\n");

    // Serial.print("imu4");
    // Serial.print(imu4.accel_x_mps2());
    // Serial.print("\t");
    // Serial.print(imu4.accel_y_mps2());
    // Serial.print("\t");
    // Serial.print(imu4.accel_z_mps2());
    // Serial.print("\n");

    if (!motionDetected1(ax1, ay1, az1) && !motionDetected2(ax2, ay2, az2) && !motionDetected3(ax3, ay3, az3) && !motionDetected4(ax4, ay4, az4)) {
        delay(10);
        return;
    }

    recordIMU();
    // printFeatures();
    classify();
    delay(1);
}

void calibrate() {
    float ax1, ay1, az1, ax2, ay2, az2, ax3, ay3, az3, ax4, ay4, az4;

    for (int i = 0; i < 10; i++) {
        imu_read(&ax1, &ay1, &az1, &ax2, &ay2, &az2, &ax3, &ay3, &az3, &ax4, &ay4, &az4);
        delay(100);
    }

    baseline1[0] = ax1;
    baseline1[1] = ay1;
    baseline1[2] = az1;

    baseline2[0] = ax2;
    baseline2[1] = ay2;
    baseline2[2] = az2;

    baseline3[0] = ax3;
    baseline3[1] = ay3;
    baseline3[2] = az3;

    baseline4[0] = ax4;
    baseline4[1] = ay4;
    baseline4[2] = az4;
}

bool motionDetected1(float ax1, float ay1, float az1) {
    return (abs(ax1) + abs(ay1) + abs(az1)) > ACCEL_THRESHOLD;
}

bool motionDetected2(float ax2, float ay2, float az2) {
    return (abs(ax2) + abs(ay2) + abs(az2)) > ACCEL_THRESHOLD;
}

bool motionDetected3(float ax3, float ay3, float az3) {
    return (abs(ax3) + abs(ay3) + abs(az3)) > ACCEL_THRESHOLD;
}

bool motionDetected4(float ax4, float ay4, float az4) {
    return (abs(ax4) + abs(ay4) + abs(az4)) > ACCEL_THRESHOLD;
}

void recordIMU() {
    float ax1, ay1, az1, ax2, ay2, az2, ax3, ay3, az3, ax4, ay4, az4;

    for (int i = 0; i < NUM_SAMPLES; i++) {
        imu_read(&ax1, &ay1, &az1, &ax2, &ay2, &az2, &ax3, &ay3, &az3, &ax4, &ay4, &az4);

        ax1 = constrain(ax1 - baseline1[0], -TRUNCATE_AT, TRUNCATE_AT);
        ay1 = constrain(ay1 - baseline1[1], -TRUNCATE_AT, TRUNCATE_AT);
        az1 = constrain(az1 - baseline1[2], -TRUNCATE_AT, TRUNCATE_AT);

        ax2 = constrain(ax2 - baseline2[0], -TRUNCATE_AT, TRUNCATE_AT);
        ay2 = constrain(ay2 - baseline2[1], -TRUNCATE_AT, TRUNCATE_AT);
        az2 = constrain(az2 - baseline2[2], -TRUNCATE_AT, TRUNCATE_AT);

        ax3 = constrain(ax3 - baseline3[0], -TRUNCATE_AT, TRUNCATE_AT);
        ay3 = constrain(ay3 - baseline3[1], -TRUNCATE_AT, TRUNCATE_AT);
        az3 = constrain(az3 - baseline3[2], -TRUNCATE_AT, TRUNCATE_AT);

        ax4 = constrain(ax4 - baseline4[0], -TRUNCATE_AT, TRUNCATE_AT);
        ay4 = constrain(ay4 - baseline4[1], -TRUNCATE_AT, TRUNCATE_AT);
        az4 = constrain(az4 - baseline4[2], -TRUNCATE_AT, TRUNCATE_AT);

        features1[i * NUM_AXES + 0] = ax1;
        features1[i * NUM_AXES + 1] = ay1;
        features1[i * NUM_AXES + 2] = az1;

        features2[i * NUM_AXES + 0] = ax2;
        features2[i * NUM_AXES + 1] = ay2;
        features2[i * NUM_AXES + 2] = az2;

        features3[i * NUM_AXES + 0] = ax3;
        features3[i * NUM_AXES + 1] = ay3;
        features3[i * NUM_AXES + 2] = az3;
        
        features4[i * NUM_AXES + 0] = ax4;
        features4[i * NUM_AXES + 1] = ay4;
        features4[i * NUM_AXES + 2] = az4;
        
        features[i * NUM_AXES + 0] = ax1;
        features[i * NUM_AXES + 1] = ay1;
        features[i * NUM_AXES + 2] = az1;

        features[i * NUM_AXES + 3] = ax2;
        features[i * NUM_AXES + 4] = ay2;
        features[i * NUM_AXES + 5] = az2;

        features[i * NUM_AXES + 6] = ax3;
        features[i * NUM_AXES + 7] = ay3;
        features[i * NUM_AXES + 8] = az3;
        
        features[i * NUM_AXES + 9] = ax4;
        features[i * NUM_AXES + 10] = ay4;
        features[i * NUM_AXES + 11] = az4;

        delay(INTERVAL);
    }
}

void printFeatures() {
    const uint16_t numFeatures1 = sizeof(features1) / sizeof(double);
    const uint16_t numFeatures2 = sizeof(features2) / sizeof(double);
    const uint16_t numFeatures3 = sizeof(features3) / sizeof(double);
    const uint16_t numFeatures4 = sizeof(features4) / sizeof(double);

    for (int i = 0; i < numFeatures1; i++) {
        Serial.print("IMU1:");
        Serial.print("\t");
        Serial.print(features1[i]);
        Serial.print(i == numFeatures1 - 1 ? 'n' : ',');
    }

    for (int i = 0; i < numFeatures2; i++) {
        Serial.print("IMU2:");
        Serial.print("\t");
        Serial.print(features2[i]);
        Serial.print(i == numFeatures2 - 1 ? 'n' : ',');
    }

    for (int i = 0; i < numFeatures3; i++) {
        Serial.print("IMU3:");
        Serial.print("\t");
        Serial.print(features3[i]);
        Serial.print(i == numFeatures3 - 1 ? 'n' : ',');
    }

    for (int i = 0; i < numFeatures4; i++) {
        Serial.print("IMU4:");
        Serial.print("\t");
        Serial.print(features4[i]);
        Serial.print(i == numFeatures4 - 1 ? 'n' : ',');
    }
}

void classify() { 

  Serial.println("Detected gestures:");
  Serial.println(classifier.idxToLabel(classifier.predict(features)));
    
}