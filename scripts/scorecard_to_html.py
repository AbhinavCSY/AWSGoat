import json
from pathlib import Path

data = json.loads(Path("scorecard.json").read_text())

html = f"""
<!DOCTYPE html>
<html>
<head>
  <title>OpenSSF Scorecard Report</title>
  <style>
    body {{ font-family: Arial, sans-serif; padding: 24px; }}
    h1 {{ color: #1f2937; }}
    .score {{ font-size: 36px; font-weight: bold; margin: 16px 0; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
    th, td {{ border: 1px solid #ddd; padding: 10px; }}
    th {{ background-color: #f3f4f6; }}
    .good {{ color: #16a34a; font-weight: bold; }}
    .bad {{ color: #dc2626; font-weight: bold; }}
  </style>
</head>
<body>

<h1>OpenSSF Scorecard Report</h1>

<p><b>Repository:</b> {data.get("repo", {}).get("name", "N/A")}</p>
<div class="score">Overall Score: {data["score"]} / 10</div>

<table>
<tr>
  <th>Check</th>
  <th>Score</th>
  <th>Reason</th>
</tr>
"""

for check in data["checks"]:
    cls = "good" if check["score"] >= 7 else "bad"
    html += f"""
<tr>
  <td>{check["name"]}</td>
  <td class="{cls}">{check["score"]}</td>
  <td>{check.get("reason", "")}</td>
</tr>
"""

html += """
</table>
</body>
</html>
"""

Path("scorecard-report.html").write_text(html)
print("✔ scorecard-report.html generated")
