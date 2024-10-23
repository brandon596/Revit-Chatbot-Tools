import json

def load_json_file():
    # Open and read the JSON file
    with open('video_links.json', 'r') as file:
        data = json.load(file)
    return data

def retrieve_urls(citations: list):
    video_links = load_json_file()
    media_urls = set()
    subtitles = set()
    for row in video_links:
        source_to_show = row["Page URL"]
        related_links = row["Related URLs"]
        video_URL = row["Video URL"]
        all_urls = source_to_show + related_links + video_URL
        for citation in citations:
            if citation["Url"] in all_urls:
                media_urls.add(video_URL)
                subtitles.add(source_to_show)
    links_out = {"Video_Links": [{"url": link} for link in media_urls], "Subtitle": [{"url": link} for link in subtitles]}
    links_out["qty"] = len(media_urls)

    return links_out
    # if len(media_urls) > 0:
    #     links_out = {"Video_Links": [{"url": link} for link in media_urls], "Subtitle": [{"url": link} for link in subtitles]}
    #     links_out["qty"] = len(media_urls)
    #     return links_out
    # else:
    #     #return "nil"
    #     return links_out #tempget