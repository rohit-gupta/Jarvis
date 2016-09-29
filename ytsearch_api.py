#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import json

from youtube_api import *
from approved_channels import id_to_channel

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s) By %s" % (search_result["snippet"]["title"], search_result["id"]["videoId"], search_result["snippet"]["channelId"]))
      #videos.append("%s" % json.dumps(search_result))
  print "Videos:\n", "\n".join(videos), "\n"


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="XMen")
  argparser.add_argument("--f", help="Search file", default="movie_titles.csv")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  print args
  movie_titles = []
  with open(args.f, 'wb') as f:
    movie_titles = f.readlines()

  for movie_title in movie_titles:
    args.q = movie_title
    try:
      youtube_search(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)