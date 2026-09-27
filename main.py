from impulse_momentum_math import momentum, impulse

def get_float_input(prompt: str) -> float:
    """prompt user for numeric input, retrying on invalid entry"""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid entry. Please enter a valid number.")


def get_mass_velocity() -> tuple[float, float]:
    """collect values for mass and velocity"""
    mass = get_float_input("Enter object mass (kg): ")
    velocity = get_float_input("Enter velocity (m/s): ")
    return mass, velocity


def display_momentum(mass: float, velocity: float) -> None:
    """calculate and display results for momentum using p=mv"""
    p = momentum(velocity, mass)
    j = impulse(p)

    print("\n--- IMPULSE AND MOMENTUM RESULTS ---")
    print(f"MOMENTUM (P): {p:.2f} kg·m/s")
    print(f"IMPULSE (J):  {j:.2f} N·s")

if __name__ == "__main__":
    mass, velocity = get_mass_velocity()
    display_momentum(mass, velocity)