#include <iterator>
#include <algorithm>
#include <iostream>
#include <type_traits>

#include "de.hpp"

namespace ut {
    auto inprint = [](auto i) { std::cout<<i<<" "; };

    template<typename T>
    void print(const T& i) {
        // is_aggregate_v
        if constexpr (de::Iter<T>) {
            std::for_each(i.begin(), i.end(), inprint);     // print iterable var
        } else {
            inprint(i);     /// print other var
        }
    }

    // can be cast to any type
    struct CastAny {
        template<typename T> 
        operator T();
    };

    template<typename T>
    consteval auto get_field_nums(auto&&... args) {
        // auto&&... args = std::decay_t<T>
        if constexpr ( !requires{ T{args...}; }) {
            return sizeof...(args) -1;
        } else {
            return get_field_nums<T>(args..., CastAny{});
        }
    }

    template<typename T>
    struct Iterator {
        T* ptr;

        Iterator(T *v):ptr(v) {}
        Iterator& operator++() { ptr++; return *this; }
        Iterator& operator++(int) { auto tmp=*this; this++; return tmp; }
        auto operator<=>(const Iterator<T> &i) const = default;
        T& operator*() { return *ptr; }
    };

    template<typename T, typename Iterator = Iterator<T>>
    struct List {
        // struct Iterator;
        using iterator = Iterator;

        iterator begin() { return iterator(); }
        iterator end() { return iterator(); }
    };

}