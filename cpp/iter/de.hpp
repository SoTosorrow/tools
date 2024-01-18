#include <algorithm>

namespace de {
    template<typename T>
    concept Iter = requires(T t) {
        std::begin(t);
        std::end(t);
    };

    template<typename T>
    concept ValueTypeAble = requires(T t) {
        typename T::value_type;
    };
}