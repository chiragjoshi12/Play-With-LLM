const { OpenAI } = require('openai');

const openai = new OpenAI({ apiKey: 'your_api_key_here' }); // Replace 'your_api_key_here' with your actual API key

// ? GPT-4o Vison and Text API
async function VisonAndText() {
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content: [
            {
              type: "text",
              text: "You are a helpful assistant."
            }
          ]
        },
        {
          role: "user",
          content: [
            {
              type: "image_url",
              image_url: {
                url: "https://storage.googleapis.com/kaggle-avatars/images/17363235-kg.png"
              }
            },
            {
              type: "text",
              text: "What this in this image?"
            }
          ]
        }
      ],
      temperature: 1,
      max_tokens: 256,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
    });

    const modelResponse = response.choices.map(choice => choice.message.content).join('\n');
    console.log(modelResponse);
  } catch (error) {
    console.error('Error:', error);
  }
}

VisonAndText();

// ? Dall-e-3 Image Generation
async function generateImage(prompt) {
  try {
    const response = await openai.images.generate({
      model: "dall-e-3",
      prompt: prompt,
      n: 1,
      size: "1024x1024",
    });
    const imageUrl = response.data[0].url;
    console.log(imageUrl);
    return imageUrl;
  } catch (error) {
    console.error('Error:', error);
  }
}

generateImage("a white siamese cat");

// ? GPT-3.5 Turbo Text API
async function GPT35Turbo() {
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "system",
          content: [
            {
              type: "text",
              text: "You are a helpful assistant."
            }
          ]
        },
        {
          role: "user",
          content: [
            {
              type: "text",
              text: "Who won the world series in 2020?"
            }
          ]
        }
      ],
      temperature: 1,
      max_tokens: 256,
      top_p: 1,
      frequency_penalty: 0,
      presence_penalty: 0,
    });

    const modelResponse = response.choices.map(choice => choice.message.content).join('\n');
    console.log(modelResponse);
  } catch (error) {
    console.error('Error:', error);
  }
}

GPT35Turbo();