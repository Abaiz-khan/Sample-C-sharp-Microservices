{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ddc6f6bf-7921-4058-b208-314ae5ca2ca7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'world_alerts_count' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 8\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;66;03m# Create pie chart\u001b[39;00m\n\u001b[1;32m      7\u001b[0m labels \u001b[38;5;241m=\u001b[39m [\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mWorld Service\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mHello Service\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m----> 8\u001b[0m values \u001b[38;5;241m=\u001b[39m [world_alerts_count, service_alerts_count]\n\u001b[1;32m      9\u001b[0m pie_chart \u001b[38;5;241m=\u001b[39m go\u001b[38;5;241m.\u001b[39mFigure(data\u001b[38;5;241m=\u001b[39m[go\u001b[38;5;241m.\u001b[39mPie(labels\u001b[38;5;241m=\u001b[39mlabels, values\u001b[38;5;241m=\u001b[39mvalues)])\n\u001b[1;32m     11\u001b[0m \u001b[38;5;66;03m# Adjust layout\u001b[39;00m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'world_alerts_count' is not defined"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import plotly.graph_objs as go\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "\n",
    "# Read alert data from text files\n",
    "def read_alerts(file_path):\n",
    "    with open(file_path, 'r') as file:\n",
    "        alerts = file.readlines()\n",
    "    return [alert.strip() for alert in alerts]\n",
    "\n",
    "# Define paths to alert files\n",
    "sample_services_dir = \"../Sample-services\"  # Assuming the Sample-services directory is one level above\n",
    "zap_alerts_world_file = os.path.join(sample_services_dir, \"zap-alerts-world.txt\")\n",
    "zap_alerts_file = os.path.join(sample_services_dir, \"zap-alerts.txt\")\n",
    "\n",
    "zap_alerts_world = read_alerts(zap_alerts_world_file)\n",
    "zap_alerts = read_alerts(zap_alerts_file)\n",
    "\n",
    "# Function to filter alerts based on label\n",
    "def filter_alerts(alerts, label):\n",
    "    filtered_alerts = [alert for alert in alerts if label in alert.lower()]\n",
    "    return filtered_alerts\n",
    "\n",
    "# Calculate KPIs\n",
    "total_alerts = len(zap_alerts_world) + len(zap_alerts)\n",
    "world_alerts_count = len(zap_alerts_world)\n",
    "service_alerts_count = len(zap_alerts)\n",
    "\n",
    "# Create pie chart\n",
    "labels = ['World Service', 'Hello Service']\n",
    "values = [world_alerts_count, service_alerts_count]\n",
    "pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "\n",
    "# Adjust layout\n",
    "pie_chart.update_layout(\n",
    "    title='Distribution of Alerts Between Microservices',\n",
    "    title_font_size=24,\n",
    "    width=800,\n",
    "    height=600,\n",
    "    margin=dict(t=100, b=0, l=0, r=0),\n",
    "    font=dict(size=18)\n",
    ")\n",
    "\n",
    "# Display pie chart\n",
    "pie_chart.show()\n",
    "\n",
    "# Function to display alert details and handle button clicks\n",
    "def display_alerts():\n",
    "    # Logic to retrieve and display alert details\n",
    "    alerts = [\n",
    "        {\"id\": 1, \"message\": \"Alert 1\", \"datetime\": \"2024-02-13 10:00:00\", \"solved\": False},\n",
    "        {\"id\": 2, \"message\": \"Alert 2\", \"datetime\": \"2024-02-13 11:00:00\", \"solved\": False},\n",
    "        # Add more alert data as needed\n",
    "    ]\n",
    "\n",
    "    for alert in alerts:\n",
    "        display(widgets.HTML(f\"<strong>{alert['message']}</strong> - {alert['datetime']}\"))\n",
    "        if not alert['solved']:\n",
    "            button = widgets.Button(description=\"Mark as Solved\")\n",
    "            button.on_click(lambda event, alert_id=alert['id']: mark_as_solved(alert_id))\n",
    "            display(button)\n",
    "\n",
    "# Function to handle button click event\n",
    "def mark_as_solved(alert_id):\n",
    "    # Logic to mark alert as solved\n",
    "    print(f\"Alert {alert_id} marked as solved.\")\n",
    "\n",
    "# Plot pie chart\n",
    "plot_pie_chart()\n",
    "\n",
    "# Display alert details\n",
    "display_alerts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11e7a80d-e544-4b18-8d59-2ab9deb2bdca",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
