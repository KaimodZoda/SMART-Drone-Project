#pragma once
#include <cstdarg>
namespace Eloquent {
    namespace ML {
        namespace Port {
            class DecisionTree {
                public:
                    /**
                    * Predict class for features vector
                    */
                    int predict(float *x) {
                        if (x[6] <= 3.609999895095825) {
                            return 4;
                        }

                        else {
                            if (x[0] <= 2.2200000286102295) {
                                return 3;
                            }

                            else {
                                if (x[8] <= 4.194999933242798) {
                                    if (x[7] <= 5.619999885559082) {
                                        if (x[6] <= 14.644999980926514) {
                                            if (x[9] <= 12.080000400543213) {
                                                if (x[10] <= -7.53000020980835) {
                                                    return 1;
                                                }

                                                else {
                                                    return 2;
                                                }
                                            }

                                            else {
                                                if (x[8] <= -2.6599998474121094) {
                                                    return 0;
                                                }

                                                else {
                                                    return 5;
                                                }
                                            }
                                        }

                                        else {
                                            if (x[8] <= 1.2450000643730164) {
                                                if (x[1] <= 1.0100000202655792) {
                                                    return 0;
                                                }

                                                else {
                                                    return 2;
                                                }
                                            }

                                            else {
                                                return 5;
                                            }
                                        }
                                    }

                                    else {
                                        if (x[0] <= 11.524999618530273) {
                                            return 1;
                                        }

                                        else {
                                            if (x[9] <= 13.885000228881836) {
                                                return 5;
                                            }

                                            else {
                                                return 0;
                                            }
                                        }
                                    }
                                }

                                else {
                                    if (x[7] <= 8.204999923706055) {
                                        return 5;
                                    }

                                    else {
                                        return 1;
                                    }
                                }
                            }
                        }
                    }

                    /**
                    * Predict readable class name
                    */
                    const char* predictLabel(float *x) {
                        return idxToLabel(predict(x));
                    }

                    /**
                    * Convert class idx to readable name
                    */
                    const char* idxToLabel(uint8_t classIdx) {
                        switch (classIdx) {
                            case 0:
                            return "Backward";
                            case 1:
                            return "Down";
                            case 2:
                            return "Forward";
                            case 3:
                            return "Left";
                            case 4:
                            return "Right";
                            case 5:
                            return "Up";
                            default:
                            return "Houston we have a problem";
                        }
                    }

                protected:
                };
            }
        }
    }