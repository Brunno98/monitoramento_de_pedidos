from aws_lambda_typing import events
from datetime import datetime
import json

import psycopg


def lambda_handler(event: events.DynamoDBStreamEvent, context):
    conn = create_connection()
    conn_health_check(conn)
    records = event.get('Records')

    for record in records:
        event_name = record.get('eventName')
        if event_name == "REMOVE":
            print("Ignorando evento de remoção")
            continue

        print("Evento de inserção")
        data = to_data(record)
        data['acao'] = event_name
        data['event_date'] = datetime.fromtimestamp(record.get(
            'dynamodb').get('ApproximateCreationDateTime')).isoformat()
        print(f"inserindo novo registro de pedido: {json.dumps(data)}")
        save(conn, data)

    conn.close()


def to_data(record: events.dynamodb_stream.DynamodbRecord):
    print(json.dumps(record))
    raw_data = record.get('dynamodb', {}).get('NewImage')
    return {
        "pedido_id": raw_data.get('pedido_id', {}).get('S'),
        "client_id": raw_data.get('client_id', {}).get('S'),
        "valor_total": raw_data.get('valor_total', {}).get('N'),
        "status": raw_data.get('status', {}).get('S'),
        "data_criacao": raw_data.get('data_criacao', {}).get('S'),
    }


def create_connection(
    dbname="postgres",
    user="postgres",
    password="mypassword",
    host="postgres",
    port="5432"
) -> psycopg.Connection:
    return psycopg.connect(
        f"dbname={dbname} user={user} password={password} host={host} port={port}"
    )


def conn_health_check(conn: psycopg.Connection):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            if result and result[0] == 1:
                print("✅ Conexão com o banco funcionando!")
                return True
    except psycopg.OperationalError as e:
        print("❌ Erro ao conectar com o banco:", e)


def save(conn: psycopg.Connection, data: dict[str, str]):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO historico_pedidos ("pedido_id", "acao", "status", "data_evento")
            values (%s, %s, %s, %s)""",
                    (data.get('pedido_id'), data.get('acao'), data.get('status'), data.get('event_date')))
        conn.commit()
        print("✅ registro inserido com sucesso!")
