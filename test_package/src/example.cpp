#include <iostream>

int main() {
    std::cout << "Hello world" << std::endl;
#ifdef EXAMPLE_DEFINE
    std::cout << "Got preprocessor define from base class" << std::endl;
#else
    std::cout << "Missing preprocessor define" << std::endl;
    return -1;
#endif
}
