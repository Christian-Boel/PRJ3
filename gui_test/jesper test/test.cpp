#include "test.py"
#include <pybind1/pybind11.h>
#include <iostream>

namespace py = pybind11;
using namespace std;

void main(){
    py::scoped_interpreter python;
    
    auto printVariabel = py::module::import("sendFunction");
    cout << printVa
}