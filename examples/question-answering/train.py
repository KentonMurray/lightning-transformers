import argparse
import os

import pytorch_lightning as pl
from transformers import AutoTokenizer

from lightning_transformers.data import LitTransformerDataModule
from lightning_transformers.models import LitQuestionAnsweringTransformer

# TODO is this even needed? We can pass use_fast to the tokenizer
os.environ["TOKENIZERS_PARALLELISM"] = "true"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = pl.Trainer.add_argparse_args(parser)
    parser = LitTransformerDataModule.add_argparse_args(parser)
    parser = LitQuestionAnsweringTransformer.add_argparse_args(parser)
    args = parser.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path, use_fast=args.use_fast)

    dm = LitTransformerDataModule(args.dataset_name, args.train_file, args.validation_file)
    dm.setup()

    model = LitQuestionAnsweringTransformer(dm.model_name_or_path, dm.label2id, dm.tokenizer)

    trainer = pl.Trainer.from_argparse_args(args.trainer)
    trainer.fit(model, dm)
    trainer.test(datamodule=dm)
    model.save_pretrained("outputs")
