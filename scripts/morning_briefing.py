#!/usr/bin/env python3
"""Morning briefing: weather + curated news from HN and IndieHackers."""

import json
import re
import subprocess
import sys
from datetime import datetime
from typing import Optional
import requests

# Chuck's interests for relevance scoring
INTERESTS = [
    "startup", "founder", "co-founder", "seed", "vc", "venture", "funding",
    "cto", "engineering team", "tech lead", "managing", "leadership",
    "ai", "claude", "anthropic", "llm", "gpt", "machine learning",
    "indie hacker", "solo founder", "microsaas", "saas", "bootstrapped",
    "side project", "profitable", "revenue", "mrr", "arr",
    "claude code", "coding assistant", "ai coding",
]

def get_weather(zip_code: str = "11215") -> str:
    """Fetch weather from wttr.in."""
    try:
        resp = requests.get(f"https://wttr.in/{zip_code}?format=3", timeout=10)
        weather_line = resp.text.strip()
        
        # Get more details
        resp2 = requests.get(f"https://wttr.in/{zip_code}?format=%C+%t+%h+%w", timeout=10)
        details = resp2.text.strip()
        
        return f"Weather for {zip_code}: {details}"
    except Exception as e:
        return f"Weather unavailable: {e}"

def score_relevance(title: str, text: str = "") -> int:
    """Score content based on Chuck's interests."""
    content = (title + " " + text).lower()
    score = 0
    for interest in INTERESTS:
        if interest.lower() in content:
            score += 1
    return score

def fetch_hn_top_stories(limit: int = 30) -> list[dict]:
    """Fetch top stories from Hacker News API."""
    try:
        # Get top story IDs
        resp = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10)
        story_ids = resp.json()[:limit]
        
        stories = []
        for sid in story_ids:
            resp = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{sid}.json", timeout=5)
            item = resp.json()
            if item and item.get("type") == "story":
                stories.append({
                    "title": item.get("title", ""),
                    "url": item.get("url", f"https://news.ycombinator.com/item?id={sid}"),
                    "score": item.get("score", 0),
                    "comments": item.get("descendants", 0),
                    "source": "HN",
                    "relevance": score_relevance(item.get("title", "")),
                })
        return stories
    except Exception as e:
        return [{"title": f"HN fetch error: {e}", "url": "", "score": 0, "source": "HN", "relevance": 0}]

def fetch_indiehackers(limit: int = 20) -> list[dict]:
    """Fetch recent posts from IndieHackers (scrape front page)."""
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; MorningBriefing/1.0)"}
        resp = requests.get("https://www.indiehackers.com/", headers=headers, timeout=15)
        
        # Simple regex extraction for post titles and links
        # IndieHackers uses React, so we look for JSON data or meta content
        stories = []
        
        # Try to find post data in the page
        # Look for patterns like href="/post/..." with titles
        post_pattern = r'href="(/post/[^"]+)"[^>]*>([^<]+)</a>'
        matches = re.findall(post_pattern, resp.text)
        
        seen = set()
        for url_path, title in matches[:limit]:
            title = title.strip()
            if title and title not in seen and len(title) > 10:
                seen.add(title)
                stories.append({
                    "title": title,
                    "url": f"https://www.indiehackers.com{url_path}",
                    "score": 0,  # IH doesn't show scores publicly
                    "comments": 0,
                    "source": "IH",
                    "relevance": score_relevance(title),
                })
        
        # If regex didn't work well, try alternative patterns
        if len(stories) < 5:
            # Look for any interesting links
            link_pattern = r'<a[^>]+href="(https://www\.indiehackers\.com/post/[^"]+)"[^>]*>([^<]+)</a>'
            matches = re.findall(link_pattern, resp.text)
            for url, title in matches[:limit]:
                title = title.strip()
                if title and title not in seen and len(title) > 10:
                    seen.add(title)
                    stories.append({
                        "title": title,
                        "url": url,
                        "score": 0,
                        "comments": 0,
                        "source": "IH",
                        "relevance": score_relevance(title),
                    })
        
        return stories[:limit]
    except Exception as e:
        return [{"title": f"IndieHackers fetch error: {e}", "url": "", "score": 0, "source": "IH", "relevance": 0}]

def rank_stories(stories: list[dict], max_items: int = 10) -> list[dict]:
    """Rank stories by combined relevance and popularity."""
    for s in stories:
        # Combined score: relevance * 100 + log(popularity)
        popularity = s.get("score", 0) + s.get("comments", 0)
        s["combined_score"] = (s["relevance"] * 100) + min(popularity, 500)
    
    # Sort by combined score, then by raw score
    ranked = sorted(stories, key=lambda x: (x["combined_score"], x.get("score", 0)), reverse=True)
    return ranked[:max_items]

def format_briefing() -> str:
    """Generate the full morning briefing."""
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    
    lines = [
        f"MORNING BRIEFING — {date_str}",
        "=" * 50,
        "",
        get_weather("11215"),
        "",
        "-" * 50,
        "TOP ARTICLES (ranked by relevance to your interests)",
        "-" * 50,
        "",
    ]
    
    # Fetch from both sources
    hn_stories = fetch_hn_top_stories(30)
    ih_stories = fetch_indiehackers(20)
    
    all_stories = hn_stories + ih_stories
    top_stories = rank_stories(all_stories, max_items=10)
    
    for i, story in enumerate(top_stories, 1):
        source_tag = f"[{story['source']}]"
        relevance_tag = f"(rel:{story['relevance']})" if story['relevance'] > 0 else ""
        score_info = f"↑{story['score']}" if story.get('score') else ""
        
        lines.append(f"{i}. {source_tag} {story['title']}")
        lines.append(f"   {story['url']}")
        if score_info or relevance_tag:
            lines.append(f"   {score_info} {relevance_tag}".strip())
        lines.append("")
    
    lines.extend([
        "-" * 50,
        "Your tracked interests: startups, CTO/leadership, AI/Claude, indie hacking, MicroSaaS",
        "",
        "— Gomez"
    ])
    
    return "\n".join(lines)

def send_email(to_addr: str, subject: str, body: str) -> bool:
    """Send email using the existing send_email.py script."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    send_script = os.path.join(script_dir, "send_email.py")
    
    result = subprocess.run(
        ["python3", send_script, to_addr, subject, body],
        capture_output=True, text=True, timeout=30
    )
    return result.returncode == 0

if __name__ == "__main__":
    briefing = format_briefing()
    
    if "--print" in sys.argv:
        print(briefing)
    else:
        # Send via email
        today = datetime.now().strftime("%b %d")
        subject = f"Morning Briefing — {today}"
        
        if send_email("chuck.blake@gmail.com", subject, briefing):
            print(f"Briefing sent to chuck.blake@gmail.com")
        else:
            print("Failed to send briefing email")
            print(briefing)  # Print anyway so it's not lost
