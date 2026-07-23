## Overview

This repository provides a structured curriculum for computational text analysis and data management, with an emphasis on machine learning and generative AI. The series progresses from core programming principles to advanced text classification, sentiment analysis, and archival research.

Through hands-on coding exercises, participants work with diverse data formats, including numerical records, health data, and text collections—drawing heavily upon primary source materials from the UCSF Industry Document Library. Sessions emphasize applied practice, integrating conceptual frameworks directly with technical execution.

The focus of the series is to help participants build practical skills through hands-on work. Sessions emphasize applied coding, with lectures and theory used to support the exercises.

---

## Table of Contents

1. [Note on Integrating AI Tools Into the Workshop Series](#note-on-integrating-ai-tools-into-the-workshop-series)
2. [Note on the Workshop Coding Environment](#note-on-the-workshop-coding-environment)
3. [Workshop Series Data and Learning Resources](#workshop-series-data-and-learning-resources)
4. [Intro to Python Part 1: Variables, Lists, Loops, Conditionals](#intro-to-python-part-1-variables-lists-loops-conditionals)
5. [Intro to Python Part 2: Pandas and Graphing](#intro-to-python-part-2-pandas-and-graphing)
6. [Intro to SQL](#intro-to-sql)
7. [Intro to Python and SQL Part 1](#intro-to-python-and-sql-part-1)
8. [Intro to Python and SQL Part 2](#intro-to-python-and-sql-part-2)
9. [Analyzing Covid Testing Data with Python and SQL](#analyzing-covid-testing-data-with-python-and-sql)
10. [Python and Web APIs: Working with Dictionaries and JSON](#python-and-web-apis-working-with-dictionaries-and-json)
11. [Image, Audio, and Video to Text Transcription with Python](#image-audio-and-video-to-text-transcription-with-python)
12. [Image Annotation and Object Detection](#image-annotation-and-object-detection)
13. [Python Background for Text Analysis and Natural Language Processing](#python-background-for-text-analysis-and-natural-language-processing)
14. [Predicting COVID Test Outcome with Scikit-Learn](#predicting-covid-test-outcome-with-scikit-learn)
15. [Document Classification with Scikit-Learn](#document-classification-with-scikit-learn)
16. [Document Topic Modeling with Python](#document-topic-modeling-with-python)
17. [Classification, Sentiment Analysis, and Topic Modeling Using Pre-Trained APIs](#classification-sentiment-analysis-and-topic-modeling-using-pre-trained-apis)
18. [Sharing, Versioning, and Collaborating with Git and GitHub](#sharing-versioning-and-collaborating-with-git-and-github)
19. [Cloud-Based SQL Database and AI Integrations](#cloud-based-sql-database-and-ai-integrations)
20. [Citation](#citation)

---

## Note on Integrating AI tools into the workshop series

Compared to past workshops we have offered, this series incorporates AI-assisted programming earlier on while still starting with the basics. Intro to Python Parts 1 and 2 and Intro to SQL will use AI sparingly. As the series progresses, we will dive into topics like web APIs, text analysis, natural language processing, machine learning, regression, document analysis, and AI system interaction, gradually incorporating more AI-driven techniques.

Furthermore, in our previous workshop series, programming progressed from writing code by hand to downloading, reviewing, and modifying prepared code. That process made sense as we shifted to more complex tasks, requiring less manual coding and more adjustments to existing code. Now, the emphasis is on using AI-powered systems to generate code rather than pre-written codebases. While this approach enables new developers to generate code more rapidly, it also highlights the importance of learning to review and test code. We will focus on building these skills alongside our use of AI.

### Local GenAI (Ollama)

This workshop series also introduces GenAI for text, image, and video analysis using GenAI based local large language models (LLMs). Because it's important to provide learning opportunities for experimentation in a low-risk environment, this workshop focuses on open source software and avoids commercial GenAI systems that require a paid account or a payment method enabled account. Ollama makes it possible for participants to learn GenAI coding and analysis methods without needing to pay for access or risk unexpected charges from cloud-based APIs. Running models locally also raises useful questions around local computation, data privacy, and reproducibility. We use Python to interact with these models programmatically via an API, applying them to tasks such as text generation, document analysis, image description, and OCR.

---

## Note on the Workshop Coding Environment

This workshop uses a combination of hosted Jupyter notebooks and local installation to balance accessibility with long-term technical independence. Hosted environments help reduce setup barriers so we can focus on core programming, data science, and machine learning concepts, while local development builds the skills needed to manage your own tools, work offline, and maintain control over your computational environment.

For more information, see [Workshop_Coding_Environment.md](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Workshop_Coding_Environment.md).

---

## Workshop Series Data and Learning Resources

See the Learning Resources page for a collection of external links, tutorials, and data sources related to this workshop series.

* [Learning Resources](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/LEARNING-RESOURCES.md)

---

## Intro to Python Part 1: Variables, Lists, Loops, Conditionals

This section introduces fundamental Python programming concepts including variables, data types, lists, loops, and conditionals. It follows the Software Carpentry Python Novice Gapminder tutorial to provide hands-on examples and exercises.

### Key Topics:
* Creating and using variables
* Understanding data types and type conversion
* Working with lists
* Writing loops and conditionals

### Resources:
* [Software Carpentry Python Novice Gapminder Tutorial](https://swcarpentry.github.io/python-novice-gapminder/)
* Notebooks:
  * [`variables-functions.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/variables-functions.ipynb) — Focus on variables, assignment, and basic functions.
  * [`lists-loops-conditionals.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Lists-Loops-Conditionals.ipynb) — Covers list manipulation, loops, and conditional statements.

### Recordings:
* [Spring 2025 UCSF Workshop Recording](https://media.ucsf.edu/media/Variables-Lists-Loops-Conditionals/1_4n0afrx6)
* [UCSF CLE Page](https://courses.ucsf.edu/course/view.php?id=5281)

---

## Intro to Python Part 2: Pandas and Graphing

Building on the basics, this section introduces pandas DataFrames for data manipulation and matplotlib for basic graphing and visualization. The aim is to help learners work effectively with tabular data.

### Key Topics:
* Working with pandas DataFrames
* Importing and cleaning data
* Generating summary statistics
* Creating basic visualizations using matplotlib

### Resources:
* Same [Software Carpentry Tutorial](https://swcarpentry.github.io/python-novice-gapminder/)
* Notebooks:
  * [`Lists-Averages.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Lists-Averages.ipynb) — Using lists and loops for calculations such as averages.
  * [`Pandas-Dataframes.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Pandas-Dataframes.ipynb) — Loading data into DataFrames and calculating descriptive statistics.
  * [`Colab-Pandas-Dataframe.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Colab-Pandas-Dataframe.ipynb) — Running pandas code in Google Colab, including visualization examples.
* Additional material: [Intro to Python Part 2 Repository](https://github.com/geoffswc/IntroToPythonPart2)

### Recordings:
* [Pandas and Plotting](https://media.ucsf.edu/media/Pandas-Plotting/1_7fxqtni2)

---

## Intro to SQL

### Online Tutorial Resources:

The Intro to SQL workshop at the UCSF Library follows the "Data Management with SQL for Ecologists" workshop from Data Carpentry:

* [Data Management with SQL for Ecologists](https://datacarpentry.github.io/sql-ecology-lesson/)

### Recordings:
* [UCSF Software Carpentry SQL Workshop](https://media.ucsf.edu/media/Intro-To-SQL-Workshop-4-24-2020/0_fh21geaw)

---

## Intro to Python and SQL Part 1

> **Note:** This workshop is an alternative to Intro to Python Part 1 and covers closely related material. However, this workshop introduces SQL based operations on Pandas dataframes early, and places a greater emphasis on SQL than pandas dataframe operations.

Learners explore how to load datasets and analyze them using both Python and SQL. Example datasets include COVID testing data from Carbon Health.

### Key Topics:
* Reading data files into pandas
* Basic data exploration and cleaning
* Using SQL queries for data manipulation within Python environments

### Resources:
* [`Python_SQL_Day_1.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Python_SQL_Day_1.ipynb) — Loading COVID testing data and exploring it in Google Colab.
* [`Oregon-Sugar-Document.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Oregon-Sugar-Document.ipynb) — Processing tab-delimited text data relevant to archival research.

#### Data Sources:
* [COVID Clinical Data](https://covidclinicaldata.org)
* [UCSF Industry Documents Library](https://www.industrydocuments.ucsf.edu)

### Recordings:
* [Data Analysis with Python and SQL Part 1 Workshop Recording](https://media.ucsf.edu/media/Data-Analysis-Python-SQL-Part-1-10-2025/1_v2f15lms)

---

## Intro to Python and SQL Part 2

> **Note:** This workshop is an alternative to Intro to Python Part 1 and covers closely related material. However, this workshop introduces SQL based operations on Pandas dataframes early, and places a greater emphasis on SQL than pandas dataframe operations.

This section covers Python lists, loops and conditionals for the first half, then introduces text-based SQL querying through the LIKE function on a text based dataset from the Industry Archives.

### Key Topics:
* Creating mock data for experimentation
* Executing SQL queries on COVID datasets using pandasql and Google Colab
* Understanding local vs cloud-based SQL environments

### Resources:
* [`Covid_Mock_Data.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Covid_Mock_Data.ipynb) — Using generative AI to create synthetic datasets.
* [`Covid_Queries.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Covid_Queries.ipynb) — Running SQL queries on COVID data in Google Colab.
* [`Covid_Queries_Local.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Covid_Queries_Local.ipynb) — Local SQL querying via pandasql.

### Recordings:
* [Data Analysis with Python and SQL Part 2 Workshop Recording](https://media.ucsf.edu/media/t/1_abvrwg4h)

---

## Analyzing Covid Testing Data with Python and SQL

Learners explore how to load datasets and analyze them using both Python and SQL. Example datasets include COVID testing data from Carbon Health.

This workshop contains material similar to Intro to Python and SQL Part 1 (above). The main difference is that this workshop uses DuckDB instead of PandaSQL and makes much greater use of GenAI to create code and write SQL queries. The material in the previous two workshops is still helpful, and the SQL statements will be the same regardless of whether you use PandaSQL or DuckDB. However, unless you have a particular legacy reason to use PandaSQL, I'd recommend going with DuckDB for running SQL statements on Pandas dataframes.

### Resources:
* Notebooks:
  * [`Python-Pandas-DuckDB-Covid-Data.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Python-Pandas-DuckDB-Covid-Data.ipynb)

### Recordings:
* [April 2026 Workshop Recording](https://media.ucsf.edu/media/t/1_cphabzd1)

---

## Python and Web APIs: Working with Dictionaries and JSON

This section covers how to work with Python dictionaries and parse JSON data from web APIs. Examples include building caffeine content databases and querying the National Library of Medicine RXNorm API, as well as the UCSF Industry Documents Library API.

### Key Topics:
* Creating and using Python dictionaries
* Parsing JSON data returned from web APIs
* Querying real-world biomedical and archival data APIs

### Resources:
* [Python-JSON-Workshop](https://github.com/geoffswc/Python-JSON-Workshop) — Full Tutorial for working with APIs with Python and JSON.
* [`Python-Dictionaries.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Python-Dictionaries.ipynb) — Introduction to dictionaries and key/value storage.
* [`Caffeine-Dictionary.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Caffeine-Dictionary.ipynb) — Example project mapping caffeine content in beverages.
* [`Web-API-Python.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Web-API-Python.ipynb) — Accessing and parsing data from RXNorm API.
* [`Industry_Documents_API.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Industry_Documents_API.ipynb) and [`Industry-Documents-ApiB.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Industry-Documents-ApiB.ipynb) — Using UCSF’s Industry Documents Library API for archival research.

### Recordings:
* [Python and Web APIs Workshop Recording](https://media.ucsf.edu/media/Python-Web-API/1_2j7irpnk)

> **NOTE: API as Programming Access to GenAI Methods**
>
> APIs have always provided access to both data and functionality. In earlier versions of this workshop series, APIs were primarily introduced in the context of accessing external data sources. More recently, their role has expanded significantly as a primary interface for interacting with AI systems programmatically. I am currently working to incorporate this expanded role of APIs more fully into the workshop series. The 2026 workshop recording reflects this shift in approach. In order to provide a free, open source GenAI system that allows participants to learn without providing a payment method to a cloud based GenAI API (OpenAI, Gemini, etc.), this workshop series will use Ollama, an open source GenAI platform that runs locally on your laptop.

### 2026 Update Recordings:
* [Python and Web APIs 2026 Workshop Recording](https://media.ucsf.edu/media/t/1_3ilgluwo)

### 2026 Update Resources:
* [Ollama Platform](https://ollama.com/) — Link to the Ollama open source platform, installation instructions, available models, and sample use.
* [`Ollama-Image-Summarization-OCR.py`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Ollama-Image-Summarization-OCR.py) — A workbook showing use of Ollama to describe an image and extract embedded text.

---

## Image, Audio, and Video to Text Transcription with Python

Focuses on converting multimedia content to text using optical character recognition (OCR) and audio transcription tools.

### Key Topics:
* Using Tesseract OCR for scanned documents
* Alternative OCR methods with Doctr
* Transcribing audio and video files using OpenAI’s Whisper
* Speaker diarization and clustering techniques

### Resources:
* [`Py_Tesseract_OCR.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Py_Tesseract_OCR.ipynb) — Applying OCR to scanned images.
* [`Doctr_Ocr.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Doctr_Ocr.ipynb) — Exploring other OCR tools.
* [`Whisper_AI_Transcription.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Whisper_AI_Transcription.ipynb) — Audio/video transcription workflows.
* [`Whisper_Diarized_Pipeline.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Whisper_Diarized_Pipeline.ipynb) — Diarization for speaker separation.

### Recordings:
* [Image, Audio, and Video to Text Transcription with Python](https://media.ucsf.edu/media/Image-Audio-Video-Transcription-Python/1_4qeq6u32)

---

## Image Annotation and Object Detection

Introduction to annotating images and detecting objects using TensorFlow and cloud APIs.

### Key Topics:
* Manual and automated labeling of images
* Using TensorFlow object detection tools
* Exploring Google Vision API for advanced image analysis (requires paid account)
* Using a GenAI approach to identifying objects in an image frame

### Resources:
* [`TensorFlow_Labels.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/TensorFlow_Labels.ipynb) — Hands-on object labeling with TensorFlow.
* [Google Cloud Vision API](https://cloud.google.com/vision)
* [Use a Hybrid GenAI approach to identify imagery in a video](https://github.com/geoffswc/Identify-Imagery-GenAI)

---

## Python Background for Text Analysis and Natural Language Processing

Covers foundational NLP techniques such as cleaning text, tokenization, stop word removal, stemming, and lemmatization. Applicable to single documents or collections.

### Key Topics:
* Text preprocessing steps for NLP
* Applying tokenization and filtering to sample texts
* Working with multiple documents for corpus-level analysis

### Resources:
* [`Single-Text-Document.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Single-Text-Document.ipynb) — Preprocessing a single text document.
* [`Multiple-Document.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Multiple-Document.ipynb) — Extending techniques to multiple documents.

### Workshop Repository:
* [Document Classification](https://github.com/geoffswc/Document-Classification) — Workbooks and tutorial links for document classification, including text preparation.

### Sample dataset:
* [UCSF Box Sample Dataset](https://ucsf.app.box.com/v/IDL-DataSets/file/780928732201)

### Recordings:
* [Python Background For Text and NLP](https://media.ucsf.edu/media/t/1_75gwhnkz)

---

## Predicting COVID Test Outcome with Scikit-Learn

Introduction to supervised machine learning for classification problems using COVID symptom data. Emphasizes practical model building with scikit-learn.

### Resources:
* [Course GitHub Repository](https://github.com/geoffswc/Covid-Test-Predictions) — Repository for simple random forest model with minimal dataset.
* [`ML-Covid-Data.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/ML-Covid-Data.ipynb) — Machine learning code generated with ChatGPT and modified during the May 2026 workshop.

### Recordings:
* [May 2026 Workshop Recording](https://media.ucsf.edu/media/Covid-ML-Scikit-Learn-05-2026/1_b2lfyedv?st=30)

---

## Document Classification with Scikit-Learn

Explores text classification techniques including bag-of-words, random forest classifiers, and building machine learning pipelines.

### Key Topics:
* Representing text as sets and bag-of-words
* Training random forest models on movie reviews
* Using scikit-learn pipelines for streamlined workflows

### Resources:
* [`Random_Forest_Simple.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Random_Forest_Simple.ipynb) — Simple example using two short movie reviews to illustrate sentiment analysis.
* [`Movie_Review_Pipeline.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Movie_Review_Pipeline.ipynb) — Classification example using movie review dataset from NLTK.

### Links:
* [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
* [Cornell Movie Review Dataset](https://www.cs.cornell.edu/people/pabo/movie-review-data/)

### Recordings:
* [Document Classification with Python and Scikit-Learn](https://media.ucsf.edu/media/Document-Classification-Python-Scikit-Learn/1_4nkyk948)

---

## Document Topic Modeling with Python

Unsupervised learning for discovering latent topics in text collections using K-Means Clustering.

### Workshop Resources:
* [`Simple-Kmeans.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Simple-Kmeans.ipynb) — Simple example using K-Means Clustering to illustrate unsupervised machine learning.
* [`k-means-visualization.png`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/visualizations/k-means-visualization.png)

### Tutorials and Code Samples:
* [Scikit-learn tutorial: Clustering text documents using k-means](https://scikit-learn.org/stable/auto_examples/text/plot_document_clustering.html#sphx-glr-auto-examples-text-plot-document-clustering-py)
* [LinkedIn Learning course on data science with Python](https://www.linkedin.com/learning/python-for-data-science-and-machine-learning-essential-training-part-2) — Good tutorial on dimensionality reduction.

### Recordings:
* [Topic Modeling with Python and Scikit-Learn](https://media.ucsf.edu/media/t/1_r4k6ivfz)

---

## Classification, Sentiment Analysis, and Topic Modeling Using Pre-Trained APIs

Using external APIs and libraries like Google Cloud NLP, VADER, and zero-shot HuggingFace transformers for classification and sentiment analysis.

### Resources:
* [HuggingFace Zero-Shot Classification](https://huggingface.co/tasks/zero-shot-classification)
* [Vader Sentiment GitHub](https://github.com/cjhutto/vaderSentiment)

### Workbooks:
* HuggingFace Classifier for Text Classification:
  * Application to Multiple Advertising and Legal Documents from the IDL: [`HuggingFaceClassifier.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/HuggingFaceClassifier.ipynb)
  * Application to Smoking-Related Documents from the IDL: [`HuggingFace_ZeroShot_Classifier.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/HuggingFace_ZeroShot_Classifier.ipynb)
* VADER for Text Sentiment Analysis:
  * Application to Multiple Movie Reviews: [`Vader_Movie_Reviews.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Vader_Movie_Reviews.ipynb)
  * Application to Smoking-Related Documents from the IDL: [`Vader_Sentiment.ipynb`](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops/blob/main/Vader_Sentiment.ipynb)

### Recordings:
* [December 2025 Workshop Recording](https://media.ucsf.edu/media/classification-sentiment-pretrained/1_h1pxglha)

---

## Sharing, Versioning, and Collaborating with Git and GitHub

Introduces version control and collaborative workflows using Git and GitHub, including sample projects and workshop materials.

### Resources:
* [Sample Repository](https://github.com/geoffswc/My-Project/)
* [Software Carpentry Git Workshop](https://swcarpentry.github.io/git-novice/)
* [UCSF CLE Recording](https://courses.ucsf.edu/course/view.php?id=5208)
* [GitHub Markdown Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

### Recordings:
* [Winter 2025 GitHub Workshop](https://media.ucsf.edu/media/Github-Workshop-2025/1_52ih4iqd)

---

## Cloud-Based SQL Database and AI Integrations

Working with cloud SQL services such as the Google BigQuery sandbox to query large public datasets without requiring paid accounts.

* [Google BigQuery Sandbox](https://cloud.google.com/bigquery/docs/sandbox)

---

## Citation

If you use this curriculum, code, or these workshop materials in your research or teaching, please cite them using CITATION.cff or as follows:

**APA:**
> Boushey, G. (2026). *Document Analysis with Python, SQL, Machine Learning, and AI* (Version 2.0.0). [Computer software]. UCSF Library. https://github.com/UCSD-DSOS/UCSF-DSOS-Python-SQL-Workshops

**BibTeX:**
```bibtex
@software{Boushey_Document_Analysis_Python_SQL_AI_2026,
  author    = {Boushey, Geoffrey},
  title     = {Document Analysis with Python, SQL, Machine Learning, and AI},
  url       = {[https://github.com/UCSF-DSOS/UCSF-DSOS-Python-SQL-Workshops](https://github.com/geoffswc/UCSF-DSOS-Python-SQL-Workshops)},
  version   = {2.0.0},
  year      = {2026},
  publisher = {UCSF Library}
}
```
