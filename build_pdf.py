#!/usr/bin/env python3
"""Render an arXiv-style markdown essay to PDF via pandoc + headless Chrome (CDP)."""
import base64
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import websocket

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DEBUG_PORT = 9333


def cdp_print_to_pdf(html_path: Path) -> bytes:
    proc = subprocess.Popen(
        [CHROME, "--headless=new", "--disable-gpu",
         f"--remote-debugging-port={DEBUG_PORT}",
         "--remote-allow-origins=*",
         "--no-first-run", "--no-default-browser-check"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        for _ in range(50):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{DEBUG_PORT}/json/version", timeout=0.5)
                break
            except Exception:
                time.sleep(0.1)

        put_req = urllib.request.Request(
            f"http://127.0.0.1:{DEBUG_PORT}/json/new?file://{html_path}",
            method="PUT",
        )
        req = urllib.request.urlopen(put_req, timeout=5)
        tab = json.loads(req.read())
        ws_url = tab["webSocketDebuggerUrl"]

        ws = websocket.create_connection(ws_url, timeout=10)
        try:
            ws.send(json.dumps({"id": 1, "method": "Page.enable"}))
            ws.recv()

            # wait for the load event
            deadline = time.time() + 10
            while time.time() < deadline:
                msg = json.loads(ws.recv())
                if msg.get("method") == "Page.loadEventFired":
                    break

            ws.send(json.dumps({
                "id": 2,
                "method": "Page.printToPDF",
                "params": {
                    "printBackground": True,
                    "displayHeaderFooter": False,
                    "preferCSSPageSize": True,
                },
            }))
            while True:
                msg = json.loads(ws.recv())
                if msg.get("id") == 2:
                    return base64.b64decode(msg["result"]["data"])
        finally:
            ws.close()
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: build_pdf.py <markdown-file>")

    src = Path(sys.argv[1]).resolve()
    pdf_out = src.with_suffix(".pdf")

    shutil.copy(src, "_paper.md")

    result = subprocess.run(
        ["pandoc", "_paper.md", "--from=markdown+pipe_tables",
         "--template=arxiv.html", "--standalone", "-o", "paper.html"]
    )
    print(f"pandoc exit: {result.returncode}")
    result.check_returncode()

    html_path = Path("paper.html").resolve()
    pdf_bytes = cdp_print_to_pdf(html_path)
    pdf_out.write_bytes(pdf_bytes)

    Path("_paper.md").unlink(missing_ok=True)
    html_path.unlink(missing_ok=True)
    print(f"wrote {pdf_out}")


if __name__ == "__main__":
    main()
