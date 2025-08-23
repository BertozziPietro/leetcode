import os
import json
import re

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load configuration
config_path = os.path.join(current_dir, "config.json")
with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

# Load the study plan specified in the config
study_plan_file = config["study_plan_file"]
study_plan_path = os.path.join(current_dir, study_plan_file)
with open(study_plan_path, "r", encoding="utf-8") as f:
    study_plan = json.load(f)

# Extract study plan info
study_plan_name = study_plan["study_plan_name"]
base_url = study_plan["base_url"]
repo_path = study_plan["repo_path"]
language = study_plan["language"]
extension = study_plan["extension"]
problems_by_category = study_plan["problems_by_category"]

# Function to normalize problem filenames
def normalize_filename(problem_id, problem_name):
    # Convert to lowercase and replace all non-alphanumeric characters with underscores
    safe_name = re.sub(r'[^a-z0-9]', '_', problem_name.lower())
    # Remove multiple consecutive underscores
    safe_name = re.sub(r'_+', '_', safe_name).strip('_')
    problem_code = f"lc_{problem_id:04d}_" + safe_name
    return problem_code + extension

# Create the base repository directory (one level up from the script)
base_dir = os.path.join("..", repo_path.strip("./"))
os.makedirs(base_dir, exist_ok=True)

# Create categories and problem files
for category, problems in problems_by_category.items():
    # Normalize category name for directory
    category_dir = os.path.join(base_dir, category.replace(" ", "_").replace("/", "_").lower())
    os.makedirs(category_dir, exist_ok=True)
    
    for problem in problems:
        problem_id = problem["id"]
        problem_name = problem["name"]
        
        filename = normalize_filename(problem_id, problem_name)
        filepath = os.path.join(category_dir, filename)
        
        # Write problem file only if it doesn't exist
        if not os.path.exists(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {problem_name} (https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/)\n")
                f.write(f"# Study Plan: {study_plan_name}\n")
                f.write(f"# Category: {category}\n")
                f.write(f"# Problem: {problem_name}\n")

# Update the main README file (one level up)
readme_path = os.path.join("..", "README.md")
with open(readme_path, "a", encoding="utf-8") as f:
    f.write(f"## {study_plan_name}\n")
    f.write(f"- **Solutions in this repository:** [{study_plan_name} {language}]({study_plan['repo_path']})\n")
    f.write(f"- **Official LeetCode problems:** [{study_plan_name} Study Plan]({base_url})\n\n")
