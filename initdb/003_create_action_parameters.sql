CREATE TABLE sample_app.action_parameters(
    parameter_id serial PRIMARY KEY,
    parameter_gid integer NOT NULL,
    p_key text NOT NULL,
    p_value text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(parameter_gid, p_key)
);

INSERT INTO
    sample_app.action_parameters(parameter_gid, p_key, p_value)
VALUES
    (1, 'safety', '1'),
    (1, 'emergency', '1'),
    (1, 'precise', '1'),
    (2, 'safety', '2'),
    (2, 'emergency', '2'),
    (2, 'precise', '2'),
    (3, 'safety', '3'),
    (3, 'emergency', '3'),
    (3, 'precise', '3'),
    (4, 'safety', '4'),
    (4, 'emergency', '4'),
    (4, 'precise', '4'),
    (5, 'safety', '5'),
    (5, 'emergency', '5'),
    (5, 'precise', '5'),
    (6, 'safety', '6'),
    (6, 'emergency', '6'),
    (6, 'precise', '6');
