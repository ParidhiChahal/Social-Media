# Social-Media
# 🚀 Social Media Content Generator

**AI-powered content creation** – Generate engaging posts, catchy captions, and relevant hashtags for any topic.

## Features
- Auto-generate engaging social media posts using AI
- Create catchy captions for images and content
- Produce relevant hashtags from any topic
- Interactive Streamlit web interface
- Customizable AI parameters (temperature, tokens, sampling)
- Batch content generation for multiple topics

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
# Web interface (recommended)
streamlit run app.py

# CLI
python content_generator.py
```

## Tech Stack
Python • Hugging Face Transformers • GPT-2 • Streamlit

### Issue: Generated content is too short or cut off
**Solution:** Increase `max_new_tokens` parameter in the generate_post function

### Issue: Model download takes too long on first run
**Solution:** First run downloads GPT-2 (~500MB) from Hugging Face Hub — subsequent runs load from cache

---

## References & Resources

- [Hugging Face Documentation](https://huggingface.co/)
- [Transformers Library](https://huggingface.co/docs/transformers)
- [GPT-2 Model Card](https://huggingface.co/gpt2)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

## Author

**Name:** Paridhi Chahal
**Roll Number:** 2301730186
**Project:** Social Media Content Generator
**Date:** 2024-2025

---

## Conclusion

The Social Media Content Generator demonstrates practical application of Generative AI in automating content creation. By combining Hugging Face GPT-2 models with Python and Streamlit, we create an efficient tool that saves time and improves social media productivity.

This project showcases:
- Integration of modern AI APIs
- Practical content automation techniques
- User-friendly interface design
- Real-world application development

---

**Last Updated:** 2025
**Version:** 1.0
