#include "FiveTickVolumeFeature.hpp"
#include "gtest/gtest.h"

TEST(FeatureTests, TestSum5TickVolume)
{
    intproj::FiveTickVolumeFeature vf;
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false } }), 1);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false } }), 2);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 4);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 6);
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false }, { 1, 1, true } }), 8);
    EXPECT_EQ(vf.compute_feature({ { 1, 1, false }, { 1, 1, true } }), 9);
    EXPECT_EQ(vf.compute_feature({ { 2, 1, false }, { 1, 1, true } }), 10);
}
