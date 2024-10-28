from flask import Flask, request, jsonify
import getVideo_links
import torch
from sentence_transformers import SentenceTransformer
import numpy as np
import json

embedder = SentenceTransformer("all-MiniLM-L6-v2")
with open('video_links.json', 'r') as file:
    data = json.load(file)
corpus = [title["Title"] for title in data]
CUT_OFF = 0.7

corpus_embeddings = np.load("embeddings.npy")

top_k = min(1, len(corpus))

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route('/3oie09i2Wd22/get-video-urls', methods=["POST"])
def get_citations():
    citations = request.json
    print(citations)
    citations = citations.get("CitationSources")
    #print(citations)
    links_out = getVideo_links.retrieve_urls(citations)
    
    return jsonify(links_out), 201

@app.route('/3oie09i2Wd22/semantic_search', methods=["POST"])
def semantic_search():
    post = request.json
    query = post.get("query")
    query_embedding = embedder.encode(query)

    # We use cosine-similarity and torch.topk to find the highest score
    similarity_scores = embedder.similarity(query_embedding, corpus_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=top_k)

    print("\nQuery:", query)
    print("Top most similar sentences in corpus:")

    for score, idx in zip(scores, indices):
        if score > CUT_OFF:
            print(corpus[idx], f"(Score: {score:.4f})")
            found_title = corpus[idx]
            found = True
        else:
            print("No similar results")
            found = False
    if found:
        for row in data:
            if found_title == row["Title"]:
                output = {
                    "Video_Links": [
                        {
                            "mimeType": "video/webm", 
                            "url": row["Video URL"]
                        }
                        ], 
                    "Subtitle": "Source: " + row["Page URL"], 
                    "qty": 1
                    }
    else:
        output = {
                    "Video_Links": [
                        {
                            "mimeType": "video/webm", 
                            "url": ""
                        }
                        ], 
                    "Subtitle": "Source: ", 
                    "qty": 0
                    }
    return jsonify(output), 201

if __name__ == '__main__':
    app.run(debug=True)