# Image Classification App

A Streamlit web application for classifying images into three categories: plastic, organic, and metal using a TensorFlow/Keras model.

## Features

- 🖼️ Image upload and classification
- 🤖 TensorFlow/Keras model integration
- 📱 Responsive Streamlit interface
- 🔄 Real-time predictions

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment to Streamlit Cloud

### Option 1: Direct Deployment (Recommended)

1. Go to [Streamlit Cloud](https://share.streamlit.io)
2. Connect your GitHub repository
3. Configure deployment:
   - **Main file path**: `app.py`
   - **Python version**: 3.9
   - **Requirements file**: `requirements.txt` (if needed)
4. Click **Deploy!**

### Option 2: Using GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/deploy-to-streamlit.yml`) that:

- Runs on every push to `main` or `master` branch
- Tests the Streamlit app
- Prepares for deployment

To deploy using GitHub Actions:

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io)
3. Connect your repository
4. The workflow will help validate your setup

## Project Structure

```
├── app.py                    # Main Streamlit application
├── my_model.h5              # Trained TensorFlow model
├── requirements.txt         # Python dependencies
├── packages.txt             # System dependencies
├── .streamlit/config.toml   # Streamlit configuration
├── Code.ipynb              # Jupyter notebook with model training code
├── domain-setup-guide.md   # Custom domain setup instructions
├── vercel.json             # Vercel configuration
├── _redirects              # Netlify/Cloudflare redirects
├── _headers                # Security headers
├── deploy.sh               # Deployment script
├── .github/workflows/      # GitHub Actions workflows
│   └── deploy-to-streamlit.yml
└── README.md               # Project documentation
```

## Model Details

- **Architecture**: MobileNetV2-based classifier
- **Classes**: plastic, organic, metal
- **Input**: RGB images (224x224 pixels)
- **Framework**: TensorFlow/Keras

## Dependencies

- streamlit >= 1.28.0
- tensorflow >= 2.13.0
- pillow >= 10.0.0
- numpy >= 1.24.0

## Custom Domain Setup

Connect your own domain to the Streamlit app using one of these methods:

### Option 1: Cloudflare Pages (Recommended)
1. Sign up at [Cloudflare Pages](https://pages.cloudflare.com/)
2. Connect your GitHub repository
3. Use the provided `_headers` and `_redirects` files
4. Configure DNS to point to Cloudflare

### Option 2: Vercel
1. Sign up at [Vercel](https://vercel.com)
2. Connect your GitHub repository
3. Use the provided `vercel.json` configuration
4. Deploy and configure custom domain

### Option 3: Netlify
1. Sign up at [Netlify](https://netlify.com)
2. Connect your GitHub repository
3. Use the provided `_redirects` file
4. Configure custom domain

For detailed instructions, see [`domain-setup-guide.md`](./domain-setup-guide.md).

## License

This project is part of a computer vision coursework assignment.
