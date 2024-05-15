from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")

prompt = "An astronaut riding a green horse"

image = pipe(prompt=prompt).images[0]

image.save('example.png')