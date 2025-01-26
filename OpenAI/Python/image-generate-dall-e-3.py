from openai import OpenAI

# Create client using OPENAI_API_KEY
client = OpenAI(api_key="OPENAI_API_KEY") # Replace "OPENAI_API_KEY" with your API

response = client.images.generate(
  model="dall-e-3",
  prompt="Imagine a futuristic cityscape blending advanced technology with lush, verdant nature. Towering skyscrapers are intertwined with massive, ancient trees, their branches forming natural bridges between buildings. Holographic billboards and neon lights illuminate the scene, reflecting off glass facades and cascading waterfalls. The streets below are bustling with diverse, colorful characters — a mix of humans, robots, and fantastical creatures, all coexisting in harmony. The sky above is a swirl of auroras and distant planets, hinting at a universe full of possibilities. Capture this harmonious blend of nature and technology in a vibrant, detailed image.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)