# MNIST Handwritten Digit Recognition
![Python](https://img.shields.io/badge/Python-3.x-blue) ![Neural Network](https://img.shields.io/badge/Neural%20Network-SciPy-orange) ![GUI](https://img.shields.io/badge/GUI-Tkinter-green)

A neural network-based handwritten digit recognition system with an interactive GUI. Train a custom feedforward neural network on the MNIST dataset and recognize hand-drawn digits in real-time through an intuitive canvas interface.

Built to demonstrate core machine learning fundamentals: neural network architecture, backpropagation, optimization algorithms, and practical model deployment with a user interface.

---

## What It Does

Upload the MNIST dataset, train a neural network from scratch, and interact with the trained model through a drawing canvas:

- **Neural Network Training** — Train a fully-connected feedforward network using scipy.optimize
- **Real-Time Predictions** — Draw digits on a Tkinter GUI canvas and receive instant predictions
- **Image Preprocessing** — Automatic scaling, color inversion, and normalization for accurate recognition
- **High Accuracy** — Achieves competitive accuracy on the MNIST test set
- **Interactive Experience** — User-friendly canvas for testing model predictions

---

## Why This Project

This project showcases three essential machine learning and software engineering competencies:

| Skill | How It's Demonstrated |
|-------|----------------------|
| **Neural Network Implementation** | Custom feedforward architecture with configurable layers, sigmoid activation, and backpropagation |
| **Numerical Optimization** | Uses `scipy.optimize` for gradient-based learning with cost function minimization |
| **GUI Development** | Tkinter-based drawing canvas with real-time prediction display and model interaction |
| **ML Pipeline Design** | End-to-end workflow: data loading → preprocessing → training → inference → visualization |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Core language |
| **NumPy** | Matrix operations and vectorization |
| **SciPy** | Numerical optimization (fmin_cg for gradient descent) |
| **Tkinter** | GUI framework for drawing canvas |
| **PIL (Pillow)** | Image processing and preprocessing |
| **MNIST Dataset** | 70,000 labeled handwritten digit images (28×28 grayscale) |

---

## Project Structure

```
MNIST_Project_/
├── Main.py                   ← Entry point: orchestrates training and GUI launch
├── Model.py                  ← Neural network training logic and cost function
├── RandInitialise.py         ← Weight initialization for network layers
├── Prediction.py             ← Forward propagation and prediction functions
├── GUI.py                    ← Tkinter canvas for drawing and real-time prediction
├── mnist-original.mat.zip    ← MNIST dataset (70,000 images)
└── README.md
```

---

## Quickstart

### 1. Clone and Set Up Environment

```bash
git clone https://github.com/an1208/MNIST_Project_.git
cd MNIST_Project_
```

### 2. Install Dependencies

```bash
pip install numpy scipy pillow matplotlib
```

> **Note:** Tkinter is typically pre-installed with Python. If not, install it via your package manager (e.g., `apt-get install python3-tk` on Ubuntu).

### 3. Extract the MNIST Dataset

```bash
unzip mnist-original.mat.zip
```

### 4. Train and Run

```bash
python Main.py
```

**What happens:**
1. Loads 70,000 MNIST images from `mnist-original.mat`
2. Initializes a neural network with randomly initialized weights
3. Trains the model using scipy's `fmin_cg` optimizer
4. Launches the Tkinter GUI canvas
5. Draw a digit → model predicts in real-time

---

## How It Works

### Neural Network Architecture

```
Input Layer:    784 units (28×28 flattened image)
       ↓
Hidden Layer:   25 units (configurable)
       ↓
Output Layer:   10 units (digits 0-9)
```

- **Activation Function:** Sigmoid (logistic function)
- **Optimization:** Conjugate Gradient (scipy.optimize.fmin_cg)
- **Regularization:** Optional L2 regularization to prevent overfitting

### Training Process

1. **Data Loading:** Reads MNIST `.mat` file containing training and test sets
2. **Weight Initialization:** Random initialization using `RandInitialise.py`
3. **Cost Computation:** Calculates cross-entropy loss with regularization
4. **Gradient Descent:** Optimizes weights using scipy's conjugate gradient solver
5. **Model Evaluation:** Tests accuracy on the MNIST test set

### GUI Interaction

1. **Draw on Canvas:** Use your mouse to draw a digit
2. **Preprocessing Pipeline:**
   - Capture canvas image
   - Resize to 28×28 pixels
   - Invert colors (black background → white background)
   - Normalize pixel values to [0, 1]
3. **Prediction:** Feed preprocessed image through the trained network
4. **Display Result:** Show predicted digit on the GUI

---

## Code Walkthrough

### Main.py
Entry point that:
- Loads MNIST data
- Initializes network weights
- Calls training function
- Launches GUI

### Model.py
Core training logic:
- **Cost function:** Computes cross-entropy loss
- **Gradient computation:** Backpropagation algorithm
- **Training loop:** Calls scipy optimizer with cost and gradient functions

### Prediction.py
Inference logic:
- **Forward pass:** Propagates input through network layers
- **Hypothesis calculation:** Applies sigmoid activation
- **Prediction:** Returns digit with highest probability

### GUI.py
Tkinter interface:
- **Canvas:** Drawing area for user input
- **Image capture:** Converts canvas to PIL Image
- **Preprocessing:** Resizes, inverts, and normalizes
- **Display:** Shows predicted digit

### RandInitialise.py
Weight initialization:
- Generates random weights in range `[-ε, ε]`
- Ensures symmetry breaking for effective training

---

## Performance

**Current Accuracy:** ~95% on MNIST test set

> **Note:** Accuracy depends on hyperparameters (hidden layer size, regularization strength, training iterations). Fine-tuning can improve results.

---

## Potential Improvements

### Short-Term Enhancements
- **Better Image Preprocessing:** Implement centering and normalization techniques used in production MNIST models
- **Configurable Architecture:** Add command-line arguments for layer sizes and learning rate
- **Save/Load Trained Model:** Serialize weights to avoid retraining
- **Visualization:** Plot training loss curve and accuracy metrics

### Long-Term Extensions
- **Convolutional Neural Network (CNN):** Replace feedforward network with CNN for higher accuracy (>99%)
- **Data Augmentation:** Apply rotations, translations, and distortions to improve generalization
- **Batch Training:** Implement mini-batch gradient descent instead of full-batch
- **Web Deployment:** Convert GUI to Flask/FastAPI web app with HTML canvas
- **Multi-Digit Recognition:** Extend to recognize sequences of digits (e.g., handwritten numbers)

---

## Dataset Information

**MNIST Dataset:**
- 60,000 training images
- 10,000 test images
- Image size: 28×28 pixels (grayscale)
- 10 classes (digits 0–9)

**Source:** [Yann LeCun's MNIST Database](http://yann.lecun.com/exdb/mnist/)

---

## Troubleshooting

### Common Issues

**Issue:** GUI doesn't launch  
**Solution:** Ensure Tkinter is installed. On Linux: `sudo apt-get install python3-tk`

**Issue:** Dataset file not found  
**Solution:** Extract `mnist-original.mat.zip` before running `Main.py`

**Issue:** Low prediction accuracy  
**Solution:** Try increasing hidden layer size or training iterations in `Model.py`

**Issue:** Predictions are inverted (predicts 0 as 9, etc.)  
**Solution:** Verify color inversion in `GUI.py` preprocessing — MNIST expects white digits on black background

---

## Learning Resources

If you're new to neural networks or the MNIST dataset, these resources may help:

- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) by Michael Nielsen
- [3Blue1Brown Neural Network Series](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Andrew Ng's Machine Learning Course](https://www.coursera.org/learn/machine-learning)
- [MNIST Dataset Documentation](http://yann.lecun.com/exdb/mnist/)

---

## License

This project is open-source and available for educational purposes.

---

## Author
**Anushka Sharma**
ECE undergraduate · ML/Data Analysis minor · Maharaja Surajmal Institute of Technology
[LinkedIn](https://www.linkedin.com/in/anushka-sharma-1208ans) · anushka.sh0812@gmail.com

---

## Acknowledgments

- **MNIST Dataset:** Yann LeCun, Corinna Cortes, and Christopher J.C. Burges
- **Optimization:** SciPy developers for robust numerical optimization tools
- **Inspiration:** Andrew Ng's Machine Learning course on Coursera
