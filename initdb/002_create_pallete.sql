CREATE TABLE sample_app.palettes(
    palette_id serial PRIMARY KEY,
    qr_id int NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (palette_id, qr_id)
);

INSERT INTO
    sample_app.palettes(qr_id)
VALUES
    (1),
    (2),
    (3);
