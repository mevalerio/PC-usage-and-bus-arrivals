import requests
import json
import sys

def get_bus_arrivals(stop_point_id):
    url = f"https://api.tfl.gov.uk/StopPoint/{stop_point_id}/Arrivals"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        arrivals = response.json()
        return arrivals
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data: {e}"}

def format_arrivals(arrivals):
    if "error" in arrivals:
        return arrivals["error"]

    if not arrivals:
        return "No bus arrivals found."

    # Sort arrivals by timeToStation
    arrivals.sort(key=lambda x: x['timeToStation'])

    output = []
    for i, arrival in enumerate(arrivals[:5]):  # Display top 5 arrivals
        line_name = arrival.get('lineName', 'N/A')
        destination_name = arrival.get('destinationName', 'N/A')
        time_to_station_seconds = arrival.get('timeToStation', 0)

        minutes = time_to_station_seconds // 60
        seconds = time_to_station_seconds % 60

        color_start = "${color white}"  # Default color
        if time_to_station_seconds < 60:  # Less than 1 minute
            color_start = "${color red}"
        elif time_to_station_seconds < 180:  # Less than 3 minutes
            color_start = "${color orange}"
        elif time_to_station_seconds < 300:  # Less than 5 minutes
            color_start = "${color green}"

        output.append(color_start + f"{line_name} to {destination_name}: {minutes}m {seconds}s" + "${color white}")
    return "\n".join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bus_arrivals.py <stop_point_id>")
        sys.exit(1)

    stop_point_id = sys.argv[1]
    arrivals = get_bus_arrivals(stop_point_id)
    print(format_arrivals(arrivals))