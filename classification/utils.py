import torch
import torch.nn as nn
from tqdm import trange
import matplotlib.pyplot as plt
import hashlib
import numpy as np

from model import ModelM3


##------------------ Fetching data ------------------##
def fetch(url):
    import requests, gzip, os, hashlib, numpy
    fp = os.path.join("./tmp", hashlib.md5(url.encode('utf-8')).hexdigest())
    if os.path.isfile(fp):
        with open(fp, "rb") as f:
            dat = f.read()
    else:
        with open(fp, "wb") as f:
            dat = requests.get(url).content
            f.write(dat)
    return numpy.frombuffer(gzip.decompress(dat), dtype=np.uint8).copy()

X_train = fetch("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")[0x10:].reshape((-1, 28, 28))
Y_train = fetch("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")[8:]
X_test = fetch("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")[0x10:].reshape((-1, 28, 28))
Y_test = fetch("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")[8:]

url = "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz"
hashlib.md5(url.encode('utf-8')).hexdigest()


##------------------ Initializing the network ------------------##
model = ModelM3()
BS = 256
losses,accur = [],[]
loss_function = nn.CrossEntropyLoss()
optim = torch.optim.Adam(model.parameters())
for i in (w := trange(1000)):
    samp = np.random.randint(0, X_train.shape[0], size=(BS))
    X = torch.tensor(X_train[samp].reshape((-1,1,28,28))).float()
    Y = torch.tensor(Y_train[samp]).long()
    optim.zero_grad()
    out = model(X)
    loss = loss_function(out, Y)
    loss.backward()
    optim.step()
    losses.append(loss.item())
    cat = torch.argmax(out, dim=1)
    accuracy = (cat == Y).float().mean()
    accur.append(accuracy.item())
    w.set_description("loss %.2f accuracy %.2f" % (loss.item(), accuracy.item()))

plt.ylim(-.1,1.1)
plt.plot(losses)
plt.plot(accur)

