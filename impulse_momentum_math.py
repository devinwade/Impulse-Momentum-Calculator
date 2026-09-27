def momentum(velocity: float, mass: float):
    """Calculates momentum using p = mv"""
    if mass < 0:
        raise ValueError("Mass cannot be less than zero")
    else:
        p = (mass * velocity)
        return p

def impulse(m_final, m_initial= 0):
    """calculates impulse using j = Δp, initial momentum is assumed to be 0"""
    return m_final - m_initial
