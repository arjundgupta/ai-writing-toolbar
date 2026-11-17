# AI Writing Toolbar

A Chrome extension that brings an AI writing assistant to any text you highlight. Select text on any page to improve, rewrite, or expand it, or open a chat sidebar that can reference your open tabs.

![VibeType toolbar on a highlighted LinkedIn post](assets/preview.png)

**Website and demo video:** https://vibetype.vercel.app

## How it works

- **Floating toolbar:** highlight text to Improve, Rewrite, Elaborate, or Chat
- **Sidebar chat:** ask about what you're reading, with context from multiple tabs
- **Page context:** parses the page, splits it into chunks, and uses OpenAI embeddings to find the parts most relevant to your text

## Tech

chrome extension (manifest v3, shadow dom), javascript, openai

## Structure

```
manifest.json          extension config
content.js             floating toolbar on every page
sidebar.html/.js/.css  chat sidebar
background.js          messaging between tabs
html_parser.js         page HTML to clean text
content_chunker.js     splits content into chunks
semantic_search.js     finds relevant chunks with embeddings
```

This branch has the extension. The content API is on `main`.
