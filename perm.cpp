#include <iostream>
#include <string>

void print_digits(int n, std::string const& prefix = "") {
    if (!n) {
        std::cout << prefix <<"z"<< std::endl;
        return;
    }
    print_digits(n-1, prefix + '0');
    print_digits(n-1, prefix + '1');
}

int main(int, char**) {
    print_digits(4);
}
