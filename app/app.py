import os
import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "secret"),
    )

@app.get("/")
def root():
    return jsonify(status="ok", message="API entry point"), 200

@app.get("/users")
def users():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM users ORDER BY id;")
            rows = cur.fetchall()
            return jsonify([{"id": r[0], "name": r[1]} for r in rows])

@app.get("/add")
def add_user():
    name = request.args.get("name")
    if not name:
        return jsonify(error="pass ?name=..."), 400
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id;", (name,))
            new_id = cur.fetchone()[0]
            conn.commit()
            return jsonify(id=new_id, name=name), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
