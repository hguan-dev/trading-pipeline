#include "features/NTradesFeature.hpp"
#include <iostream>
#include <pybind11/pybind11.h>

#include "features/FiveTickVolumeFeature.hpp"
#include "features/PercentBuyFeature.hpp"
#include "features/PercentSellFeature.hpp"

int main()
{
    return 0;
}


int add(int a, int b)
{
    return a + b;
}

PYBIND11_MODULE(intern, m)
{
    m.def("add", &add, "A function that adds two numbers");

    m.def("num_trades_in_tick", &intproj::NTradesFeature::compute_feature, "Number of trades in a tick");
    m.def("percent_buy_trades", &intproj::PercentBuyFeature::compute_feature, "Percentage of buy trades in a tick");
    m.def("percent_sell_trades", &intproj::PercentSellFeature::compute_feature, "Percentage of sell trades in a tick");
    m.def(
      "sum_volume_last_5_ticks", &intproj::FiveTickVolumeFeature::compute_feature, "Sum of volume in the last 5 ticks");
}
