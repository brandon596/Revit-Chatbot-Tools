import json

def load_json_file():
    # Open and read the JSON file
    with open('video_links.json', 'r') as file:
        data = json.load(file)
    return data

def retrieve_urls(citations: list):
    links_out = {"Video Links": set(), "Subtitle": set()}
    video_links = load_json_file()
    for row in video_links:
        source_to_show = row["Page URL"]
        # related_links = None #Temp
        related_links = row["Related URLs"]
        video_URL = row["Video URL"]
        all_urls = [source_to_show, related_links, video_URL]
        for citation in citations:
            if citation["Url"] in all_urls:
                links_out["Video Links"].add(video_URL)
                links_out["Subtitle"].add(source_to_show)
    if len(links_out["Video Links"]) > 0:
        links_out["Video Links"] = list(links_out["Video Links"])
        links_out["Subtitle"] = list(links_out["Subtitle"])
        return links_out
    else:
        #return "nil"
        return links_out #temp