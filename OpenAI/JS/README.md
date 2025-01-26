# 🚀 OpenAI API Integration in JS 
![OpenAI-JS Banner](https://github.com/chiragjoshi12/OpenAI/blob/main/img/OpenAI-JS%20Banner.png)

This project demonstrates the integration of OpenAI's API for various use cases including GPT-4 Vision and Text API, DALL-E 3 Image Generation, and GPT-3.5 Turbo Text API using Node.js.

## 🔧 Installation

1. 📥 Clone the repository:
   ```bash
   git clone https://github.com/chiragjoshi12/OpenAI.git
   cd OpenAI/JS
    ```

2. 📦 Install the required dependencies:
  ```bash
   npm install openai
  ```

3. 🔑 Replace the placeholder in the app.js file with your actual OpenAI API key:
   ```bash
   const openai = new OpenAI({ apiKey: 'your_api_key_here' });
   ```

## 🚀 Usage

### 🖼️ GPT-4 Vision and Text API
This example demonstrates how to use the GPT-4 Vision and Text API to analyze an image and respond to a text query. The function `VisonAndText` is responsible for sending the request and handling the response.

### 🎨 DALL-E 3 Image Generation
This example demonstrates how to generate an image using DALL-E 3. The function `generateImage` takes a prompt and returns the generated image URL.

### 📝 GPT-3.5 Turbo Text API
This example demonstrates how to use the GPT-3.5 Turbo Text API to get a text completion. The function `GPT35Turbo` sends a request with a user query and processes the response.

Happy Coding 🤖✨

---

Readme made with 💖 using [README Generator by Chirag Joshi](https://github.com/chiragjoshi12/readme-generator)
