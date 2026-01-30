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

def format_briefing_html() -> str:
    """Generate HTML morning briefing."""
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    weather = get_weather("11215")
    
    # Fetch from both sources
    hn_stories = fetch_hn_top_stories(30)
    ih_stories = fetch_indiehackers(20)
    all_stories = hn_stories + ih_stories
    top_stories = rank_stories(all_stories, max_items=10)
    
    # Build article rows
    articles_html = ""
    for i, story in enumerate(top_stories, 1):
        source = story['source']
        source_color = "#ff6600" if source == "HN" else "#4f46e5"
        relevance = story.get('relevance', 0)
        score = story.get('score', 0)
        
        meta_parts = []
        if score:
            meta_parts.append(f"↑{score}")
        if relevance > 0:
            meta_parts.append(f"🎯 relevant")
        meta = " · ".join(meta_parts)
        
        articles_html += f'''
        <tr>
            <td style="padding: 16px 0; border-bottom: 1px solid #e5e7eb;">
                <div style="display: flex; align-items: flex-start; gap: 12px;">
                    <span style="background: {source_color}; color: white; font-size: 11px; font-weight: 600; padding: 4px 8px; border-radius: 4px; min-width: 24px; text-align: center;">{source}</span>
                    <div>
                        <a href="{story['url']}" style="color: #111827; text-decoration: none; font-weight: 500; font-size: 15px; line-height: 1.4;">{story['title']}</a>
                        <div style="color: #6b7280; font-size: 13px; margin-top: 4px;">{meta}</div>
                    </div>
                </div>
            </td>
        </tr>'''
    
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; background-color: #f3f4f6; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;">
    <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f3f4f6; padding: 32px 16px;">
        <tr>
            <td align="center">
                <table width="100%" style="max-width: 600px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
                    <!-- Header -->
                    <tr>
                        <td style="background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%); padding: 32px; border-radius: 12px 12px 0 0;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 24px; font-weight: 600;">☀️ Morning Briefing</h1>
                            <p style="margin: 8px 0 0 0; color: #93c5fd; font-size: 14px;">{date_str}</p>
                        </td>
                    </tr>
                    
                    <!-- Weather -->
                    <tr>
                        <td style="padding: 24px; background-color: #f0f9ff; border-bottom: 1px solid #e0f2fe;">
                            <div style="display: flex; align-items: center; gap: 12px;">
                                <span style="font-size: 28px;">🌡️</span>
                                <div>
                                    <div style="font-weight: 600; color: #0c4a6e; font-size: 16px;">{weather}</div>
                                </div>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Articles Header -->
                    <tr>
                        <td style="padding: 24px 24px 8px 24px;">
                            <h2 style="margin: 0; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; color: #6b7280; font-weight: 600;">Top Articles For You</h2>
                        </td>
                    </tr>
                    
                    <!-- Articles -->
                    <tr>
                        <td style="padding: 0 24px;">
                            <table width="100%" cellpadding="0" cellspacing="0">
                                {articles_html}
                            </table>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="padding: 24px; background-color: #f9fafb; border-radius: 0 0 12px 12px; border-top: 1px solid #e5e7eb;">
                            <p style="margin: 0; font-size: 12px; color: #9ca3af; text-align: center;">
                                Curated for: startups · CTO/leadership · AI/Claude · indie hacking · MicroSaaS
                            </p>
                            <p style="margin: 8px 0 0 0; font-size: 12px; color: #9ca3af; text-align: center;">
                                — Gomez ⚡
                            </p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>'''
    
    return html

def format_briefing() -> str:
    """Generate the full morning briefing (plain text fallback)."""
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

def send_email(to_addr: str, subject: str, body: str, html: bool = False) -> bool:
    """Send email using the existing send_email.py script."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    send_script = os.path.join(script_dir, "send_email.py")
    
    args = ["python3", send_script, to_addr, subject, body]
    if html:
        args.append("--html")
    
    result = subprocess.run(args, capture_output=True, text=True, timeout=30)
    return result.returncode == 0

if __name__ == "__main__":
    if "--print" in sys.argv:
        if "--plain" in sys.argv:
            print(format_briefing())
        else:
            print(format_briefing_html())
    else:
        # Send via email (HTML by default)
        today = datetime.now().strftime("%b %d")
        subject = f"☀️ Morning Briefing — {today}"
        briefing_html = format_briefing_html()
        
        if send_email("chuck.blake@gmail.com", subject, briefing_html, html=True):
            print(f"Briefing sent to chuck.blake@gmail.com")
        else:
            print("Failed to send briefing email")
            # Fallback to plain text
            print(format_briefing())
