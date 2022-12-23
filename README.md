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
| ![GAN with MNIST](img/00_gan.png) | ![GAN with MNIST](img/100_gan.png) | ![GAN with MNIST](img/loss_gan.png) |

#### Deep Convolutional Generative Adversarial Networks - DCGANs
A DCGANs implementation using the transposed convolution technique. [Notebook](https://github.com/mafda/generative_adversarial_networks_101/blob/master/src/mnist/02_DCGAN_MNIST.ipynb)

| Epoch 00                            | Epoch 100                            | Loss                                  |
| ----------------------------------- | ------------------------------------ | ------------------------------------- |
| ![GAN with MNIST](img/00_dcgan.png) | ![GAN with MNIST](img/100_dcgan.png) | ![GAN with MNIST](img/loss_dcgan.png) |

#### Conditional Generative Adversarial Nets - CGANs
A CGANs implementation using fully connected layers and embedding layers. [Notebook](https://github.com/mafda/generative_adversarial_networks_101/blob/master/src/mnist/03_CGAN_MNIST.ipynb)

| Epoch 00                            | Epoch 100                            | Loss                                  |
| ----------------------------------- | ------------------------------------ | ------------------------------------- |
| ![CGAN with MNIST](img/00_cgan.png) | ![CGAN with MNIST](img/100_cgan.png) | ![CGAN with MNIST](img/loss_cgan.png) |


## References
    * [THE MNIST DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/)





