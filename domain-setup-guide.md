# Custom Domain Setup Guide for Streamlit Cloud

This guide covers multiple ways to connect a custom domain to your Streamlit app.

## 🎯 Quick Start Options

### Option 1: Cloudflare Pages (Recommended)

Cloudflare Pages provides free hosting and can proxy your Streamlit app.

#### Setup Steps:
1. **Sign up for Cloudflare** (if you haven't already)
2. **Add your domain to Cloudflare** (or use their free subdomain)
3. **Create a Pages project**:
   - Go to [Cloudflare Pages](https://pages.cloudflare.com/)
   - Click "Create a project"
   - Choose "Connect to Git" and select your repository
   - Set build command: `echo "No build needed"`
   - Set build output: `/`
   - Add environment variable: `STREAMLIT_URL` = `https://your-app.streamlit.app`

4. **Configure DNS**:
   - Point your domain to Cloudflare
   - Enable SSL/TLS encryption

### Option 2: Vercel (Alternative)

Vercel can also proxy to external services.

#### Setup Steps:
1. **Connect your repository to Vercel**
2. **Create `vercel.json`** in your project root:
```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "https://your-app.streamlit.app/$1"
    }
  ]
}
```

### Option 3: Netlify (Another Alternative)

Similar to Vercel, Netlify can proxy external URLs.

#### Setup Steps:
1. **Connect your repository to Netlify**
2. **Create `_redirects`** in your public folder:
```
/*  https://your-app.streamlit.app/:splat  200
```

## 🔧 DNS Configuration

### For Custom Domain (example.com)

If using a service like Cloudflare, Netlify, or Vercel:

```
Type: CNAME
Name: www (or @ for root domain)
Value: your-app.streamlit.app
TTL: Auto
```

### For Subdomain (app.example.com)

```
Type: CNAME
Name: app
Value: your-app.streamlit.app
TTL: Auto
```

## 🛡️ Security Considerations

1. **HTTPS**: All proxy services support SSL/TLS
2. **CORS**: Ensure your Streamlit app allows the proxy domain
3. **Rate Limiting**: Consider implementing rate limiting on your proxy

## 📝 Environment Variables

Add these to your proxy service:

```bash
STREAMLIT_URL=https://your-app.streamlit.app
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
STREAMLIT_SERVER_HEADLESS=true
```

## 🚀 Deployment Steps

1. **Deploy your Streamlit app first**
2. **Get the Streamlit Cloud URL** (e.g., `https://your-app.streamlit.app`)
3. **Choose a proxy service** (Cloudflare Pages recommended)
4. **Configure DNS** to point to your proxy
5. **Test the connection**

## 🔍 Testing Your Setup

Use these tools to verify your domain setup:

1. **DNS Lookup**: `nslookup yourdomain.com`
2. **SSL Check**: Check SSL certificate validity
3. **CORS Test**: Verify cross-origin requests work
4. **Load Test**: Ensure the proxy handles traffic properly

## 💡 Pro Tips

1. **Use a subdomain** (app.yourdomain.com) for easier management
2. **Set up proper redirects** from www to non-www (or vice versa)
3. **Configure monitoring** to track your app's performance
4. **Set up backup domains** in case of issues

## 🆘 Troubleshooting

**Common Issues:**
- **DNS Propagation**: Can take 24-48 hours
- **SSL Certificate**: May need manual approval for some domains
- **CORS Errors**: Add proxy domain to allowed origins in Streamlit config

**Debug Commands:**
```bash
# Check DNS
dig yourdomain.com

# Test connection
curl -I https://yourdomain.com

# Check SSL
openssl s_client -connect yourdomain.com:443
```
