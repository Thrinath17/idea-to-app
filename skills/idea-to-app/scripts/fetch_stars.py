"""Fetch GitHub star counts for catalog repos and write catalog.json.
Uses the search API in batches (10 req/min unauthenticated), then the REST API for any repo search missed."""
import json, sys, time, urllib.request, urllib.parse, datetime, os
sys.path.insert(0, os.path.dirname(__file__))
from catalog_src import CATEGORIES, O

def get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "catalog-builder"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

repos = sorted({x["repo"] for x in O if x["repo"]})
stars = {}
batch = []
def flush(batch):
    q = "+".join("repo:" + r for r in batch)
    d = get(f"https://api.github.com/search/repositories?q={q}&per_page=100")
    for it in d.get("items", []):
        stars[it["full_name"].lower()] = it["stargazers_count"]
for r in repos:
    if len("+".join("repo:" + x for x in batch + [r])) > 240:
        flush(batch); batch = []; time.sleep(6.5)
    batch.append(r)
if batch: flush(batch)

missing = [r for r in repos if r.lower() not in stars]
print("search found", len(stars), "of", len(repos), "| filling", len(missing), "via REST", file=sys.stderr)
for r in missing:
    try:
        stars[r.lower()] = get(f"https://api.github.com/repos/{r}")["stargazers_count"]
    except Exception as e:
        print("  no data for", r, e, file=sys.stderr)

today = datetime.date.today().isoformat()
for x in O:
    x["stars"] = stars.get(x["repo"].lower()) if x["repo"] else None
out = {"capturedAt": today, "categories": [{"id": c, "name": n} for c, n in CATEGORIES], "options": O}
dest = sys.argv[1]
json.dump(out, open(dest, "w"), indent=1)
print("wrote", dest, "|", len(O), "options |", sum(1 for x in O if x["stars"]), "with stars", file=sys.stderr)
for x in sorted([x for x in O if x["repo"] and x["stars"] is None], key=lambda x: x["name"]):
    print("  MISSING", x["name"], x["repo"], file=sys.stderr)
