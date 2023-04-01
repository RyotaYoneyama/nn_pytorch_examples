import os
import sys

from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import lightning.pytorch as pl
from lightning.pytorch.loggers import MLFlowLogger

sys.path.append(
    os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
)
from src.models.simple_auto_encoder.network import SimpleAutoEncoder


def main():

    transform = transforms.ToTensor()
    train_set = MNIST(
        os.path.join(os.getcwd(), "../data/"),
        download=True,
        train=True,
        transform=transform,
    )
    test_set = MNIST(
        os.path.join(os.getcwd(), "../data/"),
        download=True,
        train=False,
        transform=transform,
    )
    train_loader = DataLoader(train_set)
    test_loader = DataLoader(test_set, shuffle=False)

    # model
    autoencoder = SimpleAutoEncoder

    mlf_logger = MLFlowLogger(experiment_name="simple_ae", save_dir="mlruns")

    # train model
    trainer = pl.Trainer(
        limit_train_batches=100,
        max_epochs=100,
        devices=1,
        accelerator="gpu",
        logger=mlf_logger,
    )
    trainer.fit(model=autoencoder, train_dataloaders=train_loader)
    trainer.test(model=autoencoder, dataloaders=test_loader)


if __name__ == "__main__":
    main()
