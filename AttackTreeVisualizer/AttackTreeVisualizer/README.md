
The Attack Tree Visualizer is a Python application that allows users to:

1) Load an attack tree from a JSON file and visualize it.
2) Add monetary values or probabilities to the leaf nodes of the attack tree.
3) Aggregate these values to compute an overall threat assessment.



# ---------------------------
# Requirnemnts
# ---------------------------
1) Python 3.x
2) NetworkX
3) Matplotlib

To install the necessary Python packages, run:


pip install -r requirements.txt


# ---------------------------
# Installation
# ---------------------------

1) Clone the repository to your local machine.

git clone https://github.com/ImNasser/Information-Security-Management/

2) Navigate to the project folder and install the required packages.

cd AttackTreeVisualizer
pip install -r requirements.txt

# ---------------------------
# Usage
# ---------------------------
Run the main Python script to start the application.

python3 src/main.py


Follow the on-screen instructions to add values to the leaf nodes and visualize the attack tree.

# ---------------------------
# Project Structure
# ---------------------------

AttackTreeVisualizer/
|-- src/
|   |-- main.py
|   |-- load_data.py
|   |-- draw_tree.py
|   |-- user_input.py
|   |-- aggregate_values.py
|-- data/
|   |-- attack_tree.json
|-- README.md
|-- requirements.txt



# ---------------------------
# Troubleshooting
# ---------------------------
If you encounter any issues, please check the current working directory printed in the terminal. Make sure the relative path to attack_tree.json is correct.




