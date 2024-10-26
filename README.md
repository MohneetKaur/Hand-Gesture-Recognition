## Setup Instructions

Follow these steps to set up the project environment and install dependencies:

### 1. Create a Virtual Environment
We create a virtual environment to isolate project dependencies and ensure consistency across different systems.

```bash
conda create -p venv python==3.10
conda activate venv
```

### 2. Install Required Dependencies
Install all the necessary libraries listed in the requirements.txt file to ensure the project runs smoothly.

```bash
pip install -r requirements.txt
```

### 3. Build and Install the Package
We build the package and install it locally to use it within the virtual environment.

```bash
python -m build
pip install dist/your_package_name.whl
```