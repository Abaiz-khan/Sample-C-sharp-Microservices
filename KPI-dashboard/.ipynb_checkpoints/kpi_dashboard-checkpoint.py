{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3cd3b70f-aa73-45b9-a71a-500431b04857",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import plotly.graph_objs as go\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "# Function to plot pie chart\n",
    "def plot_pie_chart():\n",
    "    # Logic to retrieve alert data from text files and calculate values for the pie chart\n",
    "    labels = ['World Service', 'Hello Service']\n",
    "    values = [60, 40]  # Sample values, replace with actual data\n",
    "\n",
    "    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])\n",
    "    fig.show()\n",
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
