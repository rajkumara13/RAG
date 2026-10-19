**# Learning RAG with Python

I'm exploring **Retrieval-Augmented Generation (RAG)** and learning how to build a system that can work with information from documents instead of relying only on an AI model's existing knowledge.

This project is my hands-on journey into RAG, starting with reading PDF files, extracting text, and splitting that text into smaller chunks.

## What is RAG?

RAG stands for Retrieval-Augmented Generation. It combines information retrieval with a language model to generate answers using relevant information from external documents.

For example, imagine you have a PDF containing 100 pages of notes. Instead of manually searching every page, a RAG system can retrieve relevant passages from the PDF and use them to help answer your question.

## What I'm Learning

- **PDF Text Extraction:** Reading PDF files and extracting their text using Python.
- **Text Processing:** Cleaning extracted text and understanding how it can be represented as a list of words.
- **Chunking:** Dividing large amounts of text into smaller, manageable pieces.
- **Embeddings:** Learning how text can be converted into numerical representations of meaning.
- **Retrieval:** Finding the chunks that are most relevant to a user's question.
- **Answer Generation:** Using retrieved information to help a language model generate an answer.

## Understanding Chunking

A PDF can contain thousands of words. Passing all that text to a language model at once can be inefficient and may exceed its context limit.

Chunking solves this problem by dividing the text into smaller sections.

For example, consider this sentence:

> Python is a programming language. It is widely used in artificial intelligence and data science. RAG helps language models work with external documents.

It could be divided into chunks like these:

**Chunk 1**
```text
Python is a programming language.
It is widely used in artificial intelligence.
```

**Chunk 2**
```text
It is widely used in artificial intelligence.
RAG helps language models work with external documents.
```

Notice that part of the text appears in both chunks. This is called **chunk overlap**. It helps preserve context when a meaningful sentence or idea crosses a chunk boundary.

The chunk size and overlap can be adjusted depending on the document and the retrieval approach.

## How RAG Works

```text
PDF Document
     |
     v
Extract Text
     |
     v
Clean and Process Text
     |
     v
Split Text into Chunks
     |
     v
Generate Embeddings
     |
     v
Store Vectors
     |
     v
Retrieve Relevant Chunks
     |
     v
Generate an Answer
```

This represents the overall RAG workflow I'm learning to build step by step.

## Technologies

- Python
- pypdf — PDF text extraction
- Virtual environments — dependency isolation
- Git and GitHub — version control

Additional libraries and models will be introduced as the project develops.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rajkumara13/RAG.git
cd RAG
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the dependency

```bash
pip install pypdf
```

If a `requirements.txt` file is available, you can install the project's listed dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the Python script

Run the PDF extraction script from the project directory. For example, if your script is named `pdf_reader.py`:

```bash
python pdf_reader.py
```

Make sure the PDF file path in the script points to a valid PDF on your computer.

## Project Goals

My goal is to understand how RAG works internally rather than treating it as a black box. I'm starting with the fundamentals and gradually working toward a complete document-based question-answering system.

Planned improvements include:

- Experimenting with different chunk sizes and overlap values.
- Generating embeddings for text chunks.
- Implementing semantic search.
- Connecting a language model to the retrieval pipeline.
- Building a system that answers questions using information from PDF documents.

## What I'm Learning Through This Project

This project helps me practice Python, document processing, text splitting, and the core concepts behind modern AI applications. I'm building it incrementally so I can understand each stage before moving to the next.

---

**Author:** Rajkumar A.  
**GitHub:** [rajkumara13](https://github.com/rajkumara13)

**
