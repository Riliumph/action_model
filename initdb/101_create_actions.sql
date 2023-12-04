CREATE TABLE sample_app.actions (
    action_id serial PRIMARY KEY,
    action_name text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO
    sample_app.actions(action_name)
VALUES
    ('ユースケース１'),
    ('移動'),
    ('荷揚げ'),
    ('フォーク回転'),
    ('荷下ろし');
