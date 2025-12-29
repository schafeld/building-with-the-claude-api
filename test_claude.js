import Anthropic from '@anthropic-ai/sdk';
import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

const client = new Anthropic({
    apiKey: process.env.ANTHROPIC_API_KEY // Get API key from .env file
});

const message = await client.messages.create({
    model: 'claude-sonnet-4-5-20250929',
    max_tokens: 1024,
    messages: [
        { role: 'user', content: 'Who came up first with the idea of Heliocentrism?' }
    ]
});

console.log(message.content[0].text);