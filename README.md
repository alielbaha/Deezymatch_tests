# Deep Phonemizer - Installation and Usage Guide

## Introduction
**Deep Phonemizer** is a tool designed for converting text into phonemes using deep learning models. It is widely used in speech synthesis and linguistic research. This guide provides detailed instructions on how to install and use Deep Phonemizer, along with common errors and troubleshooting steps.

---

## Installation Guide

### Install PyTorch (Compatible Version)
Deep Phonemizer requires **PyTorch 2.4 or earlier**. Later versions (2.5 and above) introduce changes that may cause errors when loading saved models.

To install PyTorch 2.4:
```bash
pip install torch==2.4.0 torchvision torchaudio
```

To verify the installation:
```python
import torch
print(torch.__version__)  # Should print 2.4.0
```

### Install Deep Phonemizer
Once PyTorch is installed, install Deep Phonemizer with:
```bash
pip install deep-phonemizer
```

To check if the installation was successful:
```python
import dp
print(dp.__version__)
```

---

## Usage Guide

### Loading a Pretrained Model
```python
from dp.phonemizer import Phonemizer
phonemizer = Phonemizer.from_checkpoint("en_us_cmudict")
```

### Converting Text to Phonemes
```python
text = "Hello world!"
phonemes = phonemizer.phonemise(text)
print(phonemes)  # Output: 'həˈloʊ wɝld'
```

### Saving and Loading a Custom Model
```python
phonemizer.save("custom_model.pth")
# Later, you can load it back:
phonemizer = Phonemizer.from_checkpoint("custom_model.pth")
```

---

## Common Errors and Troubleshooting

### 1. `ModuleNotFoundError: No module named 'dp'`
- This means Deep Phonemizer is not installed.
- Run: `pip install deep-phonemizer`

### 2. `UnpicklingError: Weights only load failed`
**Cause:** PyTorch 2.6+ changed the default value of `weights_only` to `True` when using `torch.load`, breaking older model checkpoints.

**Solution:** Downgrade PyTorch to 2.4:
```bash
pip install torch==2.4.0 --force-reinstall
```
Alternatively, modify your code to explicitly set `weights_only=False`:
```python
model = torch.load("model.pth", weights_only=False)
```

### 3. `RuntimeError: Model file cannot be found`
- Ensure you are providing the correct path to the model file.
- Use absolute paths if relative paths cause issues.

### 4. `torch.serialization.pickle.UnpicklingError: Unsupported global`
- Some models use custom classes that need to be manually added to safe globals in PyTorch.
- Workaround:
```python
import torch.serialization
from dp.preprocessing.text import Preprocessor

torch.serialization.add_safe_globals([Preprocessor])
model = torch.load("model.pth")
```

---

## Why Deep Phonemizer Doesn't Work with PyTorch 2.5+
Deep Phonemizer relies on PyTorch's `torch.load` function to load model checkpoints. In PyTorch 2.5 and later:
1. **`weights_only=True` is the default:** This prevents models that contain additional objects from loading correctly.
2. **Stricter unpickling security:** Many custom classes (like Deep Phonemizer's `Preprocessor`) must be explicitly allowlisted, requiring extra steps.
3. **Potential API changes:** PyTorch updates often introduce breaking changes in serialization and model loading.

For these reasons, **Deep Phonemizer is best used with PyTorch 2.4 or earlier**.

To check your PyTorch version:
```python
import torch
print(torch.__version__)
```
If it's 2.5+, downgrade using:
```bash
pip install torch==2.4.0 --force-reinstall
```

---

## Conclusion
By following this guide, you should be able to install, use, and troubleshoot Deep Phonemizer effectively. If you run into any issues, ensure that your PyTorch version is compatible and check for common errors. Happy phonemizing!

