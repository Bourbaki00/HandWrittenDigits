# HandWrittenDigit Classification

This repository presents the basic notions of training a CNN on a hand written digit dataset.

## Definition

## Configure environment
- Install all the dependencies required to run the model
```shell
(base)$: pip3 install .
```
- Move to the folder 
```shell
(base)$: cd classification
```
- Run (default)
```shell
(base)$: python3 eval.py
```
- Run (custom image)
```shell
either change the data through the variable or enter it manually for now 
```
## Models

Definition and training some models with MNIST and CIFAR-10 datasets.

### MNIST dataset

## Results
Training models with Pytorch.

| Epoch 00                          | Epoch 100                          | Loss                                |
| --------------------------------- | ---------------------------------- | ----------------------------------- |
| ![GAN with MNIST](assets/mnist_results.png) | ![GAN with MNIST](assets/mnist_results.png) | ![GAN with MNIST](assets/loss.png) |
| [1, 1, 1, 1, 1, 1, 1, 1] | [3, 8, 6, 9, 1, 5, 0, 5] | Loss : 0.07  Accuracy : .99 |


## References
    * [THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/)





