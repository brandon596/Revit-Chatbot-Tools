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
        return "nil"

example = {
    "CitationSources": [
      {
        "Id": "1",
        "Name": "To Insert Conduit Parts and Fittings into a Tube and Pipe Assembly",
        "Text": "Click anywhere in the background of the graphics window to place the conduit part. Optionally, click again to place multiple occurrences. Right-click in the graphics window and select Done. After the conduit part is placed, you can connect it to other components using the Connect Fittings command at a later time.",
        "Url": "https://help.autodesk.com/cloudhelp/2023/ENU/Inventor-Help/files/GUID-D7D1137F-2964-4618-B6CE-FA776F409BE4.htm"
      },
      {
        "Id": "2",
        "Name": "To Insert Conduit Parts and Fittings into a Tube and Pipe Assembly",
        "Text": "Click anywhere in the background of the graphics window to place the conduit part. Optionally, click again to place multiple occurrences. Right-click in the graphics window and select Done. After the conduit part is placed, you can connect it to other components using the Connect Fittings command at a later time.",
        "Url": "https://help.autodesk.com/videos/EwdnRpazriCqCYAbmkUD2SlVvk5PLPtu/video.webm"
      }
    ],
    "Content": "To place conduits using the BIM Module, follow these steps:\n\n1. Click anywhere in the background of the graphics window to place the conduit part.\n2. Optionally, click again to place multiple occurrences.\n3. Right-click in the graphics window and select \"Done.\"\n4. After the conduit part is placed, you can connect it to other components using the \"Connect Fittings\" command at a later time [1].",
    "MarkdownContent": "To place conduits using the BIM Module, follow these steps:\n\n1. Click anywhere in the background of the graphics window to place the conduit part.\n2. Optionally, click again to place multiple occurrences.\n3. Right-click in the graphics window and select \"Done.\"\n4. After the conduit part is placed, you can connect it to other components using the \"Connect Fittings\" command at a later time [1].\n\n[1]: https://help.autodesk.com/cloudhelp/2023/ENU/Inventor-Help/files/GUID-D7D1137F-2964-4618-B6CE-FA776F409BE4.htm \"To Insert Conduit Parts and Fittings into a Tube and Pipe Assembly\""
  }

example = example["CitationSources"]
print(retrieve_urls(example))