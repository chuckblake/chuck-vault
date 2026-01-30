#!/usr/bin/env python3
"""Fetch real-time MTA subway arrival times for the R train."""

import sys
import time
from datetime import datetime
import requests

try:
    from google.transit import gtfs_realtime_pb2
except ImportError:
    print("Error: gtfs-realtime-bindings not installed")
    sys.exit(1)

# MTA GTFS-RT feed for N/Q/R/W trains
FEED_URL = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"

# Station IDs (from MTA GTFS static data)
# Format: stop_id + direction (N=north/Manhattan, S=south/Brooklyn)
STATIONS = {
    "4th_ave_9th_st": {
        "name": "4th Ave-9th St",
        "to_manhattan": "R31N",  # Northbound toward Manhattan
        "to_brooklyn": "R31S",   # Southbound toward Bay Ridge
    },
    "cortlandt_st": {
        "name": "Cortlandt St", 
        "to_manhattan": "R27N",  # Northbound (toward Queens)
        "to_brooklyn": "R27S",   # Southbound toward Brooklyn
    }
}

def fetch_arrivals(stop_id: str, line: str = "R") -> list[int]:
    """Fetch arrival times in minutes for a given stop."""
    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)
        
        now = int(time.time())
        arrivals = []
        
        for entity in feed.entity:
            if not entity.HasField("trip_update"):
                continue
            
            trip = entity.trip_update
            route_id = trip.trip.route_id
            
            # Filter for R train only
            if route_id != line:
                continue
            
            for stop_time in trip.stop_time_update:
                if stop_time.stop_id == stop_id:
                    # Get arrival time (or departure if no arrival)
                    if stop_time.HasField("arrival"):
                        arr_time = stop_time.arrival.time
                    elif stop_time.HasField("departure"):
                        arr_time = stop_time.departure.time
                    else:
                        continue
                    
                    minutes = (arr_time - now) // 60
                    if minutes >= 0:
                        arrivals.append(minutes)
        
        return sorted(arrivals)[:5]  # Return next 5 trains
        
    except Exception as e:
        return [f"Error: {e}"]

def get_train_times(direction: str) -> str:
    """Get R train times for commute direction."""
    if direction == "work":
        # Home to work: 4th Ave-9th St northbound
        stop_id = STATIONS["4th_ave_9th_st"]["to_manhattan"]
        station = STATIONS["4th_ave_9th_st"]["name"]
        dest = "Manhattan"
    elif direction == "home":
        # Work to home: Cortlandt St southbound  
        stop_id = STATIONS["cortlandt_st"]["to_brooklyn"]
        station = STATIONS["cortlandt_st"]["name"]
        dest = "Brooklyn"
    else:
        return f"Unknown direction: {direction}. Use 'work' or 'home'."
    
    arrivals = fetch_arrivals(stop_id, "R")
    
    if not arrivals:
        return f"No R trains found at {station} → {dest}"
    
    if isinstance(arrivals[0], str):  # Error message
        return arrivals[0]
    
    times = ", ".join(f"{m}min" for m in arrivals)
    return f"Next R trains ({station} → {dest}):\n{times}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mta_train_times.py <work|home>")
        print("  work = 4th Ave-9th St → Manhattan")
        print("  home = Cortlandt St → Brooklyn")
        sys.exit(1)
    
    direction = sys.argv[1].lower()
    print(get_train_times(direction))
