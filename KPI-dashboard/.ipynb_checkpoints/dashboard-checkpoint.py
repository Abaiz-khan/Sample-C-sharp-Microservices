import os
import plotly.graph_objs as go

# Read alert data from text files
def read_alerts(file_path):
    with open(file_path, 'r') as file:
        alerts = file.readlines()
    return [alert.strip() for alert in alerts]

# Define paths to alert files
sample_services_dir = "../Sample-services"  # Assuming the Sample-services directory is one level above
zap_alerts_world_file = os.path.join(sample_services_dir, "zap-alerts-world.txt")
zap_alerts_file = os.path.join(sample_services_dir, "zap-alerts.txt")

zap_alerts_world = read_alerts(zap_alerts_world_file)
zap_alerts = read_alerts(zap_alerts_file)

# Function to filter alerts based on label
def filter_alerts(alerts, label):
    filtered_alerts = [alert for alert in alerts if label in alert.lower()]
    return filtered_alerts

# Calculate KPIs
total_alerts = len(zap_alerts_world) + len(zap_alerts)
world_alerts_count = len(zap_alerts_world)
service_alerts_count = len(zap_alerts)

# Create pie chart
labels = ['World Service', 'Hello Service']
values = [world_alerts_count, service_alerts_count]
pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Adjust layout
pie_chart.update_layout(
    title='Distribution of Alerts Between Microservices',
    title_font_size=24,
    width=800,
    height=600,
    margin=dict(t=100, b=0, l=0, r=0),
    font=dict(size=18)
)

# Display pie chart
pie_chart.show()
