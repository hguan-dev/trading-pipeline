#include "PercentSellFeature.hpp"
#include "gtest/gtest.h"

TEST(FeatureTests, PctSellTest)
{
    intproj::PercentSellFeature psf;
    EXPECT_EQ(psf.compute_feature({ { 1, 1, false } }), 1);
    EXPECT_EQ(psf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 0.5);
    float result = psf.compute_feature({ { 1, 1, false }, { 1, 1, true }, { 1, 2, false } });
    float epsilon = 0.01f;
    EXPECT_NEAR(result, 0.67f, epsilon);
}
