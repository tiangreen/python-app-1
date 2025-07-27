import subprocess
import sys
from pathlib import Path

COMFY_REPO = "https://github.com/comfyanonymous/ComfyUI.git"
MODEL_URL = "https://huggingface.co/FluxAI/flux-model/resolve/main/flux-model.safetensors"


def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


def clone_comfyui(target_dir: Path):
    if target_dir.exists():
        print(f"ComfyUI already cloned at {target_dir}")
        return
    run_command(["git", "clone", COMFY_REPO, str(target_dir)])


def install_requirements(comfy_dir: Path):
    req_file = comfy_dir / "requirements.txt"
    if req_file.exists():
        run_command([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
    else:
        print("No requirements.txt found in ComfyUI repo")


def download_model(model_dir: Path):
    model_dir.mkdir(parents=True, exist_ok=True)
    model_path = model_dir / "flux-model.safetensors"
    if model_path.exists():
        print(f"Model already present at {model_path}")
        return
    import requests
    print(f"Downloading model from {MODEL_URL}")
    resp = requests.get(MODEL_URL, stream=True)
    resp.raise_for_status()
    with open(model_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    print(f"Model saved to {model_path}")


def main():
    project_dir = Path.cwd() / "comfyui"
    models_dir = project_dir / "models"
    clone_comfyui(project_dir)
    install_requirements(project_dir)
    download_model(models_dir)
    print("Setup complete. You can now run ComfyUI.")


if __name__ == "__main__":
    main()
