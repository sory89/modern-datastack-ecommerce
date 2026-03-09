import bcrypt
import json
from pathlib import Path

# Ecriture dans /dags qui est un volume partagé entre tous les containers
passwords_file = Path("/opt/airflow/dags/simple_auth_manager_passwords.json.generated")
password = "admin123"
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
data = {"admin": hashed}
passwords_file.write_text(json.dumps(data))
print(f"Fichier cree : {passwords_file}")
print("Login : admin / admin123")