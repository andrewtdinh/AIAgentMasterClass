## Version 6
Here is the [youtube tutorial video](https://www.youtube.com/watch?v=7dKQPbSXiB8&list=PLyrg3m7Ei-MpsdEA6eKN1k2gJpuhllNTi&index=7)

This is a local RAG agent plus additional capabilities.
To run the agent, activate the virtual environment, navigate into the v6 folder, install dependencies, and execute the below commands in order:

1. To generate a local chroma storage:
```
python rag-document-loader.py
```
After running the above document, you should see a chroma_db sub-directory in your folder.


2. To load the UI
```
streamlit run rag-task-agent.py
```