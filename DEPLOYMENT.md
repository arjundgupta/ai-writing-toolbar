# VibeType API Deployment Guide

This guide covers multiple ways to host your VibeType API without using Vercel.

## Prerequisites

1. **OpenAI API Key**: You need an OpenAI API key for the semantic search functionality
2. **Python 3.8+**: The API requires Python 3.8 or higher

## Quick Start (Local Development)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Environment Variable
```bash
# On Windows
set OPENAI_API_KEY=your-openai-api-key-here

# On macOS/Linux
export OPENAI_API_KEY=your-openai-api-key-here
```

### 3. Run the API
```bash
python deploy.py
```

Or manually:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Hosting Options

### Option 1: Railway (Recommended - Easy & Free)

Railway is a modern platform that's perfect for Python APIs.

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Initialize and Deploy**:
   ```bash
   railway init
   railway up
   ```

4. **Set Environment Variables**:
   ```bash
   railway variables set OPENAI_API_KEY=your-openai-api-key
   ```

5. **Get your URL**:
   ```bash
   railway domain
   ```

### Option 2: Render (Free Tier Available)

Render provides easy deployment with a free tier.

1. **Create a Render account** at https://render.com

2. **Create a new Web Service**

3. **Connect your GitHub repository**

4. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**: Add `OPENAI_API_KEY`

5. **Deploy**

### Option 3: DigitalOcean App Platform

1. **Create a DigitalOcean account**

2. **Create a new App**

3. **Connect your repository**

4. **Configure**:
   - **Source**: Your GitHub repo
   - **Build Command**: `pip install -r requirements.txt`
   - **Run Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**: Add `OPENAI_API_KEY`

### Option 4: Heroku (Paid)

1. **Install Heroku CLI**

2. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

3. **Set environment variable**:
   ```bash
   heroku config:set OPENAI_API_KEY=your-openai-api-key
   ```

4. **Deploy**:
   ```bash
   git push heroku main
   ```

### Option 5: Docker Deployment

#### Using Docker Compose (Recommended)

1. **Create Docker files**:
   ```bash
   python deploy.py
   ```

2. **Run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

#### Using Docker directly

1. **Build the image**:
   ```bash
   docker build -t vibetype-api .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 -e OPENAI_API_KEY=your-key vibetype-api
   ```

### Option 6: AWS/GCP/Azure

For cloud providers, you can use:

- **AWS**: AWS App Runner, Elastic Beanstalk, or ECS
- **GCP**: Cloud Run or App Engine
- **Azure**: Azure Container Instances or App Service

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key for embeddings | Yes |
| `PORT` | Port to run the server on (set by hosting platform) | No |

## API Endpoints

Once deployed, your API will have these endpoints:

- `GET /` - Health check
- `GET /health` - Detailed health check
- `POST /process` - Main endpoint for processing HTML content
- `POST /parse-only` - Parse HTML without chunking or search

## Testing Your Deployment

1. **Health Check**:
   ```bash
   curl https://your-app-url.railway.app/health
   ```

2. **Process Content**:
   ```bash
   curl -X POST "https://your-app-url.railway.app/process" \
     -H "Content-Type: application/json" \
     -d '{
       "html": "<html><body><h1>Test</h1><p>This is a test.</p></body></html>",
       "query": "What is this about?",
       "chunk_size": 750,
       "top_k": 3
     }'
   ```

## Monitoring and Logs

- **Railway**: `railway logs`
- **Render**: Available in dashboard
- **Heroku**: `heroku logs --tail`
- **Docker**: `docker logs container-name`

## Troubleshooting

### Common Issues

1. **OpenAI API Key not set**:
   - Ensure the environment variable is properly set
   - Check for typos in the variable name

2. **Port binding issues**:
   - Use `$PORT` environment variable for cloud platforms
   - Ensure port 8000 is available locally

3. **Memory issues**:
   - The API can be memory-intensive with large HTML content
   - Consider upgrading your hosting plan if needed

4. **Dependency issues**:
   - Ensure all dependencies are in `requirements.txt`
   - Some platforms may require additional system packages

### Performance Tips

1. **Chunk size**: Adjust `chunk_size` parameter based on your content
2. **Top-k results**: Limit `top_k` to reduce processing time
3. **Caching**: Consider implementing response caching for repeated queries

## Security Considerations

1. **API Key**: Never commit your OpenAI API key to version control
2. **CORS**: The API allows all origins by default - restrict this for production
3. **Rate Limiting**: Consider implementing rate limiting for production use
4. **Input Validation**: The API validates input, but consider additional sanitization

## Cost Optimization

1. **OpenAI Usage**: Monitor your OpenAI API usage to control costs
2. **Hosting**: Choose appropriate hosting plans based on your traffic
3. **Caching**: Implement caching to reduce API calls to OpenAI

## Support

If you encounter issues:
1. Check the logs for error messages
2. Verify environment variables are set correctly
3. Test locally first to isolate issues
4. Check the API documentation at `/docs` endpoint 