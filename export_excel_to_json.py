import pandas as pd
import json
from sentence_transformers import SentenceTransformer
import numpy as np

def export_excel_to_json(): #only call or run when changes to excel are made
    # Load the Excel file
    df = pd.read_excel("")

    df.fillna("", inplace=True)

    # Convert the DataFrame to a JSON object
    json_data = df.to_dict(orient='records')

    # Save the JSON object to a file
    with open("video_links.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    # Optionally, print the JSON output
    # print(json.dumps(json_data, indent=4))

    #Updating embeddings for semantic search
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    # Corpus
    corpus = [row["Title"] for row in json_data]

    

    # Use "convert_to_tensor=True" to keep the tensors on GPU (if available)
    corpus_embeddings = embedder.encode(corpus)
    # print(type(corpus_embeddings))

    # Save to .npy file
    np.save('embeddings.npy', corpus_embeddings)

export_excel_to_json()  #only call or run when changes to excel are made