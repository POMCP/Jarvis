from googleapiclient.discovery import build
import re


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def google_results_count(query):
    service = build("customsearch", "v1",
                    developerKey="AIzaSyAeSL5HTHJcxH9SeeWfS_qf2nFWRHBc8HU")

    result = service.cse().list(
            q=query, cx="014232785313891304027:nfy0x-f7cn8").execute()
    return cleanhtml(result["items"][00]["htmlSnippet"])

print google_results_count('Python is awesome')