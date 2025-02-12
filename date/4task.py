from datetime import datetime
print("Difference in seconds:", int(abs((datetime.strptime("2024-02-12 14:31:00", "%Y-%m-%d %H:%M:%S") - datetime.strptime("2024-02-10 12:00:00", "%Y-%m-%d %H:%M:%S")).total_seconds())))
