# Step-by-Step Guide to Run the AI Validation Pipeline

This guide provides simple instructions to run the `ai_validation_pipeline.py` project, which validates a voice command recognition model for automotive infotainment systems. The project demonstrates skills relevant to the AI Validation Engineer role at Cinemo GmbH. Follow these steps to set up and execute the code on a Windows, macOS, or Linux computer.

## Prerequisites
- A computer with internet access.
- Basic familiarity with running commands in a terminal or command prompt.
- Approximately 10-15 minutes for setup and execution.

## Step 1: Install Python
1. **Check if Python is installed**:
   - Open a terminal (Windows: Command Prompt or PowerShell; macOS/Linux: Terminal).
   - Type `python --version` or `python3 --version` and press Enter.
   - If Python 3.8 or higher is installed (e.g., `Python 3.10.0`), proceed to Step 2.
   - If not, continue below to install Python.

2. **Download and install Python**:
   - Visit [python.org/downloads](https://www.python.org/downloads/).
   - Download the latest Python version (e.g., Python 3.10 or higher).
   - Run the installer:
     - Windows: Check "Add Python to PATH" during installation.
     - macOS/Linux: Follow the installer prompts.
   - Verify installation by running `python --version` again in the terminal.

## Step 2: Set Up a Project Folder
1. Create a folder for the project (e.g., `cinemo_project`):
   - Windows: Create a folder in File Explorer (e.g., `C:\cinemo_project`).
   - macOS/Linux: Run `mkdir cinemo_project` in the terminal.
2. Download the `ai_validation_pipeline.py` file (provided with this application) and place it in the `cinemo_project` folder.

## Step 3: Install Required Libraries
1. Open a terminal and navigate to the project folder:
   - Windows: `cd C:\cinemo_project`
   - macOS/Linux: `cd ~/cinemo_project`
2. Install the required Python libraries by running:
   ```bash
   pip install numpy pandas matplotlib transformers torch
   ```
   - This installs:
     - `numpy`: For numerical operations.
     - `pandas`: For data handling and reporting.
     - `matplotlib`: For generating visualizations.
     - `transformers`: For the speech recognition model.
     - `torch`: For running the machine learning model.
   - If you encounter errors (e.g., due to system compatibility), proceed to Step 4. The code includes a fallback mock model that runs without `transformers` or `torch`.

3. Verify installation:
   - Run `pip list` in the terminal.
   - Ensure `numpy`, `pandas`, `matplotlib`, `transformers`, and `torch` are listed. If not, contact the applicant for assistance.

## Step 4: Run the Code
1. In the terminal, ensure you’re in the project folder (e.g., `cinemo_project`).
2. Run the script:
   ```bash
   python ai_validation_pipeline.py
   ```
   - If Python is installed as `python3`, use:
     ```bash
     python3 ai_validation_pipeline.py
     ```
3. The script will:
   - Execute test cases for a voice command recognition model (using a real model if `transformers` is installed, or a mock model otherwise).
   - Generate outputs (see Step 5).

## Step 5: Check the Outputs
After running the script, check the following outputs in the `cinemo_project` folder:
1. **Console Output**:
   - The terminal displays a summary, including:
     - Total number of tests (e.g., 9).
     - Pass rate (e.g., 88.89%).
     - Number of failed tests.
     - Model used (real or mock).
2. **Log File** (`validation_report.log`):
   - Contains detailed logs for each test case (e.g., test ID, input, predicted output, pass/fail status).
   - Open with a text editor (e.g., Notepad, VS Code).
3. **CSV Report** (`validation_report.csv`):
   - A table with test results (test ID, input, expected/predicted outputs, confidence, condition, pass/fail).
   - Open with Excel, Google Sheets, or a text editor.
4. **Visualization** (`validation_results.png`):
   - A bar chart showing the number of passed vs. failed tests.
   - Open with an image viewer.

## Troubleshooting
- **Error: "ModuleNotFoundError: No module named 'transformers'"**:
  - The script will automatically use a mock model, and the pipeline will still run.
  - Outputs will indicate "Model Used: Mock" in the console and logs.
- **Error: "pip not found"**:
  - Ensure Python is added to your system’s PATH. Reinstall Python and check "Add Python to PATH" (Windows) or run `pip3 install` (macOS/Linux).
- **Other errors**:
  - Contact the applicant for support or refer to the `README.md` for additional details.

## Notes
- The project simulates voice command recognition for automotive infotainment, testing scenarios like noisy inputs, accents, and multilingual commands (English, German, Spanish).
- It’s optimized for embedded systems by minimizing dependencies and avoiding network calls.
- The code is modular and can be extended for real audio inputs or other models, as noted in the `README.md`.

For questions or clarification, please contact the applicant. Thank you for reviewing this project!