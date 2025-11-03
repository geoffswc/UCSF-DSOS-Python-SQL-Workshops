# Data and Document Analysis with Python, SQL, and AI

## Overview

This is a collection of code and data resources used in the UCSF Library "Document Analysis with Python, SQL, and AI" workshop series. The materials here can be used for teaching foundational programming, data analysis, and AI techniques relevant to data science, NLP, machine learning, text classification and sentiment analysis, and archival research.

The series generally starts with foundational Python programming concepts and advances to more complex topics, including data analysis, document analysis, and artificial intelligence (AI)-based research. Throughout the workshops, we will dive into various data types—including numerical data, health data, text, and images/videos—and explore analysis techniques like regression, classification, and sentiment analysis. The end of the series will focus on text analysis, especially analyzing documents from the UCSF Industry Document Library.

The focus of the series is to help participants build practical skills. Sessions will involve a lot of hands-on coding while keeping lectures and theory to a minimum.



## Table of Contents

1. [Note on Integrating AI Tools Into the Workshop Series](#note-on-integrating-ai-tools-into-the-workshop-series)
2. [Workshop Series Data and Learning Resources](#workshop-series-data-and-learning-resources)
3. [Intro to Python Part 1: Variables, Lists, Loops, Conditionals](#intro-to-python-part-1-variables-lists-loops-conditionals)  
3-alt. [Intro to Python and SQL Part 1](#intro-to-python-and-sql-part-1)  
4. [Intro to Python Part 2: Pandas and Graphing](#intro-to-python-part-2-pandas-and-graphing)  
4-alt. [Intro to Python and SQL Part 2](#intro-to-python-and-sql-part-2)  
5. [Python and Web APIs: Working with Dictionaries and JSON](#python-and-web-apis-working-with-dictionaries-and-json)  
6. [Image, Audio, and Video to Text Transcription with Python](#image-audio-and-video-to-text-transcription-with-python)  
7. [Image Annotation and Object Detection](#image-annotation-and-object-detection)  
8. [Python Background for Text Analysis and Natural Language Processing](#python-background-for-text-analysis-and-natural-language-processing)  
9. [Predicting COVID Test Outcome with Scikit-Learn](#predicting-covid-test-outcome-with-scikit-learn)  
10. [Document Classification with Scikit-Learn](#document-classification-with-scikit-learn)  
11. [Document Topic Modeling with Python](#document-topic-modeling-with-python)  
12. [Classification, Sentiment Analysis, and Topic Modeling Using Pre-Trained APIs](#classification-sentiment-analysis-and-topic-modeling-using-pre-trained-apis)  
13. [Sharing, Versioning, and Collaborating with Git and GitHub](#sharing-versioning-and-collaborating-with-git-and-github)
14. [Cloud-Based SQL Database and AI Integrations](#cloud-based-sql-database-and-ai-integrations)

---

## Note on Integrating AI tools into the workshop series

Compared to past workshops we have offered, this series incorporates AI-assisted programming earlier on while still starting with the basics. Intro to Python Parts 1 and 2 and Intro to SQL will use AI sparingly. As the series progresses, we will dive into topics like web APIs, text analysis, natural language processing, machine learning, regression, document analysis, and AI system interaction, gradually incorporating more AI-driven techniques.

Furthermore, in our previous workshop series, programming progressed from writing code by hand to downloading, reviewing, and modifying pre-prepared code. That process made sense as we shifted to more complex tasks, requiring less manual coding and more adjustments to existing code. Now, the emphasis is on using AI-powered systems to generate code rather than pre-written codebases. While this approach enables new developers to generate code more rapidly, it also highlights the importance of learning to review and test code. We will focus on building these skills alongside our use of AI.

---

## Workshop Series Data and Learning Resources

See the Learning Resources page for a collection of external links, tutorials, and data sources related to this workshop series. 

- [Learning Resources](LEARNING-RESOURCES.md) 

---


## Intro to Python Part 1: Variables, Lists, Loops, Conditionals

This section introduces fundamental Python programming concepts including variables, data types, lists, loops, and conditionals. It follows the Software Carpentry Python Novice Gapminder tutorial to provide hands-on examples and exercises.

### Key Topics:
- Creating and using variables
- Understanding data types and type conversion
- Working with lists
- Writing loops and conditionals

### Resources:
- [Software Carpentry Python Novice Gapminder Tutorial](https://swcarpentry.github.io/python-novice-gapminder/)
- Notebooks:
  - [variables-functions.ipynb](variables-functions.ipynb)  
    Focus on variables, assignment, and basic functions.
  - [lists-loops-conditionals.ipynb](lists-loops-conditionals.ipynb)  
    Covers list manipulation, loops, and conditional statements.

---

## Intro to Python and SQL Part 1

Note: This workshop is an alternative to Intro to Python Part 1 and covers closely related material. However, this workshop introduces SQL based operations on Pandas dataframes early, and places a greater empahsis on SQL than pandas dataframe operations.

Learners explore how to load datasets and analyze them using both Python and SQL. Example datasets include COVID testing data from Carbon Health.

### Key Topics:
- Reading data files into pandas
- Basic data exploration and cleaning
- Using SQL queries for data manipulation within Python environments

### Resources: 
- [Python_SQL_Day_1.ipynb](Python_SQL_Day_1.ipynb)  
  Loading COVID testing data and exploring it in Google Colab.
- [Oregon-Sugar-Document.ipynb](Oregon-Sugar-Document.ipynb)  
  Processing tab-delimited text data relevant to archival research.

#### Data Sources:  
- [COVID Clinical Data](https://covidclinicaldata.org)  
- [UCSF Industry Documents Library](https://www.industrydocuments.ucsf.edu)

### Recordings:
- [Data Analysis with Python and SQL Part 1 Workshop Recording](https://media.ucsf.edu/media/Data-Analysis-Python-SQL-Part-1-10-2025/1_v2f15lms)

---


## Intro to Python Part 2: Pandas and Graphing

Building on the basics, this section introduces pandas DataFrames for data manipulation and matplotlib for basic graphing and visualization. The aim is to help learners work effectively with tabular data.

### Key Topics:
- Working with pandas DataFrames
- Importing and cleaning data
- Generating summary statistics
- Creating basic visualizations using matplotlib

### Resources:
- Same [Software Carpentry Tutorial](https://swcarpentry.github.io/python-novice-gapminder/)
- Notebooks:
  - [Lists-Averages.ipynb](Lists-Averages.ipynb)  
    Using lists and loops for calculations such as averages.
  - [Pandas-Dataframes.ipynb](Pandas-Dataframes.ipynb)  
    Loading data into DataFrames and calculating descriptive statistics.
  - [Colab-Pandas-Dataframe.ipynb](Colab-Pandas-Dataframe.ipynb)  
    Running pandas code in Google Colab, including visualization examples.
- Additional material:  
  https://github.com/geoffswc/IntroToPythonPart2

---

## Intro to Python and SQL Part 2

Note: This workshop is an alternative to Intro to Python Part 1 and covers closely related material. However, this workshop introduces SQL based operations on Pandas dataframes early, and places a greater empahsis on SQL than pandas dataframe operations.

This section covers Python lists, loops and conditionals for the first half, then introduces text-based SQL querying through the LIKE function on a text based dataset from the Industry Archives. 

### Key Topics:
- Creating mock data for experimentation
- Executing SQL queries on COVID datasets using pandasql and Google Colab
- Understanding local vs cloud-based SQL environments

### Resources:
- [Covid_Mock_Data.ipynb](Covid_Mock_Data.ipynb)  
  Using generative AI to create synthetic datasets.
- [Covid_Queries.ipynb](Covid_Queries.ipynb)  
  Running SQL queries on COVID data in Google Colab.
- [Covid_Queries_Local.ipynb](Covid_Queries_Local.ipynb)  
  Local SQL querying via pandasql.

### Recordings:
- [Data Analysis with Python and SQL Part 2 Workshop Recording](https://media.ucsf.edu/media/t/1_abvrwg4h)

---

## Python and Web APIs: Working with Dictionaries and JSON

This section covers how to work with Python dictionaries and parse JSON data from web APIs. Examples include building caffeine content databases and querying the National Library of Medicine RXNorm API, as well as the UCSF Industry Documents Library API.

### Key Topics:
- Creating and using Python dictionaries
- Parsing JSON data returned from web APIs
- Querying real-world biomedical and archival data APIs

### Resources:
- [Python-JSON-Workshop](https://github.com/geoffswc/Python-JSON-Workshop)  
  Full Tutorial for working with APIs with Python and JSON.
- [Python-Dictionaries.ipynb](Python-Dictionaries.ipynb)  
  Introduction to dictionaries and key/value storage.
- [Caffeine-Dictionary.ipynb](Caffeine-Dictionary.ipynb)  
  Example project mapping caffeine content in beverages.
- [Web-API-Python.ipynb](Web-API-Python.ipynb)  
  Accessing and parsing data from RXNorm API.
- [Industry_Documents_API.ipynb](Industry_Documents_API.ipynb) and [Industry-Documents-ApiB.ipynb](Industry-Documents-ApiB.ipynb)  
  Using UCSF’s Industry Documents Library API for archival research.

### Recordings
- [Python and Web APIs Workshop Recording](https://media.ucsf.edu/media/Python-Web-API/1_2j7irpnk)

---

## Image, Audio, and Video to Text Transcription with Python

Focuses on converting multimedia content to text using optical character recognition (OCR) and audio transcription tools.

### Key Topics:
- Using Tesseract OCR for scanned documents
- Alternative OCR methods with Doctr
- Transcribing audio and video files using OpenAI’s Whisper
- Speaker diarization and clustering techniques

### Resources:
- [Py_Tesseract_OCR.ipynb](Py_Tesseract_OCR.ipynb)  
  Applying OCR to scanned images.
- [Doctr_Ocr.ipynb](Doctr_Ocr.ipynb)  
  Exploring other OCR tools.
- [Whisper_AI_Transcription.ipynb](Whisper_AI_Transcription.ipynb)  
  Audio/video transcription workflows.
- [Whisper_Diarized_Pipeline.ipynb](Whisper_Diarized_Pipeline.ipynb)  
  Diarization for speaker separation.

---

## Image Annotation and Object Detection

Introduction to annotating images and detecting objects using TensorFlow and cloud APIs.

### Key Topics:
- Manual and automated labeling of images
- Using TensorFlow object detection tools
- Exploring Google Vision API for advanced image analysis (requires paid account)
- Using a GenAI approach to identifying objects in an image frame

### Resources:
- [TensorFlow_Labels.ipynb](TensorFlow_Labels.ipynb)  
  Hands-on object labeling with TensorFlow.  
  [Notebook Link](https://github.com/geoffswc/Libguide-AI-Tools-Archival-Research/blob/main/TensorFlow_Labels.ipynb)
- Google Vision API: https://cloud.google.com/vision
- [Use a Hybrid GenAI approach to identify imagery in a video](https://github.com/geoffswc/Identify-Imagery-GenAI)

---

## Python Background for Text Analysis and Natural Language Processing

Covers foundational NLP techniques such as cleaning text, tokenization, stop word removal, stemming, and lemmatization. Applicable to single documents or collections.

### Key Topics:
- Text preprocessing steps for NLP
- Applying tokenization and filtering to sample texts
- Working with multiple documents for corpus-level analysis

### Resources:
- [Single-Text-Document.ipynb](Single-Text-Document.ipynb)  
  Preprocessing a single text document.
- [Multiple-Document.ipynb](Multiple-Document.ipynb)  
  Extending techniques to multiple documents.

### Workshop Repository:
- [Document Classification](https://github.com/geoffswc/Document-Classification)
  Workbooks and tutorial links for document classification, including text preparation

### Sample dataset: 
- https://ucsf.app.box.com/v/IDL-DataSets/file/780928732201

### Recording

- [Python Background For Text and NLP](https://media.ucsf.edu/media/t/1_75gwhnkz)

---

## Predicting COVID Test Outcome with Scikit-Learn

Introduction to supervised machine learning for classification problems using COVID symptom data. Emphasizes practical model building with scikit-learn.

### Repository:  
https://github.com/geoffswc/Covid-Test-Predictions

---

## Document Classification with Scikit-Learn

Explores text classification techniques including bag-of-words, random forest classifiers, and building machine learning pipelines.

### Key Topics:
- Representing text as sets and bag-of-words
- Training random forest models on movie reviews
- Using scikit-learn pipelines for streamlined workflows

### Resources:
- [Example-Classification-Set-DefaultDict.ipynb](Example-Classification-Set-DefaultDict.ipynb)  
  Introduction to Python sets and bag-of-words.
- [Simple-Classification-Scikit-Learn.ipynb](Simple-Classification-Scikit-Learn.ipynb)  
  Applying random forest classifiers.
- [Sentiment-Pipeline-Example.ipynb](Sentiment-Pipeline-Example.ipynb)  
  Larger dataset sentiment analysis with pipelines.  
  Repository: https://github.com/geoffswc/Document-Classification

---

## Document Topic Modeling with Python

Unsupervised learning for discovering latent topics in text collections using Latent Dirichlet Allocation (LDA).

### Resources:
- Repository: https://github.com/geoffswc/YouTube-Transcript-Python
- Tutorial: https://www.tidytextmining.com/topicmodeling

---

## Classification, Sentiment Analysis, and Topic Modeling Using Pre-Trained APIs

Using external APIs and libraries like Google Cloud NLP, VADER, and zero-shot HuggingFace transformers for classification and sentiment analysis.

### Resources:
- [HuggingFaceClassifier.ipynb](HuggingFaceClassifier.ipynb)  
  Zero-shot classification with HuggingFace models.  
  https://huggingface.co/tasks/zero-shot-classification
- [VaderTest.ipynb](VaderTest.ipynb)  
  Sentiment analysis using VADER.  
  https://github.com/cjhutto/vaderSentiment
- [Predict_Text_Sentiment_And_Category.ipynb](Predict_Text_Sentiment_And_Category.ipynb)  
  Demonstration of Google Cloud Language API (paid service).

---

## Sharing, Versioning, and Collaborating with Git and GitHub

Introduces version control and collaborative workflows using Git and GitHub, including sample projects and workshop materials.

### Resources:
- Sample repository: https://github.com/geoffswc/Capstone
- Software Carpentries Git workshop: https://swcarpentry.github.io/git-novice/
- UCSF CLE recording: https://courses.ucsf.edu/course/view.php?id=5208

---

## Cloud-Based SQL Database and AI Integrations

Working with cloud SQL services such as the Google BigQuery sandbox to query large public datasets without requiring paid accounts.

Google BigQuery Sandbox: https://cloud.google.com/bigquery/docs/sandbox

