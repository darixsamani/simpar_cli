# simpar-cli
This is cli for a simple paragraph recognition based on the morphology operator

## Screen

| Image   | MASK Image  | Image recognized  |
:-------------------------:|:-------------------------:|:-------------------------:|
|  ![Image](https://github.com/darixsamani/simpar_cli/blob/main/img/simple_a26.jpg) | ![Mask](https://github.com/darixsamani/simpar_cli/blob/main/img/mask.jpg)   | ![Image recognized](https://github.com/darixsamani/simpar_cli/blob/main/img/simple_a26_r.jpg)


## How to Install

```
pip install simpar-cli

```

## How to use


```
uv run simpar_cli/main.py ./img/simple_a20.jpg

```

```
uv run simpar_cli/main.py ./img/simple_a20.jpg ouput.png
```
 


## Next

![next](https://github.com/darixsamani/simpar_cli/blob/main/img/next.png)

### Francais
  Nous faisons une reconnaissance de paragraphe basée sur une les opération morphologiques qui est une
  méthode analytique qui  est instable lorsque la structure de l'image est complexe dans la suite de notre travail nous allons 
  a partir des images et leurs masque entraîner une modelé d'intelligence artificielle pour
  générer les masques de reconnaissance de paragraphe d'image, Ainsi Nous allons mieux gérer la structure des images complexes

### English

We make a paragraph recognition based on a morphological operation which is an analytical 
method which is unstable when the structure of the image is complex in the rest of our work we will
start from the images and their masks lead to a modeling of artificial intelligence 
to generate the image paragraph recognition masks, thus we will better handle the structure of complex images

