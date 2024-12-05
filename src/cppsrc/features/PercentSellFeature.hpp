#ifndef PERCENTSELLFEATURE_HPP
#define PERCENTSELLFEATURE_HPP

#include "BaseFeature.hpp"
#include <cmath>
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;// Price, Volume, Buy/Sell flag

class PercentSellFeature : public BaseFeature
{
  public:
    // Compute the percentage of sell trades in the dataset
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        int sell_count = 0;
        for (const auto &trade : data) {
            if (!std::get<2>(trade)) { sell_count++; }
        }
        float percentage = (data.empty()) ? 0.0f : static_cast<float>(sell_count) / data.size();
        return std::round(percentage * 100.0f) / 100.0f;
    }
};

}// namespace intproj

#endif// PERCENTSELLFEATURE_HPP
