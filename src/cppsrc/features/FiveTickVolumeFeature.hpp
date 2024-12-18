#ifndef FIVETICKVOLUMEFEATURE_HPP
#define FIVETICKVOLUMEFEATURE_HPP

#include "BaseFeature.hpp"
#include <deque>
#include <tuple>
#include <vector>

namespace intproj {

using Trade = std::tuple<float, float, bool>;// Price, Volume, Buy/Sell flag

class FiveTickVolumeFeature : public BaseFeature
{
  public:
    // Stores the past trades (at most 5 ticks of data)
    std::deque<std::vector<Trade>> past_trades;
    float total_volume = 0.0f;// Running total of volumes

    float compute_feature(std::vector<Trade> data) override
    {
        // Calculate the total volume of the current tick
        float current_tick_volume = 0.0f;
        for (const auto &trade : data) { current_tick_volume += std::get<1>(trade); }

        // Add the current tick's volume to the running total
        total_volume += current_tick_volume;

        // Store the current tick's data
        past_trades.push_back(data);

        // If we have more than 5 ticks, remove the oldest tick
        if (past_trades.size() > 5) {
            const auto &oldest_tick = past_trades.front();
            for (const auto &trade : oldest_tick) { total_volume -= std::get<1>(trade); }
            past_trades.pop_front();
        }

        // Return the current running total volume
        return total_volume;
    }
};

}// namespace intproj

#endif// FIVETICKVOLUMEFEATURE_HPP
