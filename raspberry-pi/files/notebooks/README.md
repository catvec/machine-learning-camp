# Notebooks
You are using Jupyter Lab, a tool similar to Google Colab, but it runs **on** your Raspberry Pi.

This means any Python or commands you run here are actually running on your Raspberry Pi (So you can do things like access the camera and screen)!

# Files
Here is a quick rundown of the files in this folder:

- Special files (Please don't edit, or stuff will stop working 😉)
  - [`pyproject.toml`](./pyproject.toml): Sets up the Python project and specifies packages we want to use
  - [`uv.lock`](./uv.lock): Helps install Python packages
  - [`notebook-server.sh`](./notebook-server.sh): Runs the Jupyter Lab
