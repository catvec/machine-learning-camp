# Putney MIT Technology Camp
Resources for the Putney MIT technology camp (last updated 2026).

# Table Of Contents
- [Overview](#overview)
- [Development](#development)

# Overview
Resources for the Putney MIT technology camp.

See [`docs/`](./docs/) for instructor and student resources.

# Development
> These instructions are meant for developers who are creating the material. For instructor and student guides see [`docs/`](./docs/)

Repository structure:

- [`notebooks/`](./notebooks): Jupyter notebooks
- [`assets/`](./assets): Static assets references in Jupyter notebooks

## Setup
The tooling in this repository uses [uv](https://docs.astral.sh/uv/) to manage Python dependencies and virtual environments. Once you have uv installed run:

``` shell
uv sync
```

## Writing Notebooks
The jupyter notebooks in this repository are meant to run in Google Colab. Write notebooks in Google Colab's editor. 

- **Checking in to source control**:  
  - In order to preserve changes to the notebooks in source control click the File > Download > `.ipynb` button
  - Then copy the file into the [`notebooks/`](./notebooks) directory
  - By default notebook files are not suitable to check in to source control. To format and clean notebook files run:
    ``` shell
    uv run ./scripts/format-notebooks.sh
    ```
- **Images in notebooks:**  
  - If you want to use an image in a notebook download the image into the [`assets/`](./assets) directory. This way the notebooks will always reference images that we know exist. As we will use these notebooks over the course of years it is expected that many sites on the internet will go dormant between these years, and we don't want to deal with dead links and images.
    - Ensure the creator of the image has granted usage of the image via the creative commons
  - Add the image URL to the `IMAGE_CREDITS.md` file in the assets folder
  - Then commit and push the image to GitHub
  - Get the raw URL for the image, it should be something like:
    ```
https://github.com/catvec/putney-mit-technology-camp/blob/main/assets/what-is-ai/7-layer-neural-network.png?raw=true)
    ```
