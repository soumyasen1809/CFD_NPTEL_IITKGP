//Equation to solve:     5x1 + x2 = 7 ; x1 + 5x2 = 11

#include <iostream>

int main() {

  double x_1 = 0.01;  // Initialize x1 = 0
  double x_1_new = 0.0;

  double x_2 = 0.01;  // Initialize x2 = 0
  double x_2_new = 0.0;

  double eps = 1.0;  // Tolerance limit epsilon, initialized to 1

  int count_steps_jac = 0;

  // Jacobi iterative method

  while (eps > 0.01){
    x_1_new = (7-x_2)/5.0;
    x_2_new = (11-x_1)/5.0;

    eps = x_1_new - x_1;

    x_1 = x_1_new;
    x_2 = x_2_new;
    count_steps_jac++;
  }

  std::cout << "X1 for Jacobi method: " << x_1 << std::endl;
  std::cout << "X2 for Jacobi method: " << x_2 << std::endl;
  std::cout << "Number of steps taken for Jacobi method:  " << count_steps_jac << std::endl;


  // Gauss Siedel Iterative method

  eps = 1.0;    // Tolerance limit reset

  int count_steps_gaus = 0;

  x_1 = 0.01;
  x_1_new = x_1;  // Initialize x_1_new as x_1
  x_2 = 0.01;
  x_2_new = x_2;  // Initialize x_2_new as x_2

  while (eps > 0.01){
    x_1_new = (7-x_2_new)/5.0;
    x_2_new = (11-x_1_new)/5.0;

    eps = x_1_new - x_1;

    x_1 = x_1_new;
    x_2 = x_2_new;
    count_steps_gaus++;
  }

  std::cout << "X1 for Gauss Siedel method: " << x_1 << std::endl;
  std::cout << "X2 for Gauss Siedel method: " << x_2 << std::endl;
  std::cout << "Number of steps taken for Gauss Siedel method:  " << count_steps_gaus << std::endl;
}
