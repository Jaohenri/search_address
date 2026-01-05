"""Module to run the CEP lookup application."""

try:
    from .cep import Cep
except ImportError:
    from cep import Cep


if __name__ == "__main__":

    while True:

        print("\nCep lookup application.")
        print("\n-----------------------\n")
        cep1 = Cep(input("Please inform a cep: "))

        state = input("Do you want to search another Cep? Y/N?")

        if state.lower() == "n":
            break
