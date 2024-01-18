struct vir {
    virtual void func1() =0;
    virtual void func2() =0;
};

#include<iostream>
#include<memory>

struct Tmp
{
    void func1() { std::cout<<1<<"\n"; }
    void func2() { std::cout<<2<<"\n"; }
};
struct Tmp2
{
    void func1() { std::cout<<11<<"\n"; }
    void func2() { std::cout<<22<<"\n"; }
};

/// actually fat pointer
template<typename T>
struct vir_impl : vir {
    T* data;
    vir_impl(T* d) : data(d) {}
    virtual void func1() { data->func1(); }
    virtual void func2() { data->func2(); }
};

/// test code
int main() {
    Tmp t;
    auto v = std::make_shared<vir_impl<Tmp>>(&t);
    v->func1();
    v->func2();

    Tmp2 t2;
    auto v2 = std::make_shared<vir_impl<Tmp2>>(&t2);
    v2->func1();
    v2->func2();
    return 0;
}
