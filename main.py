#
import random

with open("projects.txt", "r", encoding="utf-8") as f:
    projects = [line.strip() for line in f if line.strip()]

print("Dự án ngẫu nhiên:", random.choice(projects))--06--09--10--11--12--13--16
