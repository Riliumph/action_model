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
    -- 晴・移動
    (1, 'safety', '1'),
    (1, 'emergency', '1'),
    (1, 'precise', '1'),
    -- 雨・移動
    (2, 'safety', '2'),
    (2, 'emergency', '2'),
    (2, 'precise', '2'),
    -- 晴・荷揚げ
    (3, 'safety', '3'),
    (3, 'emergency', '3'),
    (3, 'precise', '3'),
    -- 晴・フォーク回転
    (4, 'safety', '4'),
    (4, 'emergency', '4'),
    (4, 'precise', '4'),
    -- 晴・荷下ろし
    (5, 'safety', '5'),
    (5, 'emergency', '5'),
    (5, 'precise', '5'),
    -- 雨・荷下ろし
    (6, 'safety', '6'),
    (6, 'emergency', '6'),
    (6, 'precise', '6');
