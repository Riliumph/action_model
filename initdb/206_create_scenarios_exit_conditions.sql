CREATE TABLE sample_app.scenario_exit_conditions(
    exec_condition_id serial PRIMARY KEY,
    scenario_id integer NOT NULL,
    seq integer NOT NULL,
    l_value text NOT NULL,
    operator text NOT NULL,
    r_value text NOT NULL,
    created_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    updated_at timestamptz DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(scenario_id) REFERENCES sample_app.scenarios(scenario_id)
);
