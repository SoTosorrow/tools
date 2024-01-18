#include "util.hpp"
#include <functional>
#include <execution>

// template<typename T>
// struct Strategy {
//     using T_type = T::value_type;
//     virtual ~Strategy() = default;

//     virtual void exec( const std::function<void(T_type&)> ) const = 0;
// };

// template<typename T>
// struct ForEachImpl: Strategy<T> {

//     void exec(const std::function<void(T_type&)> f) const override {
//         std::cout<<"1\n";
//     }
// };

/*
    Wrapper<std::vector> wrapper;
    wrapper.filter().map().reduce().collect();
*/
template<de::Iter T>
struct Wrapper
{
    T v;
    using T_type = T::value_type;
    // T_type inner;

    // template<typename F>
    // which is better? template F vs function

    /// .forEach([](auto& v){
    ///     ++v;
    /// })
    // template<typename F>
    Wrapper& forEach(
        const std::function<void(T_type&)> f
        // F f
    ) {
        std::for_each(
            // std::execution::par, 
            std::begin(v), std::end(v), 
            f
        );
        return *this;
    }

    /// .map([](auto& v){
    ///     return v+100;
    /// })
    Wrapper& map(
        std::function<T_type(T_type&)> f
    ) {
        std::transform(
            std::begin(v), std::end(v), 
            std::begin(v), 
            f
        );
        return *this;
    }

    // @check to optimize copy and reserve
    /// return a new data
    Wrapper copy_map(
        const std::function<T_type(T_type&)> f
    ) {
        auto v2 = T{};
        if constexpr (std::is_same_v<T, std::vector<T_type>>) {
            v2.reserve(v.size());   // v.size() or v.capacity()
        }
        std::transform(
            std::begin(v), std::end(v), 
            std::back_inserter(v2),
            f
        );
        return Wrapper{std::move(v2)};
    }

    /// .filter([](auto& v){
    ///     return v<115;
    /// })
    Wrapper& filter(
        const std::function<bool(T_type&)> f
    ) {
        std::erase_if(
            v, 
            std::not_fn(f)
        );
        return *this;
    }

    /// .reduce(
    ///     [](int a,int b){
    ///         return a+b;
    ///     }, 0
    /// )
    // template<typename Reducer, typename Init>
    T_type reduce(
        const std::function<T_type(T_type, T_type)> f,
        T_type init
    ) {
        return std::accumulate(
            std::begin(v), std::end(v), 
            init, 
            f
        );
    }

    // todo lazy compute
    // todo execution policy

    void print() {
        // if constexper (de::Iter<T>) {}
        ut::print(v);
    }

    auto collect() -> T {
        return std::move(v);
    }

    // template<typename Result>
    // auto toT() -> Result {

    // }
};

/*
template<typename Compare = std::less<>>
Wrapper& sort(Compare comp = Compare()) {
    std::sort(data.begin(), data.end(), comp);
    return *this;
}

Wrapper& unique() {
    auto newEnd = std::unique(data.begin(), data.end());
    data.erase(newEnd, data.end());
    return *this;
}

Wrapper& concat(const T& other) {
    data.insert(data.end(), other.begin(), other.end());
    return *this;
}

Wrapper& take(size_t n) {
    if (n < data.size()) {
        data.resize(n);
    }
    return *this;
}

Wrapper& drop(size_t n) {
    if (n < data.size()) {
        data.erase(data.begin(), data.begin() + n);
    } else {
        data.clear();
    }
    return *this;
}

template<typename Predicate>
bool anyOf(Predicate pred) {
    return std::any_of(data.begin(), data.end(), pred);
}

template<typename Predicate>
bool allOf(Predicate pred) {
    return std::all_of(data.begin(), data.end(), pred);
}

template<typename Predicate>
bool noneOf(Predicate pred) {
    return std::none_of(data.begin(), data.end(), pred);
}

template<typename Predicate>
bool anyOf(Predicate pred) {
    return std::any_of(data.begin(), data.end(), pred);
}

template<typename Predicate>
bool allOf(Predicate pred) {
    return std::all_of(data.begin(), data.end(), pred);
}

template<typename Predicate>
bool noneOf(Predicate pred) {
    return std::none_of(data.begin(), data.end(), pred);
}



*/