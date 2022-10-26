from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout

class MyBase(object):
    def source(self):
        self.output.info("My cool source!")
        print("source call")
    def build(self):
        print("Inherited build")
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.output.info("My cool package!")
    def package_info(self):
        self.output.info("My cool package_info!")

    def layout(self):
        cmake_layout(self)

class PyReq(ConanFile):
    name = "pyreq"
    version = "0.1.3"

    def init(self):
        f = open("./test_package/version.txt","w")
        f.write(self.version)