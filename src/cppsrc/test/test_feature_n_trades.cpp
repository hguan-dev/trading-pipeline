#include "NTradesFeature.hpp"
#include "gtest/gtest.h"

TEST(FeatureTests, NTradesTest)
{
    intproj::NTradesFeature ntf;
    EXPECT_EQ(ntf.compute_feature({ { 1, 1, false } }), 1);
    EXPECT_EQ(ntf.compute_feature({ { 2, 1, false }, { 2, 2, true } }), 2);
}
