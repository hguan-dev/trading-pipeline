#ifndef FIVETICKVOLUMEFEATURE_HPP
#define FIVETICKVOLUMEFEATURE_HPP

#include "BaseFeature.hpp"
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;// Price, Volume, Buy/Sell flag

class FiveTickVolumeFeature : public BaseFeature
{
  public:
    // Compute the sum of volume in the last 5 ticks
    float compute_feature(std::vector<std::tuple<float, float, bool>> data) override
    {
        float sum = 0.0f;
        int count = 0;
        for (auto it = data.rbegin(); it != data.rend() && count < 5; ++it) {
            sum += std::get<1>(*it);// Add the volume (second element in tuple)
            count++;
        }
        return sum;
    }
};

}// namespace intproj

#endif// FIVETICKVOLUMEFEATURE_HPP
