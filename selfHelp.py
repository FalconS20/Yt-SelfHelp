import feedparser
import os
from datetime import datetime, timedelta

# Base YouTube URL for channels
BASE_YOUTUBE_URL = "https://www.youtube.com/feeds/videos.xml?channel_id="

# Define YouTube channels by categories
youtube_channels = {
    "Productivity, Self-Improvement & Personal Growth": [
        "UCoOae5nYA7VqaXzerajD0lg",  # Ali Abdaal
        "UCwAnu01qlnVg1Ai2AbtTMaA",  # Jeff Su
        "UC525q2RIufHjnaHOuIUFY9A",  # Shu Omi
        "UC2Zs9v2hL2qZZ7vsAENsg4w",  # Justin Sung
        "UClDcKhHgT3x88I0q7BOT0ow",  # Jun Yuh
        "UCBX_-ls-dXuhFNSWSXcHrTA",  # Koi
        "UCskE6NgyY5Ym-ArzJvnhREw",  # KevZ
        "UChgNGLBeUG7yC-3SxaZlSBg",  # Angel Zheng
        "UCpTupIxGdmt3sTpOHjegwxQ",  # Anthony Vicino
        "UCWjJsRjG_KIHlAr0jRr7big",  # Archer Newton
        "UCAFA5SxepYXxICZVgrcOntQ",  # Dabi
        "UCzB7zFhM1jLQdV0A-iZtZqg",  # Deya
        "UC3F3zZFiRElw2GLwzndp05A",  # Gabe Bult
        "UCiSJ2SLUxa6vE-97xAqRCtA",  # Kutch
        "UCl0Na-giucIFjh2I9cqOnmw",  # Laurie Wang
        "UCdGuT4qRHJaB-gf9AVlssaw",  # Matt Huang
        "UCLiAWvpRFtNiVOu6OyEfmDA",  # Nicholas Garofola
        "UCQpPo9BNwezg54N9hMFQp6Q",  # Nischa
        "UCt1ES-_FMXQfM3JeO_FrOXw",  # ParkNotes
        "UCOV2T-bKuIu-THONA9XAZag",  # Reinventing Poppy
        "UC2UXDak6o7rBm23k3Vv5dww",  # Tina Huang
        "UCG-KntY7aVnIGXYEBQvmBAQ",  # Thomas Frank
        "UCBOPiSs5Ae_Pws-AImpvxPw",  # Robert Creating
        "UCbDmEdLs-SB3FjrDFQJ4TDg",  # Reysu
        "UCl2d5Qgfcactbzkfpp0ayug",  # Mike Dee
        "UCaffuWQ2mLfRevosyKoz87Q",  # Zach Highley
        "UCb9fs9s67BXlX7rXVzRf5cQ",  # Amy Wang
        "UCZgNB0DO5AJ6awbw9tgiwoQ",  # Alexis Kingsley
        "UClvdIQwkgwMFwyjsDZoi-4g",  # Collin The Chad
        "UCeF0JdmMHLcMQFNOtWX2_cQ",  # Liz Loves Reading
        "UCA-mWX9CvCTVFWRMb9bKc9w",  # Dan Martell
        "UC1OLfEQ-DeCFBSUIyPgVqmw",  # Rachelle in theory
        "UCKtiMrNZq0gGbPTnsMu7Bsw",  # Ruri Ohama
        "UCJCR3IMdS5zHNh1OAQd7vMg",  # Charlotte Fraza
        "UC-dmJ79518WlKMbsu50eMTQ",  # Clark Kegley
        "UCq5iwmJnLnrVv9zUQU5zbKw", # Nick Russell
        "UCmvYCRYPDlzSHVNCI_ViJDQ", # Tiago Forte
        "UCUFFHXvzAMRSD8Bq4bJppxQ", # Elizabeth Filips
        "UC1OLfEQ-DeCFBSUIyPgVqmw", # Rachelle in theory
        "UCk2uK3jPlliD6_JCAUb4myw", # Destina
        "UCmgNUsFzcte6qmsCLL429pg", # Meg Shinagawa
        "UCEdXA7uliIbBT5aWhuR3dFQ", # Caren Magill | ADHD Coach + Multipotentialite
        "UCVTIFLAmnSjlT0sGz2BYJmQ", # Antonia's Universe
        "UC1QnKYxNXosv9ykUt_6wCMg", # Dr Alex Young
        "UClaaXhWDyCjfNKhcpKR-GBg", # Jeremy's Tutorials
        "UCEHp_b02I0GvTYCBPX_0w1g"  # Mariana Vieira
    ],
    "Health, Wellness, and Medical": [
        "UCR_Tzu1r5M9uoNB3CF4Zg3g",  # Dr Sid Warrier
        "UC3w193M5tYPJqF0Hi-7U-2g",  # Dr. Eric Berg DC
        "UCc34FvrsixVdHuvaipikMxA",  # Dr. Sarin
        "UCKRpf_HZfpLwxuIgyeYnsVw",  # GunjanShouts
        "UCZlpezVo9CCp6fuPdPlKWdQ",  # Michael Chua, MD
        "UCoCbt0YNJL4_MtIo6Lg1ybA",  # Traya Health
        "UCM5cdocmS8t-0EURE8uvadA",  # SAAOL Heart Center
        "UCyNaCRf6Aaljcm9ZWARawXw"   # RESPIRE
    ],
    "Personal Development & Motivation": [
        "UCNjPtOCvMrKY5eLwr_-7eUg",  # Alux.com
        "UCqVEHtQoXHmUCfJ-9smpTSg",  # Answer in Progress
        "UCU_W0oE_ock8bWKjALiGs8Q",  # Charisma on Command
        "UCHb00yEZ_yY_inLGdSBa7GQ",  # CoolMitra
        "UCEzSFZRs8zJb5x5depOtUHA",  # Dan Go
        "UCYKwtzEUK4mfpZpvl8u2QTg",  # Dhairyam Motivation
        "UCdmDDJXog3qWbYAf7Gud8vQ",  # Drishti Sharma
        "UCurYxozQbvKn-oNUxNJh45Q",  # GREAT IDEAS GREAT LIFE
        "UCSvoBOtMz9AWVpk84XgVOeA",  # Joseph Tsar
        "UCuoxrRDDgk3UUnxR4tlkJYQ",  # Marie Forleo
        "UCDgUAAHgsV2fFZQm2fIWBnA",  # Prince Ea
        "UCwrzhaGy4oAHu8clPCVol3g"   # SONU SHARMA
    ],
    "Fashion & Lifestyle": [
        "UCZyCposXwcyopaACep44maQ",  # Alex Costa
        "UCnd5xZAWXs0soICzuxGNtFw",  # Vaibhav Keswani
        "UCgQH__KQFjEZDbOiM0c5_Pg",  # The Dynamite Male
        "UCVaSUu1B_Y4R2rFLUpvRmlA"   # The Formal Edit
    ]
}

# Function to get videos from an RSS feed
def get_videos_from_rss(rss_url):
    try:
        feed = feedparser.parse(rss_url)
        if feed.bozo:
            raise ValueError(f"Failed to parse feed from {rss_url}. Error: {feed.bozo_exception}")

        today = datetime.now()

        # Calculate previous Monday and the end of the last Sunday
        # Monday is weekday 0, Sunday is weekday 6
        current_weekday = today.weekday()

        # If today is Monday (weekday 0), go to last week's Monday
        last_monday = today - timedelta(days=current_weekday + 7)  # Start of previous Monday
        last_sunday = last_monday + timedelta(days=6, hours=23, minutes=59, seconds=59)  # End of previous Sunday

        videos = []

        for entry in feed.entries:
            try:
                published = datetime(*entry.published_parsed[:6])
                thumbnail_url = entry.media_thumbnail[0]['url'] if 'media_thumbnail' in entry else None

                # Check if the video was published between last Monday and last Sunday
                if last_monday <= published <= last_sunday:
                    videos.append({
                        'title': entry.title,
                        'link': entry.link,
                        'published': published,
                        'channel': feed.feed.title,
                        'thumbnail': thumbnail_url
                    })
            except Exception as e:
                print(f"Error processing entry: {e}")

        return videos
    except Exception as e:
        print(f"Error retrieving videos from {rss_url}: {e}")
        return []

# Aggregate videos by categories
all_videos_by_category = {}
for category, channels in youtube_channels.items():
    category_videos = []
    for channel_id in channels:
        rss_url = BASE_YOUTUBE_URL + channel_id
        category_videos.extend(get_videos_from_rss(rss_url))
    all_videos_by_category[category] = sorted(category_videos, key=lambda x: x['published'], reverse=True)

# Create HTML content with navbar and video cards
html_content = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Videos by Category</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Kalam:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f8f9fa;
        }

        h2 {
            text-align: center;
            font-family: 'Kalam', cursive;
            color: #333;
            margin-bottom: 20px;
        }

        .navbar {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }

        .navbar a {
            margin: 0 15px;
            text-decoration: none;
            font-weight: 600;
            color: #333;
        }

        .navbar a:hover {
            color: #007bff;
        }

        .video-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }

        .card {
            border: 1px solid #ddd;
            border-radius: 8px;  /* Reduced border-radius for a sharper look */
            width: 250px;
            background-color: #fff;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            text-decoration: none;
            color: black;
            transition: transform 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .thumbnail {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }

        .video-title {
            font-weight: 600;
            font-size: 1em;  /* Slightly reduced font size for titles */
            margin: 10px 0;
            padding: 0 10px;
        }

        .channel, .published {
            font-size: 0.9em;
            color: gray;
            margin-bottom: 8px;
        }

        .published {
            margin-bottom: 12px;
        }

        .category {
            margin-top: 30px;
        }
        h4{
            text-align: center;
            padding:10px;
            background-color: grey;
            color:white;
        }
    </style>
</head>
<body>

<h2>YouTube Videos by Category</h2>

<div class="navbar">
    <a href="#Productivity_Self_Improvement_and_Personal_Growth">Productivity, Self-Improvement & Personal Growth</a>
    <a href="#Health_Wellness_and_Medical">Health, Wellness, and Medical</a>
    <a href="#Personal_Development_and_Motivation">Personal Development & Motivation</a>
    <a href="#Fashion_and_Lifestyle">Fashion & Lifestyle</a>
</div>
"""

# Loop through each category and its videos
for category, videos in all_videos_by_category.items():
    category_id = category.replace(" ", "_").replace("&", "and").replace(",", "")
    html_content += f'<div class="category" id="{category_id}"><h2>{category}</h2><div class="video-container">'

    for video in videos:
        html_content += f"""
        <a href="{video['link']}" target="_blank" class="card">
            <img src="{video['thumbnail']}" alt="{video['title']}" class="thumbnail">
            <div class="video-title">{video['title']}</div>
            <div class="channel">{video['channel']}</div>
            <div class="published">{video['published'].strftime('%d %b %Y')}</div>
        </a>
        """

    html_content += "</div></div>"

# Close HTML content
html_content += """
<h4>All content on this webpage, including YouTube videos and other media, belongs to their respective owners and is solely used to showcase user creativity.</h4>
</body>
</html>
"""

script_directory = os.path.dirname(os.path.abspath(__file__))
html_file_path = os.path.join(script_directory, "index.html")

with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML file saved to {html_file_path}")
