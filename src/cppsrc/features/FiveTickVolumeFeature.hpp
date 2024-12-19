#pragma once

#include "BaseFeature.hpp"
#include <deque>
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;

class FiveTickVolumeFeature : public BaseFeature
{
  public:
    std::deque<float> tick_volumes;// updated to store only volume (not trades) for last 5 ticks
    float total_volume = 0.0f;

    float compute_feature(std::vector<Trade> data) override
    {
        float current_tick_volume = 0.0f;
        for (const auto &trade : data) { current_tick_volume += std::get<1>(trade); }
        total_volume += current_tick_volume;
        tick_volumes.push_back(current_tick_volume);

        if (tick_volumes.size() > 5) {
            total_volume -= tick_volumes.front();
            tick_volumes.pop_front();
        }

        return total_volume;
    }
};

}// namespace intproj
