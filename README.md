# Python-App-1

This repository includes utility functions with tests and a helper script to set up the Flux AI model for use with [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## Setting Up Flux on ComfyUI

Run the provided script to clone ComfyUI, install dependencies, and download the Flux model:

```bash
python install_flux_comfyui.py
```

The script creates a `comfyui` directory in the project root and places the model under `comfyui/models/flux-model.safetensors`.

Once complete, you can launch ComfyUI from the newly created directory.

## Testing

Use `pytest` to run unit tests for the utility functions:

```bash
pytest -q
```
