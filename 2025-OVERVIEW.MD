# Document Analysis Workshop Series: Introduction and Curriculum Overview

## Introduction

This workshop series will guide you through the key skills needed for document analysis using **Python**, **SQL**, and **AI tools**. The goal is to build up from basic programming concepts to creating a full workflow that processes multimedia documents such as videos and audio files. You will learn how to:
* download videos and image files
* extract audio
* split it into chunks
* transcribe speech
* identify speakers
* recognize key objects and describe them
* classify records by topic
* assess the sentiment of text (positive/negative/neutral)
* organize the data using **pandas**
* run **SQL-style queries** on the data
* apply **AI models** for classification and topic analysis.

We will start by showing a complete example script that does all of this, so you can see the final goal. Then, each part of the curriculum will break down the components of the example, helping you build up your skills step-by-step.

## Curriculum Structure and How It Connects to the Example

1.  **Python Basics: Variables, Lists, Loops, and Conditionals**
    Learn the fundamentals of Python programming that allow you to control workflows and work with collections of data.

    ```python
    video_urls = ['[http://example.com/video1.mp4](http://example.com/video1.mp4)', '[http://example.com/video2.mp4](http://example.com/video2.mp4)']

    for url in video_urls:
        print(f"Processing video: {url}")
    ```

2.  **Working with Data Using Pandas and Simple Graphing**
    Learn to organize and explore your data using **pandas DataFrames** and create simple visualizations to understand transcript data.

    ```python
    import pandas as pd

    data = [
        {"speaker": "Speaker 0", "text": "Hello there!", "start": 0.0, "end": 2.5},
        {"speaker": "Speaker 1", "text": "Hi!", "start": 2.6, "end": 3.0}
    ]

    df = pd.DataFrame(data)
    print(df.head())
    ```

3.  **Loading Data and Exploring with Python and SQL**
    Understand how to load transcript data and explore it with basic statistics and queries using SQL syntax in Python.

    ```python
    df = pd.read_csv("transcript.csv")
    print(df.describe())
    print(df['speaker'].value_counts())
    ```

4.  **Using pandasql to Query DataFrames with SQL**
    Learn how to run SQL queries directly on pandas DataFrames using the `pandasql` library for easy data analysis.

    ```python
    from pandasql import sqldf

    query = "SELECT speaker, COUNT(*) as turns FROM df GROUP BY speaker"
    result = sqldf(query, globals())
    print(result)
    ```

5.  **Working with Web APIs and JSON Data**
    Get familiar with making API requests, handling **JSON** responses, and using dictionaries in Python, which is essential when working with AI services.

    ```python
    import requests

    response = requests.get("[http://example.com/video.mp4](http://example.com/video.mp4)")
    if response.status_code == 200:
        with open("video.mp4", "wb") as f:
            f.write(response.content)

    segment = {
        "start": 0.0,
        "end": 2.5,
        "speaker": "Speaker 0",
        "text": "Hello world"
    }
    print(segment["text"])
    ```

6.  **Audio and Video Transcription with Whisper**
    Learn how to use the **Whisper model** to transcribe audio from your video files accurately.

    ```python
    import whisper

    model = whisper.load_model("small")
    result = model.transcribe("audio_chunk.wav")
    print(result['text'])
    ```

7.  **Image Annotation and Object Detection (Optional Extension)**
    Explore the basics of detecting and annotating objects in images as a potential future addition to multimedia document analysis.

7.  **Image Annotation and Object Detection (Optional Extension)**
    Explore the basics of detecting and annotating objects in images as a potential future addition to multimedia document analysis.

    ```python
    import requests
    import json

    # Placeholder for the GPT-5 API endpoint for vision/object detection
    GPT5_API_URL = "[https://api.gpt5.example/v1/vision/analyze](https://api.gpt5.example/v1/vision/analyze)" 
    
    # Payload for the API request
    # 'image_url' would be the actual path/URL to the image
    payload = {
        "model": "gpt-5-vision",
        "image_url": "[http://example.com/image_with_umbrella.jpg](http://example.com/image_with_umbrella.jpg)",
        "prompt": "Identify if an umbrella is in the image, and provide a brief description of the context in which it appears."
    }

    try:
        # Simulate API call
        response = requests.post(
            GPT5_API_URL, 
            headers={"Authorization": "Bearer YOUR_API_KEY"},
            json=payload
        )
        
        # Simulate a successful response
        if response.status_code == 200:
            result = response.json()
            # Assuming the API returns a structure with a 'description' key
            print("Object Analysis (Umbrella):")
            print(result.get("description", "Analysis pending.")) 
        else:
            print(f"API Error: Status {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
    ```

8.  **Text Preprocessing for NLP**
    Understand basic text cleaning and preparation techniques needed before running analysis like classification or topic modeling.

    ```python
    text = "Hello! This is an example."
    clean_text = text.lower().strip()
    print(clean_text)
    ```

9.  **Introduction to Machine Learning with Scikit-Learn**
    Build your first machine learning model to get hands-on experience with predictive modeling.

    ```python
    from sklearn.linear_model import LogisticRegression

    X = [[1, 2], [2, 1], [1, 0]]
    y = [0, 1, 0]

    model = LogisticRegression().fit(X, y)
    print(model.predict([[1, 1]]))
    ```

10. **Document Classification Using Random Forest**
    Learn how to classify documents based on text using a more robust model like the **Random Forest classifier**.

    ```python
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np

    texts = ["I love this!", "I hate that.", "This is great.", "This is terrible."]
    # Labels (1: Positive, 0: Negative)
    labels = np.array([1, 0, 1, 0])

    # 1. Feature Extraction
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    # 2. Model Training
    # Using 100 decision trees (n_estimators)
    clf = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, labels)

    # 3. Prediction
    test_text = vectorizer.transform(["I love it"])
    prediction = clf.predict(test_text)
    
    # The output will be the predicted class (0 or 1)
    print(prediction)
    ```

11. **Topic Modeling with Latent Dirichlet Allocation**
    Discover how to automatically find topics in a collection of documents using **LDA** (Latent Dirichlet Allocation).

    ```python
    from sklearn.decomposition import LatentDirichletAllocation
    from sklearn.feature_extraction.text import CountVectorizer

    texts = ["cats are great pets", "dogs are loyal animals"]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)

    lda = LatentDirichletAllocation(n_components=2)
    lda.fit(X)

    print("Topics:", lda.components_)
    ```

12. **Classification, Sentiment Analysis, and Topic Modeling Using Generative AI**
    See how to call **generative AI APIs** to get advanced classification, sentiment, or topic insights from your text.

    ```python
    import requests

    api_url = "[https://api.example.com/genai/classify](https://api.example.com/genai/classify)"
    data = {"text": "I love this product!"}

    response = requests.post(api_url, json=data)
    result = response.json()
    print(result['classification'])
    ```

13. **Version Control and Collaboration Using Git and GitHub**
    Learn basic **Git** commands to manage your code and collaborate with others.

    ```bash
    git init
    git add .
    git commit -m "Initial commit of document analysis pipeline"
    git push origin main
    ```

14. **Using Cloud Storage and Integrating AI**
    Understand how to store your results in the cloud (like Google Drive) and connect to AI services for seamless workflows.

    ```python
    import os
    import pandas as pd

    drive_path = "/content/gdrive/MyDrive/DiarizedTranscripts"
    files = os.listdir(drive_path)
    print(f"Files in Google Drive folder: {files}")

    df = pd.read_csv(os.path.join(drive_path, files[0]))
    print(df.head())
    ```
