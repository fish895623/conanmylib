from conans import ConanFile, CMake


class MylibConan(ConanFile):
    name = "mylib"
    version = "0.0.1"
    license = "MIT"
    author = "fish895623 dan990429@gmail.com"
    url = "https://github.com/fish895623/conanmylib.git"
    description = "Testing for conan uploading"
    topics = ("privatetest")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        self.run("git clone https://github.com/fish895623/conanmylib.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(cache_build_folder='build')
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["mylib"]
