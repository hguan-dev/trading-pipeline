#ifndef PERCENTBUYFEATURE_HPP
#define PERCENTBUYFEATURE_HPP

#include "BaseFeature.hpp"
#include <cmath>
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;// Price, Volume, Buy/Sell flag

class PercentBuyFeature : public BaseFeature
{
  public:
    // Compute the percentage of buy trades in the dataset
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        int buy_count = 0;
        for (const auto &trade : data) {
            if (std::get<2>(trade)) { buy_count++; }
        }
        return (data.empty()) ? 0.0f : std::round(static_cast<float>(buy_count) / data.size() * 100.0f) / 100.0f;
    }
};

}// namespace intproj

#endif// PERCENTBUYFEATURE_HPP
