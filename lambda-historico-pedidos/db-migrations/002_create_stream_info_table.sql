
CREATE TABLE stream_info (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    record_id VARCHAR(255) NOT NULL,
    batch_size INTEGER NOT NULL,
    execution_time NUMERIC(10, 6)
);