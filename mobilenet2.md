# MobileNetV2 Comprehensive Guide

## Primary Sources for MobileNetV2 Facts

### 1. Number of Layers
**Primary Source:** [MobileNetV2 Paper (arXiv:1801.04381)](https://arxiv.org/pdf/1801.04381) - Table 1

The MobileNetV2 architecture consists of **53 convolutional layers** total:
- 1 initial convolution layer (32 filters)
- 19 bottleneck residual stages with varying configurations
- 1 final convolution layer (1280 filters)
- Plus batch normalization and ReLU6 layers between convolutions

### 2. Number of Parameters
**Primary Source:** [MobileNetV2 Paper - Figure 7](https://arxiv.org/pdf/1801.04381)

The paper reports **3.4 million parameters** for the base MobileNetV2 model.

However, different implementations may vary slightly:
- Keras implementation: **3,504,872 parameters**
- PyTorch implementation: **3,505,960 parameters**

The slight differences are due to implementation details in the classification head.

### 3. Size of Images
**Primary Source:** [MobileNetV2 Paper - Figure 5](https://arxiv.org/pdf/1801.04381)

The base configuration uses **224×224 input resolution**.

The paper also supports configurable input sizes:
- Standard options: 192×192, 160×160, 128×128, 96×96
- Minimum supported: 32×32
- Width multipliers: 1.0, 0.75, 0.5, 0.35

### 4. Size of Training Dataset
**Primary Source:** [MobileNetV2 Paper - Section 4 (Experiments)](https://arxiv.org/pdf/1801.04381)

MobileNetV2 was trained on **ImageNet** dataset, which contains:
- **1.28 million training images**
- **1,000 classes**
- Validation set used for evaluation

The paper mentions training configurations including larger batch sizes (1024) on 8 GPUs with 250 training epochs.

---

## Training Time for MobileNetV2

### Original Paper Configuration (ImageNet)

**Primary Source:** [d-li14/mobilenetv2.pytorch](https://github.com/d-li14/mobilenetv2.pytorch)

| Configuration | Hardware | Time | Epochs |
|--------------|----------|------|--------|
| **Base training** | 4× Titan XP GPUs | ~2 days | 150 |
| **Enhanced training** | 8× GPUs (batch size 1024) | ~3 days | 250 |

### Key Training Parameters

- **Batch size:** 256 (base) or 1024 (enhanced)
- **Epochs:** 90-150 (standard), up to 250 (best results)
- **Learning rate:** 0.05 (base), ramping from 0.1→0.4 in first 5 epochs
- **Learning rate schedule:** Cosine decay
- **Weight decay:** 0.00004

### Alternative Reports

| Source | Hardware | Time | Notes |
|--------|----------|------|-------|
| ResearchGate | 8× GPUs | ~250 epochs | 31.5 GPU-hours for MobileNetV2-w0.35 |
| TensorFlow implementation | 1 GPU | ~5 days | Reported in issue #5 |
| Fine-tuning (2-class) | GPU | <5 hours | 150 epochs (custom dataset) |

### Summary

**Typical training time ranges:**
- **From scratch (ImageNet):** 2-5 days on multiple GPUs
- **Fine-tuning:** Hours to 1-2 days
- **GPU-hours:** ~24-72 GPU-hours for full training

---

## Pre-processing Steps for MobileNetV2 in PyTorch (Official Guide)

### Official Pre-processing Pipeline

**Source:** [PyTorch MobileNetV2 Documentation](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/)

The official preprocessing steps for MobileNetV2 (since it's pretrained on ImageNet) are:

```python
from PIL import Image
from torchvision import transforms

# Define preprocessing pipeline
preprocess = transforms.Compose([
    transforms.Resize(256),                    # Resize to 256x256
    transforms.CenterCrop(224),                # Center crop to 224x224
    transforms.ToTensor(),                     # Convert to tensor [0,1]
    transforms.Normalize(                      # ImageNet normalization
        mean=[0.485, 0.456, 0.406],            # ImageNet mean
        std=[0.229, 0.224, 0.225]              # ImageNet std
    ),
])

# Load and preprocess image
input_image = Image.open(filename)
input_tensor = preprocess(input_image)
input_batch = input_tensor.unsqueeze(0)  # Add batch dimension
```

### For Training/Fine-tuning (Data Augmentation)

**Source:** [PyTorch Transfer Learning Tutorial](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)

For training (not just inference), use data augmentation:

```python
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),       # Random crop & scale
        transforms.RandomHorizontalFlip(),       # Horizontal flip
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                           [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], 
                           [0.229, 0.224, 0.225])
    ])
}

# Load custom dataset using ImageFolder
image_datasets = {
    x: datasets.ImageFolder(os.path.join(data_dir, x), 
                           data_transforms[x])
    for x in ['train', 'val']
}
```

### Dataset Structure for Custom Data

ImageFolder expects this directory structure:
```
root/
  class1/
    img1.jpg
    img2.jpg
  class2/
    img3.jpg
    img4.jpg
```

### Loading Pretrained MobileNetV2

```python
import torch
import torch.nn as nn

# Load pretrained model
model = torch.hub.load('pytorch/vision', 'mobilenet_v2', pretrained=True)

# For fine-tuning: replace classifier head
model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
```

### Comparison to Google Teachable Machine

| Teachable Machine | PyTorch Equivalent |
|-------------------|-------------------|
| Upload images by class | Organize in `class_name/` folders |
| Train model | Call `model.train()` with data loaders |
| Test model | Call `model.eval()` and inference |
| Export model | `torch.save(model.state_dict(), 'model.pth')` |

**Key difference:** Teachable Machine is no-code/low-code, while PyTorch requires writing preprocessing code but offers more control and flexibility.

---

## Complete Fine-tuning Example

**Source:** [Roboflow MobileNetV2 Tutorial](https://blog.roboflow.com/how-to-train-mobilenetv2-on-a-custom-dataset/)

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, models, transforms

# 1. Define transforms
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
}

# 2. Load data
train_dataset = datasets.ImageFolder('data/train', data_transforms['train'])
val_dataset = datasets.ImageFolder('data/val', data_transforms['val'])

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=32, shuffle=False)

# 3. Load pretrained model and modify classifier
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes=2)

# 4. Train
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
criterion = nn.CrossEntropyLoss()

# 5. Save model
torch.save(model.state_dict(), 'mobilenet_v2_finetuned.pth')
```

---

## References

1. Sandler, Mark, et al. "MobileNetV2: Inverted Residuals and Linear Bottlenecks." arXiv preprint arXiv:1801.04381 (2018). [https://arxiv.org/abs/1801.04381](https://arxiv.org/abs/1801.04381)
2. Keras MobileNetV2 Documentation. [https://keras.io/api/applications/mobilenet/](https://keras.io/api/applications/mobilenet/)
3. PyTorch MobileNetV2 Documentation. [https://pytorch.org/vision/main/models/generated/torchvision.models.mobilenet_v2.html](https://pytorch.org/vision/main/models/generated/torchvision.models.mobilenet_v2.html)
4. PyTorch Transfer Learning Tutorial. [https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
