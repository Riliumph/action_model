CREATE TABLE sample_app.maps_palettes(
    id serial PRIMARY KEY,
    grid_id int NOT NULL,
    palette_id int NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (grid_id) REFERENCES sample_app.maps(grid_id),
    FOREIGN KEY(palette_id) REFERENCES sample_app.palettes(palette_id)
);

INSERT INTO
    sample_app.maps_palettes(grid_id, palette_id)
VALUES
    (1, 1),
    (8, 2),
    (9, 3);
