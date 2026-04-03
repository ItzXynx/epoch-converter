import sys
from datetime import datetime, timezone

# convert between unix timestamps and human readable dates
# i always forget how to do this

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # print current time
        now = datetime.now(timezone.utc)
        print(f"now: {now.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print(f"epoch: {int(now.timestamp())}")
        sys.exit()
    
    arg = sys.argv[1]
    
    try:
        # assume it's a timestamp
        ts = int(arg)
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        print(f"timestamp: {ts}")
        print(f"utc: {dt.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print(f"local: {datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError:
        # assume it's a date string
        try:
            dt = datetime.fromisoformat(arg)
            print(f"date: {arg}")
            print(f"epoch: {int(dt.timestamp())}")
        except:
            print("couldnt parse date")
