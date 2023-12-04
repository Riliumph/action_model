CREATE TABLE sample_app.scenarios_parameters_rules(
    id serial PRIMARY KEY,
    scenario_id integer NOT NULL,
    scenario_seq integer NOT NULL,
    parameter_gid integer NOT NULL,
    weather text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (scenario_id) REFERENCES sample_app.scenarios(scenario_id)
);
