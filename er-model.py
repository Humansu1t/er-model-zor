from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

# Create a figure
fig, ax = plt.subplots(figsize=(12, 8))

# Define box parameters for tables
box_params = {
    "facecolor": "#DFF0D8",
    "edgecolor": "black",
    "boxstyle": "round,pad=0.3"
}

# Define font parameters
font_params = {
    "fontsize": 10,
    "fontweight": "bold",
    "ha": "center"
}

# Table positions
positions = {
    "Departments": (0.2, 0.8),
    "Programs": (0.5, 0.8),
    "Hosts": (0.8, 0.8),
    "Employees": (0.5, 0.5),
    "ProgramSchedule": (0.5, 0.2),
}

# Table contents
tables = {
    "Departments": ["PK: DepartmentID", "DepartmentName", "Description"],
    "Programs": ["PK: ProgramID", "ProgramName", "Description", "AirTime", "FK: DepartmentID"],
    "Hosts": ["PK: HostID", "HostName", "ContactInfo", "FK: ProgramID"],
    "Employees": ["PK: EmployeeID", "EmployeeName", "Position", "FK: DepartmentID", "ContactInfo"],
    "ProgramSchedule": ["PK: ScheduleID", "FK: ProgramID", "AirDate", "StartTime", "EndTime"],
}

# Draw boxes and table names
for table_name, pos in positions.items():
    ax.text(*pos, f"{table_name}\n" + "\n".join(tables[table_name]), bbox=box_params, **font_params)

# Draw relationships (arrows)
arrows = [
    ("Departments", "Programs"),
    ("Departments", "Employees"),
    ("Programs", "Hosts"),
    ("Programs", "ProgramSchedule"),
]

for start, end in arrows:
    start_pos = positions[start]
    end_pos = positions[end]
    ax.annotate(
        "", xy=end_pos, xycoords="axes fraction", xytext=start_pos, textcoords="axes fraction",
        arrowprops=dict(arrowstyle="-|>", color="black", lw=1.5)
    )

# Adjust axis and remove ticks
ax.axis("off")
plt.title("Database Schema for ZO‘R TV", fontsize=14, fontweight="bold")
plt.tight_layout()

# Save and show the diagram
plt.savefig("C:/Users/YourName/Downloads/ZOR_TV_DB_Schema.png", dpi=300)  # Update the path as needed
plt.show()
