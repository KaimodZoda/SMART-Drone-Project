#include <Wire.h>
#include "mpu6500.h"  

#define TCAADDR 0x70

/* Mpu6500 objects */
bfs::Mpu6500 imu1;
bfs::Mpu6500 imu2;
bfs::Mpu6500 imu3;
bfs::Mpu6500 imu4;

void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void imu_setup() {
  Serial.begin(38400);
  while (!Serial);

  Wire.begin();

  /* Initialize the multiplexer */
  tcaselect(2); // Select the port of the multiplexer

  /* Initialize and configure IMU 1 */
  imu1.Config(&Wire, bfs::Mpu6500::I2C_ADDR_PRIM);

  if (!imu1.Begin()) {
    Serial.println("Error initializing communication with IMU 1");
    while(1) {}
  }

  /* Initialize and configure IMU 2 */
  tcaselect(3); // Select the port of the multiplexer
  imu2.Config(&Wire, bfs::Mpu6500::I2C_ADDR_PRIM);

  if (!imu2.Begin()) {
    Serial.println("Error initializing communication with IMU 2");
    while(1) {}
  }

  /* Initialize and configure IMU 3 */
  tcaselect(4); // Select the port of the multiplexer
  imu3.Config(&Wire, bfs::Mpu6500::I2C_ADDR_PRIM);

  if (!imu3.Begin()) {
    Serial.println("Error initializing communication with IMU 3");
    while(1) {}
  }

  /* Initialize and configure IMU 4 */
  tcaselect(5); // Select the port of the multiplexer
  imu4.Config(&Wire, bfs::Mpu6500::I2C_ADDR_PRIM);

  if (!imu4.Begin()) {
    Serial.println("Error initializing communication with IMU 4");
    while(1) {}
  }

  /* Set the sample rate divider for all IMUs */
  if (!imu1.ConfigSrd(19) || !imu2.ConfigSrd(19) || !imu3.ConfigSrd(19) || !imu4.ConfigSrd(19)) {
    Serial.println("Error configured SRD");
    while(1) {}
  }
}

void imu_read(float *ax1, float *ay1, float *az1,float *ax2, float *ay2, float *az2,float *ax3, float *ay3, float *az3,float *ax4, float *ay4, float *az4) {

    tcaselect(2);
    imu1.Read();

    *ax1 = imu1.accel_x_mps2();
    *ay1 = imu1.accel_y_mps2();
    *az1 = imu1.accel_z_mps2();

    tcaselect(3);
    imu2.Read();

    *ax2 = imu2.accel_x_mps2();
    *ay2 = imu2.accel_y_mps2();
    *az2 = imu2.accel_z_mps2();

    tcaselect(4);
    imu3.Read();

    *ax3 = imu3.accel_x_mps2();
    *ay3 = imu3.accel_y_mps2();
    *az3 = imu3.accel_z_mps2();

    tcaselect(5);
    imu4.Read();

    *ax4 = imu4.accel_x_mps2();
    *ay4 = imu4.accel_y_mps2();
    *az4 = imu4.accel_z_mps2();
}