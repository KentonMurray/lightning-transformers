pytorch-lightning>=1.4.0
torch>=1.7.1,!=1.9.0 # todo: figure out why 1.9.0 crashes transformers inference
numpy
tqdm

#metrics
torchmetrics>=0.7.0

# huggingface
transformers
datasets

# hydra
hydra-core>=1.1.0

# task-specific
sentencepiece
torchmetrics[text]