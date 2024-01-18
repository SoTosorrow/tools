// #include<streambuf>?
#include<sstream>
#include<iostream>
#include<thread>

int main() {
    std::string s = "123_123 123 asd";
    std::stringstream ss;ss << s;
    std::string tmp;


    auto thd_handle = std::thread([&ss](){
        std::cout<<"thread1\n";
        while(true){
            ss << "123 ";
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }
    });
    while(ss >> tmp) {
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
        std::cout<<tmp<<"\n";
    }
    std::cout<<"main go away\n";

    thd_handle.join();

    return 0;
}