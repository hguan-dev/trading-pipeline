# Set the project name and required CMake version
cmake_minimum_required(VERSION 3.20)
project(intern LANGUAGES CXX)

# Set the C++ flags and compiler options
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

# Find Python and pybind11
find_package(Python3 3.12 COMPONENTS Interpreter Development EXACT REQUIRED)
find_package(pybind11 REQUIRED)

# Find GTest
find_package(GTest REQUIRED)
enable_testing()

# Collect the main source files and headers
file(GLOB INTERN_PROJECT_MAIN src/cppsrc/main.cpp)
file(GLOB_RECURSE INTERN_PROJECT_HEADERS src/cppsrc/*.hpp)
file(GLOB_RECURSE INTERN_PROJECT_TESTS src/cppsrc/test/*.cpp)

# Add the main project executable
add_executable(intern_project ${INTERN_PROJECT_MAIN} ${INTERN_PROJECT_HEADERS})

# Add the test executable
add_executable(intern_tests ${INTERN_PROJECT_TESTS} ${INTERN_PROJECT_HEADERS})

# Set the include directories for the tests
target_include_directories(intern_tests PRIVATE src/cppsrc/features src/cppsrc)

# Link the necessary libraries
target_link_libraries(intern_project PRIVATE Python3::Python pybind11::pybind11 ${Python3_LIBRARIES})
target_link_libraries(intern_tests PRIVATE Python3::Python pybind11::pybind11 ${Python3_LIBRARIES} gtest::gtest)

# Add the pybind module
pybind11_add_module(intern src/cppsrc/main.cpp)

# Install the pybind module
install(TARGETS intern DESTINATION intern_project)

