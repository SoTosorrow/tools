#include <stdio.h>
#include <stdarg.h>

int add_nums(int count, ...)
{
    int result = 0;
    va_list args;
    va_start(args, count); // C23 起能省略 count
    for (int i = 0; i < count; ++i) {
        result += va_arg(args, int);
    }
    va_end(args);
    return result;
}


int main(void)
{
    printf("%d\n", add_nums(4, 25, 25, 50, 50));
}
