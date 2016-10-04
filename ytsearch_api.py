#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import json

import numpy as np

from youtube_api import *
from approved_channels import id_to_channel, approved_channel_ids

def score_video(title, result_position):
  score = result_position
  if "teaser" in title.lower():
    score = score + 100
  if "trailer" not in title.lower():
    score = score + 100
  return score


def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q + " Trailer",
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  scores = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  result_position = 0
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video" and search_result["snippet"]["channelId"] in approved_channel_ids:
      videos.append('"%s"|%s' % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
      scores.append(score_video(search_result["snippet"]["title"], result_position))
    result_position = result_position + 1
      #videos.append("%s" % json.dumps(search_result))
  if scores:
    print options.q, "|",videos[np.argmin(scores)].encode('utf-8') #"\n".join(videos), "\n"


if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default="XMen")
  argparser.add_argument("--f", help="Search file", default="movie_titles.csv")
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

  #print args.f
  with open("%s" % (args.f), 'r') as movie_file:
    movie_titles = movie_file.readlines()
  #print movie_titles
  for movie_title in movie_titles:
    args.q = movie_title.replace('\n','')
    try:
      youtube_search(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)