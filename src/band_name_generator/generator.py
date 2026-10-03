"""Core logic for building a band name."""


def generate_band_name(city: str, pet: str) -> str:
    """Combine a city and a pet's name into a band name.

    Raises ValueError if either value is empty or only whitespace.
    """
    city = city.strip()
    pet = pet.strip()
    if not city or not pet:
        raise ValueError("Both the city and the pet's name are required.")
    return f"{city} {pet}"
