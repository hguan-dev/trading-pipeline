#ifndef NTRADESFEATURE_HPP
#define NTRADESFEATURE_HPP

#include "BaseFeature.hpp"
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;// Price, Volume, Buy/Sell flag

class NTradesFeature : public BaseFeature
{
  public:
    // Compute the number of trades in the dataset
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        return static_cast<float>(data.size());
    }
};

}// namespace intproj

#endif// NTRADESFEATURE_HPP
