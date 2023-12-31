CREATE TABLE sample_app.maps(
    grid_id serial PRIMARY KEY,
    -- 本来は外部キー
    map_id integer NOT NULL,
    x integer NOT NULL,
    y integer NOT NULL,
    z integer NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(map_id, x, y, z)
);

INSERT INTO
    sample_app.maps(map_id, x, y, z)
VALUES
    (1, 0, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 2, 0),
    (1, 0, 3, 0),
    (1, 1, 0, 0),
    (1, 1, 1, 0),
    (1, 1, 2, 0),
    (1, 1, 3, 0),
    (1, 2, 0, 0),
    (1, 2, 1, 0),
    (1, 2, 2, 0),
    (1, 2, 3, 0),
    (1, 3, 0, 0),
    (1, 3, 1, 0),
    (1, 3, 2, 0),
    (1, 3, 3, 0);
