CREATE TABLE sample_app.actions_params_rules(
    id serial PRIMARY KEY,
    action_id integer NOT NULL,
    weather text NOT NULL,
    parameter_gid integer NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    --    FOREIGN KEY (parameter_gid) REFERENCES sample_app.action_parameters (parameter_gid)
    FOREIGN KEY (action_id) REFERENCES sample_app.actions (action_id)
);

INSERT INTO
    sample_app.actions_params_rules(action_id, weather, parameter_gid)
VALUES
    (2, 'sun', 1),
    (2, 'rain', 2),
    (3, 'sun', 3),
    (4, 'sun', 4),
    (5, 'sun', 5),
    (5, 'rain', 6);
