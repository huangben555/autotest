import json
import os
from pathlib import Path

logsPath = Path(__file__).absolute().parent.parent / Path("logs")

logPath = os.path.join(logsPath, "202109051604015218")

with open(logPath) as fp:
    rows = fp.read()
    rows1 = rows.splitlines()
    rows2 = json.loads(json.dumps(rows1))
    print(rows2[0])
