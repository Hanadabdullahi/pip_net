import jupytext

# Define the file paths
py_file = '/Users/hanadabdullahi/Downloads/pip_net/PIPNet/main (kopia).py'  # Replace with your .py file
ipynb_file = '/Users/hanadabdullahi/Downloads/pip_net/PIPNet/main.ipynb'  # Replace with the desired .ipynb file name

# Read the .py file
with open(py_file, 'r') as file:
    py_content = file.read()

# Convert the .py content to a Jupyter notebook
notebook = jupytext.reads(py_content, fmt='py')

# Write the notebook to a .ipynb file
jupytext.write(notebook, ipynb_file)

print(f"Converted {py_file} to {ipynb_file}")
