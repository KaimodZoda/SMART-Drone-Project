// imu2.cpp
#include "imu2.h"

// Declare the variables
bfs::Mpu6500 imu1, imu2, imu3, imu4;
PCA9548 MP(0x70);

void imu_setup() {
    Serial.begin(9600);
    while (!Serial) {}

    Wire.begin();

    // Initialize PCA9548A with the I2C address of your specific device
    MP.begin(0x68);

    // Configure each MPU9250 sensor
    configureIMU(imu1, &MP, 0);  // Connect to channel 0 of the multiplexer
    configureIMU(imu2, &MP, 1);  // Connect to channel 1 of the multiplexer
    configureIMU(imu3, &MP, 2);  // Connect to channel 2 of the multiplexer
    configureIMU(imu4, &MP, 3);  // Connect to channel 3 of the multiplexer
}

void configureIMU(bfs::Mpu6500 &imu, PCA9548 *mux, uint8_t channel) {
    mux->isEnabled(channel);
    Wire.setClock(400000);
    imu.Config(&Wire, bfs::Mpu6500::I2C_ADDR_PRIM);

    if (!imu.Begin()) {
        Serial.println("Error initializing communication with IMU");
        while (1) {}
    }

    if (!imu.ConfigSrd(19)) {
        Serial.println("Error configured SRD");
        while (1) {}
    }
}

void imu_read(int imuIndex, float *ax, float *ay, float *az) {
    // Replace the following lines with the actual implementation based on your setup
    // For example, if using imu1, imu2, imu3, imu4, read the values accordingly
    switch (imuIndex) {
        case 0:
            imu1.Read();
            *ax = imu1.accel_x_mps2();
            *ay = imu1.accel_y_mps2();
            *az = imu1.accel_z_mps2();
            break;
        case 1:
            imu2.Read();
            *ax = imu2.accel_x_mps2();
            *ay = imu2.accel_y_mps2();
            *az = imu2.accel_z_mps2();
            break;
        case 2:
            imu3.Read();
            *ax = imu3.accel_x_mps2();
            *ay = imu3.accel_y_mps2();
            *az = imu3.accel_z_mps2();
            break;
        case 3:
            imu4.Read();
            *ax = imu4.accel_x_mps2();
            *ay = imu4.accel_y_mps2();
            *az = imu4.accel_z_mps2();
            break;
        // Add more cases if needed
        default:
            break;
    }
}
