# Deep Phonemizer - Installation 

## Introduction
**Deep Phonemizer** is a tool designed for converting text into phonemes using deep learning models. It is widely used in speech synthesis and linguistic research. This guide provides detailed instructions on how to install and use Deep Phonemizer, along with common errors and troubleshooting steps.

---

## Installation Guide


### Install packages in the requirements file of Deep-Phonemizer repository : https://github.com/spring-media/DeepPhonemizer

### Install Deep Phonemizer
Once PyTorch is installed, install Deep Phonemizer with:
```bash
pip install deep-phonemizer
```

### Install PyTorch (Compatible Version)
Deep Phonemizer requires **a PyTorch version earlier than 2.5**. Later versions (2.6) introduce changes that may cause errors when loading saved models.

Install an earlier version of Pytorch:
```bash
pip install "torch<2.5"
```

Check installation:
```python
print(torch.__version__)  # Should print a version earlier than 2.5 
```
Remark : If it still prints 2.6 restart the kernel (since the pytorch version that was installed through the requirements file is still being used).

Check again:
```python
print(torch.__version__)  # Should print a version earlier than 2.5 
```
If it's still 2.5+, downgrade using this:
```bash
pip install torch==2.4.0 --force-reinstall
```
---

## Example

### Loading a Pretrained Model
```python
from dp.phonemizer import Phonemizer
phonemizer = Phonemizer.from_checkpoint("pretrained_models/latin_ipa_forward.pt")
```
the `pretrained_models` folder contains 3 models : 
1. en_us_cmudict_ipa_forward (International Phonetic Alphabet) : English (US), German (download weights here https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/DeepPhonemizer/en_us_cmudict_ipa_forward.pt
3. en_us_cmudict_forward (ARPAbet) : English (US) (download weights here https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/DeepPhonemizer/en_us_cmudict_forward.pt)
4. latin_ipa_forward (International Phonetic Alphabet): English (US),English (UK), French, Spanish (download weights here https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/DeepPhonemizer/latin_ipa_forward.pt)

### Converting Text to Phonemes
```python
phonemizer("Hello world!", lang="en_us")
>>> həˈloʊ wɝld'
```
---

## You might enconter the following errors:

### `UnpicklingError: Weights only load failed`
**Cause:** PyTorch 2.6+ changed the default value of `weights_only` to `True` when using `torch.load`, breaking older model checkpoints.

if the above solution doesn't work, do the following: 
modify your code to explicitly set `weights_only=False`
```python
model = torch.load("model-path", weights_only=False)
```

---

## Why it doesn't work with PyTorch 2.5+
Deep Phonemizer relies on PyTorch's `torch.load` function to load model checkpoints. In PyTorch 2.5 and later:
**`weights_only=True` is the default:** This prevents models that contain additional objects from loading correctly.



