#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""



def read_urls(filename):
    """
    Extracts and returns a list of unique puzzle URLs from a given log file.

    Args:
        filename (str): The path to the log file.

    Returns:
        list: A sorted list of unique puzzle URLs.
    """
    # Extract the hostname from the filename (assumes format like "www.example.com.log").
    hostname_match = re.search(r'www\.\w+\.\w+', filename)
    if not hostname_match:
        raise ValueError("Invalid filename format. Expected 'www.example.com.log'.")
    hostname = hostname_match.group()

    # Read the log file content.
    with open(filename, 'r', encoding='utf-8') as f:
        log_data = f.read()

    # Find all puzzle URLs in the log file.
    # Example regex to match URLs with 'puzzle' in their path.
    puzzle_urls = re.findall(r'GET\s(\/.*?puzzle.*?)\sHTTP', log_data)

    # Build complete URLs and remove duplicates.
    full_urls = {f"http://{hostname}{path}" for path in puzzle_urls}

    # Return the sorted list of URLs.
    return sorted(full_urls)

  # +++your code here+++
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++


def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
