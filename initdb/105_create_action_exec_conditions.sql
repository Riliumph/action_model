CREATE TABLE sample_app.action_exec_conditions(
    exec_condition_id serial PRIMARY KEY,
    action_link_id integer NOT NULL,
    l_value text NOT NULL,
    operator text NOT NULL,
    r_value text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(action_link_id) REFERENCES sample_app.action_links(action_link_id)
);

INSERT INTO
    sample_app.action_exec_conditions(action_link_id, l_value, operator, r_value)
VALUES
    (1, 'hoge', '=', 'hoge');
