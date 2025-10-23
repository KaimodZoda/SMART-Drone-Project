// imu2.h
#ifndef IMU2_H
#define IMU2_H

#include "Wire.h"
#include "mpu6500.h"
#include "TCA9548.h"

extern bfs::Mpu6500 imu1, imu2, imu3, imu4;
extern PCA9548 MP;

void imu_setup();
void configureIMU(bfs::Mpu6500 &imu, PCA9548 *mux, uint8_t channel);
void imu_read(int imuIndex, float *ax, float *ay, float *az);  // Updated function signature

#endif
