#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "features/FiveTickVolumeFeature.hpp"
#include "features/NTradesFeature.hpp"
#include "features/PercentBuyFeature.hpp"
#include "features/PercentSellFeature.hpp"

namespace py = pybind11;

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

    // Expose NTradesFeature class
    py::class_<intproj::NTradesFeature>(m, "NTradesFeature")
      .def(py::init<>())
      .def("compute_feature", &intproj::NTradesFeature::compute_feature, "Number of trades in a tick");

    // Expose PercentBuyFeature class
    py::class_<intproj::PercentBuyFeature>(m, "PercentBuyFeature")
      .def(py::init<>())
      .def("compute_feature", &intproj::PercentBuyFeature::compute_feature, "Percentage of buy trades in a tick");

    // Expose PercentSellFeature class
    py::class_<intproj::PercentSellFeature>(m, "PercentSellFeature")
      .def(py::init<>())
      .def("compute_feature", &intproj::PercentSellFeature::compute_feature, "Percentage of sell trades in a tick");

    // Expose FiveTickVolumeFeature class
    py::class_<intproj::FiveTickVolumeFeature>(m, "FiveTickVolumeFeature")
      .def(py::init<>())
      .def("compute_feature", &intproj::FiveTickVolumeFeature::compute_feature, "Sum of volume in the last 5 ticks");
}
