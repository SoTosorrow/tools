#include <iterator>
#include <algorithm>
#include <iostream>
#include <type_traits>

namespace ut {
    auto inprint = [](auto i) { std::cout<<i<<" "; };

    void print(const auto& v) {
        std::for_each(v.begin(), v.end(), inprint);
    }

    template<typename Iter>
    void printIter(const Iter& iter) {
        if constexpr (
            std::is_same_v<
                decltype(std::begin(iter)), 
                decltype(std::end(iter))
            >
        ) {
            std::for_each(iter.begin(), iter.end(), inprint);
        } else {
            static_assert(false, "Not Iter Type");
        }
    }
}