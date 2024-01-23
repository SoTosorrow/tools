#include "util.hpp"
#include <concepts>

// 概念化自动（Concepts-based auto）
// 静态多态

template<typename T>
concept has_x = requires(T t) {
    t.x;
};

template <typename T>
concept has_x_y = has_x<T> && requires(T t) {
    t.y;
};

void fun(has_x auto x) {
    ut::print(x.x);
}
void fun(has_x_y auto x) {
    ut::print(x.y);
}

template<typename T>
concept printable = requires(T t) {
    { t.print() } -> std::same_as<void>;
};

void print(printable auto x) { x.print(); }

struct X {int x;};
struct XY {int x,y;};
struct A { void print() {ut::print("A");} };
struct B { void print() {ut::print("B");} };

int main() {
    fun(X{});
    fun(XY{});
    print(A{});
    print(B{});
    return 0;
}
