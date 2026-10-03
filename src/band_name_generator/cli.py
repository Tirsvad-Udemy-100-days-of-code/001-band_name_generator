"""Command-line interface for the Band Name Generator."""

from band_name_generator.generator import generate_band_name


def main() -> None:
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's the name of a pet?\n")
    try:
        band_name = generate_band_name(city, pet)
    except ValueError as error:
        print(error)
        raise SystemExit(1)
    print(f"Your band name could be: {band_name}")


if __name__ == "__main__":
    main()
