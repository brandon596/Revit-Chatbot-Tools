from flask import Flask, request, jsonify
import getVideo_links
# import torch
# from sentence_transformers import SentenceTransformer
# import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route('/get-video-urls', methods=["POST"])
def get_citations():
    citations = request.json
    # print(citations)
    citations = citations.get("CitationSources")
    #print(citations)
    links_out = getVideo_links.retrieve_urls(citations)
    
    return jsonify(links_out), 201

def semantic_search(query):
    pass

if __name__ == '__main__':
    app.run(debug=True)