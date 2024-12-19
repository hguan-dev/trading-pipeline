#pragma once

#include "BaseFeature.hpp"
#include <cmath>
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;

class PercentSellFeature : public BaseFeature
{
  public:
    // Compute the percentage of sell trades in the dataset
    float compute_feature(std::vector<Trade> data) override
    {
        int sell_count = 0;
        for (const auto &trade : data) {
            if (!std::get<2>(trade)) { sell_count++; }
        }
        return (data.empty()) ? 0.0f : static_cast<float>(sell_count) / data.size();
    }
};

}// namespace intproj
