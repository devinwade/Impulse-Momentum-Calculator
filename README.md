# Impulse and Momentum Calculator

Tool used for calculating impulse and momentum

Includes mathmatical validation functions, a user friendly program accepting inputs, and a pytest verification suite.

## Physics Formulation

Formula used for momentum (p = mv)

Formula used for Impulse (J = p_final - p_initial)

## Project Structure

impulse_momentum_math.py

main.py

test_impulse_momentum_math.py

## Technical Notes

impulse_momentum_math.py only calculates. It does not ask questions and it does not print the results.

main.py asks for the mass and the velocity, calls the two math functions, and prints the results. The questions run only when you start that file directly. The if __name__ == "__main__" line is what keeps an import from starting the prompts.

test_impulse_momentum_math.py checks the math functions. It does not type answers into the prompts.


## How to use

1. Open a terminal in the folder that contains `main.py`.
2. Run `python main.py`.
3. At `Enter object mass (kg):`, type the mass in kilograms and press Enter.
4. At `Enter velocity (m/s):`, type the velocity in meters per second and press Enter.
5. Read the two lines under `IMPULSE AND MOMENTUM RESULTS`.
The program asks once, prints the results, and ends. Run `python main.py` again for another mass and velocity. Press Ctrl+C if you want to quit while it is waiting for a number.
Whole numbers and decimals both work. `1.5` and `-2` are valid entries.
```text
Enter object mass (kg): 0.5
Enter velocity (m/s): 4
--- IMPULSE AND MOMENTUM RESULTS ---
MOMENTUM (P): 2.00 kg·m/s
IMPULSE (J):  2.00 N·s
```
That example is a 0.5 kg object moving at 4 m/s. Momentum is `0.5 * 4 = 2` kg·m/s. Impulse is `2.00` N·s.
If the text is not a number, such as `abc`, the program prints:
```text
Error: Invalid entry. Please enter a valid number.
```
It then asks for that same value again.
A velocity below zero is allowed. The momentum is negative, which means the opposite direction. A mass of `0` or a velocity of `0` is allowed. Both give a momentum of `0.00`.
A mass below zero stops the program and prints `ValueError: Mass cannot be less than zero`. Start it again and enter a mass of zero or greater.
Results are shown with two decimal places, as in `6.00`.