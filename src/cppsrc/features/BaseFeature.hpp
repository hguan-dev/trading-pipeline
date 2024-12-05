#ifndef INTPROJ_BASE_FEATURE_HPP
#define INTPROJ_BASE_FEATURE_HPP
#include <tuple>
#include <vector>

namespace intproj {

class BaseFeature
{
  public:
    virtual float compute_feature(std::vector<std::tuple<float, float, bool>> data) = 0;

    virtual ~BaseFeature() {}
};

}// namespace intproj

#endif// INTPROJ_BASE_FEATURE_HPP
