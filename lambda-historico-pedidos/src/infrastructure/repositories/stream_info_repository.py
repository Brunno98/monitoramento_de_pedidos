

from infrastructure.db.connection import get_connection


def save_stream_info(record_id: str, batch_size: int, execution_time: float):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                            INSERT INTO stream_info ("record_id", "batch_size", "execution_time")
                            values (%s, %s, %s)
                            """, (record_id, batch_size, execution_time))
