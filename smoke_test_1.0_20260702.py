#!/usr/bin/env python3
import json
import subprocess
import sys
import time
import urllib.request


def post(payload):
    req = urllib.request.Request(
        "http://127.0.0.1:8790/mcp",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    proc = subprocess.Popen([sys.executable, "server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        time.sleep(1)
        init = post({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
        tools = post({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
        assert init["result"]["serverInfo"]["name"] == "omnipmx-document-runtime-mcp"
        names = [t["name"] for t in tools["result"]["tools"]]
        for name in ["ocr_image", "pdf_text_extract", "ocr_pdf", "pdf_extract_or_ocr", "markdown_to_docx", "markdown_to_pdf", "csv_to_plot_png", "python_execute"]:
            assert name in names, name
        print("PASS: initialize and tools/list")
    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    main()
