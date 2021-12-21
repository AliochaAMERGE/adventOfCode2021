#include <iostream>
#include <fstream>
#include <math.h>

int main(int argc, char const *argv[])
{
  std::string line;

  std::ifstream ifs("input");

  if (ifs.is_open())
  {
    ifs >> line;

    // number of bits in our mesurement
    int size = line.size();

    // array containing the number of '0' (-1) or '1' (+1)
    int tab[size];
    for (int i = 0; i < size; i++)
      tab[i] = 0;

    // count the number of '0' (-1) or '1' (+1)
    for (size_t i = 0; i < size; i++)
    {
      if (line[i] == '0')
        tab[i] -= 1;
      else
        tab[i] += 1;
    }
    while (ifs)
    {
      ifs >> line;
      for (int i = 0; i < size; i++)
      {
        if (line[i] == '0')
          tab[i] -= 1;
        else
          tab[i] += 1;
      }
    }

    // now our array is initialized

    int gamma_rate[size];

    for (size_t i = 0; i < size; i++)
    {
      if (tab[i] >= 0)
      {
        gamma_rate[i] = 1;
      }
      else
      {
        gamma_rate[i] = 0;
      }
    }
    int gamma = 0;
    int epsilon = 0;

    for (size_t i = size; i > 0; i--)
    {
      std::cout << gamma_rate[i-1] ;
      gamma += gamma_rate[i-1] * pow(2, i-1);
      epsilon += (1 - gamma_rate[i-1]) * pow(2, i-1);
    }

    std::cout << std::endl;

    std::cout << "gamma : " << gamma << std::endl;
    std::cout << "epsilon : " << epsilon << std::endl;

    std::cout << "result : " << gamma * epsilon << std::endl;
  }

  ifs.close();
  return 0;
}

// 100101000101
// 011010111010