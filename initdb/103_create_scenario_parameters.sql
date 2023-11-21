CREATE TABLE sample_app.scenario_parameters(
    parameter_id serial PRIMARY KEY,
    parameter_gid integer NOT NULL,
    p_key text NOT NULL,
    p_value text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP
);
