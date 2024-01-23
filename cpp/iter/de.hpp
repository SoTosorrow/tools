#include <string>

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

    template<typename T>
    concept CanToString = requires(T t) {
        { t } -> std::convertible_to<std::string>;
    };
}