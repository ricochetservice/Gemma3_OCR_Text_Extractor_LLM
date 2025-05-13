# Gemma-3 OCR Application: A Cutting-Edge Optical Character Recognition Solution

This repository hosts an advanced optical character recognition (OCR) application that utilizes Gemma-3's vision model in conjunction with Streamlit to execute powerful, locally-hosted text extraction from images. The solution harnesses the capabilities of Gemma-3 Vision, a sophisticated AI model designed to parse and structure text from images with exceptional accuracy.

## Overview

The Gemma-3 OCR App stands as a robust, self-contained, and offline application for performing text extraction. By leveraging Streamlit, this web application offers an intuitive user interface for seamless interaction, providing users with an environment to upload images and extract meaningful, structured data.

The application employs Gemma-3 Vision, an advanced multimodal model capable of processing images and extracting text with high fidelity. It is built to operate in a completely local environment, ensuring data privacy while offering powerful computational vision capabilities without external dependencies.

## Table of Contents

- [Installation & Setup](#installation--setup)
  - [Setting Up Ollama on Linux](#setting-up-ollama-on-linux)
  - [Setting Up Ollama on Windows](#setting-up-ollama-on-windows)
  - [Setting Up Ollama on macOS](#setting-up-ollama-on-macos)
  - [Dependency Installation](#dependency-installation)
- [Application Usage](#application-usage)
  - [Running the Application](#running-the-application)
  - [Model Initialization](#model-initialization)
  - [Additional Configuration](#additional-configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Licensing](#licensing)

## Installation & Setup

### Setting Up Ollama on Linux

To initiate the setup of the Ollama framework, which powers the Gemma-3 Vision model, follow the installation instructions provided below. Ollama acts as the orchestrator for the machine learning models, enabling the inference capabilities necessary for Gemma-3.

#### Setup Ollama on Linux

Execute the following command in your terminal to install Ollama on a Linux system:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

This script will automatically download and install Ollama to your system, enabling you to interact with the Gemma-3 Vision Model.

#### Pull the Gemma-3 Vision Model

Once Ollama is installed, initiate the download of the Gemma-3 Vision Model by executing:

```bash
ollama run gemma3:12b
```

This will pull the required model and prepare it for inference.

### Setting Up Ollama on Windows

For Windows users, the installation steps for Ollama involve setting up a Windows Subsystem for Linux (WSL) environment, as Ollama is designed to operate in a Linux-like environment. Below are the steps to get Ollama running on Windows.

#### Step 1: Install Windows Subsystem for Linux (WSL)

1. Open PowerShell as an administrator.
2. Run the following command to enable WSL:

```powershell
wsl --install
```

3. Restart your system if required. Follow the instructions to install a Linux distribution (e.g., Ubuntu).

#### Step 2: Install Ollama on WSL

1. Once WSL is set up, open a WSL terminal (e.g., Ubuntu).
2. Execute the following command to install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Step 3: Pull the Gemma-3 Vision Model

Once Ollama is installed, initiate the download of the Gemma-3 Vision Model by executing:

```bash
ollama run gemma3:12b
```

This will download the model and make it ready for use.

### Setting Up Ollama on macOS

For macOS users, Ollama can be installed using the native Homebrew package manager. Follow the instructions below to get started.

#### Step 1: Install Homebrew

If Homebrew is not installed on your system, run the following command in the Terminal to install it:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### Step 2: Install Ollama

Once Homebrew is installed, you can install Ollama by running the following command:

```bash
brew install ollama
```

#### Step 3: Pull the Gemma-3 Vision Model

After Ollama is installed, download the Gemma-3 Vision Model by executing:

```bash
ollama run gemma3:12b
```

This command will retrieve the required model and prepare it for inference on your macOS machine.

### Dependency Installation

Ensure that you have Python 3.11 or later installed. If you do not have Python installed, please download and install it from the official website.

Next, proceed to install the necessary Python dependencies to run the application. These dependencies are critical for the Streamlit interface, image processing, and interaction with the Gemma-3 model:

```bash
pip install streamlit ollama pillow
```

These libraries are integral to the functioning of the app:

- **Streamlit**: Provides the web framework to build the user interface.
- **Ollama**: Manages interactions with the Gemma-3 Vision Model.
- **Pillow**: Facilitates image processing operations within Python.

## Application Usage

### Running the Application

To begin using the application, run the following command to launch the Streamlit app:

```bash
streamlit run app.py
```

This command will launch the app locally, opening a browser window where users can interact with the OCR system.

- **Image Upload**: Users can upload an image file (supports PNG, JPG, and JPEG formats) from which structured text will be extracted.
- **OCR Processing**: Upon clicking the "Extract Text" button, the image will be processed by the Gemma-3 Vision Model to extract text in a structured format.

### Model Initialization

The application relies on Gemma-3 Vision, which is instantiated within the backend of the app. The model processes the uploaded image and outputs a structured text representation, suitable for easy analysis and application.

The model operates entirely offline and does not require any cloud-based infrastructure, ensuring data privacy and security.

**Model Invocation**:

```python
response = ollama.chat(
    model='gemma3:12b',
    messages=[{
        'role': 'user',
        'content': "Analyze the text in the provided image and extract all readable content, presenting it in a clear, structured markdown format.",
        'images': [uploaded_file.getvalue()]
    }]
)
```

### Additional Configuration

#### Customizing Image Path

To customize the image used as the app’s logo, place the image file (e.g., `gemma3.png`) in the root directory of your project. The image will be encoded into base64 and rendered within the app header.

**Example**:

```python
image_path = os.path.join(os.getcwd(), "gemma3.png")
with open(image_path, "rb") as img_file:
    st.markdown(f"""# <img src="data:image/png;base64,{base64.b64encode(img_file.read()).decode()}" width="50" style="vertical-align: -12px;"> Gemma-3 OCR""", unsafe_allow_html=True)
```

## Troubleshooting

If you encounter issues, consider the following steps:

- **Missing Dependencies**: Ensure all dependencies are installed by running `pip install -r requirements.txt`.
- **Model Not Found**: Ensure the Gemma-3 Vision Model has been correctly pulled and initialized by Ollama.
- **Streamlit Errors**: Check the browser console for any JavaScript-related errors or missing assets.

For more advanced debugging, please refer to the Ollama and Streamlit official documentation.

## Contributing

Contributions to this project are welcome. If you encounter a bug, need a feature enhancement, or wish to contribute in any way, please open an issue or submit a pull request. Ensure that you follow the standard coding practices, write comprehensive tests, and adhere to the project's coding style.

## Licensing

This project is licensed under the MIT License. See `LICENSE` for more details.

By following these comprehensive steps, you should be able to seamlessly integrate the Gemma-3 OCR App into your local environment and begin extracting structured text from images efficiently. The power of Gemma-3 Vision combined with the user-friendly interface of Streamlit delivers a robust OCR solution in a 100% offline configuration.