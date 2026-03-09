#!/bin/bash
python3 - <<'EOF'
import bcrypt, json, os
from pathlib import Path

pwd = os.environ.get("AIRFLOW_ADMIN_PASSWORD", "admin123").encode()
h = bcrypt.hashpw(pwd, bcrypt.gensalt()).decode()
f = Path("/opt/airflow/passwords/simple_auth_manager_passwords.json.generated")
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps({"admin": h}))
print("Login: admin /", pwd.decode())
EOF