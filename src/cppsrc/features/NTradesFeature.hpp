#pragma once

#include "BaseFeature.hpp"
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;

class NTradesFeature : public BaseFeature
{
  public:
    // Compute the number of trades in the dataset
    float compute_feature(std::vector<Trade> data) override
    {
        return static_cast<float>(data.size());
    }
};

}// namespace intproj
