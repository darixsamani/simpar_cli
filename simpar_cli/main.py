import typer
from simpar_cli.simpar import Simpar


def main(image: str, imgr: str = "output.png"):
    simpar = Simpar(image, imgr)
    simpar.simpar()
    


if __name__ == "__main__":
    typer.run(main)