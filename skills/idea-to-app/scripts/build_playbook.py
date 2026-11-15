"""Rebuild references/playbook.html from playbook_template.html + catalog.json.
Usage: python3 -I build_playbook.py [extra_output_path]"""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
ref = os.path.join(here, "..", "references")
cat = json.load(open(os.path.join(ref, "catalog.json")))
data = json.dumps(cat, separators=(",", ":")).replace("</", "<\\/")
html = open(os.path.join(ref, "playbook_template.html")).read().replace("__CATALOG__", data)
outs = [os.path.join(ref, "playbook.html")] + sys.argv[1:]
for o in outs:
    open(o, "w").write(html)
    print("wrote", o)
